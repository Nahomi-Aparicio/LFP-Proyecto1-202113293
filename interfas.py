from tkinter import *
from tkinter import filedialog
from tkinter import Scrollbar as scroll
import webbrowser
from analizador import Analizador
from tkinter import END, messagebox
import os

class Interfaz:
    global analizar2
    analizar2=Analizador()
    def __init__(self):
        self.archivo=None
        
        self.menu_inicio()
        
    def menu_inicio(self):
        self.ventana = Tk()
        self.ventana.title("proyecto1")
        self.ventana.geometry("600x330")
        self.ventana.resizable(0,0)
    #frame archivo 
        f1=Frame(self.ventana,bg='#a1f5f1').place(x=0,y=0,width=200,height=200)
       
        label1=Label(f1,text="Archivo",bg='#1ab3ac',font=('Cooper Black', 12),fg = '#a1f5f1').place(x=0,y=0,width=200,height=30.33)        
        Abrir= Button(f1, text="Abrir",bg= "#a1f5f1",fg='#1ab3ac',font=('Cooper Black', 12),command=self.abri).place(x=0, y=30, width=200, height=30)
        guardar= Button(f1, text="Guardar",bg= "#a1f5f1",fg='#1ab3ac',font=('Cooper Black', 12),command=self.guardar).place(x=0, y=60, width=200, height=30)
        guardar_como = Button(f1, text="Guardar como",bg= "#a1f5f1",fg='#1ab3ac',font=('Cooper Black', 12),command=self.guardarComo).place(x=0, y=90, width=200, height=30)
        Analizar= Button(f1, text="Analizar",bg= "#a1f5f1",fg='#1ab3ac',font=('Cooper Black', 12),command=self.analizado).place(x=0, y=120, width=200, height=30)
        Errores= Button(f1, text="Errores",bg= "#a1f5f1",fg='#1ab3ac',font=('Cooper Black', 12),command=self.erroreslexicos).place(x=0, y=150, width=200, height=30)
        salir= Button(f1, text="Salir",bg= "#a1f5f1",fg='#1ab3ac',font=('Cooper Black', 12),command=self.salir).place(x=0, y=180, width=200, height=30)

#frame ayuda
        f2=Frame(self.ventana,bg='#d1f2ff').place(x=200,y=0,width=500,height=500) 
        label1=Label(f2,text="Ayuda",bg='#a56fb1',font=('Cooper Black', 12),fg = '#f4cffe').place(x=0,y=210,width=200,height=30.33)  
        Manual_usuario= Button(f2, text="Manual de usuario",bg= "#f4cffe",fg='#a56fb1',font=('Cooper Black', 12),command=self.manual_usuario).place(x=0, y=240, width=200, height=30)
        Manual_tecnico= Button(f2, text="Manual tecnico",bg= "#f4cffe",fg='#a56fb1',font=('Cooper Black', 12),command=self.manual_tecnico).place(x=0, y=270, width=200, height=30)
        Temas_ayuda= Button(f2, text="Temas de ayuda",bg= "#f4cffe",fg='#a56fb1',font=('Cooper Black', 12),command=self.ayuda).place(x=0, y=300, width=200, height=30)
        
    #caja de texto 
        self.caja = Text(self.ventana)
        self.caja.place(x=220, y=20, width=350, height=300)
        self.scroll = scroll(self.caja) 
        self.scroll.pack(side=RIGHT, fill=Y)      
        self.caja.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.caja.yview)
        self.ventana.mainloop()
        
    #--------------------------------METODOS PARA ARCHIVO ---------------------------------------------------
    def abri(self):
        self.caja.delete("1.0",END)
        
        
        self.archivo = filedialog.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("txt files","*.txt"),("all files","*.*")))
        try:
            
            archivo2=open(self.archivo,"r+",encoding="utf-8")
            contenido_archivo=archivo2.read()
            
            self.caja.insert(1.0,contenido_archivo)
            self.contenido=contenido_archivo
            archivo2.close()
        except UnicodeDecodeError:
            messagebox.showerror("Error", "el archivo no es compatible")
        except FileNotFoundError:
            messagebox.showerror("ERROR", "no se encontro el archivo")

    def analizado(self):
        analizar2.compilar(xml=self.archivo)
       
#guardar
    def guardar(self):
        contenido=self.caja.get(1.0,END)
        print(contenido)
        if self.archivo==None:
            self.guardarComo()
        else:
            self.archivo2=open(self.archivo,"w+",encoding="utf-8")
            self.archivo2.write(contenido)
            
            self.archivo2.close()

            messagebox.showinfo("guardar", "el archivo se guardo correctamente")

#guardar como 
    def guardarComo(self):

        archivo_guardar=filedialog.asksaveasfilename(initialdir = "/",title = "Guardar archivo",defaultextension=".txt", filetypes = (("txt files","*.txt"),("all files","*.*")))
        try:
            if archivo_guardar is not None:
                contenido=self.caja.get(1.0,END)
                archivo2=open(archivo_guardar,"w+",encoding="utf-8")
                archivo2.write(contenido)
                archivo2.close()
                self.archivo=archivo_guardar
            else:
                print('no archivo ')
       
            
        except FileNotFoundError:
            messagebox.showerror("Error", "no se pudo guardar el archivo")
    #def mostrararchivo(self):
    def erroreslexicos(self):
        if self.archivo==None:
            messagebox.showerror("ERROR", "no se encontro el archivo")
        else:
             analizar2.erroress()
       
#------------------------------------METODOS PARA AYUDA---------------------------------------------------
    def manual_usuario(self):
                            
        path = 'Manual_de_usuario_202113293.pdf'
        os.system(path)
    
    def manual_tecnico(self):
        path = 'ManualTecnico_202113293_Proyecto1.pdf'
        os.system(path)

    def ayuda(self):
        inf = open('INFORMACION_202113293.html','w',encoding="utf-8")
        info="""<html>
        <body bgcolor="#f4cffe">
        <h2>Informacion del desarollador</h2>
        <p style="color:#51a5e2">Nombre:</p>
        <p >genesis Nahomi Aparicio Acan</p>
        <p style="color:#51a5e2">carne:</p>
        <p >202113293</p>
        <p style="color:#51a5e2">curso</p>
        <p >lenguajes formales  y de programacion</p>
        <p style="color:#326657">UNIVERSIDAD SAN CARLOS DE GUATEMALA</p>
        </body>
        </html>
        """
        inf.write(info)
        inf.close()
        webbrowser.open_new_tab('INFORMACION_202113293.html')

        

    def salir(self):
        self.ventana.quit()


