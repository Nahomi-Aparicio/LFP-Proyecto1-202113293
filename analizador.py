from enum import Enum
import os
from aritmeticas import aritmeticas
from perfiles import OPerandopy
import math
import re
import webbrowser
listaErrores_lexicos=[]
class Token(Enum):
    Tk_menor="<"
    Tk_mayor=">"
    Tk_E_numero="Numero"
    Tk_Numero="[0.0-9.0]*"
    Tk_pleca="/"
    Tk_OPERACION="Operacion"
    Tk_igual="="
    Tk_Tipo="Tipo"
    TK_Suma="SUMA"
    Tk_Resta="RESTA"
    Tk_Multiplicacion="MULTIPLICACION"
    Tk_Division="DIVISION"
    Tk_Potencia="POTENCIA"
    TK_RAIZ="RAIZ"
    TK_Inverso="INVERSO"
    TK_Seno="SENO"
    TK_Coseno="COSENO"
    TK_Tangente="TANGENTE"
    TK_Mod="MOD"
#titulo segunda etiqueta
    TK_Texto="[a-zA-Z,À-ÿ\u00f1\u00d1,'+'-'-','*',0.0-9.0*,':','%','=','/','^','√','(',')'*]*"
    TK_TextoPrincipal="Texto"
    TK_Operaciones="[,.a-zA-ZÀ-ÿ\u00f1\u00d1 ]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1])[a-zA-ZÀ-ÿ\u00f1\u00d1_.]*[0.0-9.0]*[,.a-zA-ZÀ-ÿ\u00f1\u00d1 ]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1])[a-zA-ZÀ-ÿ\u00f1\u00d1_.:]*[0.0-9.0]*"
    Tk_Titulo="Titulo"
    Tk_Descripcion="Descripcion"
    TK_DESCRIPTION2  = "\[TEXTO\]"
    Tk_Contenido="Contenido"
    Tk_Funcion="Funcion"
    Tk_ESCRIBIR="ESCRIBIR"
    TK_CONTENIDO2  = "\[TIPO\]"
    Tk_Color="Color"
    Tk_color2='[AZUL,ROJO,VERDE,AMARILLO,NEGRO,NARANJA,MORADO,ROSADO]*'
    Tk_tamano="Tamanio"
    TK_Estilo="Estilo"

#analisador lexico 
# 

class Errorres_lexicos:
    def __init__(self,_tokem,_filas,_columnas,descripcion="") :
        self.tokem=_tokem
        self.filas=_filas
        self.columnas=_columnas
        self.descripcion=descripcion

    def getErrores(self):
        return {"tokem":self.tokem,"filas":self.filas,"columnas":self.columnas,"descripcion":self.descripcion}
   

class Analizador:
    global  operandopy2,aritmetica,operacionesarit
    operandopy2=OPerandopy()
    aritmetica=aritmeticas()
    operacionesarit=[]

    

    def __init__(self):
        self.cadena = ""
        self.linea=0
        self.columna=0
        self.lista_cadena=[]
        self.tmp_cadena=""
        self.listanumero=[]
        self.listatodo=[]
        self.aquistatexto=[]
        self.aqui_titulo=[]
        self.intento=[]

        self.colorTT=None
        self.tamano=None






#quito loa < > de la cadena
    def quitar(self,_cadena:str,_num:int):
        _tmp=""
        contador1=0
        for i in _cadena:
            if contador1>=_num:
                _tmp +=i
            else:
                self.tmp_cadena+=i
            contador1+=1
        return _tmp
           

