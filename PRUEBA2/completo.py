import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import pandas as pd
import numpy as np
import scipy.stats as stats
from PIL import Image, ImageTk  # Para mostrar imágenes

class GeneradorNumerosPseudoaleatorios:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        ventana_principal.title("Generador de Números Pseudoaleatorios")
        ventana_principal.geometry("1200x800")
        ventana_principal.configure(bg="#f0f0f0")

        self.cuaderno_principal = ttk.Notebook(ventana_principal)
        self.cuaderno_principal.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.pagina_generador = tk.Frame(self.cuaderno_principal, bg="#f0f0f0")
        self.cuaderno_principal.add(self.pagina_generador, text="Generador")
        self.configurar_pagina_generador()

        self.instancias = {}
        self.ventana_chi = None

    def configurar_pagina_generador(self):
        marco_principal = tk.Frame(self.pagina_generador, bg="#f0f0f0")
        marco_principal.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        tk.Label(marco_principal, text="Generador de Números Pseudoaleatorios", 
                 font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#003366").pack(pady=10)
        tk.Label(marco_principal, text="Seleccione un Método:", 
                 font=("Arial", 12), bg="#f0f0f0").pack(pady=5)

        self.metodos = ["Cuadrados Medios", "Producto Medio", "Multiplicador Constante", "Algoritmo Lineal"]
        self.variable_metodo = tk.StringVar(value="")
        self.desplegable_metodo = ttk.Combobox(marco_principal, textvariable=self.variable_metodo, 
                                              values=self.metodos, state="readonly", width=30)
        self.desplegable_metodo.pack(pady=5)

        self.marco_entradas = tk.Frame(marco_principal, bg="#f0f0f0")
        self.marco_entradas.pack(pady=10)

        self.entradas = {}
        etiquetas = ["Semilla (X0):", "Iteraciones:"]
        for i, etiqueta in enumerate(etiquetas):
            tk.Label(self.marco_entradas, text=etiqueta, bg="#f0f0f0").grid(row=i, column=0, padx=5, pady=5)
            entrada = tk.Entry(self.marco_entradas, width=20, state="disabled")
            entrada.grid(row=i, column=1, padx=5, pady=5)
            self.entradas[etiqueta] = entrada

        self.marco_especifico_metodo = tk.Frame(marco_principal, bg="#f0f0f0")
        self.marco_especifico_metodo.pack(pady=5)
        self.desplegable_metodo.bind("<<ComboboxSelected>>", self.actualizar_campos_entrada)

        self.boton_generar = tk.Button(marco_principal, text="Generar Números", command=self.generar_numeros,
                                    bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), relief="raised")
        self.boton_generar.pack(pady=10)

    def actualizar_campos_entrada(self, evento=None):
        for etiqueta, entrada in list(self.entradas.items()):
            if not entrada.winfo_exists():
                del self.entradas[etiqueta]
            else:
                entrada.config(state="normal")

        for widget in self.marco_especifico_metodo.winfo_children():
            widget.destroy()

        metodo = self.variable_metodo.get()
        etiquetas = {
            "Multiplicador Constante": ["Constante:"],
            "Cuadrados Medios": [],
            "Producto Medio": ["Segunda Semilla (X1):"],
            "Algoritmo Lineal": ["Multiplicador (a):", "Incremento (c):", "Módulo (M):"]
        }

        for i, etiqueta in enumerate(etiquetas.get(metodo, [])):
            tk.Label(self.marco_especifico_metodo, text=etiqueta, bg="#f0f0f0").grid(row=i, column=0, padx=5, pady=5)
            entrada = tk.Entry(self.marco_especifico_metodo, width=20)
            entrada.grid(row=i, column=1, padx=5, pady=5)
            self.entradas[etiqueta] = entrada

    def tiene_digitos_par(self, numero):
        try:
            num = int(numero)
            return len(str(abs(num))) % 2 == 0
        except ValueError:
            return False

    def generar_numeros(self):
        metodo = self.variable_metodo.get()
        if not metodo:
            messagebox.showerror("Error", "Por favor seleccione un método")
            return

        try:
            semilla = self.entradas["Semilla (X0):"].get()
            iteraciones = self.entradas["Iteraciones:"].get()
            if metodo != "Algoritmo Lineal" and (not self.tiene_digitos_par(semilla)):
                messagebox.showerror("Error", "La semilla (X0) debe tener un número par de dígitos")
                return
            semilla = int(semilla)
            iteraciones = int(iteraciones)
            if semilla < 0 or iteraciones <= 0:
                messagebox.showerror("Error", "La semilla (X0) debe ser no negativa y las iteraciones positivas")
                return
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")
            return

        resultados = None
        historial = None

        if metodo == "Multiplicador Constante":
            try:
                constante = self.entradas["Constante:"].get()
                if not self.tiene_digitos_par(constante):
                    messagebox.showerror("Error", "La constante debe tener un número par de dígitos")
                    return
                constante = int(constante)
                if constante <= 0:
                    messagebox.showerror("Error", "La constante debe ser positiva")
                    return
                resultados, historial = self.multiplicador_constante(semilla, constante, iteraciones)
            except (ValueError, KeyError):
                messagebox.showerror("Error", "Ingrese una constante válida")
                return

        elif metodo == "Cuadrados Medios":
            if not self.tiene_digitos_par(semilla):
                messagebox.showerror("Error", "La semilla (X0) debe tener un número par de dígitos")
                return
            resultados, historial = self.metodo_cuadrados_medios(semilla, iteraciones)

        elif metodo == "Producto Medio":
            try:
                semilla2 = self.entradas["Segunda Semilla (X1):"].get()
                if not self.tiene_digitos_par(semilla2):
                    messagebox.showerror("Error", "La segunda semilla (X1) debe tener un número par de dígitos")
                    return
                semilla2 = int(semilla2)
                if semilla2 < 0:
                    messagebox.showerror("Error", "La segunda semilla (X1) debe ser no negativa")
                    return
                resultados, historial = self.metodo_producto_medio(semilla, semilla2, iteraciones)
            except (ValueError, KeyError):
                messagebox.showerror("Error", "Ingrese una segunda semilla válida")
                return

        elif metodo == "Algoritmo Lineal":
            try:
                a = self.entradas["Multiplicador (a):"].get()
                c = self.entradas["Incremento (c):"].get()
                m = self.entradas["Módulo (M):"].get()
                a, c, m = int(a), int(c), int(m)
                if a <= 0 or c < 0 or m <= 0:
                    messagebox.showerror("Error", "Multiplicador (a) y Módulo (M) deben ser positivos, Incremento (c) no negativo")
                    return
                resultados, historial = self.algoritmo_lineal(semilla, a, c, m, iteraciones)
            except (ValueError, KeyError):
                messagebox.showerror("Error", "Ingrese parámetros válidos (a, c, M)")
                return

        if resultados and historial:
            id_instancia = f"{metodo}_{len([k for k in self.instancias.keys() if k.startswith(metodo)]) + 1}"
            self.instancias[id_instancia] = {
                'metodo': metodo,
                'resultados': resultados,
                'historial': historial,
                'pestañas': [],
                'pruebas_ejecutadas': {
                    'chi_cuadrada': False,
                    'kolmogorov': False,
                    'poker': False,
                    'abajo_arriba': False,
                    'abajo_arriba_media': False,
                    'huecos': False
                }
            }
            self.boton_generar.config(state="disabled")
            self.mostrar_resultados(id_instancia)

    def multiplicador_constante(self, x0, constante, iteraciones):
        historial = []
        resultados = []

        longitud_semilla = len(str(abs(x0)))
        lugares_decimales = min(longitud_semilla, 4) if longitud_semilla <= 4 else longitud_semilla
        longitud = len(str(x0))

        for i in range(iteraciones):
            producto = x0 * constante
            producto_str = str(producto).zfill(longitud * 2)
            inicio = (len(producto_str) - longitud) // 2
            nueva_semilla = int(producto_str[inicio:inicio + longitud])
            ri = nueva_semilla / (10 ** longitud)
            ri_formateado = round(ri, lugares_decimales) if lugares_decimales <= 4 else f"{ri:.{lugares_decimales}f}"

            historial.append({
                "Iteración": i + 1, "Semilla": x0, "Constante": constante,
                "Producto": producto, "Producto con Ceros": producto_str,
                "Nueva Semilla": nueva_semilla, "Ri": ri_formateado
            })
            x0 = nueva_semilla
            resultados.append(ri)

        return resultados, historial

    def metodo_cuadrados_medios(self, x0, iteraciones):
        historial = []
        resultados = []

        longitud_semilla = len(str(abs(x0)))
        lugares_decimales = min(longitud_semilla, 4) if longitud_semilla <= 4 else longitud_semilla
        longitud = len(str(x0))

        x = x0
        for i in range(iteraciones):
            cuadrado = x ** 2
            cuadrado_str = str(cuadrado).zfill(longitud * 2)
            inicio = (len(cuadrado_str) - longitud) // 2
            nueva_semilla = int(cuadrado_str[inicio:inicio + longitud])
            ri = nueva_semilla / (10 ** longitud)
            ri_formateado = round(ri, lugares_decimales) if lugares_decimales <= 4 else f"{ri:.{lugares_decimales}f}"

            historial.append({
                "Iteración": i + 1, "Semilla": x, "Cuadrado": cuadrado,
                "Cuadrado con Ceros": cuadrado_str, "Nueva Semilla": nueva_semilla, "Ri": ri_formateado
            })
            x = nueva_semilla
            resultados.append(ri)

        return resultados, historial

    def metodo_producto_medio(self, x0, x1, iteraciones):
        historial = []
        resultados = []

        longitud_semilla = len(str(abs(x0)))
        lugares_decimales = min(longitud_semilla, 4) if longitud_semilla <= 4 else longitud_semilla
        longitud = max(len(str(x0)), len(str(x1)))

        for i in range(iteraciones):
            producto = x0 * x1
            producto_str = str(producto).zfill(longitud * 2)
            inicio = (len(producto_str) - longitud) // 2
            nueva_semilla = int(producto_str[inicio:inicio + longitud])
            ri = nueva_semilla / (10 ** longitud)
            ri_formateado = round(ri, lugares_decimales) if lugares_decimales <= 4 else f"{ri:.{lugares_decimales}f}"

            historial.append({
                "Iteración": i + 1, "X0": x0, "X1": x1, "Producto": producto,
                "Producto con Ceros": producto_str, "Nueva Semilla": nueva_semilla, "Ri": ri_formateado
            })
            x0, x1 = x1, nueva_semilla
            resultados.append(ri)

        return resultados, historial

    def algoritmo_lineal(self, x0, a, c, m, iteraciones):
        historial = []
        resultados = []

        for i in range(iteraciones):
            x1 = (a * x0 + c) % m
            ri = x1 / (m - 1)

            historial.append({
                "Iteración": i + 1, "Xi": x0, "a": a, "c": c, "M": m,
                "Xi+1": x1, "Ri": f"{ri:.6f}"
            })
            x0 = x1
            resultados.append(ri)

        return resultados, historial

    def mostrar_resultados(self, id_instancia):
        pagina_numeros = tk.Frame(self.cuaderno_principal, bg="#e0f7fa")
        self.cuaderno_principal.add(pagina_numeros, text=f"Números - {id_instancia}")
        id_pestaña = str(pagina_numeros)  # Convertimos el widget a string para obtener un identificador único
        print(f"Añadiendo pestaña 'Números - {id_instancia}': {id_pestaña}")
        self.instancias[id_instancia]['pestañas'].append(id_pestaña)

        tk.Label(pagina_numeros, text="Resultados Generados", font=("Arial", 16, "bold"), bg="#e0f7fa", fg="#00796b").pack(pady=10)

        columnas = list(self.instancias[id_instancia]['historial'][0].keys())
        arbol = ttk.Treeview(pagina_numeros, columns=columnas, show="headings", style="Custom.Treeview")
        for col in columnas:
            arbol.heading(col, text=col)
            arbol.column(col, width=120, anchor="center")
        for item in self.instancias[id_instancia]['historial']:
            arbol.insert("", "end", values=[item[col] for col in columnas])
        arbol.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.abrir_ventana_pruebas(id_instancia)

    def abrir_ventana_pruebas(self, id_instancia):
        pagina_pruebas = tk.Frame(self.cuaderno_principal, bg="#f0f0f0")
        self.cuaderno_principal.add(pagina_pruebas, text=f"Pruebas - {id_instancia}")
        id_pestaña = str(pagina_pruebas)
        print(f"Añadiendo pestaña 'Pruebas - {id_instancia}': {id_pestaña}")
        self.instancias[id_instancia]['pestañas'].append(id_pestaña)

        # Sección de Pruebas de Uniformidad (incluye Póker ahora)
        marco_uniformidad = tk.Frame(pagina_pruebas, bg="#c8e6c9")
        marco_uniformidad.pack(pady=10, padx=10, fill=tk.X)
        tk.Label(marco_uniformidad, text="PRUEBA DE UNIFORMIDAD", font=("Arial", 14, "bold"), bg="#c8e6c9", fg="#2e7d32").pack(pady=5)

        sub_marco_uniformidad = tk.Frame(marco_uniformidad, bg="#c8e6c9")
        sub_marco_uniformidad.pack(pady=5)
        btn_chi = tk.Button(sub_marco_uniformidad, text="Prueba Chi-Cuadrada", command=lambda: self.prueba_chi_cuadrada(id_instancia),
                            bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), relief="raised")
        btn_chi.pack(side=tk.LEFT, padx=5)
        btn_ks = tk.Button(sub_marco_uniformidad, text="Prueba Kolmogorov-Smirnov", command=lambda: self.prueba_kolmogorov(id_instancia),
                        bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), relief="raised")
        btn_ks.pack(side=tk.LEFT, padx=5)
        btn_poker = tk.Button(sub_marco_uniformidad, text="Prueba de Póker", command=lambda: self.prueba_poker_wrapper(id_instancia),
                            bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), relief="raised")
        btn_poker.pack(side=tk.LEFT, padx=5)

        # Sección de Pruebas de Independencia (incluye Huecos ahora)
        marco_independencia = tk.Frame(pagina_pruebas, bg="#bbdefb")
        marco_independencia.pack(pady=10, padx=10, fill=tk.X)
        tk.Label(marco_independencia, text="PRUEBA DE INDEPENDENCIA", font=("Arial", 14, "bold"), bg="#bbdefb", fg="#1976d2").pack(pady=5)

        sub_marco_independencia = tk.Frame(marco_independencia, bg="#bbdefb")
        sub_marco_independencia.pack(pady=5)
        btn_runs = tk.Button(sub_marco_independencia, text="Corrida Abajo y Arriba", command=lambda: self.metodo_abajo_arriba_wrapper(id_instancia),
                            bg="#0288d1", fg="white", font=("Arial", 10, "bold"), relief="raised")
        btn_runs.pack(side=tk.LEFT, padx=5)
        btn_runs_media = tk.Button(sub_marco_independencia, text="Corrida Sobre y Bajo Media", command=lambda: self.metodo_abajo_arriba_media_wrapper(id_instancia),
                                bg="#0288d1", fg="white", font=("Arial", 10, "bold"), relief="raised")
        btn_runs_media.pack(side=tk.LEFT, padx=5)
        btn_huecos = tk.Button(sub_marco_independencia, text="Prueba de Huecos", command=lambda: self.prueba_huecos_wrapper(id_instancia),
                            bg="#0288d1", fg="white", font=("Arial", 10, "bold"), relief="raised")
        btn_huecos.pack(side=tk.LEFT, padx=5)

        self.boton_reiniciar = tk.Button(pagina_pruebas, text="Reiniciar Todo", command=self.reiniciar,
                                        bg="#d32f2f", fg="white", font=("Arial", 12, "bold"), relief="raised")
        self.boton_reiniciar.pack(pady=20)

    def reiniciar(self):
        for id_pestaña in self.cuaderno_principal.tabs():
            texto_pestaña = self.cuaderno_principal.tab(id_pestaña, "text")
            if texto_pestaña != "Generador":
                self.cuaderno_principal.forget(id_pestaña)

        self.instancias.clear()
        self.boton_generar.config(state="normal")
        self.variable_metodo.set("")

        for entrada in self.entradas.values():
            if entrada.winfo_exists():
                entrada.delete(0, tk.END)
                entrada.config(state="disabled")

        for widget in self.marco_especifico_metodo.winfo_children():
            widget.destroy()

        self.entradas = {k: v for k, v in self.entradas.items() if k in ["Semilla (X0):", "Iteraciones:"]}

        if self.ventana_chi is not None and self.ventana_chi.winfo_exists():
            self.ventana_chi.destroy()
            self.ventana_chi = None

        messagebox.showinfo("Éxito", "Todo ha sido reiniciado correctamente")

    def reiniciar_prueba(self, id_instancia, prueba):
        print(f"Reiniciando prueba: {prueba} para instancia: {id_instancia}")
        pestañas_actuales = self.cuaderno_principal.tabs()
        print(f"Pestañas actuales: {pestañas_actuales}")
        print(f"Pestañas almacenadas en instancia antes: {self.instancias[id_instancia]['pestañas']}")
        
        # Normalizar el nombre de la prueba para coincidir con el texto de la pestaña
        if prueba == "abajo_arriba":
            prueba_normalizada = "Corrida Abajo y Arriba"
        elif prueba == "abajo_arriba_media":
            prueba_normalizada = "Corrida Sobre y Bajo Media"
        elif prueba == "poker":
            prueba_normalizada = "Póker"  # Para capturar todas las pestañas de Póker
        elif prueba == "kolmogorov":
            prueba_normalizada = "Kolmogorov-Smirnov"  # Asegurar coincidencia completa
        else:
            prueba_normalizada = prueba.replace("_", "-").title()  # Ejemplo: "chi_cuadrada" -> "Chi-Cuadrada"
        
        pestaña_esperada = f"{prueba_normalizada} - {id_instancia}"
        
        # Buscar todas las pestañas relacionadas con la prueba (especialmente para Póker que tiene múltiples pestañas)
        pestañas_a_eliminar = []
        for id_pestaña in pestañas_actuales:
            texto_pestaña = self.cuaderno_principal.tab(id_pestaña, "text")
            if prueba == "poker" and "Póker" in texto_pestaña and id_instancia in texto_pestaña:
                pestañas_a_eliminar.append(id_pestaña)
            elif pestaña_esperada == texto_pestaña:
                pestañas_a_eliminar.append(id_pestaña)
        
        print(f"Pestañas a eliminar: {pestañas_a_eliminar}")
        # Eliminar las pestañas encontradas
        for id_pestaña in pestañas_a_eliminar:
            print(f"Eliminando pestaña: {self.cuaderno_principal.tab(id_pestaña, 'text')}")
            self.cuaderno_principal.forget(id_pestaña)
            if id_pestaña in self.instancias[id_instancia]['pestañas']:
                self.instancias[id_instancia]['pestañas'].remove(id_pestaña)
        
        print(f"Pestañas almacenadas en instancia después: {self.instancias[id_instancia]['pestañas']}")
        
        self.instancias[id_instancia]['pruebas_ejecutadas'][prueba] = False
        messagebox.showinfo("Éxito", f"La prueba {prueba.replace('_', ' ').title()} ha sido reiniciada.")

    def metodo_abajo_arriba_wrapper(self, id_instancia):
        if self.instancias[id_instancia]['pruebas_ejecutadas']['abajo_arriba']:
            messagebox.showwarning("Advertencia", "La prueba Corrida Abajo y Arriba ya fue ejecutada.")
            return
        nivel_confianza = simpledialog.askfloat("Nivel de Confianza", "Ingrese el nivel de confianza (0-100):",
                                                minvalue=0, maxvalue=100, initialvalue=95)
        if nivel_confianza is not None:
            self.instancias[id_instancia]['pruebas_ejecutadas']['abajo_arriba'] = True
            self.metodo_abajo_arriba(self.instancias[id_instancia]['resultados'], nivel_confianza, id_instancia)

    def metodo_abajo_arriba(self, numeros, nivel_confianza, id_instancia):
        secuencia = [1 if numeros[i + 1] > numeros[i] else 0 for i in range(len(numeros) - 1)]
        corridas = sum(1 for i in range(len(secuencia) - 1) if secuencia[i] != secuencia[i + 1])

        n = len(numeros)
        media = (2 * n - 1) / 3
        varianza = (16 * n - 29) / 90
        desviacion_estandar = varianza ** 0.5
        z_stat = abs((corridas - media) / desviacion_estandar)
        alpha = (100 - nivel_confianza) / 100
        z_crit = stats.norm.ppf(1 - alpha / 2)
        resultado = "H0 aceptada: Independientes" if z_stat < z_crit else "H1 aceptada: No independientes"

        pagina_corridas = tk.Frame(self.cuaderno_principal, bg="#e3f2fd")
        self.cuaderno_principal.add(pagina_corridas, text=f"Corrida Abajo y Arriba - {id_instancia}")
        id_pestaña = str(pagina_corridas)
        print(f"Añadiendo pestaña 'Corrida Abajo y Arriba - {id_instancia}': {id_pestaña}")
        self.instancias[id_instancia]['pestañas'].append(id_pestaña)

        tk.Label(pagina_corridas, text="Corrida Abajo y Arriba", font=("Arial", 16, "bold"), bg="#e3f2fd", fg="#0288d1").pack(pady=10)

        df_corridas = pd.DataFrame({
            "Número": [round(x, 4) for x in numeros],
            "Dirección": ["N/A"] + secuencia,
            "Cambio": ["N/A"] + [1 if i < len(secuencia) - 1 and secuencia[i] != secuencia[i + 1] else 0 for i in range(len(secuencia))]
        })
        arbol = ttk.Treeview(pagina_corridas, columns=list(df_corridas.columns), show="headings", style="Custom.Treeview")
        for col in df_corridas.columns:
            arbol.heading(col, text=col)
            arbol.column(col, width=120, anchor="center")
        for _, fila in df_corridas.iterrows():
            arbol.insert("", "end", values=list(fila))
        arbol.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        texto_resultado = tk.Text(pagina_corridas, height=10, width=80, bg="#fff", fg="#000", font=("Arial", 10))
        texto_resultado.pack(pady=10)
        texto_resultado.insert(tk.END, f"Número de Corridas: {corridas}\nMedia: {round(media, 4)}\nVarianza: {round(varianza, 4)}\n"
                                       f"Desviación Estándar: {round(desviacion_estandar, 4)}\nEstadístico Z: {round(z_stat, 4)}\n"
                                       f"Valor Crítico (α={100-nivel_confianza:.2f}%): {round(z_crit, 4)}\nResultado: {resultado}\n")
        texto_resultado.config(state=tk.DISABLED)

        btn_reiniciar_prueba = tk.Button(pagina_corridas, text="Reiniciar Prueba", 
                                        command=lambda: self.reiniciar_prueba(id_instancia, "abajo_arriba"),
                                        bg="#d32f2f", fg="white", font=("Arial", 10, "bold"), relief="raised")
        btn_reiniciar_prueba.pack(pady=5)

    def metodo_abajo_arriba_media_wrapper(self, id_instancia):
        if self.instancias[id_instancia]['pruebas_ejecutadas']['abajo_arriba_media']:
            messagebox.showwarning("Advertencia", "La prueba Corrida Sobre y Bajo Media ya fue ejecutada.")
            return
        nivel_confianza = simpledialog.askfloat("Nivel de Confianza", "Ingrese el nivel de confianza (0-100):",
                                                minvalue=0, maxvalue=100, initialvalue=95)
        if nivel_confianza is not None:
            self.instancias[id_instancia]['pruebas_ejecutadas']['abajo_arriba_media'] = True
            self.metodo_abajo_arriba_media(self.instancias[id_instancia]['resultados'], nivel_confianza, id_instancia)

    def metodo_abajo_arriba_media(self, numeros, nivel_confianza, id_instancia):
        media_numeros = sum(numeros) / len(numeros)
        secuencia = [1 if x > media_numeros else 0 for x in numeros]
        corridas = 1 + sum(1 for i in range(len(secuencia) - 1) if secuencia[i] != secuencia[i + 1])

        n0, n1 = secuencia.count(0), secuencia.count(1)
        n = len(numeros)
        media = ((2 * n0 * n1) / n) + 0.5
        varianza = (2 * n0 * n1 * (2 * n0 * n1 - n)) / (n * n * (n - 1))
        desviacion_estandar = varianza ** 0.5

        # Verificar si la desviación estándar es cero
        if desviacion_estandar == 0:
            messagebox.showerror("Error en Prueba", 
                                "No se puede calcular el estadístico Z debido a una división por cero.\n"
                                "Esto ocurre porque los números generados no tienen variabilidad suficiente.\n"
                                "Pruebe con otros parámetros (a, c, m) en el Algoritmo Lineal.")
            return  # Salir del método sin crear la pestaña

        z_stat = abs((corridas - media) / desviacion_estandar)
        alpha = (100 - nivel_confianza) / 100
        z_crit = stats.norm.ppf(1 - alpha / 2)
        resultado = "H0 aceptada: Independientes" if z_stat < z_crit else "H1 aceptada: No independientes"

        pagina_corridas_media = tk.Frame(self.cuaderno_principal, bg="#e3f2fd")
        self.cuaderno_principal.add(pagina_corridas_media, text=f"Corrida Sobre y Bajo Media - {id_instancia}")
        id_pestaña = str(pagina_corridas_media)
        print(f"Añadiendo pestaña 'Corrida Sobre y Bajo Media - {id_instancia}': {id_pestaña}")
        self.instancias[id_instancia]['pestañas'].append(id_pestaña)

        tk.Label(pagina_corridas_media, text="Corrida Sobre y Bajo Media", font=("Arial", 16, "bold"), bg="#e3f2fd", fg="#0288d1").pack(pady=10)

        cambios = [0] * len(numeros)
        for i in range(len(secuencia) - 1):
            if secuencia[i] != secuencia[i + 1]:
                cambios[i + 1] = 1
        df_corridas = pd.DataFrame({"Número": [round(x, 4) for x in numeros],
                                "Secuencia": secuencia, "Cambio": cambios})
        arbol = ttk.Treeview(pagina_corridas_media, columns=list(df_corridas.columns), show="headings", style="Custom.Treeview")
        for col in df_corridas.columns:
            arbol.heading(col, text=col)
            arbol.column(col, width=120, anchor="center")
        for _, fila in df_corridas.iterrows():
            arbol.insert("", "end", values=list(fila))
        arbol.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        texto_resultado = tk.Text(pagina_corridas_media, height=12, width=80, bg="#fff", fg="#000", font=("Arial", 10))
        texto_resultado.pack(pady=10)
        texto_resultado.insert(tk.END, f"Media de los números: {round(media_numeros, 4)}\nNúmero de Corridas: {corridas}\n"
                                    f"n0 (≤ media): {n0}\nn1 (> media): {n1}\nMedia esperada: {round(media, 4)}\n"
                                    f"Varianza: {round(varianza, 4)}\nDesviación Estándar: {round(desviacion_estandar, 4)}\n"
                                    f"Estadístico Z: {round(z_stat, 4)}\nValor Crítico (α={100-nivel_confianza:.2f}%): {round(z_crit, 4)}\n"
                                    f"Resultado: {resultado}\n")
        texto_resultado.config(state=tk.DISABLED)

        btn_reiniciar_prueba = tk.Button(pagina_corridas_media, text="Reiniciar Prueba", 
                                        command=lambda: self.reiniciar_prueba(id_instancia, "abajo_arriba_media"),
                                        bg="#d32f2f", fg="white", font=("Arial", 10, "bold"), relief="raised")
        btn_reiniciar_prueba.pack(pady=5)

    def prueba_chi_cuadrada(self, id_instancia):    
        if self.instancias[id_instancia]['pruebas_ejecutadas']['chi_cuadrada']:
            messagebox.showwarning("Advertencia", "La prueba Chi-Cuadrada ya fue ejecutada.")
            return
        nivel_confianza = simpledialog.askfloat("Nivel de Confianza", "Ingrese el nivel de confianza (0-100):",
                                                minvalue=0, maxvalue=100, initialvalue=95)
        if nivel_confianza is not None:
            self.instancias[id_instancia]['pruebas_ejecutadas']['chi_cuadrada'] = True
            df_chi, _, k, chi_stat, chi_crit, resultado, _, _, _ = self.calcular_intervalos(self.instancias[id_instancia]['resultados'], nivel_confianza)

            pagina_chi = tk.Frame(self.cuaderno_principal, bg="#dcedc8")
            self.cuaderno_principal.add(pagina_chi, text=f"Chi-Cuadrada - {id_instancia}")
            id_pestaña = str(pagina_chi)
            print(f"Añadiendo pestaña 'Chi-Cuadrada - {id_instancia}': {id_pestaña}")
            self.instancias[id_instancia]['pestañas'].append(id_pestaña)

            tk.Label(pagina_chi, text="Prueba Chi-Cuadrada", font=("Arial", 16, "bold"), bg="#dcedc8", fg="#388e3c").pack(pady=10)

            arbol = ttk.Treeview(pagina_chi, columns=list(df_chi.columns), show="headings", style="Custom.Treeview")
            for col in df_chi.columns:
                arbol.heading(col, text=col)
                arbol.column(col, width=120, anchor="center")
            for _, fila in df_chi.iterrows():
                arbol.insert("", "end", values=[round(x, 4) if isinstance(x, (int, float)) else x for x in fila])
            arbol.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

            texto_resultado = tk.Text(pagina_chi, height=10, width=80, bg="#fff", fg="#000", font=("Arial", 10))
            texto_resultado.pack(pady=10)
            texto_resultado.insert(tk.END, f"Chi-Cuadrado Calculado: {round(chi_stat, 4)}\n"
                                           f"Valor Crítico (α={100-nivel_confianza:.2f}%, gl={k-1}): {round(chi_crit,3)}\n"
                                           f"Resultado: {resultado}\n")
            texto_resultado.config(state=tk.DISABLED)

            btn_mostrar_tabla_chi = tk.Button(pagina_chi, text="Mostrar Tabla de Chi-Cuadrada", 
                                            command=lambda: self.mostrar_tabla("chi"),
                                            bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), relief="raised")
            btn_mostrar_tabla_chi.pack(pady=5)

            btn_reiniciar_prueba = tk.Button(pagina_chi, text="Reiniciar Prueba", 
                                            command=lambda: self.reiniciar_prueba(id_instancia, "chi_cuadrada"),
                                            bg="#d32f2f", fg="white", font=("Arial", 10, "bold"), relief="raised")
            btn_reiniciar_prueba.pack(pady=5)

    def prueba_kolmogorov(self, id_instancia):
        # Validar si la cantidad de números generados es mayor a 30
        cantidad_numeros = len(self.instancias[id_instancia]['resultados'])
        if cantidad_numeros > 30:
            messagebox.showerror("Error", "La prueba Kolmogorov-Smirnov no se puede ejecutar porque la cantidad de números pseudoaleatorios generados es mayor a 30.")
            return

        # Si la cantidad es menor o igual a 30, continuar con la prueba
        if self.instancias[id_instancia]['pruebas_ejecutadas']['kolmogorov']:
            messagebox.showwarning("Advertencia", "La prueba Kolmogorov-Smirnov ya fue ejecutada.")
            return
        nivel_confianza = simpledialog.askfloat("Nivel de Confianza", "Ingrese el nivel de confianza (0-100):",
                                                minvalue=0, maxvalue=100, initialvalue=95)
        if nivel_confianza is not None:
            self.instancias[id_instancia]['pruebas_ejecutadas']['kolmogorov'] = True
            df_ks, d_stat, d_crit, resultado = self.metodo_kolmogorov(self.instancias[id_instancia]['resultados'], nivel_confianza)

            pagina_ks = tk.Frame(self.cuaderno_principal, bg="#dcedc8")
            self.cuaderno_principal.add(pagina_ks, text=f"Kolmogorov-Smirnov - {id_instancia}")
            id_pestaña = str(pagina_ks)
            print(f"Añadiendo pestaña 'Kolmogorov-Smirnov - {id_instancia}': {id_pestaña}")
            self.instancias[id_instancia]['pestañas'].append(id_pestaña)

            tk.Label(pagina_ks, text="Prueba Kolmogorov-Smirnov", font=("Arial", 16, "bold"), bg="#dcedc8", fg="#388e3c").pack(pady=10)

            arbol = ttk.Treeview(pagina_ks, columns=list(df_ks.columns), show="headings", style="Custom.Treeview")
            for col in df_ks.columns:
                arbol.heading(col, text=col)
                arbol.column(col, width=120, anchor="center")
            for _, fila in df_ks.iterrows():
                arbol.insert("", "end", values=[round(x, 4) if isinstance(x, float) else int(x) if isinstance(x, int) else x for x in fila])
            arbol.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

            texto_resultado = tk.Text(pagina_ks, height=10, width=80, bg="#fff", fg="#000", font=("Arial", 10))
            texto_resultado.pack(pady=10)
            texto_resultado.insert(tk.END, f"Estadístico D: {round(d_stat, 4)}\n"
                                        f"Valor Crítico (α={100-nivel_confianza:.2f}%, n={len(self.instancias[id_instancia]['resultados'])}): {round(d_crit, 4)}\n"
                                        f"Resultado: {resultado}\n")
            texto_resultado.config(state=tk.DISABLED)

            btn_mostrar_tabla_ks = tk.Button(pagina_ks, text="Mostrar Tabla de Kolmogorov", 
                                        command=lambda: self.mostrar_tabla("ks"),
                                        bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), relief="raised")
            btn_mostrar_tabla_ks.pack(pady=5)

            btn_reiniciar_prueba = tk.Button(pagina_ks, text="Reiniciar Prueba", 
                                            command=lambda: self.reiniciar_prueba(id_instancia, "kolmogorov"),
                                            bg="#d32f2f", fg="white", font=("Arial", 10, "bold"), relief="raised")
            btn_reiniciar_prueba.pack(pady=5)

    def calcular_intervalos(self, numeros, nivel_confianza):
        n = len(numeros)
        k = int(np.sqrt(n)) or 1
        tamano_intervalo = 1 / k
        frec_observada = np.histogram(numeros, bins=k, range=(0, 1))[0]
        frec_esperada = n / k
        chi_stat = np.sum((frec_observada - frec_esperada) ** 2 / frec_esperada)
        chi_crit = stats.chi2.ppf((100 - nivel_confianza)/100, k-1)
        resultado = "H0 aceptada: Uniformes" if chi_stat < chi_crit else "H1 aceptada: No uniformes"

        datos = [{"Iteración": i+1, "Límite Inf": round(i*tamano_intervalo, 4), "Límite Sup": round((i+1)*tamano_intervalo, 4),
                  "Oi": frec_observada[i], "Ei": round(frec_esperada, 4), "(Oi-Ei)^2/Ei": round((frec_observada[i]-frec_esperada)**2/frec_esperada, 4)}
                 for i in range(k)]
        return pd.DataFrame(datos), n, k, chi_stat, chi_crit, resultado, tamano_intervalo, min(numeros), max(numeros)

    def metodo_kolmogorov(self, numeros, nivel_confianza):
        n = len(numeros)
        if n == 0:
            raise ValueError("La lista de números no puede estar vacía")
        
        numeros_ordenados = sorted(numeros)
        d_plus_vals = [abs((i + 1) / n - numeros_ordenados[i]) for i in range(n)]
        d_minus_vals = [abs(numeros_ordenados[i] - i / n) for i in range(n)]
        
        d_plus = max(d_plus_vals)
        d_minus = max(d_minus_vals)
        d_stat = max(d_plus, d_minus)
        
        alpha = (100 - nivel_confianza) / 100
        if n > 35:
            valores_criticos = {0.1: 1.22 / np.sqrt(n), 0.05: 1.36 / np.sqrt(n), 0.01: 1.63 / np.sqrt(n)}
            d_crit = valores_criticos.get(alpha, 1.36 / np.sqrt(n))
        else:
            d_crit = stats.ksone.ppf(1 - alpha / 2, n)
        
        resultado = "H0 aceptada: Uniformes" if d_stat < d_crit else "H1 aceptada: No uniformes"
        
        datos = [{
            "i": int(i + 1),
            "x(i)": round(numeros_ordenados[i], 4),
            "F(x(i))": round((i + 1) / n, 4),
            "Fo(x)": round(numeros_ordenados[i], 4),
            "D+": round(d_plus_vals[i], 4),
            "D-": round(d_minus_vals[i], 4)
        } for i in range(n)]
        
        return pd.DataFrame(datos), d_stat, d_crit, resultado

    def prueba_poker_wrapper(self, id_instancia):
        if self.instancias[id_instancia]['pruebas_ejecutadas']['poker']:
            messagebox.showwarning("Advertencia", "La prueba de Póker ya fue ejecutada.")
            return
        nivel_confianza = simpledialog.askfloat("Nivel de Confianza", "Ingrese el nivel de confianza (0-100):",
                                                minvalue=0, maxvalue=100, initialvalue=95)
        if nivel_confianza is not None:
            self.instancias[id_instancia]['pruebas_ejecutadas']['poker'] = True
            self.prueba_poker(self.instancias[id_instancia]['resultados'], nivel_confianza, id_instancia)

    def prueba_poker(self, numeros, nivel_confianza, id_instancia):
        numeros_str = [f"{num:.10f}".split('.')[1][:5] for num in numeros]
        conteo_digitos = [{str(i): num.count(str(i)) for i in range(10)} for num in numeros_str]
        df_digitos = pd.DataFrame(conteo_digitos)
        df_digitos.insert(0, "Número", [f"0.{num}" for num in numeros_str])

        categorias = {"TD": 0, "1P": 0, "2P": 0, "T": 0, "F": 0, "P": 0, "Q": 0}
        clasificacion = []
        for num in numeros_str:
            conteos = sorted([num.count(d) for d in set(num)], reverse=True)
            if conteos == [1, 1, 1, 1, 1]: categorias["TD"] += 1; clasificacion.append("TD")
            elif conteos == [2, 1, 1, 1]: categorias["1P"] += 1; clasificacion.append("1P")
            elif conteos == [2, 2, 1]: categorias["2P"] += 1; clasificacion.append("2P")
            elif conteos == [3, 1, 1]: categorias["T"] += 1; clasificacion.append("T")
            elif conteos == [3, 2]: categorias["F"] += 1; clasificacion.append("F")
            elif conteos == [4, 1]: categorias["P"] += 1; clasificacion.append("P")
            elif conteos == [5]: categorias["Q"] += 1; clasificacion.append("Q")

        df_clasificacion = pd.DataFrame({
            "Número": [f"0.{num}" for num in numeros_str],
            "TD": [1 if c == "TD" else 0 for c in clasificacion], "1P": [1 if c == "1P" else 0 for c in clasificacion],
            "2P": [1 if c == "2P" else 0 for c in clasificacion], "T": [1 if c == "T" else 0 for c in clasificacion],
            "F": [1 if c == "F" else 0 for c in clasificacion], "P": [1 if c == "P" else 0 for c in clasificacion],
            "Q": [1 if c == "Q" else 0 for c in clasificacion]
        })

        n, m = len(numeros), 7
        probabilidades = {"TD": 0.3024, "1P": 0.5040, "2P": 0.1080, "T": 0.0720, "F": 0.0090, "P": 0.0045, "Q": 0.0001}
        frec_esperada = {k: p * n for k, p in probabilidades.items()}
        chi_stat = sum((categorias[k] - frec_esperada[k]) ** 2 / frec_esperada[k] for k in categorias)
        alpha = (100 - nivel_confianza) / 100
        chi_crit = stats.chi2.ppf(alpha, m - 1)
        resultado = "H0 aceptada: Aleatorios" if chi_stat < chi_crit else "H1 aceptada: No aleatorios"

        df_resultados = pd.DataFrame({
            "Categoría": list(categorias.keys()), "Probabilidad": [round(p, 5) for p in probabilidades.values()],
            "Oi": list(categorias.values()), "Ei": [round(f, 5) for f in frec_esperada.values()],
            "(Oi-Ei)^2/Ei": [round((categorias[k] - frec_esperada[k]) ** 2 / frec_esperada[k], 5) for k in categorias]
        })

        # Pestaña Conteo Dígitos
        pagina_digitos = tk.Frame(self.cuaderno_principal, bg="#c8e6c9")  # Cambiado a color de uniformidad
        self.cuaderno_principal.add(pagina_digitos, text=f"Póker - Conteo Dígitos - {id_instancia}")
        id_pestaña_digitos = str(pagina_digitos)
        print(f"Añadiendo pestaña 'Póker - Conteo Dígitos - {id_instancia}': {id_pestaña_digitos}")
        self.instancias[id_instancia]['pestañas'].append(id_pestaña_digitos)

        tk.Label(pagina_digitos, text="Conteo de Dígitos", font=("Arial", 16, "bold"), bg="#c8e6c9", fg="#388e3c").pack(pady=10)
        arbol_digitos = ttk.Treeview(pagina_digitos, columns=list(df_digitos.columns), show="headings", style="Custom.Treeview")
        for col in df_digitos.columns:
            arbol_digitos.heading(col, text=col)
            arbol_digitos.column(col, width=80, anchor="center")
        for _, fila in df_digitos.iterrows():
            arbol_digitos.insert("", "end", values=list(fila))
        arbol_digitos.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Pestaña Clasificación
        pagina_clasificacion = tk.Frame(self.cuaderno_principal, bg="#c8e6c9")  # Cambiado a color de uniformidad
        self.cuaderno_principal.add(pagina_clasificacion, text=f"Póker - Clasificación - {id_instancia}")
        id_pestaña_clasificacion = str(pagina_clasificacion)
        print(f"Añadiendo pestaña 'Póker - Clasificación - {id_instancia}': {id_pestaña_clasificacion}")
        self.instancias[id_instancia]['pestañas'].append(id_pestaña_clasificacion)

        tk.Label(pagina_clasificacion, text="Clasificación de Números", font=("Arial", 16, "bold"), bg="#c8e6c9", fg="#388e3c").pack(pady=10)
        arbol_clasificacion = ttk.Treeview(pagina_clasificacion, columns=list(df_clasificacion.columns), show="headings", style="Custom.Treeview")
        for col in df_clasificacion.columns:
            arbol_clasificacion.heading(col, text=col)
            arbol_clasificacion.column(col, width=80, anchor="center")
        for _, fila in df_clasificacion.iterrows():
            arbol_clasificacion.insert("", "end", values=list(fila))
        arbol_clasificacion.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Pestaña Resultados
        pagina_resultados = tk.Frame(self.cuaderno_principal, bg="#c8e6c9")  # Cambiado a color de uniformidad
        self.cuaderno_principal.add(pagina_resultados, text=f"Póker - Resultados - {id_instancia}")
        id_pestaña_resultados = str(pagina_resultados)
        print(f"Añadiendo pestaña 'Póker - Resultados - {id_instancia}': {id_pestaña_resultados}")
        self.instancias[id_instancia]['pestañas'].append(id_pestaña_resultados)

        tk.Label(pagina_resultados, text="Resultados Estadísticos", font=("Arial", 16, "bold"), bg="#c8e6c9", fg="#388e3c").pack(pady=10)
        arbol_resultados = ttk.Treeview(pagina_resultados, columns=list(df_resultados.columns), show="headings", style="Custom.Treeview")
        for col in df_resultados.columns:
            arbol_resultados.heading(col, text=col)
            arbol_resultados.column(col, width=120, anchor="center")
        for _, fila in df_resultados.iterrows():
            arbol_resultados.insert("", "end", values=list(fila))
        arbol_resultados.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        texto_resultado = tk.Text(pagina_resultados, height=10, width=80, bg="#fff", fg="#000", font=("Arial", 10))
        texto_resultado.pack(pady=10)
        texto_resultado.insert(tk.END, f"Chi-Cuadrado Calculado: {round(chi_stat, 5)}\n"
                                    f"Valor Crítico (α={alpha:.2f}, gl={m-1}): {round(chi_crit, 5)}\nResultado: {resultado}\n")
        texto_resultado.config(state=tk.DISABLED)

        btn_mostrar_tabla_chi = tk.Button(pagina_resultados, text="Mostrar Tabla de Chi-Cuadrada", 
                                        command=lambda: self.mostrar_tabla("chi"),
                                        bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), relief="raised")
        btn_mostrar_tabla_chi.pack(pady=5)

        btn_reiniciar_prueba = tk.Button(pagina_resultados, text="Reiniciar Prueba", 
                                        command=lambda: self.reiniciar_prueba(id_instancia, "poker"),
                                        bg="#d32f2f", fg="white", font=("Arial", 10, "bold"), relief="raised")
        btn_reiniciar_prueba.pack(pady=5)

    def prueba_huecos_wrapper(self, id_instancia):
        if self.instancias[id_instancia]['pruebas_ejecutadas']['huecos']:
            messagebox.showwarning("Advertencia", "La prueba de Huecos ya fue ejecutada.")
            return
        nivel_confianza = simpledialog.askfloat("Nivel de Confianza", "Ingrese el nivel de confianza (0-100):",
                                                minvalue=0, maxvalue=100, initialvalue=95)
        if nivel_confianza is not None:
            alpha = simpledialog.askfloat("Límite Inferior", "Ingrese el valor de α (límite inferior, 0-1):",
                                          minvalue=0, maxvalue=1, initialvalue=0.4)
            beta = simpledialog.askfloat("Límite Superior", "Ingrese el valor de β (límite superior, 0-1):",
                                         minvalue=0, maxvalue=1, initialvalue=0.8)
            if alpha is not None and beta is not None:
                if alpha >= beta:
                    messagebox.showerror("Error", "El valor de α debe ser menor que β")
                    return
                self.instancias[id_instancia]['pruebas_ejecutadas']['huecos'] = True
                self.prueba_huecos(self.instancias[id_instancia]['resultados'], nivel_confianza, alpha, beta, id_instancia)

    def prueba_huecos(self, numeros, nivel_confianza, alpha, beta, id_instancia):
        df_ri = pd.DataFrame(numeros, columns=['Ri'])
        resultados_intervalos = [{'Pertenece al intervalo': 1 if alpha < df_ri.iloc[i]['Ri'] < beta else 0} for i in range(len(df_ri))]
        df_resultados_intervalos = pd.DataFrame(resultados_intervalos)

        huecos = []
        contador = False
        tamaño_hueco = 0
        for i in range(1, len(df_resultados_intervalos)):
            if df_resultados_intervalos.iloc[i-1]['Pertenece al intervalo'] == 1 and df_resultados_intervalos.iloc[i]['Pertenece al intervalo'] == 1:
                tamaño_hueco = 0
                huecos.append(tamaño_hueco)
            elif df_resultados_intervalos.iloc[i-1]['Pertenece al intervalo'] == 1 and df_resultados_intervalos.iloc[i]['Pertenece al intervalo'] == 0:
                contador = True
                tamaño_hueco = 1
            elif df_resultados_intervalos.iloc[i-1]['Pertenece al intervalo'] == 0 and df_resultados_intervalos.iloc[i]['Pertenece al intervalo'] == 0 and contador:
                tamaño_hueco += 1
            elif df_resultados_intervalos.iloc[i-1]['Pertenece al intervalo'] == 0 and df_resultados_intervalos.iloc[i]['Pertenece al intervalo'] == 1 and contador:
                if tamaño_hueco >= 5:
                    tamaño_hueco = 5
                huecos.append(tamaño_hueco)
                tamaño_hueco = 0
                contador = False

        conteo_huecos = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        for hueco in huecos:
            if hueco in conteo_huecos:
                conteo_huecos[hueco] += 1

        total = sum(conteo_huecos.values())
        resultados_huecos = []
        total_estadistico = 0
        for i in range(6):
            Oi = conteo_huecos[i]
            Ei = total * (beta - alpha) * (1 - (beta - alpha)) ** i
            estadistico = (Ei - Oi) ** 2 / Ei if Ei != 0 else 0
            total_estadistico += estadistico
            resultados_huecos.append({
                'Tamaño de Hueco (i)': i,
                'Observadas': Oi,
                'Esperada (Ei)': round(Ei, 4),
                '(Ei - Oi)^2 / Ei': round(estadistico, 4)
            })

        resultados_huecos.append({
            'Tamaño de Hueco (i)': 'Total',
            'Observadas': total,
            'Esperada (Ei)': None,
            '(Ei - Oi)^2 / Ei': round(total_estadistico, 4)
        })

        alpha_stat = (100 - nivel_confianza) / 100
        chi_crit = stats.chi2.ppf(alpha_stat, 5)
        resultado = "H0 aceptada: Aleatorios" if total_estadistico < chi_crit else "H1 aceptada: No aleatorios"

        df_huecos = pd.DataFrame(resultados_huecos)

        pagina_huecos = tk.Frame(self.cuaderno_principal, bg="#bbdefb")  # Cambiado a color de independencia
        self.cuaderno_principal.add(pagina_huecos, text=f"Huecos - {id_instancia}")
        id_pestaña = str(pagina_huecos)
        print(f"Añadiendo pestaña 'Huecos - {id_instancia}': {id_pestaña}")
        self.instancias[id_instancia]['pestañas'].append(id_pestaña)

        tk.Label(pagina_huecos, text="Prueba de Huecos", font=("Arial", 16, "bold"), bg="#bbdefb", fg="#1976d2").pack(pady=10)

        arbol = ttk.Treeview(pagina_huecos, columns=list(df_huecos.columns), show="headings", style="Custom.Treeview")
        for col in df_huecos.columns:
            arbol.heading(col, text=col)
            arbol.column(col, width=150, anchor="center")
        for _, fila in df_huecos.iterrows():
            arbol.insert("", "end", values=[round(x, 4) if isinstance(x, float) and x is not None else x for x in fila])
        arbol.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        texto_resultado = tk.Text(pagina_huecos, height=10, width=80, bg="#fff", fg="#000", font=("Arial", 10))
        texto_resultado.pack(pady=10)
        texto_resultado.insert(tk.END, f"Intervalo: [{round(alpha, 4)}, {round(beta, 4)}]\n"
                                    f"Total de Huecos: {total}\n"
                                    f"Chi-Cuadrado Calculado: {round(total_estadistico, 4)}\n"
                                    f"Valor Crítico (α={alpha_stat:.2f}, gl=5): {round(chi_crit, 4)}\n"
                                    f"Resultado: {resultado}\n")
        texto_resultado.config(state=tk.DISABLED)

        btn_mostrar_tabla_chi = tk.Button(pagina_huecos, text="Mostrar Tabla de Chi-Cuadrada", 
                                        command=lambda: self.mostrar_tabla("chi"),
                                        bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), relief="raised")
        btn_mostrar_tabla_chi.pack(pady=5)

        btn_reiniciar_prueba = tk.Button(pagina_huecos, text="Reiniciar Prueba", 
                                        command=lambda: self.reiniciar_prueba(id_instancia, "huecos"),
                                        bg="#d32f2f", fg="white", font=("Arial", 10, "bold"), relief="raised")
        btn_reiniciar_prueba.pack(pady=5)

    def mostrar_tabla(self, tipo):
        if tipo == "chi":
            if self.ventana_chi is not None and self.ventana_chi.winfo_exists():
                messagebox.showwarning("Advertencia", "La ventana de la tabla Chi-Cuadrada ya está abierta. Cierre la ventana actual para abrir una nueva.")
                self.ventana_chi.lift()
                return

            self.ventana_chi = tk.Toplevel(self.ventana_principal)
            self.ventana_chi.title("Tabla de Chi-Cuadrada")
            self.ventana_chi.geometry("800x600")

            try:
                imagen_chi = Image.open(r"C:\Users\Usuario\Desktop\EJERCICIO-PYTHON\DEPTAMADRE\Grafico 2 (1).jpg")
                imagen_chi = imagen_chi.resize((750, 550), Image.Resampling.LANCZOS)
                foto_chi = ImageTk.PhotoImage(imagen_chi)
                etiqueta = tk.Label(self.ventana_chi, image=foto_chi)
                etiqueta.image = foto_chi
                etiqueta.pack(padx=10, pady=10)
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar la imagen de la tabla Chi-Cuadrada: {str(e)}")
                self.ventana_chi.destroy()
                self.ventana_chi = None
                return

            self.ventana_chi.protocol("WM_DELETE_WINDOW", lambda: self.cerrar_ventana_chi())

        else:
            ventana_ks = tk.Toplevel(self.ventana_principal)
            ventana_ks.title("Tabla de Kolmogorov-Smirnov")
            ventana_ks.geometry("800x600")

            etiqueta_placeholder = tk.Label(ventana_ks, text="Tabla de Kolmogorov-Smirnov\nHola.",
                                           font=("Arial", 14), fg="#d32f2f")
            etiqueta_placeholder.pack(pady=20)

            try:
                imagen_ks = Image.open(r"C:\Users\Usuario\Desktop\EJERCICIO-PYTHON\DEPTAMADRE\Grafico 3.jpg")
                imagen_ks = imagen_ks.resize((750, 550), Image.Resampling.LANCZOS)
                foto_ks = ImageTk.PhotoImage(imagen_ks)
                etiqueta = tk.Label(ventana_ks, image=foto_ks)
                etiqueta.image = foto_ks
                etiqueta.pack(padx=10, pady=10)
            except FileNotFoundError:
                pass

    def cerrar_ventana_chi(self):
        if self.ventana_chi is not None:
            self.ventana_chi.destroy()
        self.ventana_chi = None

def main():
    raiz = tk.Tk()
    estilo = ttk.Style()
    estilo.configure("Custom.Treeview", background="#fff", foreground="#000", rowheight=25, fieldbackground="#fff")
    estilo.map("Custom.Treeview", background=[('selected', '#0288d1')], foreground=[('selected', '#fff')])
    app = GeneradorNumerosPseudoaleatorios(raiz)
    raiz.mainloop()

if __name__ == "__main__":
    main()