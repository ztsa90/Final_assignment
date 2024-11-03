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
Performs statistical calculations including:
- Mean and median calculations
- Standard deviation and variance
- Differential expression analysis and filtering them.
- Threshold-based filtering
- Min/max expression values for each sample

### 4. report_class.py (AnalysisReport)
Manages output generation:
- Formatted report creation
- Table and list formatting
- File or screen output handling
- Header and footer generation

### 5. except_class.py (CalculationError)
Custom exception handling for calculation-related errors.

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

Run from command line:
python final_main.py <data_path> <output_choice> <file_path> <gene_names> <threshold> <number>

## Help

For common issues or questions, please check:

File format matches expected CSV structure
Gene names exist in dataset
Threshold is a positive number
Number parameter is a positive integer
File permissions allow writing if using file output

## Authors

Zahra Taheri Hanjani
z.taheri.hanjani@st.hanze.nl