#aumentando las lineas de el archivo de entrada
    def aumentandolineas(self): 
        _tmp= self.lista_cadena[self.linea]
        if _tmp==self.tmp_cadena:
            self.linea+=1
            self.tmp_cadena=""
            self.columna=0
     
    def etiqueta(self,_cadena:str,_etiqueta:str):
        temp=""
        contador=0
        for i in _cadena:
            if contador < len(_etiqueta):
                temp+=i
            contador+=1
        if temp == _etiqueta:
            return True
        else:
            return False
   
    def Numero(self,_cadena:str):        
        tokens=[
            Token.Tk_menor.value,#<
        Token.Tk_E_numero.value,#numero
        Token.Tk_mayor.value,#>
        Token.Tk_Numero.value, #10
        Token.Tk_menor.value,#<
        Token.Tk_pleca.value,#/
        Token.Tk_E_numero.value,#numero
        Token.Tk_mayor.value,#>
        ]
        _numero=""

        for i in tokens:
            try :
               
                jefe=re.compile(f'^{i}')
                s=jefe.search(_cadena)
                
                print("|",self.linea,"|", self.columna,"|",s.group())
                self.columna+=int(s.end())

                if i ==Token.Tk_Numero.value:
                    _numero=s.group()
                    self.listanumero.append(float(_numero))
                _cadena=self.quitar(_cadena,s.end())
                self.aumentandolineas()               #print(_cadena)
            except:
                print('error en numero')
                return{'result': _numero,'cadena':_cadena,"Error":True}

        print("Numero1",_numero)
        return{'result': _numero,'cadena':_cadena,"Error":False}

    def importaroperaciones (self):
        operandopy2.operation(paso_lista=self.listatodo)
        

      
        

        
    def importacion2(self):
        aritmetica.haciendoop(lista=self.intento)
    
    
        

