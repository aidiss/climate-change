import kaggle
import zipfile
import pandas as pd


CLIMATE_CHANGE_API = "berkeleyearth/climate-change-earth-surface-temperature-data"
ZIPED_FILE_DIRECTORY = "..//raw//ziped//climate-change-earth-surface-temperature-data.zip"
EXTRACTED_FILE_DIRECTORY = "..//raw//extracted files"

BERKLEY_DATA_SOURCE = "https://berkeley-earth-temperature.s3.us-west-1.amazonaws.com/Global/Complete_TAVG_daily.txt"


def download_files() -> None:
    kaggle.api.dataset_download_files(
        dataset=CLIMATE_CHANGE_API,
        path="ziped",
        quiet=False,
        force=False,
    )


def unzip_file() -> None:
    path = ZIPED_FILE_DIRECTORY
    with zipfile.ZipFile(path, "r") as zip_ref:
        zip_ref.extractall(EXTRACTED_FILE_DIRECTORY)


def parse_berkley_earth_temperature_dataset(url=BERKLEY_DATA_SOURCE):
    df = pd.read_csv(url, header=22)
    df.columns = df.columns.str.replace("% ", "")
    return df
