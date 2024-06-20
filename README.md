# Directorybrute

Directorybrute is a directory and file brute-force tool designed to discover hidden directories and files on web servers using HTTP requests.

![Directorybrute](https://url_a_tu_imagen.png)

---

## Features

- Directory and file brute-forcing on web servers.
- Support for both HTTP and HTTPS.
- Option to specify a custom list of directories.
- Detailed result reporting.

---

## Installation

To install `Directorybrute`, follow these steps:

1. Clone the repository from GitHub:

   ```bash
   git clone https://github.com/tupusuario/Directorybrute.git
Navigate into the cloned repository directory:

cd Directorybrute
Install the required dependencies:


pip install -r requirements.txt
Usage
To run Directorybrute, use the following command from the command line:

python directorybrute.py [-u URL] [-w WORDLIST] [-t THREADS]
Parameters
-u URL: Specify the target website URL.
-w WORDLIST: Path to the wordlist for brute-forcing.
-t THREADS: Number of concurrent threads (optional, default is 10).
Example usage:

python directorybrute.py -u https://example.com -w wordlist.txt -t 20
Examples
Here are examples demonstrating the execution process and obtained results:

Running Directorybrute against a website:

python directorybrute.py -u https://example.com -w common.txt

Running with a custom wordlist and more concurrent threads:

bash
Copiar código
python directorybrute.py -u https://example.com -w custom.txt -t 30

Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Asegúrate de reemplazar `https://url_a_tu_imagen.png`, `https://url_a_tu_imagen_1.png` y `https://url_a_tu_imagen_2.png` con las URL correctas de tus imágenes relacionadas con tu herramienta Directorybrute. Esto debería proporcionarte un `README.md` completo y listo para usar en tu repositorio de GitHub.

