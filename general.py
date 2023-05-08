import pandas as pd

BERKLEY_DATA_SOURCE = "https://berkeley-earth-temperature.s3.us-west-1.amazonaws.com/Global/Complete_TAVG_daily.txt"


def parse_berkley_earth_temperature_dataset(url=BERKLEY_DATA_SOURCE):
    df = pd.read_csv(
        url,
        header=22,
    )
    df.columns = df.columns.str.replace("% ", "")
    return df
