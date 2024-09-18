import pandas as pd
def calculate_length(input_file, output_file):
    # Conversion from csv to Pandas
    df = pd.read_csv(input_file)

    # To calculate the segment length here we use funtions and we are adding it as a new column 'seq_length'
    df['seq_length'] = df['loc.end'] - df['loc.start']

    # Conversion from Pandas to csv
    df.to_csv(output_file, index=False)

if __name__ == '__main__':
    input_file = 'brca_cnvs_tcga-1-2-2.csv'
    output_file = 'output.csv'

    calculate_length(input_file, output_file)
