import kaggle


def download_dataset() -> None:
    kaggle.api.dataset_download_files(
        dataset="berkeleyearth/climate-change-earth-surface-temperature-data",
        path="data",
        unzip=True,
        quiet=False,
        force=False,
    )


if __name__ == "__main__":
    download_dataset()
