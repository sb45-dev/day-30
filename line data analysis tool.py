import pandas as pd
import argparse


# Load CSV file
def load_data(filename):
    try:
        data = pd.read_csv(filename)
        return data
    except FileNotFoundError:
        print("❌ File not found!")
        return None
    except Exception as e:
        print("❌ Error:", e)
        return None


# Display summary
def show_summary(data):
    print("\n===== DATA SUMMARY =====")
    print("Rows:", len(data))
    print("Columns:", len(data.columns))

    print("\nColumn Names:")
    for column in data.columns:
        print("-", column)

    print("\nFirst 5 Rows:")
    print(data.head())


# Filter data
def filter_data(data, column, value):
    if column not in data.columns:
        print(f"❌ Column '{column}' does not exist.")
        print("Available columns:", list(data.columns))
        return

    result = data[data[column].astype(str).str.lower() == value.lower()]

    print("\n===== FILTERED DATA =====")

    if result.empty:
        print("No matching records found.")
    else:
        print(result.to_string(index=False))


# Group data
def group_data(data, column):
    if column not in data.columns:
        print(f"❌ Column '{column}' does not exist.")
        return

    print(f"\n===== GROUP BY {column} =====")
    print(data[column].value_counts())


# Statistical report
def statistics(data):
    print("\n===== STATISTICAL REPORT =====")

    numeric_data = data.select_dtypes(include="number")

    if numeric_data.empty:
        print("No numeric columns found.")
        return

    print(numeric_data.describe())


# Main program
def main():

    parser = argparse.ArgumentParser(
        description="Command-Line CSV Data Analysis Tool"
    )

    parser.add_argument(
        "file",
        help="Path of the CSV file"
    )

    parser.add_argument(
        "--summary",
        action="store_true",
        help="Display dataset summary"
    )

    parser.add_argument(
        "--filter",
        nargs=2,
        metavar=("COLUMN", "VALUE"),
        help="Filter data using column and value"
    )

    parser.add_argument(
        "--group",
        metavar="COLUMN",
        help="Group data by a column"
    )

    parser.add_argument(
        "--stats",
        action="store_true",
        help="Display statistical report"
    )

    args = parser.parse_args()

    # Load dataset
    data = load_data(args.file)

    if data is None:
        return

    # Execute selected command
    if args.summary:
        show_summary(data)

    elif args.filter:
        column, value = args.filter
        filter_data(data, column, value)

    elif args.group:
        group_data(data, args.group)

    elif args.stats:
        statistics(data)

    else:
        print("\nNo analysis option selected.")
        print("Use --help to see available commands.")


if __name__ == "__main__":
    main()