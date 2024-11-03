"""Module for handling gene expression data processing."""

from collections import defaultdict


class GeneExpressionData:
    """Class for handling gene expression data from liver cancer samples."""

    def __init__(self, path: str):
        """Initialize with file path."""
        self.path = path
        self.dict_gene_hcc = self.load_data()[0]
        self.dict_gene_normal = self.load_data()[1]
        self.dict_sample = self.load_data()[2]

    def load_data(self):
        """
        Load expression data from file and returns 3 dictionaries.

        Two dictionaries that contain genes as keys (in columns) and
        their expression values as lists.
        These dictionaries are categorized based on their type.
        The third dictionary contains samples as keys and
        a list of lists of their expression values.
        """
        try:
            # Initialize dictionaries
            dict_sample = {} # Dictionary to hold sample information
            dict_gene_hcc = defaultdict(list) # Dictionary for HCC gene expressions
            dict_gene_normal = defaultdict(list) # Dictionary for normal gene expressions

            # Read and parse file
            with open(self.path, 'r', encoding='utf-8') as liver_file:
                # Get header row with gene names
                line1 = liver_file.readline()
                keys = line1.split(',')
                # Skip first 2 columns (sample, type)
                keys = [key.strip() for key in keys[2:]]

                # Process each data row
                for line in liver_file:
                    words = line.split(',') # Split each line by commas
                    sample = words[0]  # Sample Id
                    gene_type = words[1]  # HCC or normal
                    # Expression values
                    items = [float(value) for value in words[2:]]
                    # Store sample info
                    dict_sample[sample] = [gene_type, items]

                    # Store expressions by type
                    for col, item in enumerate(items):
                        if gene_type == 'HCC':
                            dict_gene_hcc[keys[col]].append(item)
                        if gene_type == 'normal':
                            dict_gene_normal[keys[col]].append(item)
            return dict_gene_hcc, dict_gene_normal, dict_sample
        except FileNotFoundError:
            raise FileNotFoundError("There is not any file.")

    def return_list_gene_name(self, dict_gene_hcc):
        """Get list of gene names from HCC data and returns list of gene names."""
        return list(dict_gene_hcc.keys())

    def return_list_sample(self, dict_sample):
        """Get list of sample IDs and returns a list of sample IDs."""
        return list(dict_sample.keys())

    def expression_sample(self, dict_sample):
        """
        Get expression values for all samples and returns
        a list of expression values for each sample.
        """
        expression_sample_dict = {}
        for sample, values in dict_sample.items():
            expression_sample_dict[sample] = values[1]
        return expression_sample_dict

    def find_dict_desired_expression(
           self,
           desired_gene_name):
        """
        Get expression values for a specific gene and returns
        a Combined list of expression values for the gene.
        """
        dict_desired_expression = {}
        for gene in desired_gene_name:
            value_hcc = self. dict_gene_hcc[gene]
            value_normal = self.dict_gene_normal[gene]
            dict_desired_expression[gene] = value_hcc + value_normal
        return dict_desired_expression