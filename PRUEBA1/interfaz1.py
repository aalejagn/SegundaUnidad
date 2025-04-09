# interfaz1.py
from tkinter import Tk, Label, Button, Frame, StringVar, Canvas, Entry
from tkinter import ttk, messagebox
from db_soriana import insertar_cliente, ver_clientes, actualizar_cliente, eliminar_cliente, limpiar_campos

# Main window setup
def crear_ventana():
    ventana = Tk()
    ventana.title("Punto de Venta - TkPOS")
    ventana.geometry("800x600")
    ventana.configure(bg="#E6F0FA")
    return ventana

# Login screen with dropdown
def seleccionar_usuario(ventana):
    frame_login = Frame(ventana, bg="#E6F0FA")
    frame_login.pack(expand=True)

    Label(frame_login, text="TkPOS", font=("Arial", 36, "bold"), fg="#1E90FF", bg="#E6F0FA").pack(pady=20)
    Label(frame_login, text="Dirección: Neiva - Huila\nCelular: +573223408279\nEmail: innovasoftcode@gmail.com", 
          font=("Arial", 10), bg="#E6F0FA").pack(pady=5)
    Label(frame_login, text="Software creado por Kevin Arboleda / Innovasoft Code\n© 2024 Todos los derechos reservados", 
          font=("Arial", 8), bg="#E6F0FA").pack(pady=5)

    Label(frame_login, text="Seleccione un Tipo de Usuario:", font=("Arial", 12, "bold"), bg="#E6F0FA").pack(pady=20)
    tipo_usuario = StringVar()
    opciones = ttk.Combobox(frame_login, values=["Administrador", "Trabajador"], state="readonly", textvariable=tipo_usuario, font=("Arial", 12))
    opciones.pack(pady=10)

    Button(frame_login, text="Iniciar", font=("Arial", 12, "bold"), bg="#32CD32", fg="white", 
           command=lambda: validar_usuario(tipo_usuario.get(), ventana, frame_login)).pack(pady=20)

# Validate user selection
def validar_usuario(tipo_usuario, ventana, frame_login):
    if tipo_usuario in ["Administrador", "Trabajador"]:
        frame_login.destroy()
        crear_dashboard(ventana, tipo_usuario)
    else:
        messagebox.showerror("Error", "Por favor, seleccione un tipo de usuario")

# Main dashboard with sidebar and welcome screen
def crear_dashboard(ventana, rol):
    sidebar = Frame(ventana, bg="#D3D3D3", width=200)
    sidebar.pack(side="left", fill="y")

    opciones = ["Inventario", "Clientes", "Proveedor", "Pedidos", "Reportes", "Configuración", "Gastos", "About Us"]
    for opcion in opciones:
        if opcion == "Clientes":
            Button(sidebar, text=opcion, font=("Arial", 12), bg="#4682B4", fg="white", width=20, 
                   command=lambda: manejar_clientes(ventana, rol, sidebar)).pack(pady=5, padx=10)
        else:
            Button(sidebar, text=opcion, font=("Arial", 12), bg="#4682B4", fg="white", width=20).pack(pady=5, padx=10)

def mostrar_contenido_principal(ventana, rol, sidebar):
    for widget in ventana.winfo_children():
        if widget != sidebar:
            widget.destroy()

    main_frame = Frame(ventana, bg="#E6F0FA")
    main_frame.pack(expand=True, fill="both")

    Label(main_frame, text="PUNTO DE VENTA", font=("Arial", 20, "bold"), bg="#E6F0FA").pack(pady=10)
    Label(main_frame, text=f"Rol: {rol}", font=("Arial", 12), bg="#E6F0FA").pack()

    frame_clientes = crear_seccion_clientes(main_frame, rol)
    frame_clientes.pack(pady=10)

