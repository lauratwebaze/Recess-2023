# File Handling
# example 1
# Writing to a file
file_path = "data.txt"

# Open the file in write mode
with open(file_path, "w") as file:
    file.write("Hello, World!\n")
    file.write("This is an example of file handling in Python.\n")

# Reading from a file
with open(file_path, "r") as file:
    contents = file.read()

# Print the file contents
print(contents)

# example 2

# Reading from a file
input_file_path = "input.txt"
output_file_path = "output.txt"

try:
    with open(input_file_path, "r") as input_file:
        lines = input_file.readlines()

    # Modifying the data
    modified_lines = []
    for line in lines:
        modified_line = (
            line.strip().upper()
        )  # Convert to uppercase and remove leading/trailing whitespace
        modified_lines.append(modified_line)

    # Writing to a file
    with open(output_file_path, "w") as output_file:
        output_file.writelines(modified_lines)

    print("File processing complete.")
except FileNotFoundError:
    print("Input file not found.")
except IOError:
    print("An error occurred while reading or writing the file.")


# Exception handling
# example 1
try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Exception handling code
    print("Error: Division by zero")


# example 2
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
    except TypeError:
        print("Error: Invalid operand type")
    else:
        print("The result is:", result)
    finally:
        print("This will always execute")


# Example usage
divide_numbers(10, 2)  # Normal division, no exception
divide_numbers(10, 0)  # Division by zero
divide_numbers(10, "2")  # Invalid operand type
