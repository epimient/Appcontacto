import tkinter as tk
from tkinter import messagebox
import requests

# URL base de la API
base_url = "https://serviciowebflask.onrender.com/usuarios"

# Funciones para interactuar con la API
def crear_usuario():
    nombre = entry_nombre.get()
    email = entry_email.get()
    
    if not nombre or not email:
        messagebox.showerror("Error", "Nombre y correo son obligatorios.")
        return
    
    usuario = {"nombre": nombre, "email": email}
    response = requests.post(base_url, json=usuario)
    
    if response.status_code == 201:
        messagebox.showinfo("Éxito", "Usuario creado con éxito.")
        limpiar_campos()
    else:
        messagebox.showerror("Error", "Error al crear usuario.")

def obtener_usuarios():
    response = requests.get(base_url)
    if response.status_code == 200:
        usuarios = response.json()['usuarios']
        lista_usuarios.delete(0, tk.END)
        for usuario in usuarios:
            lista_usuarios.insert(tk.END, f"ID: {usuario['id']} - {usuario['nombre']} - {usuario['email']}")
    else:
        messagebox.showerror("Error", "Error al obtener usuarios.")

def obtener_usuario():
    try:
        id_usuario = int(entry_id.get())
        response = requests.get(f"{base_url}/{id_usuario}")
        if response.status_code == 200:
            usuario = response.json()['usuario']
            messagebox.showinfo("Usuario encontrado", f"ID: {usuario['id']} - {usuario['nombre']} - {usuario['email']}")
        else:
            messagebox.showerror("Error", "Usuario no encontrado.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un ID válido.")

def actualizar_usuario():
    try:
        id_usuario = int(entry_id.get())
        nombre = entry_nombre.get()
        email = entry_email.get()

        if not nombre or not email:
            messagebox.showerror("Error", "Nombre y correo son obligatorios.")
            return
        
        usuario = {"nombre": nombre, "email": email}
        response = requests.put(f"{base_url}/{id_usuario}", json=usuario)
        
        if response.status_code == 200:
            messagebox.showinfo("Éxito", f"Usuario con ID {id_usuario} actualizado.")
        else:
            messagebox.showerror("Error", "Error al actualizar usuario.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un ID válido.")

def eliminar_usuario():
    try:
        id_usuario = int(entry_id.get())
        response = requests.delete(f"{base_url}/{id_usuario}")
        
        if response.status_code == 200:
            messagebox.showinfo("Éxito", f"Usuario con ID {id_usuario} eliminado.")
        else:
            messagebox.showerror("Error", "Error al eliminar usuario.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un ID válido.")

def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_id.delete(0, tk.END)

# Configuración de la ventana de Tkinter
root = tk.Tk()
root.title("Gestión de Usuarios")

# Labels y Entrys
label_id = tk.Label(root, text="ID Usuario:")
label_id.grid(row=0, column=0)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1)

label_nombre = tk.Label(root, text="Nombre:")
label_nombre.grid(row=1, column=0)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=1, column=1)

label_email = tk.Label(root, text="Correo:")
label_email.grid(row=2, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1)

# Botones de acción
btn_crear = tk.Button(root, text="Crear Usuario", command=crear_usuario)
btn_crear.grid(row=3, column=0)

btn_obtener = tk.Button(root, text="Obtener Usuarios", command=obtener_usuarios)
btn_obtener.grid(row=3, column=1)

btn_actualizar = tk.Button(root, text="Actualizar Usuario", command=actualizar_usuario)
btn_actualizar.grid(row=4, column=0)

btn_eliminar = tk.Button(root, text="Eliminar Usuario", command=eliminar_usuario)
btn_eliminar.grid(row=4, column=1)

btn_limpiar = tk.Button(root, text="Limpiar Campos", command=limpiar_campos)
btn_limpiar.grid(row=5, column=0, columnspan=2)

# Lista de usuarios
lista_usuarios = tk.Listbox(root, height=10, width=50)
lista_usuarios.grid(row=6, column=0, columnspan=2)

# Ejecutar la interfaz
root.mainloop()
