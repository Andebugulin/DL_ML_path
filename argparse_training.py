# Installation and Basic Setup
#
# Install Python if you haven't already.
# Create a new Python script (e.g., my_parser.py) and import the argparse module.
# Create a Simple Parser
#
import argparse

def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="A simple command-line tool")

    # Add arguments to the parser
    parser.add_argument('--input', '-i', required=True, help='Input file path')
    parser.add_argument('--output', '-o', required=True, help='Output file path')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose mode')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the values of the parsed arguments
    input_file = args.input
    output_file = args.output
    verbose = args.verbose

    # Perform the desired action based on the parsed arguments
    if verbose:
        print(f'Processing {input_file} to {output_file} in verbose mode')
    else:
        print(f'Processing {input_file} to {output_file}')

    # Implement your logic here, e.g., reading from input_file and writing to output_file

if __name__ == '__main__':
    main()






# Create a parser object using argparse.ArgumentParser().
# Add a positional argument for a filename.
#     Parse Arguments
#
# Parse the command-line arguments using parser.parse_args().
# Print the parsed arguments to ensure they are correctly captured.
# Add Optional Arguments
#
# Add an optional argument to specify an output directory for the file.
#     Set default values for optional arguments.
#     Add More Arguments
#
# Add a boolean argument to enable a verbose mode (e.g., --verbose or -v).
# Add an integer argument for a numeric value (e.g., --count).
# Group Arguments
#
# Create argument groups for related arguments using parser.add_argument_group().
# Usage Information
#
# Add a description and epilog to your parser using description and epilog arguments in ArgumentParser.
# Add help messages for each argument using the help parameter.
# Validation and Error Handling
#
# Implement basic validation for arguments, such as checking if a file exists.
# Handle errors gracefully and display user-friendly error messages.
# Subcommands
#
# Create a parser with subcommands. For example, a file management script with subcommands like create, delete, and list.
# Advanced Features
#
# Explore more advanced features like custom argument types, choices, and action handlers.
# Implement mutually exclusive arguments using add_mutually_exclusive_group().
# Testing
#
# Write test cases using a testing framework (e.g., unittest or pytest) to verify the behavior of your argument parsing.
# Documentation
#
# Create documentation for your script, including a help message for the user explaining how to use it.
# Real-World Application
#
# Apply your argparse skills to an existing project or create a new project where command-line arguments are needed.
# Extra Challenges
#
# Explore external libraries or plugins that extend argparse functionality, like argcomplete for tab-completion support.
#     Implement custom actions for specific argument behaviors.
# Review and Refactor
#
# Review your code and refactor it for improved readability and maintainability.
#     Consider using docstrings and comments to explain the purpose of your script and each argument.
# Share Your Knowledge
#
# Write a blog post or create a tutorial about using argparse in Python to help others learn.
# Remember to consult the official Python documentation for argparse and refer to examples to deepen your understanding as you work through these tasks. Practice is key to mastering argparse, so try to apply it to various scripting and automation projects.
#
#
#
#
#
