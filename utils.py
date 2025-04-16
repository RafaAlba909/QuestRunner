import os
import platform
from colorama import init, Fore

init(autoreset=True)

def aplicar_color(texto, color):
    """Aplica color al texto usando la librería colorama o códigos ANSI"""
    colores = {
        "rojo": Fore.RED,
        "verde": Fore.GREEN,
        "amarillo": Fore.YELLOW,
        "azul": Fore.BLUE,
        "morado": Fore.MAGENTA, 
        "reset": Fore.RESET
    }

    return f"{colores.get(color, Fore.RESET)}{texto}{Fore.RESET}"


def limpiar_pantalla():
    """Limpia la pantalla dependiendo del sistema operativo"""
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def mostrar_direcciones(current_room, rooms):
    """Muestra las direcciones disponibles en la habitación actual"""
    directions = rooms[current_room]["exits"]
    return directions.keys()
