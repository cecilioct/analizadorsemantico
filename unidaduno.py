import re
print("Autores: ")
print("Cecilio Gaspar Cauich Tun")
print("Bryan Fernando Zib Euan")
print("Darwin Eligio Cocom Mis")
print("")

filename="recurso.txt"
textfile=open(filename,"r")
regex= "[aA-zZ]+"
reg = re.compile(regex)


for line in textfile:
    lista=reg.findall(line)#Revision por lineas
    variable=""


    for elemento in lista:#Extrasión de valores de la lista
        
            #comprobacion del tipo de dato
        
        if(elemento == "float"):  
            print("F L O A T")             #PARA TIP DE DATO FLOAT
            tipo=elemento

                
                #reconocimiento de la variable en la misma linea para
            regex = r"\s[aA-zZ]?"#Verifica que sea la palabra que sigue después de la palabra reservada
            reg = re.compile(regex)
            lista =reg.findall(line)
            for elemento in lista:                        
                var=elemento

            if re.search(regex, elemento): #NOTA 02
                regex = r"[aA-zZ]" #Extraemos la variable sin el espacio para poder ser comparado en la segunda linea
                reg = re.compile(regex)
                lista = reg.findall(line)
                for elemento in lista:
                     variable=elemento     #El "elemento" se asigna a "variable" --> Comprobar si se ha declarado
                  # print("Primer encuentro de var :",variable)

                

            regex = r"\s[aA-zZ]?;"#verifica si la variable fue declarada correctamente
            reg = re.compile(regex)
            lista = reg.findall(line)
            for elemento in lista:
                if re.search(regex,elemento):
                    print("Declarado Correctamente")
                else:
                    print("Erro al declarar")

                
            regex= r"[aA-zZ]?"#Reconomiento de variable por segunda vez
            reg = re.compile(regex)

            declar = False #Nota 06
            for line in textfile:#Busca en todo el texto el patron de arriba
                lista=reg.findall(line) #NOTA 03

                for elemento in lista:
                        
                    cadena = elemento
                    if re.search(regex,elemento):#Comprobamos si se encuentra alguna coincidencia con el patron
                        cadena = elemento #Nota O4

                        if not cadena: #Si cadena esta vacia no asigno nada a VARIABLE 2
                            break # solo porque el IF necesitaba un opercion puse eso, no hace nada
                        else:
                            variable2=elemento #Si se encuentra una letra se le asgina a variable2
                            if(variable2 == variable):# NOTA 05 Verifica si la variable es la que fue declarada anteriormente 
                                #print("La variable fue declarada ya")
                                declar = True

                            else:
                                print("La variable no ha sido declarada")

                        #Termina if
                bandr = False #NOTA 01
                if(declar == True):
                    regex = r"\d+[.]\d+|\d+[.]\d+\s\+\s\d+[.]\d+"
                    reg = re.compile(regex)  
                    lista = reg.findall(line)
                         
                    for elemento in lista:
                        match = re.search(regex, elemento)
                        if match:
                            print("Asginacion exitosa tipo [FLOAT]")
                            bandr = True
                                 
                                 
                    if(bandr == False):
                        print("Asignacion incorrecta tipo [FLOAT]")

                        # elif(declar==False):
                               #print("La variable no ha sido declarada")

                if(bandr==False):
                        break
                else:
                    break


    #######################################################################################################                                         Fin IF de FLOAT
    
    for elemento in lista:#Extrasión de valores de la lista
        
        if(elemento == "boolean"): 
            print("B O O L E A N") 
            print("")             #PARA TIPO BOOLEAN
            tipo=elemento

                
                #reconocimiento de la variable en la misma linea para
            regex = r"\s[aA-zZ]?"#Verifica que sea la palabra que sigue después de la palabra reservada
            reg = re.compile(regex)
            lista =reg.findall(line)
            for elemento in lista:                        
                var=elemento

            if re.search(regex, elemento): #NOTA 02
                regex = r"[aA-zZ]" #Extraemos la variable sin el espacio para poder ser comparado en la segunda linea
                reg = re.compile(regex)
                lista = reg.findall(line)
                for elemento in lista:
                    variable=elemento     #El "elemento" se asigna a "variable" --> Comprobar si se ha declarado


            regex = r"\s[aA-zZ]?;"#verifica si la variable fue declarada correctamente
            reg = re.compile(regex)
            lista = reg.findall(line)
            for elemento in lista:
                if re.search(regex,elemento):
                    print("Declarado Correctamente[BOOLEAN]")
                else:
                    print("Erro al declarar")

                
            regex= r"[aA-zZ]?"#Reconomiento de variable por segunda vez
            reg = re.compile(regex)
                

            declar = False #Nota 06
            for line in textfile:#Busca en todo el texto el patron de arriba
                lista=reg.findall(line) #NOTA 03

                for elemento in lista:

                    if re.search(regex,elemento):#Comprobamos si se encuentra alguna coincidencia con el patron
                        cadena = elemento #Nota O4

                        if not cadena: #Si cadena esta vacia no asigno nada a VARIABLE 2
                            break # solo porque el IF necesitaba un opercion puse eso, no hace nada
                        else:
                            variable2=elemento #Si se encuentra una letra se le asgina a variable2
                            if(variable2 == variable):# NOTA 05 ---Verifica si la variable es la que fue declarada anteriormente 
                                #print("Variable declarada como BOOLEAN")
                                declar = True

                            else:
                                print("Variable no declarada como [BOOLEAN]")

                        #Termina if
                bandr = False
                if(declar == True):
                    regex = "\d+\s[<|>|[=>]|[>=]|[!=]\s\d+"
                    reg = re.compile(regex)  
                    lista = reg.findall(line)
                         
                    for elemento in lista:
                        match = re.search(regex, elemento)
                        if match:
                            print("Asginacion exitosa[BOOLEAN]")
                            bandr = True
                                 
                                 
                    if(bandr == False):
                        print("Asignacion incorrecta tipo [BOOLEAN]")

                if(bandr==False):
                    break
                else:
                    break

