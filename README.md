# Directorybrute

Directorybrute is a directory and file brute-force tool designed to discover hidden directories and files on web servers using HTTP requests.

<p align="center">
  <img src="https://github.com/D1se0/directorybrute/assets/164921056/e62ade8c-809e-4cd8-be17-c2d751e470d6" alt="Directorybrute" width="400">
</p>

---
 

## Features

- Directory and file brute-forcing on web servers.
- Support for both HTTP and HTTPS.
- Option to specify a custom list of directories.
- Detailed result reporting.

---

## Installation

To install `Directorybrute`, follow these steps:

### Clone the repository from GitHub:

```bash
git clone https://github.com/D1se0/directorybrute.git
```

### Navigate into the cloned repository directory:

```bash
cd directorybrute
```
### Install the required dependencies:

```bash
./requirements.txt
```
or

```bash
pip3 install requests colorama tqdm
```

## Usage

To run `Directorybrute`, use the following command from the command line:

```bash
python3 directorybrute.py [-u URL] [-w WORDLIST] [--hp HIDDEN-PROTOCOL] [-x EXTENSIONS] [-t THREADS] [-f FILE]
```

## Parameters

  `-h`, `--help` = show this help message and exit
  
  `-w` WORDLIST, `--wordlist` WORDLIST = Path to the wordlist for brute-forcing.

  `-t` THREADS, `--threads` THREADS = Number of concurrent threads (optional, default is 10).

  `-u` URL, `--url` URL = URL with BRUTE where it will be replaced to perform brute force (for example, "example.com/BRUTE").
  
  `--https` = Use https instead of http.
  
  `--hp` HP, `--hide-status` HP = Hide specific HTTP status codes (for example, "200,202").

  `--hw` HW, `--hide-size` HW = Hide specific content sizes (for example, "128,256").

  `-x` EXTENSIONS, `--extensions` EXTENSIONS = Extensions to try, separated by commas (e.g. "txt,html,php").

  `--hd`, `--hidden-directories` = Add a period in front of each word to discover hidden directories or files.

  `-f` FILE, `--file` FILE = File name to export the results.

### Example usage:

```bash
python3 directorybrute.py -u http://example.com/BRUTE -w [WORDLIST] --hp "404" -x "txt,html,php"
```

## Examples

Here are examples demonstrating the execution process and obtained results:

Running Directorybrute against a website:

```bash
python3 directorybrute.py -u http://example.com/BRUTE -w [WORDLIST] --hp "404"
```

Running with a custom wordlist and more concurrent threads:

```bash
python3 directorybrute.py -u https://example.com -w [WORDLIST] --hp "404" -x "txt,html,php" -t 30
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

