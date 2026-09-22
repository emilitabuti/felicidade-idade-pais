# Felicidade por idade e por país

Laboratório de Machine Learning (regressão linear e logística, scikit-learn) que testa se a
felicidade segue uma **curva em U** ao longo da idade, combinando a escada de Cantril (Gallup /
World Happiness Report, via Our World in Data) com indicadores do Banco Mundial (PIB per capita,
população, área).

## Dupla

| | Nome | Usuário no GitHub |
| --- | --- | --- |
| Integrante 1 | Emili Vieira Tabuti | emilitabuti |
| Integrante 2 | Isabela Groke Gomes | Isa252 |

## Como rodar

- Python 3.12+
- `pip install -r requirements.txt`
- Abrir `PUCSP_CS_AI_10_AI_ML_Happines.ipynb` e rodar **Kernel → Restart & Run All**.

A pasta `cantril-ladder-age-groups/` contém uma cópia local dos dados usados pelo notebook. Ela serve como alternativa caso o download direto da fonte não esteja disponível no momento da execução.

## Resultados principais

- **Regressão linear:** a idade sozinha explica muito pouco da nota bruta de felicidade entre os países (R² ≈ 0,02). Ao acrescentar PIB per capita, população e área, o R² sobe para aproximadamente 0,63. Dentro dos países, a idade explica uma parcela maior da variação (R² ≈ 0,32–0,37), e o modelo quadrático apresenta ajuste melhor que o modelo linear. No modelo M3, o ponto mínimo estimado da curva ficou próximo de 63 anos.

- **Regressão logística:** usando a mediana como limite para classificar um grupo como “feliz”, o modelo obteve acurácia ≈ 0,80 e AUC ≈ 0,90 em países não vistos. Na comparação entre divisão por país e divisão aleatória, a regressão logística apresentou resultados semelhantes, enquanto o `RandomForestClassifier` teve desempenho maior na divisão aleatória, indicando possível vazamento de informação entre faixas etárias do mesmo país.

- As figuras e a discussão completa estão nas Seções 7 a 9 do notebook.

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
