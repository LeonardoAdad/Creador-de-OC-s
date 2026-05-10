import random
import time 

# ── Diccionarios ──
escenarios = {
    "Fantasía": [
        "Castillo", "Cabaña", "Bosque Mágico", "Aldea", "Cueva",
        "Taberna", "Calabozos", "Carruaje", "Establo de caballos", "Escuela mágica"
    ],
    "Ciencia ficción": [
        "Bar inteligente", "Civilizaciones espaciales", "Ciudad futurista",
        "Desarrollo en la luna", "Convivir con aliens", "El páramo",
        "Desierto con vida", "Ciudad post apocalíptica", "Vida bajo tierra", "Guerras nucleares"
    ],
    "Actualidad": [
        "El rancho", "Puestos callejeros", "Centro de la ciudad", "Cafetería",
        "Oficina", "Barrio", "Nevería la Michoacana", "Transporte público",
        "Hospital", "Obra negra"
    ]
}

profesiones = {
    "Fantasía": [
        "Mago", "Caballero", "Hada", "Elfo", "Goblin",
        "Realeza", "Plebello", "Ogro", "Arquero", "Bufon"
    ],
    "Ciencia ficción": [
        "Hacker", "Pandillero", "Yakuza", "Drug dealer", "Corporativo",
        "Policía", "Político", "Trabajador/a de noche", "Ingeniero", "Sicario"
    ],
    "Actualidad": [
        "Doctor", "Estudiante", "Chofer", "Homeless", "Godines",
        "Chef", "Artista", "Cholo", "Programador", "Abogado", "Taquero"
    ]
}

tematica = {
    "Fantasía" , "Ciencia ficción" , "Actualidad"}

genero = {
    "Femenino" , "Masculino" , "No binario"}

caracteristicas_fisicas = {
    "Complexión": [
        "Robusta", "Esbelta", "Media", "Definida"
    ],
    "Cabello": [
        "Largo", "Medio", "Corto", "Pelón"
    ],
    "Color de piel": [
        "Afro", "Moreno", "Blanco", "Olivo", "Albino", "Almendrado"
    ],
    "Color fantasía": [
        "Rojo", "Verde", "Morado", "Azul", "Amarillo", "Rosa"
    ]
}

colores_principales = {
    "Fríos", "Calidos", "Pasteles "
}
