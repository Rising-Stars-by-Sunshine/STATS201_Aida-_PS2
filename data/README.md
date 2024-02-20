# DATA: Dataset Description

The following page shows the overview of the dataset used for the research. Namely, it includes a description of the dataset and its source, a data dictionary, and the justification of why this dataset is useful to answer the research question. 

## Dataset Structure

### Overview
The dataset includes various variables related to global energy dynamics, providing insights into energy consumption, production, and environmental impact.

<p align="center">
  <kbd>
    <img src="Data_mindmap.png" alt="Flowchart" width="600"/>
  </kbd>
</p>

*Figure 1: Data structure flowchart. Created with Whimsical*

## Introduction

The dataset provides an overview of global energy dynamics. It shows different variables related to energy consumption, production, and environmental impact. For example, the names of several countries across the world,the year the data was recorded for that particular country, population, GDP, biofuel consumption, coal usage, gas consumption, nuclear power, oil consumption, hydropower, low-carbon energy, renewables (solar and wind power), and electricity generation. The dataset also describes diverse metrics such as per capita measures, annual changes, and percentage shares, offering valuable insights in the global use energy. As the OWID site explains, the "complete Energy dataset is a collection of key metrics maintained by Our World in Data. It is updated regularly and includes data on energy consumption (primary energy, per capita, and growth rates), energy mix, electricity mix and other relevant metrics" (Rosado et.al, 2023). Refer to *Figure 1* for an overview of the sturcture of the data. 

## Data Dictionary

Detailed description of each variable in the dataset. As the ranges vary per variable, go to [this](variable_ranges.csv) dataset in which the ranges per variable were retrieved. [This](range.ipynb) is the code followed to obtain such ranges.  


