import kaggle
import zipfile

CLIMATE_CHANGE_API = "berkeleyearth/climate-change-earth-surface-temperature-data"
ZIPED_FILE_DIRECTORY = "..//raw//ziped//climate-change-earth-surface-temperature-data.zip"
EXTRACTED_FILE_DIRECTORY = "..//raw//extracted files"


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