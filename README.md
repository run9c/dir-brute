# Directory Bruteforce :mag_right:

This Python script checks the HTTP status codes of different endpoints by iterating through a wordlist and appending each word to a specified URL.

## Usage :computer:
1. Make sure you have Python installed on your system.
2. Clone or download this repository.
3. Open a terminal and navigate to the project directory.
4. Run the script using the following command:

```python script_name.py -w wordlist_file.txt -u target_url```

Replace `script_name.py` with the name of your Python script, `wordlist_file.txt` with the path to your wordlist file, and `target_url` with the URL you want to check.

## Dependencies :package:
- [requests](https://pypi.org/project/requests/): Library for making HTTP requests
- [argparse](https://docs.python.org/3/library/argparse.html): Library for parsing command-line arguments

## Arguments :gear:
- `-w, --wordlist`: Path to the wordlist file.
- `-u, --url`: Target URL to check.

## Error Handling 🖥️
The script handles errors that may occur during execution.
