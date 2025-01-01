import os
import time
import random
from colorama import Fore, init

# Inicializar colorama
init(autoreset=True)

def clear_console():
    """Limpa o console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_fireworks():
    """Gera uma sequência aleatória de fogos de artifício em ASCII."""
    colors = [
        Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN
    ]
    fireworks = [
        "               __     ",
        "              [__]    ",
        "              |  |    ",
        "              |  |    ",
        "              |  |    ",
        "              |  |    ",
        "              |  |    ",
        " ,----.      /`-. \   ",
        "(      )    /-._|  \  ",
        "|`----'|   |        | ",
        "\      /   |`-...   | ",
        " `.  ,'    |'` . |  | ",
        "   ||      |`,'- |  | ",
        " ,-||-.    |`-...|  | ",
        "(  ''  )   |        | ",
        " `----'     `-....-'  "
    ]

    for line in fireworks:
        color = random.choice(colors)
        print(color + line.center(80))
        time.sleep(0.1)

def display_message():
    """Exibe a mensagem 'Feliz Ano Novo!' com cores."""
    message = "FELIZ ANO NOVO!"
    colors = [
        Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN
    ]

    for letter in message:
        if letter != " ":
            print(random.choice(colors) + letter, end="")
        else:
            print(" ", end="")
        time.sleep(0.2)
    print("\n")

if __name__ == "__main__":
    clear_console()
    for _ in range(5):
        generate_fireworks()
        time.sleep(0.5)
        clear_console()
    
    display_message()
