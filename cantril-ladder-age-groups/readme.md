# Self-reported life satisfaction by age - Data package

This data package contains the data that powers the chart ["Self-reported life satisfaction by age"](https://ourworldindata.org/grapher/cantril-ladder-age-groups?v=1&csvType=full&useColumnShortNames=false) on the Our World in Data website.

### Active Filters

A filtered subset of the full data was downloaded. The following filters were applied:

## CSV structure

Each row is an observation for an entity (usually a country or region) at a timepoint.

- "Entity" — the name of the entity, e.g. "United States".
- "Code" — our internal entity code. For most countries this is the [ISO alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code, e.g. "USA"; historical and other non-standard entities get a custom code.
- "Year" or "Day" — the timepoint. Annual data has a "Year" column holding an integer year; otherwise a "Day" column holds a date string in the form "YYYY-MM-DD".
- Every remaining column is a data column, each one a time series. Downloaded with the "full data" option each corresponds to one time series below; with "only selected data visible in the chart" they are transformed depending on the chart type, so the correspondence may be less direct.


## Metadata.json structure

The .metadata.json file contains metadata about the data package. The "charts" key contains information to recreate the chart, like the title, subtitle etc. The "columns" key contains information about each of the columns in the csv, like the unit, timespan covered, citation for the data etc.

## How we process data at Our World in Data

Our World in Data is almost never the original producer of the data - almost all of the data we use has been compiled by others. If you want to re-use data, it is your responsibility to ensure that you adhere to the sources' license and to credit them correctly. Please note that a single time series may have more than one source - e.g. when we stitch together data from different time periods by different producers or when we calculate per capita metrics using population data from a second source.

Preparing this data involves several processing steps. Depending on the data, this can include standardizing country names and world region definitions, converting units, calculating derived indicators such as per capita measures, as well as adding or adapting metadata such as the name or the description given to an indicator.
[Read about our data pipeline](https://docs.owid.io/projects/etl/).

## Detailed information about each time series


### Self-reported life satisfaction (up to 29 years)
Average of survey responses for people aged up to 29 years. The survey question asks respondents their current position on a hypothetical ladder, where the best possible life for them is a 10, and the worst possible life is a 0.
Last updated: April 1, 2025  
Date range: 2023–2023  
Source: Gallup World Poll via the World Happiness Report (2024) – processed by Our World in Data  

#### How to cite this data

Gallup World Poll via the World Happiness Report (2024) – processed by Our World in Data

#### What you should know about this data
- The Cantril ladder asks respondents to think of a ladder, with the best possible life for them being a 10 and the worst possible life being a 0. They are then asked to rate their own current lives on that 0 to 10 scale.
- The rankings are three-year averages, calculated by the World Happiness Report based on nationally representative samples collected by the Gallup World Poll. This data is averaged over the responses from 2021 to 2023.
- The number of people and countries surveyed varies year to year, but typically more than 100,000 people in 130 countries participate in the Gallup World Poll each year.
- The rankings are based entirely on the survey scores, using the Gallup weights to make the estimates representative.

#### Notes on our processing step for this indicator
Average of regions is calculated by taking a population-weighted average over all countries within that region.


### Self-reported life satisfaction (30-44 years)
Average of survey responses for people aged 30-44 years. The survey question asks respondents their current position on a hypothetical ladder, where the best possible life for them is a 10, and the worst possible life is a 0.
Last updated: April 1, 2025  
Date range: 2023–2023  
Source: Gallup World Poll via the World Happiness Report (2024) – processed by Our World in Data  

#### How to cite this data

Gallup World Poll via the World Happiness Report (2024) – processed by Our World in Data

#### What you should know about this data
- The Cantril ladder asks respondents to think of a ladder, with the best possible life for them being a 10 and the worst possible life being a 0. They are then asked to rate their own current lives on that 0 to 10 scale.
- The rankings are three-year averages, calculated by the World Happiness Report based on nationally representative samples collected by the Gallup World Poll. This data is averaged over the responses from 2021 to 2023.
- The number of people and countries surveyed varies year to year, but typically more than 100,000 people in 130 countries participate in the Gallup World Poll each year.
- The rankings are based entirely on the survey scores, using the Gallup weights to make the estimates representative.

#### Notes on our processing step for this indicator
Average of regions is calculated by taking a population-weighted average over all countries within that region.


### Self-reported life satisfaction (45-59 years)
Average of survey responses for people aged 45-59 years. The survey question asks respondents their current position on a hypothetical ladder, where the best possible life for them is a 10, and the worst possible life is a 0.
Last updated: April 1, 2025  
Date range: 2023–2023  
Source: Gallup World Poll via the World Happiness Report (2024) – processed by Our World in Data  

#### How to cite this data

Gallup World Poll via the World Happiness Report (2024) – processed by Our World in Data

#### What you should know about this data
- The Cantril ladder asks respondents to think of a ladder, with the best possible life for them being a 10 and the worst possible life being a 0. They are then asked to rate their own current lives on that 0 to 10 scale.
- The rankings are three-year averages, calculated by the World Happiness Report based on nationally representative samples collected by the Gallup World Poll. This data is averaged over the responses from 2021 to 2023.
- The number of people and countries surveyed varies year to year, but typically more than 100,000 people in 130 countries participate in the Gallup World Poll each year.
- The rankings are based entirely on the survey scores, using the Gallup weights to make the estimates representative.

#### Notes on our processing step for this indicator
Average of regions is calculated by taking a population-weighted average over all countries within that region.


### Self-reported life satisfaction (60+ years)
Average of survey responses for people aged 60+ years. The survey question asks respondents their current position on a hypothetical ladder, where the best possible life for them is a 10, and the worst possible life is a 0.
Last updated: April 1, 2025  
Date range: 2023–2023  
Source: Gallup World Poll via the World Happiness Report (2024) – processed by Our World in Data  

#### How to cite this data

Gallup World Poll via the World Happiness Report (2024) – processed by Our World in Data

#### What you should know about this data
- The Cantril ladder asks respondents to think of a ladder, with the best possible life for them being a 10 and the worst possible life being a 0. They are then asked to rate their own current lives on that 0 to 10 scale.
- The rankings are three-year averages, calculated by the World Happiness Report based on nationally representative samples collected by the Gallup World Poll. This data is averaged over the responses from 2021 to 2023.
- The number of people and countries surveyed varies year to year, but typically more than 100,000 people in 130 countries participate in the Gallup World Poll each year.
- The rankings are based entirely on the survey scores, using the Gallup weights to make the estimates representative.

#### Notes on our processing step for this indicator
Average of regions is calculated by taking a population-weighted average over all countries within that region.


## Sources

These are the sources behind the data in this package. Each time series above names the ones it draws on in its citation.

### Gallup World Poll via the World Happiness Report – World Happiness Report

The World Happiness Report is a partnership of Gallup, the Oxford Wellbeing Research Centre, the UN Sustainable Development Solutions Network, and the WHR’s Editorial Board.
      It reviews the state of happiness in the world today and shows how the science of happiness explains personal and national variations in happiness.

Producer: Gallup World Poll via the World Happiness Report  
Published: 2024-03-08  
Retrieved on: 2025-04-01  
Retrieved from: https://happiness-report.s3.amazonaws.com/2024/Ch2+Appendix.pdf  
License: World Happiness Report - Data sharing policy (https://worldhappiness.report/data-sharing/)  

Citation: Helliwell, J. F., Layard, R., Sachs, J. D., De Neve, J.-E., Aknin, L. B., & Wang, S. (Eds.). (2024). World Happiness Report 2024. University of Oxford: Wellbeing Research Centre.

    