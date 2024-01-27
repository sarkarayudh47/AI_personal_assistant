import subprocess

# Specify the path to your program
program_path = r"E:\python files\mainfunc\ex1.py"

# Run the program and capture its output
output_data = subprocess.getoutput(f'python "{program_path}"')

# Print or use the stored output
print("Stored output:", output_data)
