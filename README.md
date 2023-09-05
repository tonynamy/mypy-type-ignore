# Mypy Type Ignore

This script automatically adds `# type: ignore[error-code]` to the end of the line.
(`error-code` can be multiple error codes separated by a comma)

## Usage

This script doesn't require any dependencies. Just run it with Python 3.

1. Run `python main.py`
2. Enter the directory you want to run this script on.
3. Enter the path to your mypy executable.
4. Wait for the script to finish.
   - It automatically runs mypy on the directory you specified.
   - After mypy finishes, it saves the output to a file(`mypy_output.txt`).
   - Then it adds `# type: ignore` to the end of the line.

```bash
$ python main.py
Enter directory: <your-desired-directory>
Enter mypy executable: <your-desired-mypy-executable>
Running mypy
Added # type: ignore[error-code] to file-path:line-number
Added # type: ignore[error-code] to file-path:line-number
...
Done!
```
