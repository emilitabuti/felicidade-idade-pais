# Felicidade por idade e por país

Laboratório de Machine Learning (regressão linear e logística, scikit-learn) que testa se a
felicidade segue uma **curva em U** ao longo da idade, combinando a escada de Cantril (Gallup /
World Happiness Report, via Our World in Data) com indicadores do Banco Mundial (PIB per capita,
população, área).

## Dupla

| | Nome | Usuário no GitHub |
| --- | --- | --- |
| Integrante 1 | Emili Vieira Tabuti | emilitabuti |
| Integrante 2 | *(preencha)* | *(preencha)* |

## Como rodar

- Python 3.12+
- `pip install -r requirements.txt`
- Abrir `PUCSP_CS_AI_10_AI_ML_Happines.ipynb` e rodar **Kernel → Restart & Run All**.

A pasta `cantril-ladder-age-groups/` está incluída no repositório porque `lab_helpers.load_owid_age()`
usa o CSV dela como cópia local de fallback quando a OWID bloqueia downloads automatizados (HTTP 403,
algo observado várias vezes durante o desenvolvimento) — sem ela, o notebook pode falhar ao rodar do
zero caso a fonte esteja bloqueada no momento da correção.

## Resultados principais

- **Regressão linear:** a idade sozinha quase não explica a nota bruta entre países (R² ≈ 0,02),
  mas explicar a riqueza (log PIB per capita, log população, log área) eleva o R² para ≈ 0,63.
  Olhando o desvio *dentro* de cada país, a idade já explica bem mais (R² ≈ 0,32–0,37) e o modelo
  quadrático (M2) supera a reta (M1) — a curva em U aparece, com mínimo estimado perto dos 63 anos.
- **Regressão logística:** classificando grupos como "feliz" (acima da mediana), o modelo atinge
  acurácia ≈ 0,80 e AUC ≈ 0,90 em países nunca vistos. Comparando divisão por país com divisão
  aleatória em 20 sementes, o `RandomForestClassifier` mostrou um AUC bem maior na divisão aleatória
  (vazamento de informação entre faixas etárias do mesmo país), enquanto a regressão logística foi
  mais estável entre as duas divisões.
- Ver as figuras e a discussão completa no notebook (Seções 7 a 9).

## Limitações

- Os dados por idade são médias de grupo por país (Gallup World Poll), não respostas individuais —
  o padrão da média não descreve necessariamente um indivíduo (falácia ecológica).
- A idade entra como o ponto médio de 4 faixas (22, 37, 52, 70), não em anos individuais.
- Um único corte transversal (2021-2023) mistura efeito de idade com efeito de coorte de nascimento.
- `AGE_MID["60+ years"] = 70` é uma suposição, já que essa faixa é aberta.
- Alguns países (ex.: Taiwan, Venezuela, Iêmen) foram descartados por falta de indicador do Banco Mundial.

## Fontes e datas de download

- **World Happiness Report** — planilha da Figura 2.1 (`WHR26_Data_Figure_2.1.xlsx`),
  baixada de https://files.worldhappiness.report/WHR26_Data_Figure_2.1.xlsx em 2026-09-21.
- **Our World in Data** — "Self-reported life satisfaction by age" (Cantril ladder por faixa etária,
  média 2021-2023), https://ourworldindata.org/grapher/cantril-ladder-age-groups, cópia local
  baixada em aula (`cantril-ladder-age-groups/`), citação: Gallup World Poll via World Happiness
  Report (2024) – processado pela Our World in Data.
- **Banco Mundial** — API pública (`NY.GDP.PCAP.PP.KD`, `SP.POP.TOTL`, `AG.LND.TOTL.K2`), consultada
  em 2026-09-21, último valor não faltante entre 2019 e 2023.
