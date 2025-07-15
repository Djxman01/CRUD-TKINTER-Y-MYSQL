import tkinter as tk

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from Clientes import *
from Conexion import *

class FormularioClientes:
    global base
    base = None

    global texBoxId
    texBoxId = None 

    global texBoxNombres
    texBoxNombres = None

    global texBoxApellidos
    texBoxApellidos = None

    global groupBox 
    groupBox = None

    global tree
    tree = None

    global combo
    combo = None


     
def Formulario():
        global base
        global texBoxId
        global texBoxNombres
        global texBoxApellidos
        global tree
        global combo







        try:
            base = Tk()
            base.geometry("1200x300")
            base.title("Formulario Python")

            groupBox = LabelFrame(base, text="Datos del Personal", padx=5, pady=5)
            groupBox.grid(row=0,column=0,padx=10,pady=10)
 
            labelId= Label(groupBox, text= "Id", width=13,font=("arial,",12)).grid(row= 0,column= 0) 
            texBoxId = Entry(groupBox)
            texBoxId.grid(row=0,column=1)

            labelNombres= Label(groupBox, text= "Nombres", width=13,font=("arial,",12)).grid(row= 1,column= 0) 
            texBoxNombres = Entry(groupBox)
            texBoxNombres.grid(row=1,column=1)

            labelApellidos= Label(groupBox, text= "Apellidos", width=13,font=("arial,",12)).grid(row= 2,column= 0) 
            texBoxApellidos = Entry(groupBox)
            texBoxApellidos.grid(row=2,column=1)

            labelSexo= Label(groupBox, text= "Sexo", width=13,font=("arial,",12)).grid(row= 3,column= 0) 
            seleccionSexo = tk.StringVar()
            combo = ttk.Combobox(groupBox, values=["Masculino", "Femenino", "Prefiero no Decirlo"],textvariable=seleccionSexo)
            combo.grid(row=3, column=1)
            seleccionSexo.set("Masculino")

            Button(groupBox,text="Guardar", width=10, command= guardarRegistro).grid(row=4,column=0)
            Button(groupBox,text="Modificar", width=10).grid(row=4,column=1)
            Button(groupBox,text="Eliminar", width=10).grid(row=4,column=2)

            groupBox = LabelFrame(base,text="Lista del Personal",padx=5,pady=5,)
            groupBox.grid(row=0, column=1,padx=5,pady=5)
            #Creacion del TreeView


            #Configuracion de las columnas
            
            tree = ttk.Treeview(groupBox,columns=("Id", "Nombres", "Apellidos", "Sexo"),show='headings',height=5)
            tree.column("#1",anchor=CENTER)
            tree.heading("#1", text= "Id")

            tree.column("#2",anchor=CENTER)
            tree.heading("#2", text= "Nombres")

            tree.column("#3",anchor=CENTER)
            tree.heading("#3", text= "Apellidos")

            tree.column("#4",anchor=CENTER)
            tree.heading("#4", text= "Sexo")
         
            # Agregar datos a la tabla
            # Mostrar la tabla

            for row in mostrarClientes():
                 tree.insert("","end",values=row)





            tree.pack()
            base.mainloop()


        except ValueError as error:
            print("Ha ocurrido un error: {}".format(error))

def guardarRegistro():
        global texBoxNombres, texBoxApellidos, combo, groupBox

        try:
            #Verificar si los widgets estan inicializados
            if texBoxNombres is None or texBoxApellidos is None or combo is None:
                print("Los widgets no estan inicializados")
                return
            nombres = texBoxNombres.get()
            apellidos = texBoxApellidos.get()
            sexo = combo.get()

            CCLientes.ingresarClientes(nombres,apellidos,sexo)
            messagebox.showinfo("Informacion","Los datos fueron guardados")

            actualizarTreeView()


            #Limpiamos los  campos
            texBoxNombres.delete(0, END)
            texBoxApellidos.delete(0, END)
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))

def actualizarTreeView():
     global tree

     try:
          tree.delete(*tree.get_children())
          datos = mostrarClientes()

          for row in mostrarClientes():
            tree.insert("","end",values=row)
    
     except ValueError as error:
             print("Error al actualizar los datos {}".format(error))

FormularioClientes()
Formulario()