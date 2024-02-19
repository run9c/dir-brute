import requests  # Importing the requests library for making HTTP requests
import argparse  # Importing argparse to parse command-line arguments
import sys  # Importing sys for system-specific parameters and functions

# Initializing the argument parser
parser = argparse.ArgumentParser(description="HTTP Status Checker")  # Creating an argument parser object

# Adding arguments to the parser
parser.add_argument('-w', '--wordlist', type=str, required=True, help="Path to the wordlist file")  # Argument for wordlist file
parser.add_argument('-u', '--url', type=str, required=True, help="Target URL to check")  # Argument for target URL
args = parser.parse_args()  # Parsing the arguments provided

print("[+] Wordlist: ", args.wordlist)  # Printing the path of the wordlist file
print("[+] URL: ", args.url)  # Printing the target URL

# Request Headers
user_agents = [
    'Macintosh; Intel Mac OS X 10_15_7',  # List of User-Agent strings to try
    'Windows NT 10.0; Win64; x64',
    'Linux; Android 10.0.0; SM-G975F Build/QP1A.190711.020'
]

# Working with file
file = open(args.wordlist, 'r')  # Opening the wordlist file in read mode
lines = file.readlines()  # Reading all lines from the wordlist file

# Checking if URL schema exists in the URL
if ('http' in args.url) or ('https' in args.url):  # Checking if URL has 'http' or 'https' schema
    pass  # Proceeding if URL schema exists
else:
    print('Please enter a URL Schema')  # Prompting user to enter URL schema
    sys.exit()  # Exiting the program if URL schema is missing

# Parsing through each word in the wordlist
try:
    for line in lines:  # Iterating through each line in the wordlist
        line = line.strip("\n")  # Removing newline character from each line
        for user_agent in user_agents:  # Iterating through each user agent
            headers = {'User-Agent': user_agent}  # Setting the User-Agent header
            r = requests.get(args.url+'/'+line, headers=headers)  # Making a GET request to the URL with the word from wordlist appended
            if(r.status_code != 404):  # Checking if response status code is not 404
                print(args.url+'/'+line, ":", r.status_code)  # Printing the URL and its corresponding status code
                break  # Exiting the loop if a valid response is obtained
except:
    print("Error Occurred")  # Handling errors that occur during the process