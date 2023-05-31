import kaggle
import zipfile
import pandas as pd
import os


CLIMATE_CHANGE_API = "berkeleyearth/climate-change-earth-surface-temperature-data"

ZIPED_FILE_DIRECTORY = "raw//ziped//climate-change-earth-surface-temperature-data.zip"
EXTRACTED_FILE_DIRECTORY = "raw//extracted files"
KAGGLE_DATASET_FILENAME = "//GlobalTemperatures.csv"

BERKLEY_DATA_SOURCE = "https://berkeley-earth-temperature.s3.us-west-1.amazonaws.com/Global/Complete_TAVG_daily.txt"

JSON_PATH = (
    "https://nyc3.digitaloceanspaces.com/owid-public/data/energy/owid-energy-data.json"
)
XLSX_PATH = (
    "https://nyc3.digitaloceanspaces.com/owid-public/data/energy/owid-energy-data.xlsx"
)
CSV_PATH = (
    "https://nyc3.digitaloceanspaces.com/owid-public/data/energy/owid-energy-data.csv"
)


def download_files() -> None:
    kaggle.api.dataset_download_files(
        dataset=CLIMATE_CHANGE_API,
        path="raw//ziped",
        quiet=False,
        force=False,
    )


def unzip_file() -> None:
    path = ZIPED_FILE_DIRECTORY
    with zipfile.ZipFile(path, "r") as zip_ref:
        zip_ref.extractall(EXTRACTED_FILE_DIRECTORY)


def download_json_world_energy_dataset():
    json_dataset = pd.read_json(JSON_PATH)
    return json_dataset


def load_kaggle_dataframe() -> pd.DataFrame:
    path = EXTRACTED_FILE_DIRECTORY + KAGGLE_DATASET_FILENAME
    if not os.path.isfile(path):
        download_files()
        unzip_file()
    df = pd.read_csv(path)
    return df


def download_xlsx_world_energy_dataset():
    excel_dataset = pd.read_excel(XLSX_PATH)
    return excel_dataset


def download_csv_world_energy_dataset():
    csv_dataset = pd.read_csv(CSV_PATH)
    return csv_dataset
