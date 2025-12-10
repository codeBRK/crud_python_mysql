import tkinter as tk

#importar los modulos restantes de tkinter
from tkinter import *

from tkinter import ttk
from tkinter import messagebox

from Productos import *

from Conexion import *

class FormularioProductos: 

    global base
    base = None

    global textBoxID
    textBoxID = None

    global textBoxDescripcion
    textBoxDescripcion = None

    global textBoxPrecio
    textBoxPrecio = None

    global textBoxStock
    textBoxStock = None

    global textBoxBuscar
    textBoxBuscar = None

    global groupBox
    groupBox = None

    global tree
    tree = None

def Formulario():

        global textBoxID
        global textBoxDescripcion
        global textBoxPrecio
        global textBoxStock
        global groupBox
        global groupBoxList
        global tree
        global base
        global textBoxBuscar

        try: 

            # Primer seccion del formulario
            base = Tk()
            base.geometry("1350x380")
            base.title("Formulario Productos")

            groupBox = LabelFrame(base,text="Datos del Producto", font={"arial", 12}, padx=5,pady=5,)
            groupBox.grid(row=0,column=0,padx=20,pady=10, sticky="n")

            labelId = Label(groupBox,text="Id:", width=13, font=("arial",12)).grid(row=0,column=0)
            textBoxID = Entry(groupBox)
            textBoxID.grid(row=0,column=1,pady=15)

            labelDescipcion = Label(groupBox,text="Descripcion:", width=13, font=("arial",12)).grid(row=1,column=0)
            textBoxDescripcion = Entry(groupBox)
            textBoxDescripcion.grid(row=1,column=1,pady=15)

            labelPrecio = Label(groupBox,text="Precio:", width=13, font=("arial",12)).grid(row=2,column=0)
            textBoxPrecio = Entry(groupBox)
            textBoxPrecio.grid(row=2,column=1,pady=15)
            
            labelStock = Label(groupBox,text="Stock:", width=13, font=("arial",12)).grid(row=3,column=0)
            textBoxStock = Entry(groupBox)
            textBoxStock.grid(row=3,column=1,pady=15)

            Button(groupBox, text="Guardar", width=12, font={"arial", 12}, command=guardarProducto).grid(row=4,column=0,pady=10)
            Button(groupBox, text="Actualizar", width=12, font={"arial", 12}, command=actualizarProducto).grid(row=4,column=1,pady=10)
            Button(groupBox, text="Eliminar", width=12, font={"arial", 12}, command=eliminarProducto).grid(row=4,column=2,pady=10)
            
            # Segunda seccion del formulario

            groupBoxList = LabelFrame(base,text="Lista de productos", font={"arial", 12}, padx=5,pady=5,)   
            groupBoxList.grid(row=0,column=1,padx=0,pady=10, sticky="n")

            labelBuscar = Label(groupBoxList,text="Buscar:", width=10, font=("arial",12)).grid(row=0,column=0, sticky="w")
            textBoxBuscar = Entry(groupBoxList, width=90)
            textBoxBuscar.grid(row=0,column=1,pady=10, sticky="w")

            Button(groupBoxList, text="Buscar", width=12, font={"arial", 12}, command=filtrarProducto).grid(row=0,column=2,pady=10, sticky="e")
            Button(groupBoxList, text="Mostrar Todo", width=12, font={"arial", 12}, command=actualizarTreeview).grid(row=0,column=3,pady=10, sticky="e")
            

            #crear un treeview para mostrar la lista de productos
            #Configurar las columnas del treeview

            tree = ttk.Treeview(groupBoxList, columns=("Id", "Descripcion", "Precio", "Stock"), show="headings", height=10,)
            tree.column("# 1", anchor=CENTER)
            tree.heading("# 1", text="Id")

            tree.column("# 2", anchor=CENTER, width=300)
            tree.heading("# 2", text="Descripcion")


            tree.column("# 3", anchor=CENTER)
            tree.heading("# 3", text="Precio")


            tree.column("# 4", anchor=CENTER)
            tree.heading("# 4", text="Stock")

            tree.grid(row=1,column=0, columnspan=4, pady=10)

            #agregar los datos al treeview
            productos = Productos.mostrarProductos()
            for producto in productos:
                tree.insert("", tk.END, values=producto)

            #Ejecutar la funcion al seleccionar un item del treeview y mostrar los datos en los campos de entrada
            tree.bind("<<TreeviewSelect>>", seleccionarProducto)

            #tree.pack()

            base.mainloop()

        except ValueError as error:
            print("Error al mostrar la interfaz!:, error {}".format(error))

