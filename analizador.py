from enum import Enum
from intentonumero import numero

import re

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
    TK_Raiz="RAIZ"
    TK_Inverso="INVERSO"
    TK_Seno="SENO"
    TK_Coseno="COSENO"
    TK_Tangente="TANGENTE"
    TK_Mod="MOD"

#analisador lexico  

class Analizador:
    

    def __init__(self):
        self.cadena = ""
        self.linea=0
        self.columna=0
        self.lista_cadena=[]
        self.tmp_cadena=""
        self.lista1=[]
        self.listaToken=[]
        self.nuuu=numero

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
#limpio supuestamente los numeros <Numero >10</Numero>
    

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


        #<Numero > 5 </Numero>

        _numero=""

        for i in tokens:
            try :
               
                jefe=re.compile(f'^{i}')
                s=jefe.search(_cadena)
                
                print("|",self.linea,"|", self.columna,"|",s.group())
                self.columna+=int(s.end())
                
#guardar el token self.columna+=int(s.end())

                self.listaToken.append([self.linea,self.columna,s.group(),i]) #supuestamente guardo token en una lista falta nombre de token 
                #self.nuuu(i,self.linea,self.columna)
                
                
                if i ==Token.Tk_Numero.value:

                    _numero=s.group()
                _cadena=self.quitar(_cadena,s.end())
                self.aumentandolineas()               #print(_cadena)
            except:
#guardar error para tabla de errores

                return{'result': _numero,'cadena':_cadena,"Error":True}


        # en _numero se guarda los 
        
        print("Numero1",_numero)
        self.lista1.append(_numero)
       
        #print('sumanumero',self.lista1)
        #print(self.listaToken)
        

        return{'result': _numero,'cadena':_cadena,"Error":False}



    """def suma(self):
        listasuma=self.listaToken
        print(listasuma)
        for i in listasuma:
            if i[3]=="Numero":
                print(i[2])"""



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
        _numeroop=""
        _operador=None
        for i in tokens:
            
            try :
               #print('juan')
                if "Numero" == i:
                    if self.etiqueta(_cadena,"<Numero>"):
                        _result=self.Numero(_cadena)
                       # print(_cadena)
                        _cadena=_result['cadena']
                        
                        
                        
                        if _result["Error"]:
                            print('ocurrio un en el resltado ')
                            return{'result': _numeroop,'cadena':_cadena,"Error":True}
                        
                    elif self.etiqueta(_cadena,'<Operacion=' ):
                        _result=self.operando(_cadena)
                        _cadena=_result['cadena']
                        if _result["Error"]:
                            print('hay un error dentro del numero')
                            return{'result': _numeroop,'cadena':_cadena,"Error":True}
                        
                    else:
                        print("error en el numero ")
                        return{'result': _numeroop,'cadena':_cadena,"Error":True}
                else:
                    if "OPERACION" == i: 
                        #HACER LO DE LOS OPERADORES SUMA Y DEMAS
                    #SUMA
                    #SUMA
                        subjefe = re.compile(f'^SUMA') 
                        t=subjefe.search(_cadena)
                        if t!=None:
                            
                            i='SUMA'
                            print(_cadena)                            
                            _operador=Token.TK_Suma
                            
                            

                    #RESTA
                        subjefe = re.compile(f'^RESTA') 
                        t=subjefe.search(_cadena)
                        if t!=None:
                            i='RESTA'
                            _operador=Token.Tk_Resta


                    #MULTIPLICADOR
                        subjefe = re.compile(f'^MULTIPLICACION')
                        t=subjefe.search(_cadena)
                        if t!=None:
                            i='MULTIPLICACION'
                            _operador=Token.Tk_Multiplicacion

                    #DIVISION
                        subjefe = re.compile(f'^DIVISION')
                        t=subjefe.search(_cadena)
                        if t!=None:
                            i='DIVISION'
                            _operador=Token.Tk_Division


                    #POTENCIA

                        subjefe = re.compile(f'^POTENCIA')
                        t=subjefe.search(_cadena)
                        if t!=None:
                            i='POTENCIA'
                            _operador=Token.Tk_Potencia

                    #MODULO
                        subjefe = re.compile(f'^MODULO')
                        t=subjefe.search(_cadena)
                        if t!=None:
                            i='MODULO'
                            _operador=Token.Tk_Modulo

                    #raiz
                        subjefe = re.compile(f'^RAIZ')
                        t=subjefe.search(_cadena)
                        if t!=None:
                            i='RAIZ'
                            _operador=Token.Tk_Raiz
                        
                            

                    

                        if _operador==None:
                        #otro error
                            print('error en operaciones  resta , suma, etc ')
                            return{'result': _numeroop,'cadena':_cadena,"Error":True}

                    wjefe=re.compile(f'^{i}')
                    s=wjefe.search(_cadena)
                    #guardar el token self.columna+=int(s.end())
                    
                    print("|",self.linea,"|", self.columna,"|",s.group())
                    self.columna+=int(s.end())               
                    _cadena=self.quitar(_cadena,s.end())
                self.aumentandolineas()               #print(_cadena)
            except:
#guardar error para tabla de errores
                print('hay un error operacion ')
                return{'result': _numeroop,'cadena':_cadena,"Error":True} 
                
        #NUMERO1 OPERADOR NUMERO 2
        
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
        listaq=[]
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
                            pass
                            #break
                        if self.etiqueta(_cadena, "</Tipo>"):
                            salida=False

                   



                else:
                    jefe=re.compile(f'^{i}')
                    s=jefe.search(_cadena)
                    #listaq.append(["|",self.linea,"|", self.columna,"|",s.group()])
                    #print(listaq)

                    print("|",self.linea,"|", self.columna,"|",s.group())
                    self.columna+=int(s.end())
                    _cadena=self.quitar(_cadena,s.end())
                self.aumentandolineas()               #print(_cadena)
            
            except:
                #guardar en lista ojito todos los errores en ua lista aun no lo haces 
                print('hay un erroren tipo ')
                return{'result': _numero,'cadena':_cadena,"Error":True}


        return{'result': _numero,'cadena':_cadena,"Error":False}

    def compilar(self):
        xml="ejemplo.txt"

        archivo=open(xml,"r")
        contenido_archivo=archivo.read()
        archivo.close()
        #contenido_archivo=xml   #aqui es donde se pone el xml ojo no

        #print(contenido_archivo)

        #limpiando mi cadena animo !!!
        una_cadena=""
        lista_cadena=[]
       
        

        for i in contenido_archivo:
           i=i.replace(" ","")
           i=i.replace("\n","")
           

           if i!="":
            una_cadena+=i
            lista_cadena.append(i)
           
        
        #print("----------------------------------------------")

        #print(una_cadena)
        #print("----------------------------------------------")
       # print(lista_cadena)

        self.lista_cadena=lista_cadena
        #self.Numero(una_cadena)
        #self.operando(una_cadena)
        
        print( self.tipo(una_cadena))
        #self.suma()
        print('holi')
        
        
#
Analizador().compilar()