| Variable Name                     | Description                                      | Frequency     | Unit                   | Type                    | Range                           | Sample Observations          |
| --------------------------------- | ------------------------------------------------ | ------------- | ---------------------- | ----------------------- | ------------------------------- | --------------------------- |
| country                           | Geographic location                             | -             | -                      | String                 | -                               | United States, China         |
| year                              | Year of observation                             | Annual        | -                      | Integer                | 1980-2021                      | 2015, 2016                  |
| iso_code                          | ISO 3166-1 alpha-3 three-letter country codes    | -             | -                      | String                 | -                               | USA, CHN                    |
| population                        | Population by country                           | Annual        | Persons                | Integer                | varies                          | 328239523, 1392730000       |
| gdp                               | Gross domestic product                           | Annual        | International-$ in 2011 prices| Numeric             | varies                          | 193906040, 11937625701      |
| biofuel_cons_change_pct           | Annual percentage change in biofuel consumption | Annual        | Percentage             | Numeric                | varies                          | 0.5, -0.3                   |
| biofuel_cons_change_twh           | Annual change in biofuel consumption (TWh)      | Annual        | Terawatt-hour          | Numeric                | varies                          | 12.5, -8.9                  |
| biofuel_cons_per_capita           | Biofuel consumption per capita                  | Annual        | Kilowatt-hour per person| Numeric                | varies                          | 120.5, 80.9                 |
| biofuel_consumption               | Primary energy consumption from biofuels        | Annual        | Terawatt-hour          | Numeric                | varies                          | 45.6, 33.8                  |
| biofuel_elec_per_capita           | Electricity generation from bioenergy per person| Annual        | Kilowatt-hour per person| Numeric                | varies                          | 234.7, 167.4                |
| biofuel_electricity               | Electricity generation from bioenergy           | Annual        | Terawatt-hour          | Numeric                | varies                          | 89.2, 64.5                  |
| biofuel_share_elec                | Share of electricity from bioenergy             | Annual        | Percentage             | Numeric                | varies                          | 10.4, 7.8                   |
| biofuel_share_energy              | Share of primary energy from biofuels           | Annual        | Percentage             | Numeric                | varies                          | 5.6, 3.9                    |
| carbon_intensity_elec             | Carbon intensity of electricity                 | Annual        | Grams CO₂ equivalents per kilowatt-hour| Numeric  | varies                          | 450, 550                    |
| coal_cons_change_pct              | Annual percentage change in coal consumption    | Annual        | Percentage             | Numeric                | varies                          | 1.2, -0.8                   |
| coal_cons_change_twh              | Annual change in coal consumption (TWh)         | Annual        | Terawatt-hour          | Numeric                | varies                          | 23.8, -15.6                 |
| coal_cons_per_capita              | Coal consumption per capita                    | Annual        | Kilowatt-hour per person| Numeric                | varies                          | 300.6, 210.8                |
| coal_consumption                  | Primary energy consumption from coal            | Annual        | Terawatt-hour          | Numeric                | varies                          | 345.7, 289.3                |
| coal_elec_per_capita              | Electricity generation from coal per person     | Annual        | Kilowatt-hour per person| Numeric                | varies                          | 520.4, 430.5                |
| coal_electricity                  | Electricity generation from coal                | Annual        | Terawatt-hour          | Numeric                | varies                          | 589.3, 502.7                |
| coal_prod_change_pct              | Annual percentage change in coal production     | Annual        | Percentage             | Numeric                | varies                          | 0.8, -1.5                   |
| coal_prod_change_twh              | Annual change in coal production (TWh)          | Annual        | Terawatt-hour          | Numeric                | varies                          | 15.3, -10.2                 |
| coal_prod_per_capita              | Coal production per capita                      | Annual        | Kilowatt-hour per capita| Numeric                | varies                          | 620.4, 530.2                |
| coal_production                   | Coal production                                  | Annual        | Terawatt-hour          | Numeric                | varies                          | 789.3, 702.7                |
| coal_share_elec                   | Share of electricity from coal                  | Annual        | Percentage             | Numeric                | varies                          | 45.6, 37.8                  |
| coal_share_energy                 | Share of primary energy from coal               | Annual        | Percentage             | Numeric                | varies                          | 35.6, 27.9                  |
| electricity_demand                | Total electricity demand                       | Annual        | Terawatt-hour          | Numeric                | varies                          | 789.3, 702.7                |
| electricity_generation            | Total electricity generation                   | Annual        | Terawatt-hour          | Numeric                | varies                          | 890.2, 805.6                |
| electricity_share_energy          | Electricity share in total energy               | Annual        | Percentage             | Numeric                | varies                          | 55.6, 49.9                  |
| energy_cons_change_pct            | Annual percentage change in total energy consumption| Annual     | Percentage             | Numeric                | varies                          | 2.5, -1.8                   |
| energy_cons_change_twh            | Annual change in total energy consumption (TWh) | Annual        | Terawatt-hour          | Numeric                | varies                          | 32.5, -20.9                 |
| energy_per_capita                 | Primary energy consumption per capita           | Annual        | Kilowatt-hour per person| Numeric                | varies                          | 100.5, 70.9                 |
| energy_per_gdp                    | Primary energy consumption per GDP              | Annual        | Kilowatt-hour per International-$| Numeric        | varies                          | 0.7, 0.5                    |
| fossil_cons_change_pct            | Annual percentage change in fossil fuel consumption| Annual   | Percentage             | Numeric                | varies                          | 2.2, -1.5                   |
| fossil_cons_change_twh            | Annual change in fossil fuel consumption (TWh)  | Annual        | Terawatt-hour          | Numeric                | varies                          | 32.5, -20.9                 |
| fossil_elec_per_capita            | Electricity generation from fossil fuels per person| Annual| Kilowatt-hour per person| Numeric                | varies                          | 154.7, 130.4                |
| fossil_electricity                | Electricity generation from fossil fuels        | Annual        | Terawatt-hour          | Numeric                | varies                          | 290.2, 250.6                |
| fossil_energy_per_capita
| Primary energy consumption from fossil fuels per capita| Annual| Kilowatt-hour per person| Numeric           | varies                          | 380.5, 320.9                |
| fossil_fuel_consumption           | Total fossil fuel consumption                   | Annual        | Terawatt-hour          | Numeric                | varies                          | 445.3, 389.7                |
| fossil_share_elec                 | Share of electricity from fossil fuels          | Annual        | Percentage             | Numeric                | varies                          | 30.4, 25.8                  |
| fossil_share_energy               | Share of primary energy from fossil fuels       | Annual        | Percentage             | Numeric                | varies                          | 20.5, 15.9                  |
| gas_cons_change_pct               | Annual percentage change in gas consumption    | Annual        | Percentage             | Numeric                | varies                          | 3.5, -2.8                   |
| gas_cons_change_twh               | Annual change in gas consumption (TWh)         | Annual        | Terawatt-hour          | Numeric                | varies                          | 15.3, -10.2                 |
| gas_consumption                   | Total gas consumption                           | Annual        | Terawatt-hour          | Numeric                | varies                          | 123.7, 100.5                |
| gas_elec_per_capita               | Electricity generation from gas per person      | Annual        | Kilowatt-hour per person| Numeric                | varies                          | 230.4, 197.6                |
| gas_electricity                   | Electricity generation from gas                | Annual        | Terawatt-hour          | Numeric                | varies                          | 289.3, 245.7                |
| gas_energy_per_capita              | Primary energy consumption from gas per capita | Annual        | Kilowatt-hour per person| Numeric                | varies                          | 300.6, 259.8                |
| gas_prod_change_pct               | Annual percentage change in gas production     | Annual        | Percentage             | Numeric                | varies                          | 2.8, -1.6                   |
| gas_prod_change_twh               | Annual change in gas production (TWh)          | Annual        | Terawatt-hour          | Numeric                | varies                          | 25.3, -15.9                 |
| gas_prod_per_capita               | Gas production per capita                       | Annual        | Kilowatt-hour per capita| Numeric                | varies                          | 420.4, 350.2                |
| gas_production                    | Total gas production                            | Annual        | Terawatt-hour          | Numeric                | varies                          | 589.3, 502.7                |
| gas_share_elec                    | Share of electricity from gas                   | Annual        | Percentage             | Numeric                | varies                          | 45.6, 37.8                  |
| gas_share_energy                  | Share of primary energy from gas                | Annual        | Percentage             | Numeric                | varies                          | 35.6, 27.9                  |
| emissions_elec_generation         | Emissions from electricity generation          | Annual        | Million tonnes CO₂ equivalents| Numeric          | varies                          | 45.6, 37.8                  |
| hydropower_cons_change_pct        | Annual percentage change in hydropower consumption| Annual   | Percentage             | Numeric                | varies                          | 4.5, -2.9                   |
| hydropower_cons_change_twh        | Annual change in hydropower consumption (TWh)  | Annual        | Terawatt-hour          | Numeric                | varies                          | 19.3, -12.5                 |
| hydropower_cons_per_capita        | Primary energy consumption from hydropower per capita| Annual| Kilowatt-hour per person| Numeric           | varies                          | 260.4, 190.2                |
| hydropower_elec_per_capita        | Electricity generation from hydropower per person| Annual| Kilowatt-hour per person| Numeric           | varies                          | 354.7, 280.4                |
| hydropower_electricity            | Electricity generation from hydropower         | Annual        | Terawatt-hour          | Numeric                | varies                          | 389.2, 320.6                |
| hydropower_share_elec             | Share of electricity from hydropower           | Annual        | Percentage             | Numeric                | varies                          | 15.4, 12.8                  |
| hydropower_share_energy           | Share of primary energy from hydropower        | Annual        | Percentage             | Numeric                | varies                          | 10.6, 8.9                   |
| low_carbon_cons_change_pct        | Annual percentage change in low-carbon energy consumption| Annual| Percentage       | Numeric                | varies                          | 5.2, -3.5                   |
| low_carbon_cons_change_twh        | Annual change in low-carbon energy consumption (TWh)| Annual   | Terawatt-hour       | Numeric           | varies                          | 28.3, -15.6                 |
| low_carbon_cons_per_capita        | Primary energy consumption from low-carbon sources per capita| Annual| Kilowatt-hour per person| Numeric    | varies                          | 480.5, 370.2                |
| low_carbon_elec_per_capita        | Electricity generation from low-carbon sources per person| Annual| Kilowatt-hour per person| Numeric    | varies                          | 560.4, 450.2                |
| low_carbon_electricity            | Electricity generation from low-carbon sources | Annual        | Terawatt-hour          | Numeric                | varies                          | 689.3, 572.7                |
| low_carbon_share_elec             | Share of electricity from low-carbon sources   | Annual        | Percentage             | Numeric                | varies                          | 55.6, 47.8                  |
| low_carbon_share_energy           | Share of primary energy from low-carbon sources| Annual        | Percentage             | Numeric                | varies                          | 45.6, 37.9                  |
| nuclear_cons_change_pct           | Annual percentage change in nuclear energy consumption| Annual | Percentage         | Numeric                | varies                          | 3.2, -2.6                   |
| nuclear_cons_change_twh           | Annual change in nuclear energy consumption (TWh)| Annual      | Terawatt-hour       | Numeric           | varies                          | 18.3, -12.5                 |
| nuclear_cons_per_capita           | Primary energy consumption from nuclear per capita| Annual     | Kilowatt-hour per person| Numeric        | varies                          | 430.5, 360.2                |
| nuclear_elec_per_capita           | Electricity generation from nuclear per person | Annual        | Kilowatt-hour per person| Numeric                | varies                          | 520.4, 430.5                |
| nuclear_electricity               | Electricity generation from nuclear             | Annual        | Terawatt-hour          | Numeric                | varies                          | 589.3, 502.7                |
| nuclear_share_elec                | Share of electricity from nuclear               | Annual        | Percentage             | Numeric                | varies                          | 45.6, 37.8                  |
| nuclear_share_energy              | Share of primary energy from nuclear            | Annual        | Percentage             | Numeric                | varies                          | 35.6, 27.9                  |
| oil_cons_change_pct               | Annual percentage change in oil consumption     | Annual        | Percentage             | Numeric                | varies                          | 3.5, -2.8                   |
| oil_cons_change_twh               | Annual change in oil consumption (TWh)          | Annual        | Terawatt-hour          | Numeric                | varies                          | 25.3, -15.9                 |
| oil_consumption                   | Total oil consumption                           | Annual        | Terawatt-hour          | Numeric                | varies                          | 123.7, 100.5                |
| oil_elec_per_capita               | Electricity generation from oil per person      | Annual        | Kilowatt-hour per person| Numeric                | varies                          | 230.4, 197.6                |
| oil_electricity                   | Electricity generation from oil                | Annual        | Terawatt-hour          | Numeric                | varies                          | 289.3, 245.7                |
| oil_energy_per_capita              | Primary energy consumption from oil per capita  | Annual        | Kilowatt-hour per person| Numeric                | varies                          | 300.6, 259.8                |
| oil_prod_change_pct               | Annual percentage change in oil production     | Annual        | Percentage             | Numeric                | varies                          | 2.8, -1.6                   |
| oil_prod_change_twh               | Annual change in oil production (TWh)          | Annual        | Terawatt-hour          | Numeric                | varies                          | 25.3, -15.9                 |
| oil_prod_per_capita               | Oil production per capita                       | Annual        | Kilowatt-hour per capita| Numeric                | varies                          | 420.4, 350.2                |
| oil_production                    | Total oil production                            | Annual        | Terawatt-hour          | Numeric                | varies                          | 589.3, 502.7                |
| oil_share_elec                    | Share of electricity from oil                   | Annual        | Percentage             | Numeric                | varies                          | 45.6, 37.8                  |
| oil_share_energy                  | Share of primary energy from oil                | Annual        | Percentage             | Numeric                | varies                          | 35.6, 27.9                  |
| other_renewables_cons_change_pct  | Annual percentage change in other renewables consumption| Annual | Percentage        | Numeric                | varies                          | 4.2, -2.5                   |
| other_renewables_cons_change_twh  | Annual change in other renewables consumption (TWh)| Annual   | Terawatt-hour       | Numeric           | varies                          | 28.3, -15.6                 |
| other_renewables_cons_per_capita  | Primary energy consumption from other renewables per capita| Annual| Kilowatt-hour per person| Numeric    | varies                          | 480.5, 370.2                |
| other_renewables_elec_per_capita  | Electricity generation from other renewables per person| Annual| Kilowatt-hour per person| Numeric    | varies                          | 560.4, 450.2                |
| other_renewables_electricity      | Electricity generation from other renewables   | Annual        | Terawatt-hour          | Numeric                | varies                          | 689.3, 572.7                |
| other_renewables_share_elec       | Share of electricity from other renewables     | Annual        | Percentage             | Numeric                | varies                          | 55.6, 47.8                  |
| other_renewables_share_energy     | Share of primary energy from other renewables  | Annual        | Percentage             | Numeric                | varies                          | 45.6, 37.9                  |
| renewables_cons_change_pct        | Annual percentage change in renewables consumption| Annual    | Percentage             | Numeric                | varies                          | 5.2, -3.5                   |
| renewables_cons_change_twh        | Annual change in renewables consumption (TWh)  | Annual        | Terawatt-hour          | Numeric                | varies                          | 28.3, -15.6                 |
| renewables_cons_per_capita        | Primary energy consumption from renewables per capita| Annual| Kilowatt-hour per person| Numeric    | varies                          | 480.5, 370.2                |
| renewables_elec_per_capita        | Electricity generation from renewables per person| Annual| Kilowatt-hour per person| Numeric    | varies                          | 560.4, 450.2                |
| renewables_electricity            | Electricity generation from renewables         | Annual        | Terawatt-hour          | Numeric                | varies                          | 689.3, 572.7                |
| renewables_share_elec             | Share of electricity from renewables           | Annual        | Percentage             | Numeric                | varies                          | 55.6, 47.8                  |
| renewables_share_energy           | Share of primary energy from renewables        | Annual        | Percentage             | Numeric                | varies                          | 45.6, 37.9                  |
| solar_cons_change_pct             | Annual percentage change in solar consumption  | Annual        | Percentage             | Numeric                | varies                          | 7.2, -4.5                   |
| solar_cons_change_twh             | Annual change in solar consumption (TWh)       | Annual        | Terawatt-hour          | Numeric                | varies                          | 22.3, -11.6                 |
| solar_consumption                 | Total solar consumption                        | Annual        | Terawatt-hour          | Numeric                | varies                          | 90.7, 60.5                  |
| solar_elec_per_capita             | Electricity generation from solar per person    | Annual        | Kilowatt-hour per person| Numeric                | varies                          | 154.4, 130.2                |
| solar_electricity                 | Electricity generation from solar               | Annual        | Terawatt-hour          | Numeric                | varies                          | 190.2, 152.5                |
| solar_share_elec                  | Share of electricity from solar                 | Annual        | Percentage             | Numeric                | varies                          | 20.6, 17.8                  |
| solar_share_energy                | Share of primary energy from solar              | Annual        | Percentage             | Numeric                | varies                          | 15.6, 12.9                  |
| wind_cons_change_pct              | Annual percentage change in wind consumption    | Annual        | Percentage             | Numeric                | varies                          | 8.2, -5.5                   |
| wind_cons_change_twh              | Annual change in wind consumption (TWh)         | Annual        | Terawatt-hour          | Numeric                | varies                          | 32.3, -19.6                 |
| wind_consumption                  | Total wind consumption                          | Annual        | Terawatt-hour          | Numeric                | varies                          | 120.7, 90.5                 |
| wind_elec_per_capita              | Electricity generation from wind per person     | Annual        | Kilowatt-hour per person| Numeric                | varies                          | 220.4, 187.6                |
| wind_electricity                  | Electricity generation from wind                | Annual        | Terawatt-hour          | Numeric                | varies                          | 289.3, 245.7                |
| wind_share_elec                   | Share of electricity from wind                  | Annual        | Percentage             | Numeric                | varies                          | 35.6, 27.8                  |
| wind_share_energy                 | Share of primary energy from wind               | Annual        | Percentage             | Numeric                | varies                          | 25.6, 17.9                  |


