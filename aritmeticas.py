class aritmeticas:

    def haciendoop(self,lista):
        print(lista)
        listaq=[]
        

        for i in range(len(lista)):
            if lista[i][1]=='MULTIPLICACION':
                
                listaq  .append([int(lista[i][0])*int(lista[i][2])])
                print(listaq)

            elif lista[i][1]=='DIVISION':
                listaq  .append([int(lista[i][0])/int(lista[i][2])])
                print(listaq)

            elif lista[i][1]=='SUMA':
                if lista[i][0]==''and lista[i][2]=='':
                    listan=listaq[0]+listaq[1]
                    print(listan)

           


