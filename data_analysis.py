import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    return df

def analyze_stats(df):
    summary = df.describe()
    correlation = df.corr()
    return summary, correlation

if __name__ == "__main__":
    print("Data Analysis Module Started")