# Handle "Clientes" button click
def manejar_clientes(ventana, rol, sidebar):
    for widget in ventana.winfo_children():
        if widget != sidebar:
            widget.destroy()

    main_frame = Frame(ventana, bg="#E6F0FA")
    main_frame.pack(expand=True, fill="both")

    Label(main_frame, text="PUNTO DE VENTA", font=("Arial", 20, "bold"), bg="#E6F0FA").pack(pady=10)
    Label(main_frame, text=f"Rol: {rol}", font=("Arial", 12), bg="#E6F0FA").pack()

    if rol == "Administrador":
        frame_clientes = crear_seccion_clientes(main_frame, rol)
        frame_clientes.pack(pady=10)
    else:
        Label(main_frame, text="Acceso restringido: Solo administradores pueden gestionar clientes.", 
              font=("Arial", 12), bg="#E6F0FA").pack(pady=10)

# Client management section
def crear_seccion_clientes(ventana, rol):
    frame_clientes = Frame(ventana, bg="#E6F0FA")
    
    # Entry fields
    entries = {}
    labels = ["Teléfono:", "Nombre:", "Dirección:", "RFC:", "Correo:"]
    for i, label in enumerate(labels):
        Label(frame_clientes, text=label, bg="#E6F0FA").grid(row=i, column=0, padx=5, pady=5, sticky="e")
        entry = Entry(frame_clientes)
        entry.grid(row=i, column=1, padx=5, pady=5)
        entries[label] = entry

    # Buttons
    frame_buttons = Frame(frame_clientes, bg="#E6F0FA")
    frame_buttons.grid(row=5, columnspan=2, pady=10)

    # Table
    tabla = ttk.Treeview(frame_clientes, columns=("Teléfono", "Nombre", "Dirección", "RFC", "Correo"), show="headings")
    for col in ("Teléfono", "Nombre", "Dirección", "RFC", "Correo"):
        tabla.heading(col, text=col)
        tabla.column(col, width=100)
    tabla.grid(row=6, columnspan=2, pady=10, sticky="nsew")

    # Populate the table with data from the database
    ver_clientes(tabla)

    # Button commands
    def on_agregar():
        telefono = entries["Teléfono:"].get().strip()
        nombre = entries["Nombre:"].get().strip()
        direccion = entries["Dirección:"].get().strip()
        rfc = entries["RFC:"].get().strip()
        correo = entries["Correo:"].get().strip()
        if insertar_cliente(telefono, nombre, direccion, rfc, correo):
            ver_clientes(tabla)
            limpiar_campos(entries.values())

    def on_eliminar():
        selected_item = tabla.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un cliente para eliminar.")
            return
        telefono = tabla.item(selected_item)["values"][0]
        if eliminar_cliente(telefono):
            ver_clientes(tabla)
            limpiar_campos(entries.values())

    def on_actualizar():
        selected_item = tabla.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un cliente para actualizar.")
            return
        telefono = entries["Teléfono:"].get().strip()
        nombre = entries["Nombre:"].get().strip()
        direccion = entries["Dirección:"].get().strip()
        rfc = entries["RFC:"].get().strip()
        correo = entries["Correo:"].get().strip()
        if actualizar_cliente(telefono, nombre, direccion, rfc, correo):
            ver_clientes(tabla)
            limpiar_campos(entries.values())

    def on_seleccionar(event):
        selected_item = tabla.selection()
        if selected_item:
            values = tabla.item(selected_item)["values"]
            for i, label in enumerate(labels):
                entries[label].delete(0, "end")
                entries[label].insert(0, values[i] if values[i] else "")

    # Bind the selection event
    tabla.bind("<<TreeviewSelect>>", on_seleccionar)

    # Add buttons
    Button(frame_buttons, text="Agregar", command=on_agregar).grid(row=0, column=0, padx=5)
    Button(frame_buttons, text="Eliminar", command=on_eliminar).grid(row=0, column=1, padx=5)
    Button(frame_buttons, text="Actualizar", command=on_actualizar).grid(row=0, column=2, padx=5)
    Button(frame_buttons, text="Limpiar Campos", command=lambda: limpiar_campos(entries.values())).grid(row=0, column=3, padx=5)

    # Make the table expandable
    frame_clientes.grid_rowconfigure(6, weight=1)
    frame_clientes.grid_columnconfigure(0, weight=1)
    frame_clientes.grid_columnconfigure(1, weight=1)
    
    return frame_clientes

# Run the application
if __name__ == "__main__":
    ventana = crear_ventana()
    seleccionar_usuario(ventana)
    ventana.mainloop()