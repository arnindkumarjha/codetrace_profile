import pandas as pd

def export_transformation_script(df, output_file='transformation_script.py'):
    """
    Exports a reproducible pandas transformation script based on the provided DataFrame.
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing the data to be transformed.
    output_file (str): The name of the output script file.
    """
    with open(output_file, 'w') as f:
        f.write("# Reproducible pandas transformation script\n\n")
        f.write("import pandas as pd\n\n")
        f.write("def load_data():\n")
        f.write("    df = pd.read_csv('data/sample_ui_data.csv')\n")
        f.write("    return df\n\n")
        
        f.write("def transform_data(df):\n")
        f.write("    # Example transformation steps\n")
        f.write("    df['new_column'] = df['existing_column'] * 2  # Modify as needed\n")
        f.write("    return df\n\n")
        
        f.write("if __name__ == '__main__':\n")
        f.write("    df = load_data()\n")
        f.write("    df = transform_data(df)\n")
        f.write("    print(df.head())\n")