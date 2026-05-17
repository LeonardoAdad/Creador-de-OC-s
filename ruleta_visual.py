import pygame
import random
import math
import tkinter as tk
from tkinter import messagebox
from Diccionarios import Razas, tematica, genero, caracteristicas_fisicas, colores_principales, escenarios, profesiones
from Diccionarios import Acciones_por_profesion_y_escenario as ACCIONES_PROFESION_ESCENARIO

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
ANCHO = 1600
ALTO = 1000
FPS = 60

# Colores
COLOR_BG = (10, 14, 39)
COLOR_ACCENT = (0, 255, 255)
COLOR_SUCCESS = (0, 255, 0)
COLOR_TEXT = (255, 255, 255)
COLOR_BUTTON = (0, 255, 255)
COLOR_BUTTON_HOVER = (0, 200, 200)
COLOR_BUTTON_PRESS = (0, 150, 150)
COLOR_RULETA = [(255, 107, 107), (78, 205, 196), (69, 183, 209), (249, 202, 36), 
                (108, 92, 231), (162, 155, 254), (253, 123, 168), (253, 203, 110), 
                (0, 184, 148), (253, 123, 168)]

class Ruleta:
    """Clase para manejar una ruleta individual"""
    def __init__(self, x, y, nombre, opciones):
        self.x = x
        self.y = y
        self.nombre = nombre
        self.opciones = opciones
        self.radio = 80
        self.angulo_actual = 0
        self.velocidad_angular = 0
        self.girando = False
        self.resultado = None
        self.tiempo_giro = 0
        self.duracion_giro = 2000  # milisegundos
        
    def actualizar(self, dt):
        """Actualiza la física del giro"""
        if self.girando:
            self.tiempo_giro += dt
            
            # Deceleración suave
            progreso = self.tiempo_giro / self.duracion_giro
            if progreso >= 1:
                progreso = 1
                self.girando = False
            
            # Función de easing (ease-out)
            velocidad = (1 - progreso) ** 2
            self.velocidad_angular = velocidad * 1080  # 3 giros completos
            self.angulo_actual += self.velocidad_angular * (dt / 1000)
            self.angulo_actual %= 360
            
            if not self.girando and self.opciones:
                # Determinar resultado final
                num_opciones = len(self.opciones)
                angulo_por_opcion = 360 / num_opciones
                idx = int((360 - self.angulo_actual) / angulo_por_opcion) % num_opciones
                self.resultado = self.opciones[idx]
    
    def dibujar(self, surface, font_pequeña, font_mediana):
        """Dibuja la ruleta"""
        if not self.opciones:
            # Si no hay opciones, mostrar mensaje
            texto = font_mediana.render("Sin opciones", True, (255, 107, 107))
            rect = texto.get_rect(center=(self.x, self.y + 100))
            surface.blit(texto, rect)
            return
        
        centro = (self.x, self.y)
        num_opciones = len(self.opciones)
        angulo_por_opcion = 360 / num_opciones
        
        # Dibujar secciones de la ruleta
        for i, opcion in enumerate(self.opciones):
            angulo_inicio = i * angulo_por_opcion - self.angulo_actual
            color = COLOR_RULETA[i % len(COLOR_RULETA)]
            
            # Dibujar sector circular
            puntos = [centro]
            for j in range(int(angulo_por_opcion) + 1):
                angulo = math.radians(angulo_inicio + j)
                x = centro[0] + self.radio * math.cos(angulo)
                y = centro[1] + self.radio * math.sin(angulo)
                puntos.append((x, y))
            
            if len(puntos) > 2:
                pygame.draw.polygon(surface, color, puntos)
                pygame.draw.polygon(surface, COLOR_ACCENT, puntos, 2)
            
            # Dibujar texto
            angulo_medio = math.radians(angulo_inicio + angulo_por_opcion / 2)
            radio_texto = self.radio * 0.65
            texto_x = centro[0] + radio_texto * math.cos(angulo_medio)
            texto_y = centro[1] + radio_texto * math.sin(angulo_medio)
            
            texto_corto = opcion[:10] if len(opcion) > 10 else opcion
            texto_surf = font_pequeña.render(texto_corto, True, COLOR_TEXT)
            texto_rect = texto_surf.get_rect(center=(texto_x, texto_y))
            surface.blit(texto_surf, texto_rect)
        
        # Dibujar círculo interior
        pygame.draw.circle(surface, COLOR_BG, centro, 25)
        pygame.draw.circle(surface, COLOR_ACCENT, centro, 25, 3)
        
        # Dibujar aguja (triángulo en la parte superior)
        aguja_points = [
            (centro[0], centro[1] - self.radio - 15),
            (centro[0] - 10, centro[1] - self.radio + 5),
            (centro[0] + 10, centro[1] - self.radio + 5)
        ]
        pygame.draw.polygon(surface, (255, 255, 0), aguja_points)
        pygame.draw.polygon(surface, (255, 107, 157), aguja_points, 2)
        
        # Dibujar nombre
        texto_nombre = font_mediana.render(self.nombre, True, COLOR_ACCENT)
        rect_nombre = texto_nombre.get_rect(center=(self.x, self.y - 120))
        surface.blit(texto_nombre, rect_nombre)
        
        # Dibujar resultado
        if self.resultado:
            texto_resultado = font_pequeña.render(self.resultado, True, COLOR_SUCCESS)
            rect_resultado = texto_resultado.get_rect(center=(self.x, self.y + 120))
            
            # Fondo para el resultado
            rect_fondo = rect_resultado.inflate(20, 20)
            pygame.draw.rect(surface, COLOR_BG, rect_fondo)
            pygame.draw.rect(surface, COLOR_SUCCESS, rect_fondo, 2)
            surface.blit(texto_resultado, rect_resultado)
    
    def girar(self, duracion=2000):
        """Inicia el giro de la ruleta"""
        self.girando = True
        self.tiempo_giro = 0
        self.duracion_giro = duracion
        self.resultado = None
        self.angulo_actual = random.uniform(0, 360)

    def esta_sobre(self, pos):
        """Verifica si una posición está sobre la ruleta."""
        x, y = pos
        return (x - self.x) ** 2 + (y - self.y) ** 2 <= self.radio ** 2


