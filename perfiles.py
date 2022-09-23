import math 
class OPerandopy:
    def __init__(self) -> None:
        pass

    def operation(self,paso_lista):
        self.listatodo=paso_lista
        unalista=[]
        cafelista=[]
        otralista=[]
        self.listat=[]
        
        for i in range(len(self.listatodo)):
            listamientras1=int(len(self.listatodo[i]))-3
            listaM2=int(len(self.listatodo[i]))-2
            listaM3=int(len(self.listatodo[i]))-1
            
            sumando_cont=0
            resta_cont=0
            multiplicacion_cont=0
            raiz_maiz_cont=0
            division_cont=0
            potenciando_cont=0
            residuo_contando=0
        #suma
            if self.listatodo[i][listaM2]!='tangente'and self.listatodo[i][listaM2]!='seno' and self.listatodo[i][listamientras1]=='+':
                sumando_cont=self.listatodo[i][listaM2]+self.listatodo[i][listaM3]
                unalista.append('(')
                unalista.append(str(self.listatodo[i][listaM2]))
                unalista.append('+')
                unalista.append(self.listatodo[i][listaM3])
                unalista.append(')')

                for j in range(listamientras1):
                    continuando_contando=j+1
                    continuando_contando1=j+2
                    #suma de porsiacaso
                    if self.listatodo[i][listamientras1-continuando_contando1]=="+":
                        sumando_cont=self.listatodo[i][listamientras1-continuando_contando]+sumando_cont
                        unalista.insert(0,'+')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando])

                    
                    #resta de porsiacaso
                    #for i in range(len(self.listatodo[i])):
                    #print ()
                    if self.listatodo[i][listamientras1-continuando_contando1]=="-":
                        sumando_cont=self.listatodo[i][listamientras1-continuando_contando]-sumando_cont

                        unalista.insert(0,'-')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando])

                    #multiplicacion de porsiacaso
                    if self.listatodo[i][listamientras1-continuando_contando1]=="*":
                        sumando_cont=self.listatodo[i][listamientras1-continuando_contando]*sumando_cont

                        unalista.insert(0,'*')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando])
                    #division de porsiacaso
                    if self.listatodo[i][listamientras1-continuando_contando1]=="/":

                        sumando_cont=self.listatodo[i][listamientras1-continuando_contando]/sumando_cont

                        unalista.insert(0,'/')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando])


                    if self.listatodo[i][listamientras1-continuando_contando1]=="^":
                        
                        sumando_cont=self.listatodo[i][listamientras1-continuando_contando]**sumando_cont

                        unalista.insert(0,'^')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando])
                    #reciduo
                    if self.listatodo[i][listamientras1-continuando_contando1]=="%":
                        sumando_cont=self.listatodo[i][listamientras1-continuando_contando]%sumando_cont

                        unalista.insert(0,'%')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando])


                    if self.listatodo[i][listamientras1-continuando_contando1]=='raiz':
                        sumando_cont=(sumando_cont)**(1/self.listatodo[i][listamientras1-continuando_contando])
                    

                q=str(unalista).replace(',','').replace("[","").replace("]","").replace("'","").replace(",","").replace(" ","")
                
               
                otralista.append(q)
                otralista.append('=')

                otralista.append(sumando_cont)
                p=str(otralista).replace(',','').replace("[","").replace("]","").replace("'","").replace(",","").replace(" ","")
                cafelista.append(p)
                cafelista.insert(0,':')
                cafelista.insert(0,i+1)
                cafelista.insert(0,'Operacion')
                
                a=str(cafelista).replace(',','').replace("[","").replace("]","").replace("'","")
                
                self.listat.append([a])
                unalista=[]
                otralista=[]
                
                cafelista=[]
              
        #resta
            if self.listatodo[i][listaM2]!='tangente'and self.listatodo[i][listaM2]!='seno' and self.listatodo[i][listamientras1]=='-':
                resta_cont=self.listatodo[i][listaM2]-self.listatodo[i][listaM3]
                unalista.append((str(self.listatodo[i][listaM2]),'-' ,self.listatodo[i][listaM3]))


                for j in range(listamientras1):
                    continuando_contando_r=j+1
                    continuando_contando_2r=j+2
                    if self.listatodo[i][listamientras1-continuando_contando_2r]=="+":
                        resta_cont=self.listatodo[i][listamientras1-continuando_contando_r]+resta_cont
                        unalista.insert(0,'+')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_r])

                    if self.listatodo[i][listamientras1-continuando_contando_2r]=="-":
                        resta_cont=self.listatodo[i][listamientras1-continuando_contando_r]-resta_cont
                        unalista.insert(0,'-')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_r])

                    if self.listatodo[i][listamientras1-continuando_contando_2r]=="*":
                        resta_cont=self.listatodo[i][listamientras1-continuando_contando_r]*resta_cont
                        unalista.insert(0,'*')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_r])

                    if self.listatodo[i][listamientras1-continuando_contando_2r]=="/":
                        resta_cont=self.listatodo[i][listamientras1-continuando_contando_r]/resta_cont
                        unalista.insert(0,'/')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_r])

                    if self.listatodo[i][listamientras1-continuando_contando_2r]=="^":
                        resta_cont=self.listatodo[i][listamientras1-continuando_contando_r]**resta_cont
                        unalista.insert(0,'^')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_r])

                    if self.listatodo[i][listamientras1-continuando_contando_2r]=="%":
                        resta_cont=self.listatodo[i][listamientras1-continuando_contando_r]%resta_cont
                        unalista.insert(0,'%')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_r])

                    if self.listatodo[i][listamientras1-continuando_contando_2r]=='raiz':
                        resta_cont=(resta_cont)**(1/self.listatodo[i][listamientras1-continuando_contando_r])
                        unalista.insert(0,'%')                        
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_r])
                q=str(unalista).replace(',','').replace("[","").replace("]","").replace("'","").replace(",","").replace(" ","")
                
               
                otralista.append(q)
                otralista.append('=')

                otralista.append(resta_cont)
                p=str(otralista).replace(',','').replace("[","").replace("]","").replace("'","").replace(",","").replace(" ","")
                cafelista.append(p)
                cafelista.insert(0,':')
                cafelista.insert(0,i+1)
                cafelista.insert(0,'Operacion')
                
                a=str(cafelista).replace(',','').replace("[","").replace("]","").replace("'","")
                
                self.listat.append([a])
                unalista=[]
                otralista=[]
                
                cafelista=[]
    #MULTIPLICACIO
            if self.listatodo[i][listaM2]!='tangente'and self.listatodo[i][listaM2]!='seno' and  self.listatodo[i][listamientras1]=='*':
                multiplicacion_cont=self.listatodo[i][listaM2]*self.listatodo[i][listaM3]
                unalista.append((str(self.listatodo[i][listaM2]),'*' ,self.listatodo[i][listaM3]))
                
                for j in range(listamientras1):
                    continuando_contando_m=j+1
                    continuando_contando_2m=j+2
                    if self.listatodo[i][listamientras1-continuando_contando_2m]=="+":
                        multiplicacion_cont=self.listatodo[i][listamientras1-continuando_contando_m]+multiplicacion_cont
                        unalista.insert(0,'+')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_m])

                        

                    if self.listatodo[i][listamientras1-continuando_contando_2m]=="-":
                        multiplicacion_cont=self.listatodo[i][listamientras1-continuando_contando_m]-multiplicacion_cont
                        unalista.insert(0,'-')

                    if self.listatodo[i][listamientras1-continuando_contando_2m]=="*":
                        multiplicacion_cont=self.listatodo[i][listamientras1-continuando_contando_m]*multiplicacion_cont
                        unalista.insert(0,'*')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_m])
                    
                    if self.listatodo[i][listamientras1-continuando_contando_2m]=="/":
                        multiplicacion_cont=self.listatodo[i][listamientras1-continuando_contando_m]/multiplicacion_cont
                        unalista.insert(0,'/')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_m])

                    if self.listatodo[i][listamientras1-continuando_contando_2m]=="^":
                        multiplicacion_cont=self.listatodo[i][listamientras1-continuando_contando_m]**multiplicacion_cont
                        unalista.insert(0,'^')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_m])

                    if self.listatodo[i][listamientras1-continuando_contando_2m]=="%":
                        multiplicacion_cont=self.listatodo[i][listamientras1-continuando_contando_m]%multiplicacion_cont
                        unalista.insert(0,'%')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_m])
                
                q=str(unalista).replace(',','').replace("[","").replace("]","").replace("'","").replace(",","").replace(" ","")
                otralista.append(q)
                otralista.append('=')
                otralista.append(multiplicacion_cont)
                p=str(otralista).replace(',','').replace("[","").replace("]","").replace("'","").replace(",","").replace(" ","")
                cafelista.append(p)
                cafelista.insert(0,':')
                cafelista.insert(0,i+1)
                cafelista.insert(0,'Operacion')                
                a=str(cafelista).replace(',','').replace("[","").replace("]","").replace("'","")                
                self.listat.append([a])
                unalista=[]
                otralista=[]                
                cafelista=[]

    #RAIZ
            if self.listatodo[i][listaM2]!='tangente'and self.listatodo[i][listaM2]!='seno' and self.listatodo[i][listamientras1]=='raiz':
                
                raiz_maiz_cont=self.listatodo[i][listaM3]**(1/self.listatodo[i][listaM2])
                unalista.append((str(self.listatodo[i][listaM2]),'✓' ,self.listatodo[i][listaM3]))


                for j in range(listamientras1):
                    continuando_contando_ra=j+1
                    continuando_contando_2ra=j+2
                    if self.listatodo[i][listamientras1-continuando_contando_2ra]=="+":
                        raiz_maiz_cont=self.listatodo[i][listamientras1-continuando_contando_ra]+raiz_maiz_cont
                        unalista.insert(0,'+')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_ra])
                        

                    if self.listatodo[i][listamientras1-continuando_contando_2ra]=="-":
                        raiz_maiz_cont=self.listatodo[i][listamientras1-continuando_contando_ra]-raiz_maiz_cont
                        unalista.insert(0,'-')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_ra])

                    if self.listatodo[i][listamientras1-continuando_contando_2ra]=="*":
                        raiz_maiz_cont=self.listatodo[i][listamientras1-continuando_contando_ra]*raiz_maiz_cont
                        unalista.insert(0,'-')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_ra])
                    
                    if self.listatodo[i][listamientras1-continuando_contando_2ra]=="/":
                        raiz_maiz_cont=self.listatodo[i][listamientras1-continuando_contando_ra]*raiz_maiz_cont
                        unalista.insert(0,'-')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_ra])

                    if self.listatodo[i][listamientras1-continuando_contando_2ra]=="^":
                        raiz_maiz_cont=self.listatodo[i][listamientras1-continuando_contando_ra]**raiz_maiz_cont
                        unalista.insert(0,'-')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_ra])

                    if self.listatodo[i][listamientras1-continuando_contando_2ra]=="%":
                        raiz_maiz_cont=self.listatodo[i][listamientras1-continuando_contando_ra]%raiz_maiz_cont
                        unalista.insert(0,'-')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_ra])

                    if self.listatodo[i][listamientras1-continuando_contando_2ra]=="raiz":
                        raiz_maiz_cont=self.listatodo[i][listamientras1-continuando_contando_ra]%raiz_maiz_cont
                        unalista.insert(0,'-')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_ra])

                q=str(unalista).replace(',','').replace("[","").replace("]","").replace("'","").replace(",","").replace(" ","")
                otralista.append(q)
                otralista.append('=')
                otralista.append(raiz_maiz_cont)
                p=str(otralista).replace(',','').replace("[","").replace("]","").replace("'","").replace(",","").replace(" ","")
                cafelista.append(p)
                cafelista.insert(0,':')
                cafelista.insert(0,i+1)
                cafelista.insert(0,'Operacion')                
                a=str(cafelista).replace(',','').replace("[","").replace("]","").replace("'","")                
                self.listat.append([a])
                unalista=[]
                otralista=[]                
                cafelista=[]
                

    #DIVISION
            if self.listatodo[i][listaM2]!='tangente'and self.listatodo[i][listaM2]!='seno' and  self.listatodo[i][listamientras1]=='/':
                division_cont=self.listatodo[i][listaM2]/self.listatodo[i][listaM3]
                unalista.append((self.listatodo[i][listaM2],'/ ' ,self.listatodo[i][listaM3]))
                for j in range(listamientras1):
                    continuando_contando_d=j+1
                    continuando_contando_2d=j+2
                    if self.listatodo[i][listamientras1-continuando_contando_2d]=="+":
                        division_cont=self.listatodo[i][listamientras1-continuando_contando_d]+division_cont
                        unalista.insert(0,'+')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_d])

                    if self.listatodo[i][listamientras1-continuando_contando_2d]=="-":
                        division_cont=self.listatodo[i][listamientras1-continuando_contando_d]-division_cont
                        unalista.insert(0,'-')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_d])

                    if self.listatodo[i][listamientras1-continuando_contando_2d]=="*":
                        division_cont=self.listatodo[i][listamientras1-continuando_contando_d]*division_cont
                        unalista.insert(0,'*')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_d])

                    if self.listatodo[i][listamientras1-continuando_contando_2d]=="/":
                        division_cont=self.listatodo[i][listamientras1-continuando_contando_d]/division_cont
                        unalista.insert(0,'/')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_d])
                        

                    if self.listatodo[i][listamientras1-continuando_contando_2d]=="^":
                        division_cont=self.listatodo[i][listamientras1-continuando_contando_d]**division_cont
                        unalista.insert(0,'^')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_d])


                    if self.listatodo[i][listamientras1-continuando_contando_2d]=="%":
                        division_cont=self.listatodo[i][listamientras1-continuando_contando_d]%division_cont
                        unalista.insert(0,'%')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_d])
                    

                q=str(unalista).replace(',','').replace("[","").replace("]","").replace("'","").replace(",","").replace(" ","")
                otralista.append(q)
                otralista.append('=')
                otralista.append(division_cont)
                p=str(otralista).replace(',','').replace("[","").replace("]","").replace("'","").replace(",","").replace(" ","")
                cafelista.append(p)
                cafelista.insert(0,':')
                cafelista.insert(0,i+1)
                cafelista.insert(0,'Operacion')                
                a=str(cafelista).replace(',','').replace("[","").replace("]","").replace("'","")                
                self.listat.append([a])
                unalista=[]
                otralista=[]                
                cafelista=[]

