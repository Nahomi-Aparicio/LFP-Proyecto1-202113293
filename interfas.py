
from tkinter import *
from tkinter import filedialog
from tkinter import Scrollbar as scroll
from analizador import *
from tkinter import END, messagebox
import os

class Interfaz:
    global analizar
    analizar=Analizador()




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
        guardar= Button(f1, text="Guardar",bg= "#a1f5f1",fg='#1ab3ac',font=('Cooper Black', 12),command=guardar).place(x=0, y=60, width=200, height=30)
        guardar_como = Button(f1, text="Guardar como",bg= "#a1f5f1",fg='#1ab3ac',font=('Cooper Black', 12),command=self.guardarComo).place(x=0, y=90, width=200, height=30)
        Analizar= Button(f1, text="Analizar",bg= "#a1f5f1",fg='#1ab3ac',font=('Cooper Black', 12)).place(x=0, y=120, width=200, height=30)
        Errores= Button(f1, text="Errores",bg= "#a1f5f1",fg='#1ab3ac',font=('Cooper Black', 12)).place(x=0, y=150, width=200, height=30)
        salir= Button(f1, text="Salir",bg= "#a1f5f1",fg='#1ab3ac',font=('Cooper Black', 12),command=self.salir).place(x=0, y=180, width=200, height=30)

    #frame ayuda
        f2=Frame(self.ventana,bg='#d1f2ff').place(x=200,y=0,width=500,height=500) 
        label1=Label(f2,text="Ayuda",bg='#a56fb1',font=('Cooper Black', 12),fg = '#f4cffe').place(x=0,y=210,width=200,height=30.33)  
        Manual_usuario= Button(f2, text="Manual de usuario",bg= "#f4cffe",fg='#a56fb1',font=('Cooper Black', 12),command=self.manual_usuario).place(x=0, y=240, width=200, height=30)
        Manual_tecnico= Button(f2, text="Manual tecnico",bg= "#f4cffe",fg='#a56fb1',font=('Cooper Black', 12),command=self.manual_tecnico).place(x=0, y=270, width=200, height=30)
        Temas_ayuda= Button(f2, text="Temas de ayuda",bg= "#f4cffe",fg='#a56fb1',font=('Cooper Black', 12)).place(x=0, y=300, width=200, height=30)
        
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
        
        
        self.archivo = filedialog.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("txt files","*.txt"),("all files","*.*")))
        try:
            archivo2=open(self.archivo,"r+")
            contenido_archivo=archivo2.read()
            #analizar.compilar(contenido_archivo)
            self.caja.insert(1.0,contenido_archivo)
            

            archivo2.close()
        except UnicodeDecodeError:
            messagebox.showerror("Error", "el archivo no es compatible")
        except FileNotFoundError:
            messagebox.showerror("ERROR", "no se encontro el archivo")
            
       

        
        

        #print(self.archivo)
#guardar
    def guardar(self):

        contenido=self.caja.get(1.0,END)
        if self.archivo==None:
            self.guardarComo()
        else:
            self.archivo2=open(self.archivo,"w+")
            self.archivo2.write(contenido)
            #analizar.compilar(contenido)
            self.archivo2.close()
            messagebox.showinfo("guardar", "el archivo se guardo correctamente")

#guardar como 
    def guardarComo(self):

        archivo_guardar=filedialog.asksaveasfilename(initialdir = "/",title = "Guardar archivo",defaultextension=".txt", filetypes = (("txt files","*.txt"),("all files","*.*")))
        try:
            if archivo_guardar is not None:
                contenido=self.caja.get(1.0,END)
                archivo2=open(archivo_guardar,"w+")
                archivo2.write(contenido)
                archivo2.close()
                self.archivo=archivo_guardar
            else:
                print('no archivo ')
       
            
        except FileNotFoundError:
            messagebox.showerror("Error", "no se pudo guardar el archivo")

        
    #def mostrararchivo(self):
        

#------------------------------------METODOS PARA AYUDA---------------------------------------------------

    def manual_usuario(self):
        """root = Tk()
        
        # Set the width and height of our root window.
        root.geometry("550x750")
        pix = root.getPixmap()
        
        # creating object of ShowPdf from tkPDFViewer.
        v1 = pdf.ShowPdf()
        
        # Adding pdf location and width and height.
        v2 = v1.pdf_view(root,
                        pdf_location = r"examen.pdf", 
                        width = 50, height = 100) """                       
        path = 'examen.pdf'
        os.system(path)
    
    def manual_tecnico(self):
        path = 'examen.pdf'
        os.system(path)
      
        
        
         




    def salir(self):
        self.ventana.quit()


if __name__ == "__main__":
    Interfaz()