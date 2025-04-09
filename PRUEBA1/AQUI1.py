from tkinter import Tk, Label, Button, Frame, StringVar, Canvas, Entry
from tkinter import ttk, messagebox

# Main window setup
def crear_ventana():
    ventana = Tk()
    ventana.title("Punto de Venta - TkPOS")
    ventana.geometry("800x600")
    ventana.configure(bg="#E6F0FA")  # Light blue background
    return ventana

# Login screen with dropdown
def seleccionar_usuario(ventana):
    frame_login = Frame(ventana, bg="#E6F0FA")
    frame_login.pack(expand=True)

    # Logo and title
    Label(frame_login, text="TkPOS", font=("Arial", 36, "bold"), fg="#1E90FF", bg="#E6F0FA").pack(pady=20)
    Label(frame_login, text="Dirección: Neiva - Huila\nCelular: +573223408279\nEmail: innovasoftcode@gmail.com", 
          font=("Arial", 10), bg="#E6F0FA").pack(pady=5)
    Label(frame_login, text="Software creado por Kevin Arboleda / Innovasoft Code\n© 2024 Todos los derechos reservados", 
          font=("Arial", 8), bg="#E6F0FA").pack(pady=5)

    # Dropdown for user type selection
    Label(frame_login, text="Seleccione un Tipo de Usuario:", font=("Arial", 12, "bold"), bg="#E6F0FA").pack(pady=20)
    tipo_usuario = StringVar()
    opciones = ttk.Combobox(frame_login, values=["Administrador", "Trabajador"], state="readonly", textvariable=tipo_usuario, font=("Arial", 12))
    opciones.pack(pady=10)

    # Green "Iniciar" button
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
    # Sidebar frame
    sidebar = Frame(ventana, bg="#D3D3D3", width=200)
    sidebar.pack(side="left", fill="y")

    # Sidebar buttons (navigation)
    opciones = ["Inventario", "Clientes", "Proveedor", "Pedidos", "Reportes", "Configuración", "Gastos", "Usuarios", "About Us"]
    for opcion in opciones:
        if opcion == "Usuarios":
            Button(sidebar, text=opcion, font=("Arial", 12), bg="#4682B4", fg="white", width=20, 
                   command=lambda: manejar_usuarios(ventana, rol, sidebar)).pack(pady=5, padx=10)
        else:
            Button(sidebar, text=opcion, font=("Arial", 12), bg="#4682B4", fg="white", width=20).pack(pady=5, padx=10)

    # Main content area with welcome screen
    main_frame = Frame(ventana, bg="#E6F0FA")
    main_frame.pack(expand=True, fill="both")

    # Create a canvas for the gradient background
    canvas = Canvas(main_frame, bg="#E6F0FA", highlightthickness=0)
    canvas.pack(expand=True, fill="both")

    # Simulate a gradient background
    canvas.configure(bg="#6A5ACD")

    # Title and subtitle
    Label(canvas, text="PUNTO DE VENTA", font=("Arial", 24, "bold"), fg="white", bg="#6A5ACD").place(relx=0.5, rely=0.1, anchor="center")
    Label(canvas, text="Sistema moderno y eficiente", font=("Arial", 14), fg="white", bg="#6A5ACD").place(relx=0.5, rely=0.18, anchor="center")

    # Placeholder for icons
    Label(canvas, text="[Ventas]", font=("Arial", 12), fg="white", bg="#6A5ACD").place(relx=0.2, rely=0.3, anchor="center")
    Label(canvas, text="[Reportes]", font=("Arial", 12), fg="white", bg="#6A5ACD").place(relx=0.5, rely=0.3, anchor="center")
    Label(canvas, text="[Inventario]", font=("Arial", 12), fg="white", bg="#6A5ACD").place(relx=0.8, rely=0.3, anchor="center")

    # Features list with green bullet points
    features = [
        "Rápido y fácil de usar",
        "Control de inventario en tiempo real",
        "Reportes detallados de ventas",
        "Gestión de clientes y proveedores"
    ]
    for i, feature in enumerate(features):
        Label(canvas, text="●", font=("Arial", 12), fg="#32CD32", bg="#6A5ACD").place(relx=0.35, rely=0.45 + i*0.05, anchor="w")
        Label(canvas, text=feature, font=("Arial", 12), fg="white", bg="#6A5ACD").place(relx=0.38, rely=0.45 + i*0.05, anchor="w")

    # Orange "¡COMENZAR AHORA!" button
    Button(canvas, text="¡COMENZAR AHORA!", font=("Arial", 14, "bold"), bg="#FFA500", fg="white", 
           command=lambda: mostrar_contenido_principal(ventana, rol, sidebar)).place(relx=0.5, rely=0.7, anchor="center")

