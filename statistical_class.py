"""Module for statistical analysis of gene expression data."""

import math
#find_dict_desired_expression
class StatisticalAnalysis:
    """
    A class for performing statistical analysis on gene expression data.
    Handles calculations for HCC (Hepatocellular Carcinoma) and normal tissue samples.
    """

    def __init__(self, expression_obj):
        """Initialize with a gene expression data object."""
        self.expression_obj = expression_obj

    def calculate_mean(self, desired_gene):
        """
        Calculate mean expression values for specified genes and returns
        a dictionary mapping gene names to their mean expression values.
        """

        # Get expression data for HCC and normal samples
        expressions_hcc = self.expression_obj.dict_gene_hcc
        expressions_normal = self.expression_obj.dict_gene_normal

        dict_desired = {}
        mean_dict = {}

        # Calculate mean for each gene
        for gene_name in desired_gene:
            if gene_name not in expressions_hcc or gene_name not in expressions_normal:
                raise ValueError(f"Gene {gene_name} not found")
            # Combine expressions
            dict_desired[gene_name] = expressions_hcc[gene_name] + expressions_normal[gene_name]

            if not dict_desired[gene_name]:
                raise ValueError(f"No expressions for {gene_name}")
            # Calculate mean
            total = sum(dict_desired[gene_name])
            mean = total / len(dict_desired[gene_name])
            mean_dict[gene_name] = round(mean, 3)

            # Create a title dictionary for output formatting
            title_dict = {"Desired gene name": "Mean expression"}

            # Combine title dictionary with the mean dictionary
            mean_dict = {**title_dict, **mean_dict}
        return mean_dict

    def calculate_median(self, desired_gene):
        """Calculate median for desired genes and returns a dictionary
          with gene names and median values."""

        # Get expression data
        expressions_hcc = self.expression_obj.dict_gene_hcc
        expressions_normal = self.expression_obj.dict_gene_normal

        dict_desired = {}
        median_dict = {}

        # Calculate median for each gene
        for gene_name in desired_gene:
            if gene_name not in expressions_hcc or gene_name not in expressions_normal:
                raise ValueError(f"Gene {gene_name} not found")

            # Get and sort expressions
            dict_desired[gene_name] = expressions_hcc[gene_name] + expressions_normal[gene_name]
            list_sort = sorted(dict_desired[gene_name])
            len_expression = len(list_sort)

            # Calculate median based on odd/even length
            if (len_expression % 2) == 0:
                # For even length, average the two middle numbers
                median = (list_sort[math.floor(len_expression / 2)] +
                        list_sort[math.floor(len_expression / 2) + 1]) / 2
                median_dict[gene_name] = round(median, 3)
            else:
                # For odd length, take the middle number
                median = list_sort[math.floor(len_expression/2) + 1]
                median_dict[gene_name] = round(median, 3) 

            # Create a title dictionary for output formatting
            title_dict = {"Desired gene name": "Median expression"}
            # Combine title dictionary with the median dictionary
            median_dict = {**title_dict, **median_dict}

        return median_dict
     
    def calculate_standard_deviation_variance(self, desired_gene):
        """Calculate variance and standard deviation and returns two dictionaries."""

        # Get expression data
        expressions_hcc = self.expression_obj.dict_gene_hcc
        expressions_normal = self.expression_obj.dict_gene_normal

        dict_desired = {}
        dict_std_dev = {}
        dict_var = {}

        # Get means first
        mean = self.calculate_mean(desired_gene)

        # Calculate variance and std dev for each gene
        for gene_name in desired_gene:
            if gene_name not in expressions_hcc or gene_name not in expressions_normal:
                raise ValueError(f"Gene {gene_name} not found")

            dict_desired[gene_name] = expressions_hcc[gene_name] + expressions_normal[gene_name]

            # Calculate variance
            try:
                variance = sum((expr - mean[gene_name])**2
                                for expr in dict_desired[gene_name]) / len(dict_desired[gene_name])
            except ZeroDivisionError as error:
                raise ValueError(f"No expressions for {gene_name}") from error

            # Calculate standard deviation
            standard_deviation = math.sqrt(variance)

            dict_var[gene_name] = variance
            dict_std_dev[gene_name] = standard_deviation

        # Create a title dictionary for output formatting
        title_dict_var = {"Desired gene name": "Variance of expression"}
        title_dict_dev= {"Desired gene name": "standard devition of expression"}

        # Combine title dictionary with the varince and std_dev dictionaries
        dict_var = {**title_dict_var, **dict_var}    
        dict_std_dev = {**title_dict_dev, **dict_std_dev}

        return dict_var, dict_std_dev
       
    def calculate_mean_gene_hcc(self, desired_gene):
        """Calculate mean for HCC samples only returns a dictionary with HCC means."""
    
        # Get HCC expression data only
        expressions_hcc = self.expression_obj.dict_gene_hcc
        mean_dict_hcc = {}

        # Calculate mean for each gene
        for gene_name in desired_gene:
            if gene_name not in expressions_hcc:
                raise ValueError(f"Gene {gene_name} not found in HCC data")

            mean = sum(expressions_hcc[gene_name]) / len(expressions_hcc[gene_name])
            mean_dict_hcc[gene_name] = round(mean, 3)

        # Create a title dictionary for output formatting
        title_dict = {"Desired gene name": "Mean expression for HCC type"}

        # Combine title dictionary with the mean_hcc dictionary
        mean_dict_hcc = {**title_dict, **mean_dict_hcc}

        return mean_dict_hcc

    def calculate_mean_gene_normal(self, desired_gene):
        """Calculate mean for normal samples only returns a dictionary with normal means."""

        # Get normal expression data only
        expressions_normal = self.expression_obj.dict_gene_normal
        mean_dict_normal = {}

        # Calculate mean for each gene
        for gene_name in desired_gene:
            if gene_name not in expressions_normal:
                raise ValueError(f"Gene {gene_name} not found in normal data")

            mean = sum(expressions_normal[gene_name]) / len(expressions_normal[gene_name])
            mean_dict_normal[gene_name] = round(mean, 3)
        # Create a title dictionary for output formatting
        title_dict = {"Desired gene name": "Mean expression for normal type"}

        # Combine title dictionary with the mean_normal dictionary
        mean_dict_normal = {**title_dict, **mean_dict_normal}

        return mean_dict_normal
     
    def calculate_differential(self, desired_gene):
        """Calculate differential expression between HCC and normal samples."""

        # Initialize dictionaries
        dict_differential = {}
        dict_mean_hcc = {}
        dict_mean_normal = {}

        # Calculate mean expressions
        mean_hcc = self.calculate_mean_gene_hcc(desired_gene)
        mean_normal = self.calculate_mean_gene_normal(desired_gene)

        # Calculate differential for each gene
        for gene_name in desired_gene:
            # Validate gene exists in both datasets
            if gene_name not in mean_hcc or gene_name not in mean_normal:
                raise ValueError(f"Gene {gene_name} not found in both datasets")

            # Check for division by zero
            if mean_normal[gene_name] == 0:
                raise ZeroDivisionError(f"Normal expression is zero for gene {gene_name}")

            # Store mean values
            dict_mean_hcc[gene_name] = mean_hcc[gene_name]
            dict_mean_normal[gene_name] = mean_normal[gene_name]

            # Create a title dictionary for output formatting
            title_dict = {"Gene name": "Differential value"}

            # Calculate and round differential ratio
            dict_differential[gene_name] = round(dict_mean_hcc[gene_name] /
                                                dict_mean_normal[gene_name], 3)
            
            # Combine title dictionary with the differential dictionary
            dict_differential = {**title_dict, **dict_differential}
        return dict_differential
     
    def compare_differential_numbers(self, list_gene_names, number):
        """Compare and sort differential expressions, returning a 
        dictionary of ratio the mean expression ratios for HCC and 
        normal samples, focusing on potentially suspicious genes
        """
        # Calculate differential expression for each gene
        dict_compare_differential = {
            gene_name: self.calculate_differential([gene_name])[gene_name]
            for gene_name in list_gene_names
        }

        # Process differential values - use inverse for values < 1
        dict_differential_inv = {
            gene_name: float(diff) if diff > 1 else round(1/diff, 3)
            for gene_name, diff in dict_compare_differential.items()
        }
        # Create a title dictionary for output formatting
        title_dict = {"Gene name": "Differential value"}

        # Sort the dictionary based on differential values in descending order
        # Select the top 'number' genes with highest differential values
        dict_differential_sorted = dict(sorted(
            dict_differential_inv.items(),
            key=lambda x: x[1],
            reverse=True)[:number])
                   
            # Replace the sorted dictionary values with original differential values
        dict_differential_sorted = {
            gene_name: dict_compare_differential[gene_name]
            for gene_name in dict_differential_sorted}
        # Combine title dictionary with the sorted differential dictionary
        dict_differential_sorted = {**title_dict, **dict_differential_sorted}
        return dict_differential_sorted


    def get_high_threshold(self, threshold):
        """Get expression values above specified threshold for each gene."""
        # Get expression data
        expressions_hcc = self.expression_obj.dict_gene_hcc
        expressions_normal = self.expression_obj.dict_gene_normal
        dict_above_threshold = {}
        for gene_name in expressions_hcc:
            # Creare a dictionary with values above threshold.
            dict_above_threshold[gene_name] = [
                expr for expr in expressions_hcc[gene_name] + expressions_normal[gene_name]
                if expr > threshold
            ]
            # Check that the value list for each gene is not empty
        dict_non_empty_genes = {
            gene_name: exp_lst for gene_name, exp_lst in dict_above_threshold.items()
            if exp_lst
        }
        # Create a title dictionary for output formatting
        title_dict = {"Gene name": "Expressions value"}
        # Combine title dictionary with the top N gene dictionary
        dict_non_empty_genes = {**title_dict, **dict_non_empty_genes}
        return dict_non_empty_genes
       
    def sample_min_max(self, expression_sample_dict):
        """Get min and max expression values per sample."""
        dict_min = {
            sample: min(exp_lst) for sample, exp_lst in expression_sample_dict.items()
        }
        dict_max = {
            sample: max(exp_lst) for sample, exp_lst in expression_sample_dict.items()
        }
        # Create a title dictionary for output formatting
        title_dict_min = {"Sample ID": "Minimum expression"}
        title_dict_max = {"Sample ID": "Maximum expression"}

        # Combine title dictionary with the max, min dictionaries
        dict_min = {**title_dict_min, **dict_min}
        dict_max = {**title_dict_max, **dict_max}
        return dict_min, dict_max