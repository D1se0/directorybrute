import requests
import argparse
import threading
from tqdm import tqdm
from colorama import Fore, Style

# Función para imprimir el logo en ASCII
def print_logo():
    logo = r"""
     ____  _                 _ _            _             
    |  _ \| | ___   ___ __ _| | | ___ _ __ | |_ _   _ ___ 
    | | | | |/ _ \ / __/ _` | | |/ _ \ '_ \| __| | | / __|
    | |_| | | (_) | (_| (_| | | |  __/ | | | |_| |_| \__ \
    |____/|_|\___/ \___\__,_|_|_|\___|_| |_|\__|\__,_|___/
    
                Directorybrute
    """
    return logo

# Variable global para indicar si se debe detener la ejecución de los hilos
stop_threads = False

# Función para realizar la solicitud HTTP
def check_url(base_url, wordlist, progress_bar, hidden_statuses, hidden_sizes, extensions, hidden_directories, output_file=None):
    global stop_threads

    with open(wordlist, 'r', encoding='latin-1') as file:
        words = [line.strip() for line in file]

    if hidden_directories:
        words = ['.' + word for word in words]

    results = []
    for word in words:
        if stop_threads:
            break
        
        try:
            response = requests.get(base_url.replace('BRUTE', word))
            content_length = len(response.content)
            status_code = response.status_code

            if status_code not in hidden_statuses and content_length not in hidden_sizes:
                result = f"{Fore.GREEN}[+]{Style.RESET_ALL} {base_url.replace('BRUTE', word)} [{status_code}] - {content_length} bytes"
                print(result)
                results.append(result)

                if status_code == 200:
                    stop_threads = True  # Stop other threads if a valid resource is found

        except requests.exceptions.RequestException as e:
            error_message = f"{Fore.RED}[-]{Style.RESET_ALL} Error: {e}"
            print(error_message)
            results.append(error_message)

        progress_bar.update(1)

        if stop_threads:
            break  # Exit the loop immediately if stop_threads is True

        for ext in extensions:
            if stop_threads:
                break
            
            try:
                response = requests.get(base_url.replace('BRUTE', f"{word}.{ext}"))
                content_length = len(response.content)
                status_code = response.status_code

                if status_code not in hidden_statuses and content_length not in hidden_sizes:
                    result = f"{Fore.GREEN}[+]{Style.RESET_ALL} {base_url.replace('BRUTE', f'{word}.{ext}')} [{status_code}] - {content_length} bytes"
                    print(result)
                    results.append(result)

                    if status_code == 200:
                        stop_threads = True  # Stop other threads if a valid resource is found

            except requests.exceptions.RequestException as e:
                error_message = f"{Fore.RED}[-]{Style.RESET_ALL} Error: {e}"
                print(error_message)
                results.append(error_message)

            progress_bar.update(1)

    if output_file:
        with open(output_file, 'a') as f:
            for result in results:
                f.write(result + "\n")

# Función principal para manejar los argumentos y ejecutar los hilos
def main():
    logo = print_logo()
    print(Fore.CYAN + logo + Style.RESET_ALL)

    parser = argparse.ArgumentParser(
        description="Directorybrute: Herramienta para descubrir directorios ocultos y subdominios mediante fuerza bruta.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '-w', '--wordlist', required=True, 
        help='Ruta al wordlist.'
    )
    parser.add_argument(
        '-t', '--threads', type=int, default=10, 
        help='Número de hilos para concurrencia (por defecto: 10).'
    )
    parser.add_argument(
        '-u', '--url', required=True, 
        help='URL con BRUTE donde se reemplazará para realizar la fuerza bruta (por ejemplo, "example.com/BRUTE").'
    )
    parser.add_argument(
        '--https', action='store_true', 
        help='Usar https en lugar de http.'
    )
    parser.add_argument(
        '--hp', '--hide-status', type=str, default='', 
        help='Ocultar códigos de estado HTTP específicos (por ejemplo, "200,202").'
    )
    parser.add_argument(
        '--hw', '--hide-size', type=str, default='', 
        help='Ocultar tamaños de contenido específicos (por ejemplo, "128,256").'
    )
    parser.add_argument(
        '-x', '--extensions', type=str, default='', 
        help='Extensiones a probar, separadas por comas (por ejemplo, "txt,html,php").'
    )
    parser.add_argument(
        '--hd', '--hidden-directories', action='store_true', 
        help='Añadir un punto delante de cada palabra para descubrir directorios o archivos ocultos.'
    )
    parser.add_argument(
        '-f', '--file', type=str, 
        help='Nombre del archivo para exportar los resultados.'
    )

    args = parser.parse_args()

    protocol = 'https' if args.https else 'http'
    if not args.url.startswith('http://') and not args.url.startswith('https://'):
        base_url = f"{protocol}://{args.url}"
    else:
        base_url = args.url

    hidden_statuses = {int(code) for code in args.hp.split(',') if code}
    hidden_sizes = {int(size) for size in args.hw.split(',') if size}
    extensions = [ext.strip() for ext in args.extensions.split(',') if ext]

    with open(args.wordlist, 'r', encoding='latin-1') as file:
        total_words = sum(1 for _ in file)

    progress_bar = tqdm(total=total_words * (1 + len(extensions)), desc="Brute Forcing", unit="word")

    try:
        check_url(base_url, args.wordlist, progress_bar, hidden_statuses, hidden_sizes, extensions, args.hd, args.file)
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[+]{Style.RESET_ALL} Saliendo...")
    finally:
        progress_bar.close()

    if args.file:
        with open(args.file, 'w') as f:
            f.write(logo + "\n")

if __name__ == "__main__":
    main()
