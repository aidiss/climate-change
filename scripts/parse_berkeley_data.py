import kaggle
import zipfile
import pandas as pd


BERKLEY_DATA_SOURCE = "https://berkeley-earth-temperature.s3.us-west-1.amazonaws.com/Global/Complete_TAVG_daily.txt"


def load_TAVG_daily_data(url=BERKLEY_DATA_SOURCE):
    df = pd.read_csv(url, header=22)
    df.columns = df.columns.str.replace("% ", "")
    return df


def transform_text_to_rows(df):
    df["Date Number"] = df["Date Number"].str.strip().replace("\s+", ",", regex=True)
    df[list(df.columns)] = df["Date Number"].str.split(",", expand=True)

    return df


def get_TAVG_data():
    df = load_TAVG_daily_data(url=BERKLEY_DATA_SOURCE)
    df = transform_text_to_rows(df)
    return df
