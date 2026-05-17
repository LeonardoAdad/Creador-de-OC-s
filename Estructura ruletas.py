
from Diccionarios import escenarios, profesiones, Razas, tematica, genero, caracteristicas_fisicas, colores_principales
from random import choice
import time

def ruleta_spin(opciones, mensaje):
    print("Girando...", end=' ', flush=True)
    time.sleep(1) 
    elegido = choice(opciones)
    print(f"{mensaje} {elegido}")
    return elegido

def generar_oc():
    print("Seleccionando Temática...")
    Tematica = ruleta_spin(list(tematica), "tu temática es:")
    
    print("Seleccionando Género...")
    Genero = ruleta_spin(list(genero), "tu género es:")
    
    print("Seleccionando Raza...")
    Raza = ruleta_spin(list(Razas), "tu raza es:")
    
    print("Seleccionando Características Físicas...")

    print("Complexión:")
    Complexion = ruleta_spin(caracteristicas_fisicas["Complexión"], "tu complexión es:")

    print("Cabello:")
    Cabello = ruleta_spin(caracteristicas_fisicas["Cabello"], "tu cabello es:")

    print("Color de piel:")
    Color_piel = ruleta_spin(caracteristicas_fisicas["Color de piel"], "tu color de piel es:")
    
    print("Seleccionando Profesión...")
    Profesion = ruleta_spin(profesiones[Tematica], "la profesión de tu personaje es:")
    
    print("Seleccionando Escenario...")
    Escenario = ruleta_spin(escenarios[Tematica], "el escenario de tu personaje es:")
    
    print("Paleta de colores:")
    Color_fantasia = ruleta_spin(list(colores_principales), "tu paleta de colores sera:")
    
    print("\n--- Personaje Generado ---")
    print(f"Temática: {Tematica}")
    print(f"Género: {Genero}")
    print(f"Raza: {Raza}")
    print(f"Complexión: {Complexion}")
    print(f"Cabello: {Cabello}")
    print(f"Color de piel: {Color_piel}")
    print(f"Profesión: {Profesion}")
    print(f"Escenario: {Escenario}")
    print(f"Paleta de colores: {Color_fantasia}")

if __name__ == "__main__":
    generar_oc()
    