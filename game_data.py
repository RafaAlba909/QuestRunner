
rooms = {
    "claro": {
        "description": "Estás en un claro silencioso. A tu alrededor solo hay árboles... y silencio. Al norte se vislumbra una sombra.",
        "exits": {"norte": "bosque"},
        "items": ["nota arrugada"]
    },
    "bosque": {
        "description": "El bosque es espeso. Hay un sendero angosto que lleva al este, otro al norte y uno al oeste hacia una torre.",
        "exits": {"sur": "claro", "norte": "cueva", "este": "pantano", "oeste": "torre_entrada"},
        "items": ["llave oxidada"]
    },
    "cueva": {
        "description": "Una cueva oscura. Huele a humedad... y a algo más. Hay una criatura dormida en una esquina.",
        "exits": {"sur": "bosque"},
        "items": ["mapa rasgado"]
    },
    "pantano": {
        "description": "El pantano burbujea con vida... o muerte. Solo puedes volver al bosque.",
        "exits": {"oeste": "bosque"},
        "items": []
    },
    "torre_entrada": {
        "description": "Estás frente a una torre imponente. La puerta está cerrada y parece necesitar una llave y una nota para abrirla.",
        "exits": {"este": "bosque"},
        "items": []
    },
    "torre": {
        "description": "Subes por unas escaleras y llegas a lo alto de la torre. Una vista espectacular te recibe. Has llegado al final del camino.",
        "exits": {},
        "items": []
    }
}

starting_room = "claro"
