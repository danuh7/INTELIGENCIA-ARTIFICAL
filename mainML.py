import tkinter as tk
from tkinter import filedialog

def choose_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        print("Archivo escogido:", file_path)

# Crear la ventana principal
window = tk.Tk()
window.title("Escoge el archivo de texto")

# Crear el botón
button = tk.Button(window, text="Escoger archivo", command=choose_file)
button.pack(pady=20)

# Ejecutar el bucle principal de la ventana
window.mainloop()
