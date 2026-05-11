import random
import time 

# ── Diccionarios ──
escenarios = {
    "Fantasía": [
        "Salon del trono", "montaña misteriosa", "Bosque Mágico", "Aldea", "Templo antiguo",
        "Taberna", "Caverna de dragones", "Isla Perdida", "Establo de caballos", "Escuela mágica"
    ],
    "Cyberpunk": [
        "Bar clandestino", "Base espacial", "Ciudad futurista",
        "Barrios Bajos", "Nave espacial", "Edificio corporativo",
        "Bar lujoso", "Ciberespacio", "Ciudad subterránea", "Batalla de por territorio"
    ],
    "Actualidad": [
        "El rancho", "Puestos callejeros", "Centro de la ciudad", "Cafetería",
        "Oficina", "Barrio", "Calle Transitada", "Transporte público",
        "Bar", "Parque"
    ]
}

profesiones = {
    "Fantasía": [
        "Mago", "Caballero", "Nigromante", "Arquero", "Asesino",
        "Realeza", "Plebeyo", "Bardo", "Arquero", "Bufon"
    ],
    "Cyberpunk": [
        "Hacker/Netrunner", "Pandillero", "Nomada", "Fixer", "Corporativo",
        "Policía", "Político", "Rockerboy", "Ingeniero", "Sicario"
    ],
    "Actualidad": [
        "Doctor", "Estudiante", "Chofer", "Bartender", "Oficinista",
        "Chef", "Artista", "Cholo", "Programador", "Abogado", "Profesor"
    ]
}

Razas = {
    "Humano", "Elfo", "Enano", "Orco", "Goblin", "Tifling", "Celestial", "Draconido", "Mediano", "Semielfo"
}

tematica = {
    "Fantasía", "Cyberpunk", "Actualidad"
}

genero = {
    "Femenino", "Masculino", "No binario"
}

caracteristicas_fisicas = {
    "Complexión": [
        "Robusta", "Esbelta", "Media", "Definida"
    ],
    "Cabello": [
        "Largo", "Medio", "Corto", "Pelón"
    ],
    "Color de piel": [
        "Afro", "Moreno", "Blanco", "Olivo", "Albino", "Almendrado", "Rojo", "Verde", "Morado", "Azul", "Amarillo", "Rosa"
    ]
}

colores_principales = {
    "Fríos", "Calidos", "Pasteles"
}