################################################################3

    for elemento in lista:#Extrasión de valores de la lista

            #comprobacion del tipo de dato
            if(elemento == "String"):               #PARA TIP DE DATO STRING
                print("S T R I N G")
                tipo=elemento

                
                #reconocimiento de la variable en la misma linea para
                regex = r"\s[aA-zZ]?"#Verifica que sea la palabra que sigue después de la palabra reservada
                reg = re.compile(regex)
                lista =reg.findall(line)
                for elemento in lista:                        
                    var=elemento

                if re.search(regex, elemento): #NOTA 02
                   regex = r"[aA-zZ]" #Extraemos la variable sin el espacio para poder ser comparado en la segunda linea
                   reg = re.compile(regex)
                   lista = reg.findall(line)
                   for elemento in lista:
                     variable=elemento     #El "elemento" se asigna a "variable" --> Comprobar si se ha declarado


                regex = r"\s[aA-zZ]?;"#verifica si la variable fue declarada correctamente
                reg = re.compile(regex)
                lista = reg.findall(line)
                for elemento in lista:
                    if re.search(regex,elemento):
                        print("Declarado Correctamente [STRING]")
                    else:
                        print("Erro al declarar")

                
                regex= r"[aA-zZ]?"#Reconomiento de variable por segunda vez
                reg = re.compile(regex)

                declar = False #Nota 06
                for line in textfile:#Busca en todo el texto el patron de arriba
                    lista=reg.findall(line) #NOTA 03

                    for elemento in lista:

                        if re.search(regex,elemento):#Comprobamos si se encuentra alguna coincidencia con el patron
                            cadena = elemento #Nota O4

                            if not cadena: #Si cadena esta vacia no asigno nada a VARIABLE 2
                                break # solo porque el IF necesitaba un opercion puse eso, no hace nada
                            else:
                                variable2=elemento #Si se encuentra una letra se le asgina a variable2
                                if(variable2 == variable):# NOTA 05 ---Verifica si la variable es la que fue declarada anteriormente 
                                    #print("La variable fue declarada ya")
                                    declar = True

                                else:
                                    print("Variable no declarada como [STRING]")

                        #Termina if
                    bandr= False
                    if(declar == True):
                         regex = r"[\"][aA-zZ]+[\"];|[\"][aA-zZ]+[\"] \+ [\"][aA-zZ]+[\"];"
                         reg = re.compile(regex)  
                         lista = reg.findall(line)

                         for elemento in lista:
                              #print("Esto es el ",elemento)
                              match = re.search(regex, elemento)
                              if match:
                                 print("Asginacion exitosa[STRING]")
                                 bandr = True

                         if(bandr == False):
                            print("Asignacion incorrecta tipo [STRING]")

                    if(bandr==False):
                        break
                    else:
                        break                                   

##############################################################################
   
    for elemento in lista:  # Extrasión de valores de la lista

            # comprobacion del tipo de dato
            print()
            if (elemento == "int"):  # PARA TIP DE DATO 

                # reconocimiento de la variable en la misma linea para
                regex = r"\s[aA-zZ]?"  # Verifica que sea la palabra que sigue después de la palabra reservada
                reg = re.compile(regex)
                lista = reg.findall(line)
                for elemento in lista:
                    var = elemento

            
                regex = r"\s[aA-zZ]?="  # verifica si la variable fue declarada correctamente
                reg = re.compile(regex)
                lista = reg.findall(line)
                for elemento in lista:
                    if re.search(regex, elemento):
                        #print("Declarado Correctamente")
                        declar = True  # Nota 06
                        if (declar == True):
                            regex = r"\s[0-9]+;|\s[0-9]+\s\+\s[0-9]+;"
                            reg = re.compile(regex)
                            lista = reg.findall(line)
                            bandr = False  # NOTA 01
                            for elemento in lista:
                                match = re.search(regex, elemento)
                                if match:
                                    print("Asignacion exitosa")
                                    bandr=True
                                    break
                            if (bandr == False):
                                print("Asignacion incorrecta tipo [int]")     

   #################################################################################

    for elemento in lista:  # Extrasión de valores de la lista

            # comprobacion del tipo de dato
            print()
            if (elemento == "double"):  # PARA TIP DE DATO 

                # reconocimiento de la variable en la misma linea para
                regex = r"\s[aA-zZ]?"  # Verifica que sea la palabra que sigue después de la palabra reservada
                reg = re.compile(regex)
                lista = reg.findall(line)
                for elemento in lista:
                    var = elemento

            
                regex = r"\s[aA-zZ]?="  # verifica si la variable fue declarada correctamente
                reg = re.compile(regex)
                lista = reg.findall(line)
                for elemento in lista:
                    if re.search(regex, elemento):
                        #print("Declarado Correctamente")
                        declar = True  # Nota 06
                        if (declar == True):
                            regex = r"\s[0-9]+[.][0-9]+;|\s[0-9]+[.][0-9]+\s\+\s[0-9]+[.][0-9]+;"
                            reg = re.compile(regex)
                            lista = reg.findall(line)
                            bandr = False  # NOTA 01
                            for elemento in lista:
                                match = re.search(regex, elemento)
                                if match:
                                    print("Asignacion exitosa[DOUBLE]")
                                    bandr=True
                                    break
                            if (bandr == False):
                                print("Asignacion incorrecta tipo [DOUBLE]")           



                

                
                    
                

            

                

                

            
