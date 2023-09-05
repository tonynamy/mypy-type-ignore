from collections import defaultdict
import subprocess
import re
from os import path

executable = ""  # Replace with your mypy executable
directory = ""  # Replace with your desired directory
encoding = "utf8"


def run():
    print("Running mypy")
    result = subprocess.run(
        [
            *executable.split(" "),
            "--no-color-output",
            "--no-error-summary",
            "--hide-error-context",
        ],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=directory,
    )
    mypy_output = result.stdout

    with open("mypy_output.txt", "w", encoding=encoding) as file:
        file.write(mypy_output)

    # Regular expression pattern to match file path, line number, and error code
    pattern = r"^(.*?):(\d+): error: .*?  \[(.*?)\]$"

    # Find all matches in the mypy output
    matches = re.findall(pattern, mypy_output, re.MULTILINE)

    # { (file_path, line_number) : [error_code, ...] }
    error_dict = defaultdict(list)

    # Iterate over the matches
    for match in matches:
        file_path, line_number, error_code = match
        error_dict[(path.join(directory, file_path), line_number)].append(error_code)

    for (file_path, line_number), error_codes in error_dict.items():
        ignore_statement = ", ".join(list(set(error_codes)))
        annotation = f"# type: ignore[{ignore_statement}]"

        # Read the file
        with open(file_path, "r", encoding=encoding) as file:
            lines = file.readlines()

        # Insert the annotation at the end of the corresponding line
        line_index = int(line_number) - 1
        line = lines[line_index].rstrip()
        lines[line_index] = f"{line}  {annotation}\n"

        # Write the modified content back to the file
        with open(file_path, "w", encoding=encoding) as file:
            file.writelines(lines)

        print(f"Added {annotation} to {file_path}:{line_number}")


if __name__ == "__main__":
    directory = input("Enter directory: ")
    executable = input("Enter mypy executable: ")
    run()
    print("Done!")
