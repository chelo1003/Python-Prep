class Herramientas:
    def __init__(self, lista):
        self.lista = lista

    def primo_lista(self):
        for numero in self.lista:
            if self.__numero_primo(numero):
                print("El número ", numero, " es primo")
            else:
                print("El número ", numero, " no es primo")

    
    def __numero_primo(self, numero):
        divisor = numero -1
        if divisor>0:
            while divisor>0:
                    if int(numero)%divisor != 0:
                        divisor-=1
                    elif divisor == 1:
                        return True
                    else:
                        return False
        else:
            return True
        
    def repetidos(self):    
        numero_repetido = 0
        cuenta = 0
        cuenta_local = 0
        cada_numero = 0
        while cada_numero < len(self.lista):
            num_a_controlar = self.lista[cada_numero]        
            for numero in self.lista:
                if num_a_controlar == numero:
                    cuenta_local+=1            
                    if cuenta_local > cuenta:
                        cuenta = cuenta_local
                        numero_repetido = num_a_controlar
            cuenta_local = 0
            cada_numero+=1
        return(numero_repetido, cuenta)
    
    def temperatura_lista(self, escala1, escala2):
        for numero in self.lista:
            print(numero, " grados en la escala ", escala1, " equivalen a ", self.__conversor_temperatura(numero, escala1, escala2), " en la escala ", escala2)


    def __conversor_temperatura(self, numero, escala1, escala2):
        temperatura = float(numero)
        if escala1 == escala2:
            temperatura = temperatura
        elif escala1== "C" and escala2== "F":
            temperatura = (temperatura * (9/5)) + 32
        elif escala1== "C" and escala2== "K":
            temperatura = temperatura + 273.15
        elif escala1== "F" and escala2== "C":
            temperatura = (temperatura - 32) * (5/9)
        elif escala1== "K" and escala2== "C":
            temperatura = temperatura - 273.15
        elif escala1== "K" and escala2== "F":
            temperatura = temperatura - 273.15
            temperatura = (temperatura * (9/5)) + 32
        elif escala1== "F" and escala2== "K":
            temperatura = (temperatura - 32) * (5/9)
            temperatura = temperatura + 273.15
        else:
            print("Ha ocurrido un error, por favor intente nuevamente o lea las instrucciones")
            return

        return temperatura
    
    def factorial_lista(self):
        for numero in self.lista:
            print(self.__funcion_factorial(numero))

    def __funcion_factorial(self, numero):
        if type(numero) != int or numero <= 0:
            return "Por favor introduzca un número entero y positivo"  

        if numero == 1:
            return 1
        
        numero = numero * self.__funcion_factorial(numero -1)
        return numero