import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def preprocess_data(df):
    """
    Perform preprocessing on the DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame to preprocess.

    Returns:
    pd.DataFrame: Preprocessed DataFrame.
    """
    # Example preprocessing steps
    df.dropna(inplace=True)  # Remove missing values
    # Add more preprocessing as needed
    return df

def main():
    file_path = '../data/product_order.csv'  # Adjust path as necessary
    data = load_data(file_path)
    if data is not None:
        processed_data = preprocess_data(data)
        print(processed_data.head())  # Display the first few rows of the processed data

if __name__ == "__main__":
    main()