def guardarProducto():

        global textBoxDescripcion
        global textBoxPrecio
        global textBoxStock
        global groupBox 

        try:
            #verificar si los widgets estan inicializados
            if textBoxDescripcion is None or textBoxPrecio is None or textBoxStock is None:
                print("Los campos de entrada no estan inicializados")
                return
            
            descripcion = textBoxDescripcion.get()
            precio = textBoxPrecio.get()
            stock = textBoxStock.get()

            Productos.ingresarProductos(descripcion, precio, stock)  
            messagebox.showinfo("Exito", "Producto guardado exitosamente")

            #actualizar el treeview
            actualizarTreeview()

            #limpiar los campos

            textBoxDescripcion.delete(0,END)
            textBoxPrecio.delete(0,END)
            textBoxStock.delete(0,END)

        except ValueError as error:
            print("Error al guardar el producto!:, error {}".format(error))

def actualizarTreeview():
        global tree

        try:
            #borrar los datos actuales del treeview
            tree.delete(*tree.get_children())

            #agregar los datos actualizados al treeview
            productos = Productos.mostrarProductos()
            for producto in productos:
                tree.insert("", tk.END, values=producto)
        
        except ValueError as error:
            print("Error al actualizar el treeview!:, error {}".format(error))

def filtrarTreeview(descripcion):
        global tree

        try:
            #borrar los datos actuales del treeview
            tree.delete(*tree.get_children())

            if not descripcion:            
                #agregar los datos actualizados al treeview
                productos = Productos.mostrarProductos()

            else: 
                 productos = Productos.filtrarProductos(descripcion)   

            for producto in productos:
                tree.insert("", tk.END, values=producto)
        
        except ValueError as error:
            print("Error al actualizar el treeview!:, error {}".format(error))

def seleccionarProducto(evento):
        try:
             #obtener el item seleccionado
             itemSeleccionado = tree.focus()

             if itemSeleccionado:
                #obtener los valores del item seleccionado
                valores = tree.item(itemSeleccionado)['values']

                #Establecer los valores en los campos de entrada
                textBoxID.delete(0, END)
                textBoxID.insert(0, valores[0])
                textBoxDescripcion.delete(0, END)
                textBoxDescripcion.insert(0, valores[1])
                textBoxPrecio.delete(0, END)
                textBoxPrecio.insert(0, valores[2])
                textBoxStock.delete(0, END)
                textBoxStock.insert(0, valores[3])
             
        except ValueError as error:
             print("Error al al seleccionar el produco {}".format(error))

def actualizarProducto():

        global textBoxID
        global textBoxDescripcion
        global textBoxPrecio
        global textBoxStock
        global groupBox 

        try:
            #verificar si los widgets estan inicializados
            if textBoxID is None or textBoxDescripcion is None or textBoxPrecio is None or textBoxStock is None:
                print("Los campos de entrada no estan inicializados")
                return
            
            id_producto = textBoxID.get()
            descripcion = textBoxDescripcion.get()
            precio = textBoxPrecio.get()
            stock = textBoxStock.get()

            Productos.actualizarProductos(id_producto, descripcion, precio, stock)  
            messagebox.showinfo("Exito", "Producto actualizado exitosamente")

            #actualizar el treeview
            actualizarTreeview()

            #limpiar los campos

            textBoxID.delete(0,END)
            textBoxDescripcion.delete(0,END)
            textBoxPrecio.delete(0,END)
            textBoxStock.delete(0,END)

        except ValueError as error:
            print("Error al guardar el producto!:, error {}".format(error))
         
def eliminarProducto():

        global textBoxID 
        global textBoxDescripcion
        global textBoxPrecio
        global textBoxStock
        global groupBox 

        try:
            #verificar si los widgets estan inicializados
            if textBoxID is None:
                print("Los campos de entrada no estan inicializados")
                return
            
            id_producto = textBoxID.get()

            Productos.eliminarProductos(id_producto)  
            messagebox.showinfo("Exito", "Producto Eliminado exitosamente")

            #actualizar el treeview
            actualizarTreeview()

            #limpiar los campos

            textBoxID.delete(0,END)
            textBoxDescripcion.delete(0,END)
            textBoxPrecio.delete(0,END)
            textBoxStock.delete(0,END)

        except ValueError as error:
            print("Error al guardar el producto!:, error {}".format(error))

def filtrarProducto():

        global textBoxID 
        global textBoxDescripcion
        global textBoxPrecio
        global textBoxStock
        global groupBox 
        global textBoxBuscar

        try:
            #verificar si los widgets estan inicializados
            if textBoxBuscar is None:
                print("Los campos de entrada no estan inicializados")
                return
            
            descripcion = textBoxBuscar.get()

            #Productos.filtrarProductos(descripcion)  
            #messagebox.showinfo("Exito", "Producto Filtrado exitosamente")

            #actualizar el treeview
            filtrarTreeview(descripcion)

            #limpiar los campos

            textBoxID.delete(0,END)
            textBoxDescripcion.delete(0,END)
            textBoxPrecio.delete(0,END)
            textBoxStock.delete(0,END)

        except ValueError as error:
            print("Error al guardar el producto!:, error {}".format(error))

Formulario()