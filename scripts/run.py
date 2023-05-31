from main import load_kaggle_dataframe
import argparse

if __name__ == "__main__":
    # Get our arguments from the user
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument(
        "--load_kaggle_dataframe", help="Load kaggle dataset", action="store_true"
    )

    args = parser.parse_args()

    if args.load_kaggle_dataframe:
        df = load_kaggle_dataframe()
        print(df)
