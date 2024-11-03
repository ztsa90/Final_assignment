# Gene Expression Analysis Tool

## Overview
This project analyzes gene expression patterns in liver cancer, comparing cancerous (HCC - Hepatocellular Carcinoma) and healthy liver tissues.
The analysis focuses on identifying potential Tumor Suppressor Genes (TSGs) and Oncogenes through statistical analysis of their expression patterns.
Our objective is calculating statistical metrics (mean, median, standard deviation) for gene expression across 22277 genes.
Determine differential expression between healthy and cancerous tissues and identify potential TSGs and Oncogenes based on expression patterns.

Gene Function Analysisnis based on two parameters: 
1. Tumor Suppressor Genes (TSGs) : Decreased expression in cancer indicates potential TSG Lower HCC/Normal ratio suggests reduced tumor suppression
Critical for cancer prevention when functioning normally

2. Oncogenes: Increased expression in cancer indicates potential oncogene Higher HCC/Normal ratio suggests increased cell division
May contribute to cancer development when overexpressed.

Differential Expression Analysis consist of the HCC/Normal ratio to identify potential cancer-related genes:
Ratio > 1: Indicates increased expression in cancer Potential oncogene identification may suggest increased cell division
Ratio < 1: Indicates decreased expression in cancer Potential TSG identification may suggest reduced tumor suppression.
Based on this approach, we calculated the most suspicious cancer-related genes by comparing their significance levels with one.
This method is based on the Fold-change, helps researchers identify genes with significant differences in expression between conditions, aiding in the understanding of biological processes and disease mechanisms.
We then reported the genes withratios much greater than one and much less than one in order.

# Key Features:

Data Loading: Processes CSV files containing gene expression data
Sample Organization: Separates HCC and normal tissue samples
Data Validation: Ensures data integrity and proper formatting
Expression Mapping: Maps genes to their expression values
Sample Management: Organizes sample-specific information

# Capabilities:

Reads and parses gene expression data files
Maintains separate dictionaries for HCC and normal samples
Provides gene name and sample ID listings
Extracts expression values for specific genes
Handles both individual and batch gene queries

## Description

### 1. final_main.py
The main script that orchestrates the analysis workflow. It handles:
- Command line argument parsing
- Data loading and processing 
- Statistical analysis execution
- Report generation

### 2. expression_class.py (GeneExpressionData)
Handles the core data processing functionality:
- Loading and parsing gene expression data from CSV files
- Managing dictionaries for HCC and normal tissue samples
- Extracting gene names and sample information
- Processing expression values

### 3. statistical_class.py (StatisticalAnalysis) 
Performs comprehensive statistical calculations on the expression data.
Basic Statistics:
-  Mean Calculation: Overall mean expression values Separate means for HCC and normal samples Gene-specific mean expressions
- Median Analysis: Calculates median expression values. Provides robust central tendency measures. Handles outliers effectively
- Variation Measures:Standard deviation calculation, Variance computation
- Advanced Analytics: Differential Expression: Ratio calculations between HCC and normal samples
Fold change analysis. Expression pattern comparison
- Threshold Analysis: Identifies genes above specified expression levels. Filters significant expression changes. 
- Sample Analysis: Minimum/maximum expression detection for each Sample ID.

### 4. report_class.py (AnalysisReport)
Creates formatted, readable outputs of analysis results. Output Options:
- Screen Display: Immediate console output, Interactive viewing. Real-time analysis review
- File Output: Permanent record creation. Formatted text files. Analysis documentation
- Report Features: Formatting: Clear section headers. Organized data presentation. Consistent styling
- Data Presentation:Tabular format for numerical data. Listed format for identifiers. Clear section separation

### 5. except_class.py (CalculationError)
Custom exception handling for Input-related errors.

## Getting Started
### Command Line Arguments
1. `data_path`: Path to input CSV file
2. `output_choice`: Output destination ('file' or 'screen')  
3. `file_path`: Output file path (if output_choice is 'file')
4. `gene_names`: Comma-separated list of gene names
5. `threshold`: Expression threshold value
6. `number`: Number of top genes to analyze

### Dependencies
- Python 3.x
- Standard libraries:
  - collections (defaultdict)
  - math 
  - sys

### Installing
1. Clone the repository
   https://github.com/ztsa90/Final_assignment.git
2. Ensure Python 3.x is installed
3. No additional package installation required

### Executing program
Command Line Format
The program is executed through the command line using the following format:
We have two ways to define an input argument
If the output_choice is set to "screen," there is no need for file_path since we are not writing to a file. Therefore, the argument list should be as follows:
bashCopypython final_main.py [path] [output_choice] [desired_gene_name] [threshold] [number]

If we want to write to a file, we need to specify the file_path. In this case, our input argument:
bashCopypython final_main.py [path] [output_choice] [desired_gene_name] [threshold] [number][file_path]

# Parameter Details
1. The path to your input data CSV file. Must be a valid CSV file with the correct format
   Example: data/liver_expression.csv
2. Output_choice. Specifies where to send the analysis results. Two valid options:
   screen: Display results in the terminal
   file_path: Save results to a file
3. Desired_gene_name. Can be one or some gene_names.Comma-separated list of gene names to analyze
   No spaces between genes. Case-sensitive
   Example: "GENE1,GENE2,GENE3"
4. Threshold. numerical value for expression threshold analysis
   Must be non-negative. Can be integer or float, Example: 5.0
5. Number. Integer specifying how many top differential genes to analyze. Must be positive. Example: 10
6. File_path. The destination path for the output file Required if our output choise is fila_path. 

Basic analysis with screen output:
Command Line Format
The program is executed through the command line using the following format:

1. If the output_choise is : screen.
```bash
[/users/data/liver_cancer_gene_expression] [screen] ["117_at, 1255_g_at, 1294_at"] [14] [4]
```
2. If the output_choise is : file_path
```bash
[/users/data/liver_cancer_gene_expression] [file_path] ["117_at, 1255_g_at, 1294_at"] [14] [4] [/users/data/output.txt]
```
All arguments should be updated.

## Help

For common issues or questions, please check:

File format matches expected CSV structure
Gene names exist in dataset
Threshold is a positive number
Number parameter is a positive integer
File permissions allow writing if using file output

## Authors

Author: Zahra Taheri Hanjani
Email: z.taheri.hanjani@st.hanze.nl
