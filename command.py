import argparse

# Create an ArgumentParser object named 'parser' with a description
parser = argparse.ArgumentParser(description="An addition program")

# Define a positional argument 'add' with nargs='*', meaning it accepts zero or more values
# 'metavar="num"' sets the metavariable name displayed in help messages as 'num'
# 'type=int' ensures that each argument passed is interpreted as an integer
# 'help' provides a description of what the argument does
parser.add_argument("add", nargs='*', metavar="num", type=int,
                    help="All the numbers separated by spaces will be added.")

# Parse the command-line arguments
args = parser.parse_args()

# Print the list of arguments provided for 'add'
print(f"Arguments provided: {args.add}")

# Check if any arguments were provided for 'add'
if len(args.add) != 0:
    # Calculate and print the sum of the numbers provided
    print(f"Sum of numbers: {sum(args.add)}")
