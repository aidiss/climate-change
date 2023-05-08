import kaggle

DATASET_LINK = "berkeleyearth/climate-change-earth-surface-temperature-data"


def download_dataset() -> None:
    kaggle.api.dataset_download_files(
        dataset=DATASET_LINK,
        path="data",
        unzip=True,
        quiet=False,
        force=False,
    )


if __name__ == "__main__":
    download_dataset()