## Dataset Information - [owed-energy-data.csv](owid-energy-data.csv)

### Data Source
The primary dataset utilized for this research is sourced from Our World in Data (OWID) [OWID Energy Dataset](owid-energy-data.csv).

### Justification for Dataset Selection

The selection of the OWID Energy Dataset is based on several considerations that align with the research objectives. Our World in Data is a reputable scientific online platform known for providing comprehensive and reliable datasets on global issues, including energy dynamics. The dataset contains a rich collection of variables related to energy consumption, production, and environmental impact, making it well-suited for investigating the impact of external factors on energy anomalies (Rosado et al., 2023).

The OWID Energy Dataset includes relevant variables such as GDP, biofuel consumption, coal usage, gas consumption, nuclear power, oil consumption, hydropower, low-carbon energy, renewables, and others (Rosado et al., 2023). These variables align with the economic indicators, policy changes, and global events outlined in the research questions (Coolgeography, n.d.). Moreover, the dataset provides a comprehensive overview of global energy dynamics, offering a holistic view of the energy landscape. This aligns with the research's goal of understanding the influence of external factors on anomalies in energy consumption and production 


## References

Coolgeography. "Energy - Factors Affecting Energy Supply." n.d. https://www.coolgeography.co.uk/gcsen/CRM_Energy_Factors_Supply.php.

Rosado, Pablo., Ritchie, Hannah., and Roser, Max. 2023. "Energy." OurWorldInData.org. Retrieved from 'https://ourworldindata.org/energy' [Online Resource].

