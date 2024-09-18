import csv #This is for including csv module.

# Here first I need to define input and output file. Input file should be in the same folder wıth my py code.
input_file = 'brca_cnvs_tcga-1-2-2.csv'
output_file = 'brca_cnvs_tcga_result.csv'

# The aim of the assignment to calculate the length of each segment so we use funtions.
def calculate_length(start, end):
    return int(end) - int(start)

# To create new output file with the new column information by reading the input CSV and writing to a new CSV with the additional column.
with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Read the header and add the new column name 'seq_length'
    header = next(reader)
    header.append('seq_length')
    writer.writerow(header)

    # Process each row, compute segment length, and write to the output file
    for row in reader:
        loc_start = row[2]
        loc_end = row[3]
        seq_length = calculate_length(loc_start, loc_end)
        row.append(seq_length)
        writer.writerow(row)