# Show the main content after clicking "¡COMENZAR AHORA!"
def mostrar_contenido_principal(ventana, rol, sidebar):
    # Clear the main content area (but keep the sidebar)
    for widget in ventana.winfo_children():
        if widget != sidebar:  # Skip the sidebar
            widget.destroy()

    # Main content area
    main_frame = Frame(ventana, bg="#E6F0FA")
    main_frame.pack(expand=True, fill="both")

    # Header
    Label(main_frame, text="PUNTO DE VENTA", font=("Arial", 20, "bold"), bg="#E6F0FA").pack(pady=10)
    Label(main_frame, text=f"Rol: {rol}", font=("Arial", 12), bg="#E6F0FA").pack()

    # Default content (user management section)
    frame_usuarios = crear_seccion_usuarios(main_frame)
    frame_usuarios.pack(pady=10)

# Handle "Usuarios" button click
def manejar_usuarios(ventana, rol, sidebar):
    # Clear the main content area (but keep the sidebar)
    for widget in ventana.winfo_children():
        if widget != sidebar:  # Skip the sidebar
            widget.destroy()

    # Main content area
    main_frame = Frame(ventana, bg="#E6F0FA")
    main_frame.pack(expand=True, fill="both")

    # Header
    Label(main_frame, text="PUNTO DE VENTA", font=("Arial", 20, "bold"), bg="#E6F0FA").pack(pady=10)
    Label(main_frame, text=f"Rol: {rol}", font=("Arial", 12), bg="#E6F0FA").pack()

    # Check role for "Usuarios" section
    if rol == "Administrador":
        frame_usuarios = crear_seccion_usuarios(main_frame)
        frame_usuarios.pack(pady=10)
    else:
        Label(main_frame, text="Acceso restringido: Solo administradores pueden gestionar usuarios.", 
              font=("Arial", 12), bg="#E6F0FA").pack(pady=10)

# User management section (updated to match the image)
def crear_seccion_usuarios(ventana):
    frame_usuarios = Frame(ventana, bg="#E6F0FA")
    
    # Labels and Entry fields
    Label(frame_usuarios, text="Teléfono:", bg="#E6F0FA").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    Entry(frame_usuarios).grid(row=0, column=1, padx=5, pady=5)
    
    Label(frame_usuarios, text="Nombre:", bg="#E6F0FA").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    Entry(frame_usuarios).grid(row=1, column=1, padx=5, pady=5)
    
    Label(frame_usuarios, text="Dirección:", bg="#E6F0FA").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    Entry(frame_usuarios).grid(row=2, column=1, padx=5, pady=5)
    
    Label(frame_usuarios, text="RFC:", bg="#E6F0FA").grid(row=3, column=0, padx=5, pady=5, sticky="e")
    Entry(frame_usuarios).grid(row=3, column=1, padx=5, pady=5)
    
    Label(frame_usuarios, text="Correo:", bg="#E6F0FA").grid(row=4, column=0, padx=5, pady=5, sticky="e")
    Entry(frame_usuarios).grid(row=4, column=1, padx=5, pady=5)
    
    # Buttons
    frame_buttons = Frame(frame_usuarios, bg="#E6F0FA")
    frame_buttons.grid(row=5, columnspan=2, pady=10)
    
    Button(frame_buttons, text="Agregar").grid(row=0, column=0, padx=5)
    Button(frame_buttons, text="Eliminar").grid(row=0, column=1, padx=5)
    Button(frame_buttons, text="Actualizar").grid(row=0, column=2, padx=5)
    Button(frame_buttons, text="Limpiar Campos").grid(row=0, column=3, padx=5)
    
    # Table
    tabla = ttk.Treeview(frame_usuarios, columns=("Teléfono", "Nombre", "Dirección", "RFC", "Correo"), show="headings")
    for col in ("Teléfono", "Nombre", "Dirección", "RFC", "Correo"):
        tabla.heading(col, text=col)
        tabla.column(col, width=100)
    tabla.grid(row=6, columnspan=2, pady=10, sticky="nsew")
    
    # Make the table expandable
    frame_usuarios.grid_rowconfigure(6, weight=1)
    frame_usuarios.grid_columnconfigure(0, weight=1)
    frame_usuarios.grid_columnconfigure(1, weight=1)
    
    return frame_usuarios

# Run the application
ventana = crear_ventana()
seleccionar_usuario(ventana)
ventana.mainloop()