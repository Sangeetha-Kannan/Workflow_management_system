import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def visualize_data(avg_expression_file_path, output_path):
    df_avg_expression = pd.read_csv(avg_expression_file_path)
    
    top_genes = df_avg_expression.nlargest(20, 'average_expression')

    plt.figure(figsize=(12, 8))
    sns.barplot(x='average_expression', y='ID_REF', data=top_genes, palette='viridis')
    plt.title('Top 20 Genes with Highest Average Expression')
    plt.xlabel('Average Expression Level')
    plt.ylabel('Gene')
    
    # Save the bar plot
    barplot_file_path = os.path.join(output_path, 'barplot_average_expression.png')
    plt.savefig(barplot_file_path)
    print(f"Bar plot saved to {barplot_file_path}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Visualize average gene expression data.")
    parser.add_argument("avg_expression_file_path", type=str, help="Path to the average expression data file.")
    parser.add_argument("output_path", type=str, help="Path to save the bar plot.")
    args = parser.parse_args()
    visualize_data(args.avg_expression_file_path, args.output_path)