#POTENCIA
            if self.listatodo[i][listaM2]!='tangente'and self.listatodo[i][listaM2]!='seno' and self.listatodo[i][listamientras1]=='^':
                potenciando_cont=self.listatodo[i][listaM3]**self.listatodo[i][listaM2]
                unalista.append((self.listatodo[i][listaM2],'^ ' ,self.listatodo[i][listaM3]))
                for j in range(listamientras1):
                    continuando_contando_p=j+1
                    continuando_contando_2p=j+2
                    if self.listatodo[i][listamientras1-continuando_contando_2p]=="+":
                        potenciando_cont=self.listatodo[i][listamientras1-continuando_contando_p]+potenciando_cont
                        unalista.insert(0,'+')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_p])

                    if self.listatodo[i][listamientras1-continuando_contando_2p]=="-":
                        potenciando_cont=self.listatodo[i][listamientras1-continuando_contando_p]-potenciando_cont
                        unalista.insert(0,'-')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_p])

                    if self.listatodo[i][listamientras1-continuando_contando_2p]=="*":
                        potenciando_cont=self.listatodo[i][listamientras1-continuando_contando_p]*potenciando_cont
                        unalista.insert(0,'*')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_p])


                    if self.listatodo[i][listamientras1-continuando_contando_2p]=="/":
                        potenciando_cont=self.listatodo[i][listamientras1-continuando_contando_p]/potenciando_cont
                        unalista.insert(0,'/')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_p])


                    if self.listatodo[i][listamientras1-continuando_contando_2p]=="%":
                        potenciando_cont=self.listatodo[i][listamientras1-continuando_contando_p]%potenciando_cont
                        unalista.insert(0,'%')
                        unalista.insert(0,self.listatodo[i][listamientras1-continuando_contando_p])
                
                q=str(unalista).replace(',','').replace("[","").replace("]","").replace("'","").replace(",","").replace(" ","")
                otralista.append(q)
                otralista.append('=')
                otralista.append(potenciando_cont)
                p=str(otralista).replace(',','').replace("[","").replace("]","").replace("'","").replace(",","").replace(" ","")
                cafelista.append(p)
                cafelista.insert(0,':')
                cafelista.insert(0,i+1)
                cafelista.insert(0,'Operacion')                
                a=str(cafelista).replace(',','').replace("[","").replace("]","").replace("'","")                
                self.listat.append([a])
                unalista=[]
                otralista=[]                
                cafelista=[]

    #MODULO

            if self.listatodo[i][listaM2]!='tangente'and self.listatodo[i][listaM2]!='seno' and self.listatodo[i][listamientras1]=='%':
                residuo_contando=self.listatodo[i][listaM2]%self.listatodo[i][listaM3]
                unalista.append((self.listatodo[i][listaM2],'%',self.listatodo[i][listaM3]))
                for j in range(listamientras1):
                    continuando_contando_mo=j+1
                    continuando_contando_2mo=j+2
                    if self.listatodo[i][listamientras1-continuando_contando_2mo]=="+":
                        residuo_contando=self.listatodo[i][listamientras1-continuando_contando_mo]+residuo_contando

                    if self.listatodo[i][listamientras1-continuando_contando_2mo]=="-":
                        residuo_contando=self.listatodo[i][listamientras1-continuando_contando_mo]-residuo_contando

                    if self.listatodo[i][listamientras1-continuando_contando_2mo]=="*":
                        residuo_contando=self.listatodo[i][listamientras1-continuando_contando_mo]*residuo_contando

                    if self.listatodo[i][listamientras1-continuando_contando_2mo]=="/":
                        residuo_contando=self.listatodo[i][listamientras1-continuando_contando_mo]/residuo_contando

                    if self.listatodo[i][listamientras1-continuando_contando_2mo]=="^":
                        residuo_contando=self.listatodo[i][listamientras1-continuando_contando_mo]**residuo_contando

                    if self.listatodo[i][listamientras1-continuando_contando_2mo]=="%":
                        residuo_contando=self.listatodo[i][listamientras1-continuando_contando_mo]%residuo_contando
               
                q=str(unalista).replace(',','').replace("[","").replace("]","").replace("'","").replace(",","").replace(" ","")
                otralista.append(q)
                otralista.append('=')
                otralista.append(residuo_contando)
                p=str(otralista).replace(',','').replace("[","").replace("]","").replace("'","").replace(",","").replace(" ","")
                cafelista.append(p)
                cafelista.insert(0,':')
                cafelista.insert(0,i+1)
                cafelista.insert(0,'Operacion')                
                a=str(cafelista).replace(',','').replace("[","").replace("]","").replace("'","")                
                self.listat.append([a])
                unalista=[]
                otralista=[]                
                cafelista=[]

            #inverso
            if self.listatodo[i][listaM2]=='inverso':
                #print('holi')
                inverso_contando=1/self.listatodo[i][listaM3]
                unalista.append(('1/',self.listatodo[i][listaM3]))
               
                 

                q=str(unalista).replace(',','').replace("[","").replace("]","").replace("'","").replace(",","").replace(" ","")
                otralista.append(q)
                otralista.append('=')
                otralista.append(inverso_contando)
                p=str(otralista).replace(',','').replace("[","").replace("]","").replace("'","").replace(",","").replace(" ","")
                cafelista.append(p)
                cafelista.insert(0,':')
                cafelista.insert(0,i+1)
                cafelista.insert(0,'Operacion')                
                a=str(cafelista).replace(',','').replace("[","").replace("]","").replace("'","")                
                self.listat.append([a])
                unalista=[]
                otralista=[]                
                cafelista=[]
    #seno
            if self.listatodo[i][listaM2]=='seno':
                seno_contando=(self.listatodo[i][listaM3])*(math.pi/180)
                
                seno_contando=math.sin(seno_contando)
                unalista.append(('seno(',self.listatodo[i][listaM3],')'))
                 
                q=str(unalista).replace(',','').replace("[","").replace("]","").replace("'","").replace(",","").replace(" ","")
                otralista.append(q)
                otralista.append('=')
                otralista.append(seno_contando)
                p=str(otralista).replace(',','').replace("[","").replace("]","").replace("'","").replace(",","").replace(" ","")
                cafelista.append(p)
                cafelista.insert(0,':')
                cafelista.insert(0,i+1)
                cafelista.insert(0,'Operacion')                
                a=str(cafelista).replace(',','').replace("[","").replace("]","").replace("'","")                
                self.listat.append([a])
                unalista=[]
                otralista=[]                
                cafelista=[]


    #coseno
            if self.listatodo[i][listaM2]=='coseno':
                coseno_contando=(self.listatodo[i][listaM3])*(math.pi/180)
                coseno_contando=(math.cos(coseno_contando))
                print(coseno_contando)
                unalista.append(('coseno(',self.listatodo[i][listaM3],')'))
                
                 
                q=str(unalista).replace(',','').replace("[","").replace("]","").replace("'","").replace(",","").replace(" ","")
                otralista.append(q)
                otralista.append('=')
                otralista.append(coseno_contando)
                p=str(otralista).replace(',','').replace("[","").replace("]","").replace("'","").replace(",","").replace(" ","")
                cafelista.append(p)
                cafelista.insert(0,':')
                cafelista.insert(0,i+1)
                cafelista.insert(0,'Operacion')                
                a=str(cafelista).replace(',','').replace("[","").replace("]","").replace("'","")                
                self.listat.append([a])
                unalista=[]
                otralista=[]                
                cafelista=[]
    #tangente
            if self.listatodo[i][listaM2]=='tangente':
                coseno_contando=(self.listatodo[i][listaM3])*(math.pi/180)
                tangente_contando=math.tan(coseno_contando)
                unalista.append(('tangente(',self.listatodo[i][listaM3],')'))
                q=str(unalista).replace(',','').replace("[","").replace("]","").replace("'","").replace(",","").replace(" ","")
                otralista.append(q)
                otralista.append('=')
                otralista.append(tangente_contando)
                p=str(otralista).replace(',','').replace("[","").replace("]","").replace("'","").replace(",","").replace(" ","")
                cafelista.append(p)
                cafelista.insert(0,':')
                cafelista.insert(0,i+1)
                cafelista.insert(0,'Operacion')                
                a=str(cafelista).replace(',','').replace("[","").replace("]","").replace("'","")                
                self.listat.append([a])
                unalista=[]
                otralista=[]                
                cafelista=[]

            if self.listatodo[i][0]=='+'and self.listatodo[i][1]=='*'and self.listatodo[i+1][0]=='/':
                uno1=self.listatodo[i][listaM2]*self.listatodo[i][listaM3]
                
                dos2=self.listatodo[i+1][1]/self.listatodo[i+1][2]                
                tres3=uno1+dos2
                print(tres3)
            
    def juan(self):
       

        return self.listat


    


            



                


        
                     
        # imprimo lista    print(unalista)
        # cambio lista 
        



            
