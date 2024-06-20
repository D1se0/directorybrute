# Directorybrute

Directorybrute is a directory and file brute-force tool designed to discover hidden directories and files on web servers using HTTP requests.

<img src="https://github.com/D1se0/directorybrute/assets/164921056/e62ade8c-809e-4cd8-be17-c2d751e470d6" alt="Directorybrute" width="400">

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
git clone https://github.com/tupusuario/Directorybrute.git
```

### Navigate into the cloned repository directory:

```bash
cd Directorybrute
```
### Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run `Directorybrute`, use the following command from the command line:

```bash
python3 directorybrute.py [-u URL] [-w WORDLIST] [-t THREADS]
```

## Parameters
  -u URL: Specify the target website URL.
  -w WORDLIST: Path to the wordlist for brute-forcing.
  -t THREADS: Number of concurrent threads (optional, default is 10).

### Example usage:

```bash
python3 directorybrute.py -u https://example.com -w wordlist.txt -t 20
```

## Examples

Here are examples demonstrating the execution process and obtained results:

Running Directorybrute against a website:

```bash
python3 directorybrute.py -u https://example.com -w common.txt
```

Running with a custom wordlist and more concurrent threads:

```bash
python3 directorybrute.py -u https://example.com -w custom.txt -t 30
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

