from game_data import rooms, starting_room
from inventory import Inventory
from utils import limpiar_pantalla, aplicar_color

def main():
    current_room = starting_room
    inventory = Inventory()

    print(aplicar_color("🧩 Bienvenido a QuestRunner.", "rojo"))
    print("Despiertas en un lugar desconocido... ¿podrás encontrar tu camino?")
    print("\nComandos disponibles:")
    print(aplicar_color("- ir [dirección] → para moverte (ej: 'ir norte')", "azul"))
    print(aplicar_color("- mirar → para ver el entorno y objetos", "azul"))
    print(aplicar_color("- recoger [objeto] → para agarrar cosas", "azul"))
    print(aplicar_color("- inventario → para ver lo que llevas", "azul"))
    print(aplicar_color("- ayuda → para ver estos comandos de nuevo", "azul"))
    print(aplicar_color("- limpiar → para limpiar la pantalla", "azul"))
    print(aplicar_color("- salir → para cerrar el juego", "azul"))
    print("\n" + aplicar_color("¡Haz tu primer movimiento!", "amarillo"))

    while True:
        print(f"\n📍 Estás en: {aplicar_color(current_room.replace('_', ' ').capitalize(), 'amarillo')}")
        print(rooms[current_room]["description"])

        directions = rooms[current_room]["exits"]
        if directions:
            print(f"\nPuedes ir a las siguientes direcciones: {', '.join([aplicar_color(d, 'verde') for d in directions])}\n")
        else:
            print(aplicar_color("\n(No puedes ir a ningún lado desde aquí.)\n", "rojo"))

        command = input("> ").strip().lower()

        if command in ["salir", "exit", "quit"]:
            print("\nGracias por jugar. ¡Hasta la próxima!")
            break

        elif command == "limpiar":
            limpiar_pantalla()

        elif command.startswith("ir "):
            direction = command.split(" ")[1]

            if direction in directions:
                next_room = rooms[current_room]["exits"][direction]

                if next_room == "torre_entrada":
                    if "llave oxidada" in inventory.items and "nota arrugada" in inventory.items:
                        print(aplicar_color("\n🔓 Usas la llave y la nota arrugada para abrir la puerta de la torre...\n", "morado"))
                        current_room = "torre"
                        print(aplicar_color("🎉 ¡Felicidades! Has llegado al final del juego.\n", "rojo"))
                        break
                    else:
                        print(aplicar_color("\n🚪 La puerta de la torre está cerrada. Necesitas una llave y una nota para entrar.\n", "rojo"))
                else:
                    current_room = next_room
                    print(f"\nHas ido {aplicar_color(direction, 'verde')}.")

            else:
                print(aplicar_color("\nNo puedes ir en esa dirección.\n", "rojo"))

        elif command == "mirar":
            items = rooms[current_room].get("items", [])
            if items:
                print(f"\nVes: {', '.join([aplicar_color(item, 'morado') for item in items])}\n")
            else:
                print("\nNo hay nada interesante aquí.\n")

        elif command.startswith("recoger "):
            item = command.split(" ", 1)[1]
            if item in rooms[current_room].get("items", []):
                inventory.add(item)
                rooms[current_room]["items"].remove(item)
                print(f"\nHas recogido {aplicar_color(item, 'morado')}.\n")
            else:
                print("\nEse objeto no está aquí.\n")

        elif command == "inventario":
            print("\nTu inventario contiene:")
            if inventory.items:
                print("\n".join([f"- {aplicar_color(item, 'morado')}" for item in inventory.items]))
            else:
                print("Está vacío.\n")

        elif command == "ayuda":
            print("\nComandos disponibles:")
            print(aplicar_color("- ir [dirección] → para moverte (ej: 'ir norte')", "azul"))
            print(aplicar_color("- mirar → para ver el entorno y objetos", "azul"))
            print(aplicar_color("- recoger [objeto] → para agarrar cosas", "azul"))
            print(aplicar_color("- inventario → para ver lo que llevas", "azul"))
            print(aplicar_color("- salir → para cerrar el juego", "azul"))
            print(aplicar_color("- limpiar → para limpiar la pantalla", "azul"))
            print()

        else:
            print("\nNo entiendo ese comando.\n")

if __name__ == "__main__":
    main()