class Boton:
    """Clase para los botones"""
    def __init__(self, x, y, ancho, alto, texto, color=COLOR_BUTTON):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.texto = texto
        self.color = color
        self.color_hover = COLOR_BUTTON_HOVER
        self.color_original = color
        self.presionado = False
        
    def dibujar(self, surface, font, mouse_pos):
        """Dibuja el botón"""
        color = self.color
        
        # Verificar si el mouse está sobre el botón
        if self.rect.collidepoint(mouse_pos):
            color = self.color_hover
        
        if self.presionado:
            color = COLOR_BUTTON_PRESS
        
        # Dibujar botón
        pygame.draw.rect(surface, color, self.rect)
        pygame.draw.rect(surface, COLOR_TEXT, self.rect, 3)
        
        # Dibujar texto
        texto_surf = font.render(self.texto, True, (0, 0, 0) if color == COLOR_BUTTON else COLOR_TEXT)
        texto_rect = texto_surf.get_rect(center=self.rect.center)
        surface.blit(texto_surf, texto_rect)
    
    def esta_sobre(self, pos):
        """Verifica si el mouse está sobre el botón"""
        return self.rect.collidepoint(pos)


class GeneradorOC:
    def __init__(self):
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Generador de OC - Pygame")
        self.reloj = pygame.time.Clock()
        self.corriendo = True
        self.fps = FPS
        
        # Fuentes
        self.font_grande = pygame.font.Font(None, 48)
        self.font_mediana = pygame.font.Font(None, 24)
        self.font_pequeña = pygame.font.Font(None, 18)
        
        # Datos
        self.tematica_lista = sorted(list(tematica))
        self.genero_lista = sorted(list(genero))
        self.razas_lista = sorted(list(Razas))
        self.colores_lista = sorted(list(colores_principales))
        
        self.resultados = {}
        self.generando = False
        self.queue_ruletas = []
        
        # Crear ruletas
        self.ruletas = {
            "Temática": Ruleta(200, 300, "Temática", self.tematica_lista),
            "Género": Ruleta(550, 300, "Género", self.genero_lista),
            "Raza": Ruleta(900, 300, "Raza", self.razas_lista),
            "Complexión": Ruleta(1250, 300, "Complexión", caracteristicas_fisicas["Complexión"]),
            "Cabello": Ruleta(200, 700, "Cabello", caracteristicas_fisicas["Cabello"]),
            "Color de piel": Ruleta(550, 700, "Color de piel", caracteristicas_fisicas["Color de piel"]),
            "Profesión": Ruleta(900, 700, "Profesión", []),
            "Escenario": Ruleta(1250, 700, "Escenario", []),
        }
        
        # Crear botones
        self.btn_generar = Boton(ANCHO//2 - 120, ALTO - 100, 240, 60, "GENERAR OC")
        self.btn_limpiar = Boton(ANCHO//2 - 120, ALTO - 170, 240, 60, "LIMPIAR RESULTADOS", color=(255, 107, 107))
        
        
        # Ruleta de colores
        self.ruleta_colores = Ruleta(100, 100, "Paleta", self.colores_lista)
        self.ruleta_colores.radio = 50
    
    def procesar_eventos(self):
        """Procesa los eventos del mouse y teclado"""
        mouse_pos = pygame.mouse.get_pos()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.corriendo = False

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if self.btn_generar.esta_sobre(mouse_pos) and not self.generando:
                    self.generar_oc()
                elif self.btn_limpiar.esta_sobre(mouse_pos):
                    self.limpiar()
                elif self.ruleta_colores.esta_sobre(mouse_pos) and not self.generando:
                    self.ruleta_colores.girar()
    
    def actualizar(self, dt):
        """Actualiza el estado del juego"""
        # Actualizar ruletas
        for ruleta in self.ruletas.values():
            ruleta.actualizar(dt)
        
        self.ruleta_colores.actualizar(dt)
        
        # Procesar cola de ruletas
        if self.generando:
            # Verificar si la ruleta actual terminó
            if self.queue_ruletas and not self.queue_ruletas[0]["ruleta"].girando:
                ruleta = self.queue_ruletas[0]["ruleta"]
                self.resultados[ruleta.nombre] = ruleta.resultado
                self.queue_ruletas.pop(0)

                # Actualizar opciones dependientes antes de iniciar la siguiente ruleta
                self.actualizar_opciones_dependientes()

                if self.queue_ruletas:
                    self.queue_ruletas[0]["ruleta"].girar()
                else:
                    self.generando = False
                    self.mostrar_resumen()
    
    def dibujar(self):
        """Dibuja todo en la pantalla"""
        self.pantalla.fill(COLOR_BG)
        
        mouse_pos = pygame.mouse.get_pos()
        
        # Título
        titulo = self.font_grande.render("GENERADOR DE OC", True, COLOR_ACCENT)
        rect_titulo = titulo.get_rect(center=(ANCHO // 2, 40))
        self.pantalla.blit(titulo, rect_titulo)
        
        # Dibujar ruleta de colores
        self.ruleta_colores.dibujar(self.pantalla, self.font_pequeña, self.font_mediana)
        
        # Dibujar ruletas
        for ruleta in self.ruletas.values():
            ruleta.dibujar(self.pantalla, self.font_pequeña, self.font_mediana)
        
        # Dibujar botones
        self.btn_generar.dibujar(self.pantalla, self.font_mediana, mouse_pos)
        self.btn_limpiar.dibujar(self.pantalla, self.font_mediana, mouse_pos)
        
        # Dibujar estado
        if self.generando:
            estado = self.font_pequeña.render("Generando...", True, COLOR_SUCCESS)
            self.pantalla.blit(estado, (ANCHO - 150, ALTO - 50))
        
        pygame.display.flip()
    
    def generar_oc(self):
        """Genera un nuevo OC"""
        if self.generando:
            return
        
        self.generando = True
        self.resultados = {}
        self.queue_ruletas = []
        
        # Limpiar ruletas
        for ruleta in self.ruletas.values():
            ruleta.resultado = None
            ruleta.girando = False
            ruleta.angulo_actual = 0
        self.ruleta_colores.resultado = None
        self.ruleta_colores.girando = False
        self.ruleta_colores.angulo_actual = 0
        
        # Agregar ruletas a la cola
        orden = [
            self.ruletas["Temática"],
            self.ruletas["Género"],
            self.ruletas["Raza"],
            self.ruletas["Complexión"],
            self.ruletas["Cabello"],
            self.ruletas["Color de piel"],
            self.ruleta_colores,
            self.ruletas["Profesión"],
            self.ruletas["Escenario"],
        ]
        
        for ruleta in orden:
            self.queue_ruletas.append({"ruleta": ruleta})
        
        self.actualizar_opciones_dependientes()
        
        # Iniciar primera ruleta
        if self.queue_ruletas:
            self.queue_ruletas[0]["ruleta"].girar()
    

    def actualizar_opciones_dependientes(self):
        """Asigna las opciones de Profesión y Escenario según la temática seleccionada."""
        tema = self.resultados.get("Temática")
        if not tema:
            return
        if tema in profesiones:
            self.ruletas["Profesión"].opciones = profesiones[tema]
        if tema in escenarios:
            self.ruletas["Escenario"].opciones = escenarios[tema]

    def mostrar_resumen(self):
        """Muestra resumen en consola y ventana emergente con descripción"""
        if self.ruleta_colores.resultado:
            self.resultados["Paleta"] = self.ruleta_colores.resultado

        # Imprimir resumen en consola
        print("\n" + "="*50)
        print(" TU PERSONAJE GENERADO:")
        print("="*50)
        for key, value in self.resultados.items():
            print(f"  {key}: {value}")
        print("="*50 + "\n")

        descripcion = self.generar_descripcion_detallada()

        # Mostrar una ventana emergente modal con Tkinter (bloquea hasta cerrarla)
        try:
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo("Descripción del personaje", descripcion)
            root.destroy()
        except Exception as e:
            print("No se pudo mostrar la ventana emergente:", e)

    def generar_descripcion_detallada(self):
        """Genera una narrativa más detallada y contextualizada del personaje."""
        tema = self.resultados.get("Temática", "una temática desconocida")
        profesion = self.resultados.get("Profesión", "una profesión desconocida")
        escenario = self.resultados.get("Escenario", "un escenario desconocido")
        genero_val = self.resultados.get("Género", "")
        raza = self.resultados.get("Raza", "")
        complexion = self.resultados.get("Complexión", "")
        cabello = self.resultados.get("Cabello", "")
        color_piel = self.resultados.get("Color de piel", "")
        paleta = self.resultados.get("Paleta", "")

        identidad = " ".join(filter(None, [genero_val, raza])).strip() or "El personaje"
        detalles = ", ".join(filter(None, [f"complexión {complexion}" if complexion else "", f"cabello {cabello}" if cabello else "", f"piel {color_piel}" if color_piel else ""]))

        sujeto = identidad
        if detalles:
            primer_parrafo = f"{sujeto} tiene {detalles}."
        else:
            primer_parrafo = f"{sujeto}."

        prof_lower = profesion.lower() if profesion else ""
        esc_lower = escenario.lower() if escenario else ""

        # Intenta obtener la acción exacta para la profesión y el escenario
        accion = None
        if prof_lower in ACCIONES_PROFESION_ESCENARIO:
            acciones_por_escenario = ACCIONES_PROFESION_ESCENARIO[prof_lower]
            accion = acciones_por_escenario.get(esc_lower)
            if not accion and acciones_por_escenario:
                accion = next(iter(acciones_por_escenario.values()))

        if accion:
            segundo_parrafo = accion
        else:
            segundo_parrafo = f"En {escenario}, trabaja como {profesion} dentro de la temática {tema}."

        paleta_text = f"Su paleta de colores principal es {paleta}." if paleta else ""

        descripcion = primer_parrafo + "\n\n" + f"Acción: {segundo_parrafo}" + ("\n" + paleta_text if paleta_text else "")
        return descripcion
    
    def ejecutar(self):
        """Loop principal"""
        while self.corriendo:
            dt = self.reloj.tick(self.fps)
            
            self.procesar_eventos()
            self.actualizar(dt)
            self.dibujar()
        
        pygame.quit()


if __name__ == "__main__":
    app = GeneradorOC()
    app.ejecutar()