#operadores 
    def operando (self,_cadena:str):
        tokens=[
        Token.Tk_menor.value,
        Token.Tk_OPERACION.value,
        Token.Tk_igual.value,
        "OPERACION",
        Token.Tk_mayor.value,
        "Numero",
        "Numero",
        Token.Tk_menor.value,
        Token.Tk_pleca.value,
        Token.Tk_OPERACION.value,
        Token.Tk_mayor.value,
        ]
        _derecho=None
        _izquierda=None
        _numeroop=""
        _operador=None
        for i in tokens:
            
            try :
               #print('juan')
                if "Numero" == i:
                    _result=None
                    if self.etiqueta(_cadena,"<Numero>"):
                        _result=self.Numero(_cadena)
                        _cadena=_result['cadena']
                        if _result["Error"]:
                            print('ocurrio un en el resultado operaciones')
                            return{'result': _numeroop,'cadena':_cadena,"Error":True}
                        
                    elif self.etiqueta(_cadena,'<Operacion=' ):
                        _result=self.operando(_cadena)
                        _cadena=_result['cadena']
                        if _result["Error"]:
                            print('hay un error dentro delas operaciones  numero')
                            return{'result': _numeroop,'cadena':_cadena,"Error":True}
                        
                    else:
                        print("error en el numero ")
                        return{'result': _numeroop,'cadena':_cadena,"Error":True}
                    if _izquierda == None:
                        _izquierda=_result['result']
                    else:
                        _derecho=_result['result']


                else:
                    if "OPERACION" == i: 
                   
                        subjefe = re.compile(f'^SUMA') 
                        t=subjefe.search(_cadena)
                        if t!=None:                            
                            i='SUMA'                                                    
                            _operador=Token.TK_Suma
                            _operador1='+'
                            self.listanumero.append(_operador1)
                       
                    #RESTA
                        subjefe = re.compile(f'^RESTA') 
                        t=subjefe.search(_cadena)
                        if t!=None:
                            i='RESTA'
                            _operador=Token.Tk_Resta
                            _operador2='-'
                            self.listanumero.append(_operador2)

                    #MULTIPLICADOR
                        subjefe = re.compile(f'^MULTIPLICACION')
                        t=subjefe.search(_cadena)
                        if t!=None:
                            i='MULTIPLICACION'
                            _operador=Token.Tk_Multiplicacion
                            _operador3='*'
                            self.listanumero.append(_operador3)

                    #DIVISION
                        subjefe = re.compile(f'^DIVISION')
                        t=subjefe.search(_cadena)
                        if t!=None:
                            i='DIVISION'
                            _operador=Token.Tk_Division
                            _operador4='/'
                            self.listanumero.append(_operador4)

                    #raiz
                        subjefe = re.compile(f'^RAIZ')
                        t=subjefe.search(_cadena)
                        if t!=None:
                            i='RAIZ'
                            _operador=Token.TK_RAIZ
                            _operador5="raiz"
                            self.listanumero.append(_operador5)

                    #POTENCIA

                        subjefe = re.compile(f'^POTENCIA')
                        t=subjefe.search(_cadena)
                        if t!=None:
                            i='POTENCIA'
                            _operador=Token.Tk_Potencia
                            _operador45='^'
                            self.listanumero.append(_operador45)

                    #inverso
                        subjefe = re.compile(f'^MOD')
                        t=subjefe.search(_cadena)
                        if t!=None:
                            i='MOD'
                            _operador=Token.TK_Mod
                            _operador6='%'
                            self.listanumero.append(_operador6)

                    #inverso
                        subjefe = re.compile(f'^INVERSO')
                        t=subjefe.search(_cadena)
                        if t!=None:
                            i='INVERSO'
                            _operador=Token.TK_Inverso
                            tokens.pop(6)
                            _operador7='inverso'
                            self.listanumero.append(_operador7)

                    #seno 
                        subjefe = re.compile(f'^SENO')
                        t=subjefe.search(_cadena)
                        if t!=None:
                            i='SENO'
                            _operador=Token.TK_Seno
                            tokens.pop(6)
                            _operador8='seno'                        
                            self.listanumero.append(_operador8)

                    #coseno
                        subjefe = re.compile(f'^COSENO')
                        t=subjefe.search(_cadena)
                        if t!=None:
                            i='COSENO'
                            _operador=Token.TK_Coseno
                            tokens.pop(6)
                            _operador9='coseno'                        
                            self.listanumero.append(_operador9)
                    #TANGEMTE
                        subjefe = re.compile(f'^TANGENTE')
                        t=subjefe.search(_cadena)
                        if t!=None:
                            i='TANGENTE'
                            _operador=Token.TK_Seno
                            tokens.pop(6)
                            _operador10='tangente'                        
                            self.listanumero.append(_operador10)

                        if _operador==None:
                        #otro error
                            print('error en operaciones operador sin llenar ')                            
                            return{'result': _numeroop,'cadena':_cadena,"Error":True}

                    wjefe=re.compile(f'^{i}')
                    s=wjefe.search(_cadena)

                    if i =="/":
                        if len(self.listanumero)!=0:
                            self.listatodo.append(self.listanumero)
                            self.listanumero=[]                           

                    print("|",self.linea,"|", self.columna,"|",s.group())
                    self.columna+=int(s.end())               
                    _cadena=self.quitar(_cadena,s.end())
                self.aumentandolineas() 

            except:
                print('hay un error operacion ')               
                return{'result': _numeroop,'cadena':_cadena,"Error":True} 
        
       
        print(_izquierda,_operador,_derecho)
        operacionesarit.append([_izquierda,_operador,_derecho])
        
                
        return{'result': _numeroop,'cadena':_cadena,"Error":False}
   
       
    def tipo(self,_cadena:str):
        tokens=[
            Token.Tk_menor.value,#<
            Token.Tk_Tipo.value,#tipo
            Token.Tk_mayor.value,#>
            "operacion", #operacion 1.2
            Token.Tk_menor.value,#<
            Token.Tk_pleca.value,#/
            Token.Tk_Tipo.value,#tipo
            Token.Tk_mayor.value,#>   
        ]
        _numero=""        
        for i in tokens:
            try :
                if "operacion" == i:
                    salida=True
                    while salida:
                        print('----------------------------------------------------')
                        _result=self.operando(_cadena)
                        _cadena=_result['cadena']
                        if _result["Error"]:
                            print('hay un error dentro deloperador y tipo')
                            salida=False
                            #break
                        if self.etiqueta(_cadena, "</Tipo>"):
                            salida=False

                else:
                    jefe=re.compile(f'^{i}')
                    s=jefe.search(_cadena)                    
                    print("|",self.linea,"|", self.columna,"|",s.group())
                    self.columna+=int(s.end())
                    _cadena=self.quitar(_cadena,s.end())
                self.aumentandolineas()              
            
            except:                
                print('hay un erroren tipo ')
                return{'result': _numero,'cadena':_cadena,"Error":True}

        return{'result': _numero,'cadena':_cadena,"Error":False}


    def compilar(self):
        xml="ejemplo.txt"

        archivo=open(xml,"r",encoding="utf-8")
        contenido_archivo=archivo.readlines()
        archivo.close()
        
        una_cadena=""
        lista_cadena=[]
        nueval=[]
        otral=[]

        for i in contenido_archivo:
           i=i.replace(" ","")
           i=i.replace("\n","")
           if i!="":
            una_cadena+=i
            lista_cadena.append(i)
        for l in contenido_archivo:
            if l!="":           
               otral.append(l)

        
        
       
        self.lista_cadena=lista_cadena
        
       # print(self.tipo(una_cadena))
        print(self.todo(una_cadena))
        print(self.listatodo)
       

       
             
        self.importaroperaciones()
        Q=operandopy2.juan()
        

        if self.colorTT!=None and self.tamano!=None and self.colord!=None and self.tamanoD!=None and  self.colorCo!=None and  self.tamanoCC!=None :
            
       
            f = open('holamundo.html','w',encoding="utf-8")
            salidaA = """<html>\n<head></head><body bgcolor="#f4cffe">\n<h1 align="center" style="color:"""
            salidaA +=str(self.colorTT)
            salidaA +="""  ;font-size:"""
            salidaA +=str(self.tamano)
            salidaA+="""px">"""
            salidaA += str(self.aqui_titulo).replace("[","").replace("]","").replace("'","")
            salidaA +="</font></h1>\n"
            r=0
            for x in range(len(otral)):
                if otral[x]=="<Texto>\n":
                    r=0
                    while otral[x+r]!="</Texto>\n":
                        salidaA+="""<p style="color:"""
                        salidaA +=str(self.colord)
                        salidaA +=""" ;font-size:"""
                        salidaA +=str(self.tamanoD)
                        salidaA+="""px">"""
                        salidaA+=otral[x+r]
                        salidaA+="</font></p>\n"
                        r+=1
            salidaA+="""<p align="center" style="color:#691d92;font-size:20px">\n"""
            salidaA+='operaciones resueltas '
            salidaA+="</font></p>\n"
            for y in range(len(Q)):
                salidaA+="""<p style="color:"""
                salidaA +=str(self.colorCo)
                salidaA +=""" ;font-size:"""
                salidaA +=str(self.tamanoCC)
                salidaA+="""px">"""
                salidaA+=str(Q[y]).replace("[","").replace("]","").replace("'","")
                salidaA+="</font></p>\n"
            salidaA+="</body>\n </html>"
            f.write(salidaA)
            f.close()
            webbrowser.open_new_tab('holamundo.html')
        else:
            pass



        



      
    def titulo(self,_cadena:str):
        tokens=[
            
            Token.Tk_menor.value,#<
            Token.Tk_Titulo.value,#tipo
            Token.Tk_mayor.value,#>
            Token.TK_Operaciones.value,
            Token.Tk_menor.value,#<
            Token.Tk_pleca.value,#/
            Token.Tk_Titulo.value,#tipo
            Token.Tk_mayor.value
        ]
        _titulo=""
        for i in tokens:
            try:
                jefe=re.compile(f'^{i}')
                s=jefe.search(_cadena)                    
                print("|",self.linea,"|", self.columna,"|",s.group())
                self.columna+=int(s.end())
                if i == Token.TK_Operaciones.value:
                    _titulo+=s.group()                 
                    self.aqui_titulo.append(_titulo)
                
                _cadena=self.quitar(_cadena,s.end())
                self.aumentandolineas()  
                
            except:                
                print('hay un erroren tipo ')
                return{'result': _titulo,'cadena':_cadena,"Error":True}

        return{'result': _titulo,'cadena':_cadena,"Error":False}
    
    def Descrip(self,_cadena:str):
        tokens=[
            
            Token.Tk_menor.value,#<
            Token.Tk_Descripcion.value,#tipo
            Token.Tk_mayor.value,#>
            Token.TK_DESCRIPTION2 .value,
            Token.Tk_menor.value,#<
            Token.Tk_pleca.value,#/
            Token.Tk_Descripcion.value,#tipo
            Token.Tk_mayor.value
        ]
        _descrip=""
        for i in tokens:
            try:
                jefe=re.compile(f'^{i}')
                s=jefe.search(_cadena)                    
                print("|",self.linea,"|", self.columna,"|",s.group())
                self.columna+=int(s.end())
                _cadena=self.quitar(_cadena,s.end())
                self.aumentandolineas()  
            except:                
                print('hay un erroren tipo ')
                return{'result': _descrip,'cadena':_cadena,"Error":True}

        return{'result': _descrip,'cadena':_cadena,"Error":False}

    def contenid(self,_cadena:str):
        tokens=[
            
            Token.Tk_menor.value,#<
            Token.Tk_Contenido.value,#tipo
            Token.Tk_mayor.value,#>
            Token.TK_CONTENIDO2.value,
            Token.Tk_menor.value,#<
            Token.Tk_pleca.value,#/
            Token.Tk_Contenido.value,#tipo
            Token.Tk_mayor.value
        ]
        _descrip=""
        for i in tokens:
            try:
                jefe=re.compile(f'^{i}')
                s=jefe.search(_cadena)                    
                print("|",self.linea,"|", self.columna,"|",s.group())
                self.columna+=int(s.end())
                _cadena=self.quitar(_cadena,s.end())
                self.aumentandolineas()  
            except:                
                print('hay un erroren tipo ')
                return{'result': _descrip,'cadena':_cadena,"Error":True}

        return{'result': _descrip,'cadena':_cadena,"Error":False}

    def funci(self,_cadena:str):
        tokens=[
            
            Token.Tk_menor.value,#<
            Token.Tk_Funcion.value,#tipo
            Token.Tk_igual.value,            
            "FUNCION",
            Token.Tk_mayor.value,
            #>
            "TITULO",
            "DESCRIPCION",
            "CONTENIDO",
            Token.Tk_menor.value,#<
            Token.Tk_pleca.value,#/
            Token.Tk_Funcion.value,#tipo
            Token.Tk_mayor.value
        ]
        _descrip=""
        for i in tokens:
            try:
                if "TITULO" == i:
                    if self.etiqueta(_cadena,"<Titulo>"):
                        _result=self.titulo(_cadena)
                        _cadena=_result['cadena']
                        if _result["Error"]:
                            print('ocurrio un en el resultado operaciones')
                            return{'result': _descrip,'cadena':_cadena,"Error":True}
                        elif self.etiqueta(_cadena,'<Funcion=' ):
                            _result=self.funci(_cadena)
                            _cadena=_result['cadena']
                   
                    else:
                        print("error en el numero ")
                        return{'result': _descrip,'cadena':_cadena,"Error":True}
                
                elif "DESCRIPCION" == i:
                    if self.etiqueta(_cadena,"<Descripcion>"):
                        _result=self.Descrip(_cadena)
                        _cadena=_result['cadena']
                        if _result["Error"]:
                            print('ocurrio un en el resultado')
                            return{'result': _descrip,'cadena':_cadena,"Error":True}
                   
                    else:
                        print("error en el numero ")
                        return{'result': _descrip,'cadena':_cadena,"Error":True}

                elif "CONTENIDO" == i:
                    if self.etiqueta(_cadena,"<Contenido>"):
                        _result=self.contenid(_cadena)
                        _cadena=_result['cadena']
                        if _result["Error"]:
                            print('ocurrio un en el resultado')
                            return{'result': _descrip,'cadena':_cadena,"Error":True}
                   
                    else:
                        print("error en el numero ")
                        return{'result': _descrip,'cadena':_cadena,"Error":True}
                else:
                  
                    subjefe = re.compile(f'^ESCRIBIR') 
                    t=subjefe.search(_cadena)
                    if t!=None:                            
                        i='ESCRIBIR'                                                    
                        _operador=Token.Tk_ESCRIBIR
                        
                    wjefe=re.compile(f'^{i}')
                    s=wjefe.search(_cadena)

                    print("|",self.linea,"|", self.columna,"|",s.group())
                    self.columna+=int(s.end())               
                    _cadena=self.quitar(_cadena,s.end())
                self.aumentandolineas() 




            except:                
                print('hay un error en funcion ')
                return{'result': _descrip,'cadena':_cadena,"Error":True}

        return{'result': _descrip,'cadena':_cadena,"Error":False}
    
    def texti(self,_cadena:str):
        tokens=[
            
            Token.Tk_menor.value,#<
            Token.TK_TextoPrincipal.value,#texto
            Token.Tk_mayor.value,#>
            Token.TK_Texto.value,#niuewdfhuwebcehcoi
            Token.Tk_menor.value,#<
            Token.Tk_pleca.value,#/
            Token.TK_TextoPrincipal.value,#texto
            Token.Tk_mayor.value
        ]
        _descrip=""
        self.descrip=None
        for i in tokens:
            try:
                jefe=re.compile(f'^{i}')
                so=jefe.search(_cadena)                    
                print("|",self.linea,"|", self.columna,"|",so.group())
                self.columna+=int(so.end())
                if i == Token.TK_Texto.value:
                    _descrip+=so.group()
                _cadena=self.quitar(_cadena,so.end())
                self.descrip=_descrip
                self.aumentandolineas()  
            except:                
                print('hay un erroren tipo ')
                return{'result': _descrip,'cadena':_cadena,"Error":True}
        

        return{'result': _descrip,'cadena':_cadena,"Error":False}

    def todo(self,_cadena:str):
        tokens=[
            "TIPO",
            "TEXTO",
            "FUNCION",
            "ESTILO"
        ]
        _descrip=""
        for i in tokens:
            try:
                if "TIPO" == i:
                    salida=True
                    if salida:
                        print('*******************************************')
                        _result=self.tipo(_cadena)
                        _cadena=_result['cadena']
                        if _result["Error"]:
                            print('hay un error dentro deloperador y tipo')
                            salida=False
                            #break
                        if self.etiqueta(_cadena, "</tipo>"):
                            print('paso')
                            salida=False
                if "TEXTO" == i:
                    salida=True
                    if salida:
                        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                        _result=self.texti(_cadena)
                        _cadena=_result['cadena']
                        if _result["Error"]:
                            print('hay un error dentro deloperador y tipo')
                            salida=False
                            #break
                        if self.etiqueta(_cadena, "</Texto>"):
                            print('paso')
                            salida=False
                       
                   
                   
                elif "FUNCION" == i:
                    salida=True
                    if salida:
                        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                        _result=self.funci(_cadena)
                        _cadena=_result['cadena']
                        if _result["Error"]:
                            print('hay un error dentro deloperadorw y tipo')
                            salida=False
                            #break
                        if self.etiqueta(_cadena, "</Funcion>"):
                            salida=False

                elif "ESTILO" == i:
                    salida=True
                    if salida:
                        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                        _result=self.estilo(_cadena)
                        _cadena=_result['cadena']
                        if _result["Error"]:
                            print('hay un error dentro deloperadorw y tipo')
                            salida=False
                            #break
                        if self.etiqueta(_cadena, "</Funcion>"):
                            salida=False
                   
            except:                
                print('hay un erroren tipo ')
                return{'result': _descrip,'cadena':_cadena,"Error":True}

        return{'result': _descrip,'cadena':_cadena,"Error":False}

    def titulo2(self,_cadena:str):

        Tokene=[
            Token.Tk_menor.value,#<
            Token.Tk_Titulo.value,#titulo
            Token.Tk_Color.value,
            Token.Tk_igual.value,
            Token.Tk_color2.value,
            Token.Tk_tamano.value,
            Token.Tk_igual.value,
            Token.Tk_Numero.value,
            Token.Tk_pleca.value,
            Token.Tk_mayor.value,#> 
        ]


        _titulo=""
        _colo=""
        
        for i in Tokene:
            try:
                jefe=re.compile(f'^{i}')
                s=jefe.search(_cadena)                    
                print("|",self.linea,"|", self.columna,"|",s.group())
                self.columna+=int(s.end())
                if i == Token.Tk_color2.value:
                    if s.group()=='ROJO':
                        _titulo='red'
                        self.colorTT=_titulo
                         
                    elif s.group()=='AZUL':
                        _titulo='blue'
                        self.colorTT=_titulo
                    elif s.group()=='VERDE':
                        _titulo='green'
                        self.colorTT=_titulo
                    elif s.group()=='AMARILLO':
                        _titulo='yellow'
                        self.colorTT=_titulo
                    elif s.group()=='NEGRO':
                        _titulo='black'
                        self.colorTT=_titulo
                    elif s.group()=='MOPRADO':
                        _titulo='purple'
                        self.colorTT=_titulo
                    elif s.group()=='NARANJA':
                        _titulo='orange'
                        self.colorTT=_titulo
                if i ==Token.Tk_Numero.value:
                    _colo+=s.group() 
                    self.tamano=_colo

                
                _cadena=self.quitar(_cadena,s.end())
                self.aumentandolineas()  
                
            except:                
                print('hay un erroren tipo ')
                return{'result': _titulo,'cadena':_cadena,"Error":True}

        return{'result': _titulo,'cadena':_cadena,"Error":False}

    def Descripcion2(self,_cadena:str):
        Tokene=[
            Token.Tk_menor.value,#<
            Token.Tk_Descripcion.value,#titulo
            Token.Tk_Color.value,
            Token.Tk_igual.value,
            Token.Tk_color2.value,
            Token.Tk_tamano.value,
            Token.Tk_igual.value,
            Token.Tk_Numero.value,
            Token.Tk_pleca.value,
            Token.Tk_mayor.value,#> 
        ]
        _titulo=""
        _tamanoDD=""
        self.colord=None
        self.tamanoD=None
        for i in Tokene:
            try:
                jefe=re.compile(f'^{i}')
                s=jefe.search(_cadena)                    
                print("|",self.linea,"|", self.columna,"|",s.group())
                self.columna+=int(s.end())
                if i == Token.Tk_color2.value:
                    if s.group()=='ROJO':
                        _titulo='red'
                        self.colord=_titulo
                         
                    elif s.group()=='AZUL':
                        _titulo='blue'
                        self.colord=_titulo
                    elif s.group()=='VERDE':
                        _titulo='green'
                        self.colord=_titulo
                    elif s.group()=='AMARILLO':
                        _titulo='yellow'
                        self.colord=_titulo
                    elif s.group()=='NEGRO':
                        _titulo='black'
                        self.colord=_titulo
                    elif s.group()=='MOPRADO':
                        _titulo='purple'
                        self.colord=_titulo
                    elif s.group()=='NARANJA':
                        _titulo='orange'
                        self.colord=_titulo
                if i==Token.Tk_Numero.value:
                    _tamanoDD+=s.group()
                    self.tamanoD=_tamanoDD
                _cadena=self.quitar(_cadena,s.end())

                self.aumentandolineas()  
                
            except:                
                print('hay un erroren tipo ')
                return{'result': _titulo,'cadena':_cadena,"Error":True}

        return{'result': _titulo,'cadena':_cadena,"Error":False}

    def Contenido2(self,_cadena:str):
        Tokene=[
            Token.Tk_menor.value,#<
            Token.Tk_Contenido.value,#titulo
            Token.Tk_Color.value,
            Token.Tk_igual.value,
            Token.Tk_color2.value,
            Token.Tk_tamano.value,
            Token.Tk_igual.value,
            Token.Tk_Numero.value,
            Token.Tk_pleca.value,
            Token.Tk_mayor.value,#> 
        ]


        _titulo=""
        _tamanoCC=""
        self.colorCo=None
        self.tamanoCC=None
        for i in Tokene:
            try:
                jefe=re.compile(f'^{i}')
                s=jefe.search(_cadena)                    
                print("|",self.linea,"|", self.columna,"|",s.group())
                self.columna+=int(s.end())
                if i == Token.Tk_color2.value:
                    if s.group()=='ROJO':
                        _titulo='red'
                        self.colorCo=_titulo
                         
                    elif s.group()=='AZUL':
                        _titulo='blue'
                        self.colorCo=_titulo
                    elif s.group()=='VERDE':
                        _titulo='green'
                        self.colorCo=_titulo
                    elif s.group()=='AMARILLO':
                        _titulo='yellow'
                        self.colorCo=_titulo
                    elif s.group()=='NEGRO':
                        _titulo='black'
                        self.colorCo=_titulo
                    elif s.group()=='MOPRADO':
                        _titulo='purple'
                        self.colorCo=_titulo
                    elif s.group()=='NARANJA':
                        _titulo='orange'
                        self.colorCo=_titulo
                if i==Token.Tk_Numero.value:
                    _tamanoCC+=s.group()
                    self.tamanoCC=_tamanoCC
                _cadena=self.quitar(_cadena,s.end())                
                
                self.aumentandolineas()  
                
            except:                
                print('hay un erroren tipo ')
                return{'result': _titulo,'cadena':_cadena,"Error":True}

        return{'result': _titulo,'cadena':_cadena,"Error":False}
    
    def estilo(self,_cadena:str):
        tokens=[
            
            Token.Tk_menor.value,#<
            Token.TK_Estilo.value,#tipo
            Token.Tk_mayor.value,            
           
            #>
            "TITULO2",
            "DESCRIPCION",
            "CONTENIDO",
            Token.Tk_menor.value,#<
            Token.Tk_pleca.value,#/
            Token.TK_Estilo.value,#tipo
            Token.Tk_mayor.value
        ]
        _descrip=""
        for i in tokens:
            try:
                if "TITULO2" == i:
                    if self.etiqueta(_cadena,"<Titulo"):
                        _result=self.titulo2(_cadena)
                        _cadena=_result['cadena']
                        if _result["Error"]:
                            print('ocurrio un en el resultado operaciones')
                            return{'result': _descrip,'cadena':_cadena,"Error":True}
                        
                       
                    else:
                        print("error en el numero ")
                        return{'result': _descrip,'cadena':_cadena,"Error":True}
                
                elif "DESCRIPCION" == i:
                    if self.etiqueta(_cadena,"<Descripcion"):
                        _result=self.Descripcion2(_cadena)
                        _cadena=_result['cadena']
                        if _result["Error"]:
                            print('ocurrio un en el resultado')
                            return{'result': _descrip,'cadena':_cadena,"Error":True}
                   
                    else:
                        print("error en el numero ")
                        return{'result': _descrip,'cadena':_cadena,"Error":True}

                elif "CONTENIDO" == i:
                    if self.etiqueta(_cadena,"<Contenido"):
                        _result=self.Contenido2(_cadena)
                        _cadena=_result['cadena']
                        if _result["Error"]:
                            print('ocurrio un en el resultado')
                            return{'result': _descrip,'cadena':_cadena,"Error":True}
                   
                    else:
                        print("error en el numero ")
                        return{'result': _descrip,'cadena':_cadena,"Error":True}
                else:
                  
                        
                    wjefe=re.compile(f'^{i}')
                    s=wjefe.search(_cadena)

                    print("|",self.linea,"|", self.columna,"|",s.group())
                    self.columna+=int(s.end())               
                    _cadena=self.quitar(_cadena,s.end())
                self.aumentandolineas() 




            except:                
                print('hay un error en funcion ')
                return{'result': _descrip,'cadena':_cadena,"Error":True}

        return{'result': _descrip,'cadena':_cadena,"Error":False}


        

