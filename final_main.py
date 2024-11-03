"""Main script to analyze gene expression data."""

import sys
from expression_class import GeneExpressionData
from statistical_class import StatisticalAnalysis
from report_class import AnalysisReport
from except_class import InputError

def main():
    """
      Main function to handle gene expression analysis workflow.
    Command line arguments:
    1. path: Path to input data file
    2. output_choice: Output destination ('file_path' or 'screen')
    3. file_path: Path for output file if output_choice is 'file_path'
    4. desired_gene_name: Comma-separated list of gene names
    5. threshold: Expression threshold value
    6. number: Number of top genes to analyze
    """
    try:
        # Get and validate input parameters
        path = sys.argv[1]
        output_choice = sys.argv[2].strip().lower()
        desired_gene_name = [name.strip() for name in sys.argv[3].split(',')]
        threshold = float(sys.argv[4])
        number = int(sys.argv[5])
        if output_choice == 'file_path':
           file_path = sys.argv[6]

        # Validate input parameters and raise InputError if any issues are found
        if not desired_gene_name:
            raise InputError("No gene names provided")
        if threshold < 0:
            raise InputError("Threshold must be non-negative")
        if number <= 0:
            raise InputError("Number must be positive")
        if output_choice not in ['file_path', 'screen']:
            raise InputError("Output choice must be 'file_path' or 'screen'")

        # Initialize Gene Expression Analysis
        gene_expression_obj = GeneExpressionData(path)

        # Load and process data
        dict_gene_hcc, dict_gene_normal, dict_sample = gene_expression_obj.load_data()
        list_gene_name = gene_expression_obj.return_list_gene_name(dict_gene_hcc)
        list_sample = gene_expression_obj.return_list_sample(dict_sample)
        expression_sample_dict = gene_expression_obj.expression_sample(dict_sample)
        dict_desired_expr = gene_expression_obj.find_dict_desired_expression(desired_gene_name)

        # Create an instance of the StatisticalAnalysis class to perform the analysis
        statistical_analysis = StatisticalAnalysis(gene_expression_obj)
        mean_dict = statistical_analysis.calculate_mean(desired_gene_name)
        median_dict = statistical_analysis.calculate_median(desired_gene_name)
        dict_var, dict_std_dev = statistical_analysis.calculate_standard_deviation_variance(
            desired_gene_name
        )
        mean_dict_hcc = statistical_analysis.calculate_mean_gene_hcc(desired_gene_name)
        mean_dict_normal = statistical_analysis.calculate_mean_gene_normal(desired_gene_name)
        dict_differential = statistical_analysis.calculate_differential(desired_gene_name)
        dict_differential_sorted = statistical_analysis.compare_differential_numbers(
            list_gene_name, number
        )
        dict_top_threshold = statistical_analysis.get_high_threshold(threshold)
        dict_min_sample, dict_max_sample = statistical_analysis.sample_min_max(
            expression_sample_dict
        )

        # Create a report object based on the user's output choice
        if output_choice == 'file_path':
            report_obj = AnalysisReport(destination = file_path)
        else:
            report_obj = AnalysisReport(destination ='screen')

        # Prepare the data and headers/footers for the report
        data = [
            list_sample,
            list_gene_name,
            mean_dict,
            median_dict,
            dict_var,
            dict_std_dev,
            dict_differential,
            dict_differential_sorted,
            dict_top_threshold,
            dict_min_sample,
            dict_max_sample
        ]

        headers = [
            "List of all sample names:",
            "List of all gene names:",
            "Mean dictionary of desired genes:",
            "Median dictionary of desired genes:",
            "Variance dictionary of desired genes:",
            "Standard deviation of desired genes:",
            "Ratio differential of desired genes:",
            "Gene names with most expression differential:",
            "N Gene names above the threshold:",
            "Minimum expression list for each sample:",
            "Maximum expression list for each sample:"
        ]

        footers = [
            "End of sample names list",
            "End of gene names list",
            "End of mean of desired genes",
            "End of median of desired genes",
            "End of variance of desired genes",
            "End of standard deviation of desired genes",
            "End of differential ratios of desired genes",
            "End of most differential genes",
            "End of N genes above thershold",
            "End of minimum expressions",
            "End of maximum expressions"
        ]

        # Generate the report
        for head, item, footer in zip(headers, data, footers):
            report_obj.generate_report(head, item, footer)

    # Handle InputError exceptions
    except InputError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()