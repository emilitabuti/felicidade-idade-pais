"""Funções reutilizáveis do LAB "Felicidade por Idade e por País".

Fontes: Our World in Data (Cantril ladder por faixa etária, via WHR 2024) e
API pública do Banco Mundial (PIB per capita PPC, população, área terrestre).
"""

from pathlib import Path

import numpy as np
import pandas as pd
import requests

# dados de idade (Our World in Data) 
OWID_AGE_URL = (
    "https://ourworldindata.org/grapher/cantril-ladder-age-groups.csv"
    "?v=1&csvType=full&useColumnShortNames=true"
)
# cópia local usada caso o download da OWID falhe
_LOCAL_OWID_CSV = Path(__file__).parent / "cantril-ladder-age-groups" / "cantril-ladder-age-groups.csv"

# padroniza os nomes das quatro faixas etárias
_AGE_COLUMN_LABELS = {
    "cantril_ladder_score__age_group_up_to_29_years": "Up to 29 years",
    "cantril_ladder_score__age_group_30_44_years": "30-44 years",
    "cantril_ladder_score__age_group_45_59_years": "45-59 years",
    "cantril_ladder_score__age_group_60plus_years": "60+ years",
}

# pontos médios utilizados para representar cada faixa etária.
# para "60+ years", 70 anos é uma aproximação.
AGE_MID = {
    "Up to 29 years": 22,
    "30-44 years": 37,
    "45-59 years": 52,
    "60+ years": 70,
}


def load_owid_age(url: str = OWID_AGE_URL, local_fallback: Path = _LOCAL_OWID_CSV) -> pd.DataFrame:
    """carrega os dados da OWID em formato longo, com uma linha por país e faixa etária"""

    try:
        raw = pd.read_csv(url)
    except Exception as exc:  # rede indisponível, URL mudou, etc.
        print(f"[load_owid_age] falha ao baixar de {url} ({exc}); usando cópia local {local_fallback}")
        raw = pd.read_csv(local_fallback)

    raw = raw.rename(columns=_AGE_COLUMN_LABELS)
    id_vars = ["Entity", "Code", "Year"]
    value_vars = [c for c in raw.columns if c not in id_vars]

    long_df = raw.melt(id_vars=id_vars, value_vars=value_vars, var_name="age_group", value_name="ladder_mean")
    long_df = long_df.rename(columns={"Entity": "country", "Code": "iso3", "Year": "year"})
    long_df = long_df.dropna(subset=["iso3", "ladder_mean"])
    # mantém apenas códigos ISO3 de três letras
    long_df = long_df[long_df["iso3"].str.len() == 3]

    long_df["window"] = "2021-2023"
    return long_df.reset_index(drop=True)


# dados do Banco Mundial
WB_API_BASE = "https://api.worldbank.org/v2"

WB_INDICATORS = {
    "gdp_pc": "NY.GDP.PCAP.PP.KD",
    "pop": "SP.POP.TOTL",
    "area_km2": "AG.LND.TOTL.K2",
}

def _get_valid_country_iso3() -> set:
    """retorna códigos ISO3 de países, excluindo agregados regionais"""
    resp = requests.get(f"{WB_API_BASE}/country", params={"format": "json", "per_page": 400}, timeout=30)
    resp.raise_for_status()
    _, records = resp.json()
    return {
        r["id"]
        for r in records
        if r.get("region", {}).get("value") != "Aggregates"
    }


def fetch_wb(indicator_code: str, start_year: int = 2019, end_year: int = 2023) -> pd.Series:
    """busca um indicador e retorna o último valor disponível por país na janela informada"""

    valid_iso3 = _get_valid_country_iso3()
    resp = requests.get(
        f"{WB_API_BASE}/country/all/indicator/{indicator_code}",
        params={"format": "json", "date": f"{start_year}:{end_year}", "per_page": 20000},
        timeout=60,
    )
    resp.raise_for_status()
    payload = resp.json()
    records = payload[1] if len(payload) > 1 and payload[1] else []

    rows = [
        {"iso3": r["countryiso3code"], "year": int(r["date"]), "value": r["value"]}
        for r in records
        if r["value"] is not None and r["countryiso3code"] in valid_iso3
    ]
    if not rows:
        raise ValueError(f"Nenhum dado retornado pelo Banco Mundial para o indicador {indicator_code}")

    df = pd.DataFrame(rows).sort_values("year")
    latest = df.groupby("iso3")["value"].last()
    latest.name = indicator_code
    latest.index.name = "iso3"
    return latest


def build_country_table(start_year: int = 2019, end_year: int = 2023) -> pd.DataFrame:
    """Monta a tabela com PIB per capita, população e área de cada país."""
    resp = requests.get(f"{WB_API_BASE}/country", params={"format": "json", "per_page": 400}, timeout=30)
    resp.raise_for_status()
    _, country_records = resp.json()
    country_names = {
        r["id"]: r["name"] for r in country_records if r.get("region", {}).get("value") != "Aggregates"
    }

    series_list = []
    for column_name, indicator_code in WB_INDICATORS.items():
        series = fetch_wb(indicator_code, start_year, end_year)
        series = series.rename(column_name)
        series_list.append(series)

    table = pd.concat(series_list, axis=1).reset_index()
    table["country"] = table["iso3"].map(country_names)
    table = table.dropna(subset=["country"])
    return table[["iso3", "country", *WB_INDICATORS.keys()]].reset_index(drop=True)


# conversão de nomes de países

def to_iso3(names: pd.Series) -> pd.Series:
    """converte nomes de países para códigos ISO3 e informa nomes sem correspondência"""
    import country_converter as coco

    names = pd.Series(names)
    iso3 = coco.CountryConverter().pandas_convert(names, to="ISO3", not_found=None)
    unmatched = sorted(names[iso3.isna()].unique().tolist())
    if unmatched:
        print(f"[to_iso3] {len(unmatched)} nome(s) sem correspondência ISO3: {unmatched}")
    return iso3


# dados simulados para uso offline

def make_synthetic_age_data(country_table: pd.DataFrame, seed: int = 42) -> pd.DataFrame:
    """gera dados simulados de felicidade por faixa etária para uso alternativo offline"""
    rng = np.random.default_rng(seed)
    rows = []
    for _, row in country_table.iterrows():
        base = 2.5 + 0.55 * np.log(row["gdp_pc"])
        for age_group, age_mid in AGE_MID.items():
            u_shape = 0.0035 * (age_mid - 45) ** 2
            noise = rng.normal(0, 0.15)
            ladder_mean = float(np.clip(base + u_shape + noise, 0, 10))
            rows.append(
                {
                    "country": row["country"],
                    "iso3": row["iso3"],
                    "year": 2023,
                    "age_group": age_group,
                    "ladder_mean": round(ladder_mean, 3),
                    "window": "synthetic",
                    "synthetic": True,
                }
            )
    return pd.DataFrame(rows)