Analizador().compilar()

""" else:
                    jefe=re.compile(f'^{i}')
                    s=jefe.search(_cadena)
                    print("|",self.linea,"|", self.columna,"|",s.group())
                    self.columna+=int(s.end())
                    _cadena=self.quitar(_cadena,s.end())
                    self.aumentandolineas()
                    
                    
                    
                    
                    for i in operacionesarit:
            if i[1]==Token.TK_Suma:
                print("suma")
                
                print(i[0]+i[2])
            if i[1]==Token.Tk_Resta:
                print("resta")
               
                print(i[0]-i[2])
            if i[1]==Token.Tk_Multiplicacion:
                print("multiplicacion")
                
                print(i[0]*i[2])
            if i[1]==Token.Tk_Division:
                print("division")
                
                print(i[0]/i[2])
            if i[1]==Token.TK_RAIZ:
                print("raiz")
                
                print(i[0]**(1/i[2]))
            if i[1]==Token.Tk_Potencia:
                print("potencia")
                
                print(i[0]**i[2])
            if i[1]==Token.TK_Mod:
                print("mod")
                print(i[0],i[1],i[2])
                print(i[0]%i[2])
            if i[1]==Token.TK_Inverso:
                print("inverso")
                print(i[0],i[1],i[2])
                print(i[0]**-1)
            if i[1]==Token.TK_Seno:
                print("seno")
                print(i[0],i[1],i[2])                
                print(math.sin(int(i[0])))
            if i[1]==Token.TK_Coseno:
                print("coseno")
                print(i[0],i[1],i[2])
                print(math.cos(int(i[0])))
            if i[1]==Token.TK_Tangente:
                print("tangente")
                print(i[0],i[1],i[2])
                print(math.tan(int(i[0])))
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    """