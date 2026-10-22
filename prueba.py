import webbrowser
import time
import tkinter as tk
from tkinter import messagebox
import threading
import os
import subprocess

# 1. Función para subir el volumen al 100% (Solo Windows)
def subir_volumen_maximo():
    try:
        # Crea un script VBS temporal que presiona la tecla de "Subir Volumen" 50 veces
        vbs_script = """
        Set WshShell = CreateObject("WScript.Shell")
        For i = 1 To 50
            WshShell.SendKeys(chr(175))
        Next
        """
        with open("volumen_trampa.vbs", "w") as file:
            file.write(vbs_script)
        # Ejecuta el script y luego lo borra para no dejar rastro
        subprocess.run(["cscript", "//nologo", "volumen_trampa.vbs"], creationflags=subprocess.CREATE_NO_WINDOW)
        os.remove("volumen_trampa.vbs")
    except:
        pass

# 2. Función para mostrar ventanas emergentes (Pop-ups falsos)
def mostrar_errores():
    # Ocultamos la ventana principal de Tkinter
    root = tk.Tk()
    root.withdraw()
    
    mensajes = [
        ("Fallo Crítico", "Error 404: Dignidad no encontrada."),
        ("Windows Defender", "¡ALERTA! Se ha detectado un usuario con mal gusto musical."),
        ("Sistema", "Borrando carpeta System32... 15% completado"),
        ("Sistema", "Borrando carpeta System32... 89% completado"),
        ("Sistema", "¡Es broma! Pero caíste redondito. 😜")
    ]
    
    for titulo, mensaje in mensajes:
        messagebox.showwarning(titulo, mensaje)
        time.sleep(0.5)

# --- INICIO DE LA SECUENCIA DE TROLLEO ---

# Paso 1: Abrir Opera para que parezca que todo es normal
# Intentará abrir Opera de forma genérica
try:
    os.system('start opera')
except:
    pass

time.sleep(2) # Espera 2 segundos para que se confíe

# Paso 2: Subir el volumen en un hilo paralelo para no pausar el script
hilo_volumen = threading.Thread(target=subir_volumen_maximo)
hilo_volumen.start()

# Paso 3: Lanzar el Rickroll a todo volumen
# (El parámetro autoplay=1 intenta que se reproduzca solo)
webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ?autoplay=1")
time.sleep(3)

# Paso 4: Abrir pestañas con búsquedas "comprometedoras"
busquedas_falsas = [
    "https://www.google.com/search?q=como+saber+si+soy+adoptado",
    "https://www.google.com/search?q=por+que+me+huelen+los+pies",
    "https://www.google.com/search?q=remedios+para+la+calvicie+prematura"
]

for busqueda in busquedas_falsas:
    webbrowser.open(busqueda)
    time.sleep(1)

# Paso 5: Bombardeo de mensajes de error
mostrar_errores()