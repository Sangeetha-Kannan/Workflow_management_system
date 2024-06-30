import pandas as pd
import os

def calculate_average_expression(df):
    expression_columns = df.columns[1:]  # Assuming the first column is not expression data
    df[expression_columns] = df[expression_columns].apply(pd.to_numeric, errors='coerce')
    df['average_expression'] = df[expression_columns].mean(axis=1)
    return df[['ID_REF', 'average_expression']]

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Process gene expression data.")
    parser.add_argument("input_file", type=str, help="Path to the input data file.")
    parser.add_argument("output_path", type=str, help="Path to save the processed data.")
    args = parser.parse_args()

    df = pd.read_csv(args.input_file, sep='\t', comment='!', compression='gzip', low_memory=False)
    df_avg_expression = calculate_average_expression(df.copy())
    avg_expression_file_path = os.path.join(args.output_path, "average_expression.csv")
    df_avg_expression.to_csv(avg_expression_file_path, index=False)
    print(f"Average expression data saved to {avg_expression_file_path}")
