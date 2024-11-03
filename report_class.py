class AnalysisReport:
    """Class for generating formatted analysis reports."""

    def __init__(self, destination):
        """Initialize report generator with output destination('screen' or file path)."""
        self.destination = destination

    def create_header(self, text):
        """Create formatted header with asterisk border."""
        header = f"{'*' * 25} {text} {'*' * 25}"
        return header #Return the formatted header

    def create_footer(self, end_words):
        """Create formatted footer with equals border."""
        # Create and return the footer string
        return "\n" + "=" * 35 + end_words + "=" * 35 + "\n End of Report\n"

    def report_dict(self, data_dic):
        """Format dictionary data as table with centered columns."""
        output = 112* "-" + "\n"
         # Iterate over each key-value pair in the provided dictionary
        for key, value in data_dic.items():
            # Add a formatted row for each key-value pair, centering the key and value
            output += f"|{key.center(15, ' ')} | {str(value).center(97, ' ')} |\n{112 * '-'}\n"
             # Return the formatted output string
        return output

    def report_lst(self, data_lst):
        """Format list with line breaks every 3 items."""
        # Initialize an empty string to hold the formatted result
        result = ""
        # Iterate over each item in the provided list with its index
        for idx, item in enumerate(data_lst):
            # Add the item to the result followed by spaces to align to a width of 40 characters
            result += item + (40-len(item))*" "
            # Check if the current index + 1 is a multiple of 3 to add a line break
            if (idx + 1) % 3 == 0:
                result += '\n'
                # Return the formatted result string
        return result

    def write_content(self, content):
        """Write content to the specified destination (screen or file)."""
        # Check if the destination is set to 'screen'
        if self.destination == 'screen':
            # Print the content to the console
            print(content)
        else:
            # Open the specified file in write mode with UTF-8 encoding
            with open(self.destination, 'w', encoding='utf-8') as file:
                # Write the content to the file, adding a newline at the end
                file.write(content + "\n")

    def generate_report(self, header, data, footer):
        """Generate complete report with header, formatted data and footer."""
        result = ""  # Initialize an empty string to store the report content
        # Check if the data is a dictionary
        if isinstance(data, dict):
            # Create the report with header, formatted dictionary data, and footer
            result = f"{self.create_header(header)}\n{self.report_dict(data)}\n\
                  {self.create_footer(footer)}"
        elif isinstance(data, list):
            # Create the report with header, formatted list data, and footer
            result = f"{self.create_header(header)}\n{self.report_lst(data)}\n\
            {self.create_footer(footer)}\n"
        # Write the generated report content to the specified destination
        self.write_content(result)