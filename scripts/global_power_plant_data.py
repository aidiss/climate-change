import pandas as pd

POWER_PLANT_DATASOURCE = "https://github.com/wri/global-power-plant-database/blob/master/output_database/global_power_plant_database.csv?raw=true"


def load_global_power_plant_data() -> pd.DataFrame:
    df = pd.read_csv(POWER_PLANT_DATASOURCE)
    return df
