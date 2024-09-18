import pandas as pd
def calculate_segment_length(input_file, output_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(input_file)

    # Calculate the segment length and add it as a new column 'seq_length'
    df['seq_length'] = df['loc.end'] - df['loc.start']

    # Save the updated DataFrame to a new CSV file
    df.to_csv(output_file, index=False)

if __name__ == '__main__':
    # Define the input and output file paths
    input_file = 'brca_cnvs_tcga-1-2-2.csv'
    output_file = 'output.csv'

    # Call the function to process the file and generate the output
    calculate_segment_length(input_file, output_file)
