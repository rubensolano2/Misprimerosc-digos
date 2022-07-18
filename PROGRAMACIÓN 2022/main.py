# print("programa de evaluacion")

# nota2 = int(input())


# def evaluacion(nota):
#   alumno = "aprobado"
#  if nota < 5:
#     alumno = "suspenso"
# return alumno


# print(evaluacion(nota2)


##edad =145
# if 0<edad<100:
#   print("edad es correcta")
# else:
#   print("edad incorrecta")
# salario_presi= int(input("introduce salario presidente:"))
# print("salario presidente: "+ str(salario_presi))

# salario_director= int(input("introduce salario director:"))
# print("salario director: "+ str(salario_director))

# salario_jefe_area= int(input("introduce salario jefe area:"))
# print("salario jefe area: "+ str(salario_jefe_area))

# salario_administrativo= int(input("introduce salario adfministrativo:"))
# print("salario administrativo: "+ str(salario_administrativo))

# if salario_administrativo<salario_jefe_area<salario_director<salario_presi:
#  print("todo va bien")
# else:
#   print("algo no va bien")
#

# print("progrma de becas año 2017")
# distancia_escuela= int(input("introduce la distancia a la escuela en km"))
# print("distancia a la escuela")

# numero_hermanos= int(input("introduce el nº de hermanos en el centro"))
# print(numero_hermanos)

# salario_familiar=int(input("introduce salario anual bruto"))
# print(salario_familiar)

# if distancia_escuela>40 and numero_hermanos>2 and salario_familiar <=20000:
#   print("tienes derecho a beca")
# else:
#   print("no tienes derecho a beca")

# for i in [1,2,3]:
#   print("hola")

# for i in ["primavera","verano","otoño"]:
#   print(i)

# i=1
# while i<=10:
#   print("tu perra madre" + str(i))
#  i = i+1

# print("se acab'o paco")

# edad = int(input("introduce la edad:"))

# while edad<0 and edad= stri:
#   print("Has introducido una edad negativa. vuelve a intentarlo")
#  edad =int(input("introduce tu edad porfavor:"))

# print("Gracias por colaborar pasa")
# print("Edad del aspirante" + str (edad) )
# --------------------------------------------------------------------------
# 17
# import math

# print("Programa de cáculo de raíz cuadrada")
# numero = int(input("introduce un número por favor:"))

# intentos = 0
# while numero < 0:
#   print("no se puede hallar la raíz de número negativo")
#   if intentos == 2:
#       print("has consumido demasiado intentos el programa ha finalziado")
#       break
#
#   numero = int(input("introduce un número por favor: "))
#   if numero<0:
#       intentos=intentos+1

# if intentos<2:
#   solucion= math.sqrt(numero)
#   print("la raiz cuadrada de " + str(numero)+ " es " + str(solucion))
# -----------------------------------------------------------------------------------------
# 18


# for letra in "python":
#   if letra == "h":
#      continue
# print("viendo la letra " + letra)

# nombre = "pildoras informaticas"

# contador = 0

# for i in nombre:
#   if i ==" ":
#      continue
# contador +=1

# print(contador)

# email = input("introduce tu email, por favor: ")
# for i in email:
#   if i =="@":
#      arroba = True
#     break

# else:
#    arroba = False

# print(arroba)

# ---------------------------------------------------------------------------------
# 19

# def generaPares (limite):
#   num = 1
#  miLista=[]

# while num<limite:
#    miLista.append(num*2)
#   num = num+1
# return miLista
# print(generaPares(10))

# def generaPares(limite):
#   num=1
#  while num < limite:
#  yield num*2
# num = num + 1


# devuelvePares= generaPares(10)

# for i in devuelvePares:
#   print(i)

# def generaPares(limite):
#   num=1
#  while num < limite:
#  yield num*2
# num = num + 1


# devuelvePares= generaPares(10)

# print(next(devuelvePares))
# print("Aquí podría ir más código...")
# print(next(devuelvePares))
# print("Aquí podría ir más código...")
# print(next(devuelvePares))

# ---------------------------------------------------------------------------------
# 20

# def duelvel_ciudades (*ciudades):
#   for elemento in ciudades:
#      yield elemento


# ciudades_devueltas = duelvel_ciudades("Madrid", "Barcelona", "Valenicia", "Malaga")

# print(next(ciudades_devueltas))

# print(next(ciudades_devueltas))

# def devuelve_ciudad(*ciudades):
#   for elemento in ciudades:
#      ##for Subelemento in elemento: For anidado
#         yield from elemento

# ciudades_devueltas= devuelve_ciudad(("madrid","barcelona","malaga"))

# print(next(ciudades_devueltas))

# print(next(ciudades_devueltas))

# print(ele)
# ---------------------------------------------------------------------------------
# 21

# def suma(num1, num2):
# return num1 + num2


# def resta(num1, num2):
#   return num1 - num2


# def multiplica(num1, num2):
#   return num1 * num2


# def divide(num1, num2):
#   try:
#       return num1 / num2
#   except ZeroDivisionError:
#      print("no se puede dividir entre 0")
#       return "operación erronea"

# try:
#   op1 = (int(input("Introduce el primer número: ")))
# except ValueError:
#   print("no introduzca un dato no numérico")
#   print("operación erronea")

# op2 = (int(input("Introduce el segundo número: ")))


# operacion = input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

# if operacion == "suma":
#   print(suma(op1, op2))

# elif operacion == "resta":
#   print(resta(op1, op2))

# elif operacion == "multiplica":
#   print(multiplica(op1, op2))

# elif operacion == "divide":
#   print(divide(op1, op2))

# else:
#   print("Operación no contemplada")

# print("Operación ejecutada. Continuación de ejecúción del programa ")

# ---------------------------------------------------------------------------------
# 22

# def suma(num1, num2):
#   return num1 + num2


# def resta(num1, num2):
#   return num1 - num2


# def multiplica(num1, num2):
#   return num1 * num2


# def divide(num1, num2):
#   return num1 / num2
# while True:

#   try:

#       op1 = (int(input("Introduce el primer número: ")))

#       op2 = (int(input("Introduce el segundo número: ")))
#       break
#   except ValueError:
#      print("Los Valores introducidos no son correctos")

# operacion = input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

# if operacion == "suma":
#   print(suma(op1, op2))

# elif operacion == "resta":
#   print(resta(op1, op2))

# elif operacion == "multiplica":
#   print(multiplica(op1, op2))

# elif operacion == "divide":
#   print(divide(op1, op2))

# else:
#   print("Operación no contemplada")

# print("Operación ejecutada. Continuación de ejecúción del programa ")


# def divide():

#   try:

#      op1=(float(input("introduce el primer número:")))
#     op2=(float(input("introduce un segundo número")))

#    print(("la división es:" + str(op1/op2)))
# except ValueError:
#   print("El valor introducido es erróneo")
# except ZeroDivisionError:
#   print("No se puede dividir entre cero")

# print("Cálculo finalizado")

# divide()
# ---------------------------------------------------------------------------------
# 23

# def evaluaEdad(edad):
#   if edad<0:
#      raise TypeError("no se permiten edades negativas ")
# if edad<20:
#  return "eres muy joven"
# elif edad<40:
#   return "Eres joven"
# elif edad <65:
#   return "eres maduro"
# elif edad <100:
#   return "cu'idate..."

# print(evaluaEdad(-15))

# ---------------------------------------------------------------------------------
# 26

# class Coche():
#       largoChasis=250
#      anchoChasis=120
#     ruedas=4
#    enmarcha=False

#   def arrancar(self):
#         self.enmarcha=True

# def estado(self):
#        if (self.enmarcha):
#               return "el coche está en marcha"
#      else:
#             return "el coche está parado"


# micoche=Coche()

# print("El largo del coche es: " ,micoche.largoChasis)
# print("El coche tienes: ", micoche.ruedas, "ruedas")
# micoche.arrancar()

# print(micoche.estado())

# ---------------------------------------------------------------------------------
# 27

# class Coche():

# def __init__(self):
# self._ruedas = 4
# self.largoChasis=250
# self.anchoChasis=120
# self.enmarcha=False

# def arrancar(self,arrancamos):
# self.enmarcha=arrancamos
# if(self.enmarcha):
# return "el coche está en marcha"
# else:
# return "el coche está parado"

#       def estado(self):
#              print("El coche tiene ", self._ruedas, "ruedas. un ancho de ", self.anchoChasis, " y un largo de ", self.largoChasis)


# micoche=Coche()

# print("El largo del coche es: " ,micoche.largoChasis)
# print("El coche tienes: ", micoche._ruedas, "ruedas")
# print(micoche.arrancar(True))

# micoche.estado()

# print("-----------a continuación creamos el segundo objeto--------------")

# micoche2=Coche()
# print("El largo del coche es: " ,micoche2.largoChasis)
# print("El coche tienes ", micoche2._ruedas, "ruedas")
# print(micoche2.arrancar(False))
# micoche2.__ruedas=2
# micoche2.estado()

# ---------------------------------------------------------------------------------
# 28
'''
class Coche():

    def __init__(self):
        self._ruedas = 4
        self.largoChasis = 250
        self.anchoChasis = 120
        self.enmarcha = False

    def arrancar(self, arrancamos):
        self.enmarcha = arrancamos

        if (self.enmarcha):
            chequeo = self.__chequeo_interno()
        if (self.enmarcha and chequeo == True):
            return "el coche está en marcha"

        elif (self.enmarcha and chequeo == False):
            return "algo no ha ido bien"
        else:
            return "el coche está parado"

    def estado(self):
        print("El coche tiene ", self._ruedas, "ruedas. un ancho de ", self.anchoChasis, " y un largo de ",
              self.largoChasis)

    def __chequeo_interno(self):
        print("realizando chequeo interno")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        else:
            return False


micoche = Coche()

print("El largo del coche es: ", micoche.largoChasis)
print("El coche tienes: ", micoche._ruedas, "ruedas")
print(micoche.arrancar(True))

micoche.estado()



print("-----------a continuación creamos el segundo objeto--------------")

micoche2 = Coche()
print("El largo del coche es: ", micoche2.largoChasis)
print("El coche tienes ", micoche2._ruedas, "ruedas")
print(micoche2.arrancar(False))

micoche2.estado()
'''
# ---------------------------------------------------------------------------------
# 28-36 herencia
'''
class persona():

    def __init__(self, nombre, apellido, edad):

            self.nombre= nombre
            self.apellido= apellido
            self.edad= edad

    def getDatosPersonales(self):

        return "Nombre: " + self.nombre + " Apellido: " + self.apellido + " Edad: " + str(self.edad)

    def habla(self):

        return  "Estoy hablando"

    def piensa(self):

        return  "Estoy pensando"

    def camina(self):

        return  "Estoy caminando"

    def come(self):

        return  "Estoy comeindo"

class Estudiante(persona):
    def estudiar(self):
        return "Estoy estudiando"


persona1=persona("Ana","Gomez",35)

estudiante1=Estudiante("pedro", "josé", 45)

print(persona1.getDatosPersonales())
print(estudiante1.getDatosPersonales())
'''

# ---------------------------------------------------------------------------------
# 37
'''
class persona():

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def getDatosPersonales(self):
        return "Nombre: " + self.nombre + " Apellido: " + self.apellido + " Edad: " + str(self.edad)

    def habla(self):
        return "Estoy hablando"

    def piensa(self):
        return "Estoy pensando"

    def camina(self):
        return "Estoy caminando"

    def come(self):
        return "Estoy comeindo"


class Estudiante(persona):

    def __init__(self, nombre, apellido, edad, escuela):
        self.escuela = escuela
        super().__init__(nombre, apellido, edad)


    def getDatosPersonales(self):
        return super().getDatosPersonales()+" Escuela " + self.escuela
        #return "Nombre: " + self.nombre + " Apellido: " + self.apellido + " Edad: " + str(self.edad) + " Escuela " + self.escuela

    def estudiar(self):
        return "Estoy estudiando"


persona1 = persona("Ana", "Gomez", 35)

estudiante2 = Estudiante("pedro","jose",45,"pedro")


print(persona1.getDatosPersonales())
print(estudiante2.getDatosPersonales())

'''

# ---------------------------------------------------------------------------------
# Ejercicio
'''
class CuentaCorriente():

    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def ingresar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        self.saldo -= cantidad

    def getDatos(self):
        return "Numero: " + str(self.numero) + " Titular: " + self.titular + " Saldo: " + str(self.saldo)




class CuentaJoven(CuentaCorriente):

    def __init__(self, numero, titular, saldo, bonus_promocion=0):
        super().__init__(numero, titular, saldo)
        self.bonus_promocion = bonus_promocion
        self.saldo += bonus_promocion

    def getBonus(self):
        return self.bonus_promocion

    def getDatos(self):
       return super().getDatos() + " Bonus " + str(self.bonus_promocion)

    def Ingresar(self, cantidad):
        super().ingresar(cantidad)

    def retirar(self, cantidad):

        super().retirar(cantidad)


c1 = CuentaJoven(500, "María", 37000, 15000)

c1.ingresar(5000)
c1.retirar(350)

print(c1.getDatos())
'''
# ---------------------------------------------------------------------------------
# 38-39
'''
class persona():

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def getDatosPersonales(self):
        return "Nombre: " + self.nombre + " Apellido: " + self.apellido + " Edad: " + str(self.edad)

    def habla(self):
        return "Estoy hablando"

    def piensa(self):
        return "Estoy pensando"

    def camina(self):
        return "Estoy caminando"

    def come(self):
        return "Estoy comeindo"


class Estudiante(persona):

    def __init__(self, nombre, apellido, edad, escuela):
        self.escuela = escuela
        persona.__init__(self,nombre, apellido, edad)


    def getDatosPersonales(self):
        return super().getDatosPersonales()+" Escuela " + self.escuela
        #return "Nombre: " + self.nombre + " Apellido: " + self.apellido + " Edad: " + str(self.edad) + " Escuela " + self.escuela

    def estudiar(self):
        return "Estoy estudiando"

class Trabajador(persona):


    def __init__(self, nombre, apellido, edad, empresa):
        self.empresa = empresa
        persona.__init__(self,nombre, apellido, edad)


    def getDatosPersonales(self):
        return super().getDatosPersonales()+" Empresa " + self.empresa
        #return "Nombre: " + self.nombre + " Apellido: " + self.apellido + " Edad: " + str(self.edad) + " Escuela " + self.escuela

    def trabaja(self):
        return "Estoy trabajando"

class Director(Trabajador,Estudiante):

    def __init__(self, nombre, apellido, edad, empresa, escuela, bonus):
        Trabajador.__init__(self,nombre, apellido, edad, empresa)
        Estudiante.__init__(self,nombre, apellido, edad, escuela)

        self.bonus= bonus

    def getDatosPersonales(self):
        return super().getDatosPersonales()+ " Bonus " + str(self.bonus)

    def dirige(self):

        return "Estoy dirigiendo"



persona1 = persona("Ana", "Gomez", 35)

estudiante2 = Estudiante("pedro","jose",45,"pedro")


print(persona1.getDatosPersonales())
print(estudiante2.getDatosPersonales())
print("-----------------------------------")

trabajador1=Trabajador("Antonio", "López", 55, "c cope")
print(trabajador1.getDatosPersonales())

director1= Director("juan M", "díaz",45,"palermo","san juan",1500)
print(director1.getDatosPersonales())

'''

# ---------------------------------------------------------------------------------
#40 ejercicio

class Transporte():

    def __init__(self,Color,Ruedas,Ancho,Alto,Asientos,encendido):
        self.Color=Color
        self.Ruedas=Ruedas
        self.Ancho=Ancho
        self.Alto=Alto
        self.Asientos=Asientos
        self.encendido = encendido

    def encendido(self):
        if (self.encendido == 1):
            print("el coche está encendido")
        else:
            print("el coche está apagado")

    def Acelerar(self):
        return self.Acelerar() + print("el coche está arrancado")

    def Frenar(self):
        return self.Frenar() + print ("el vehículo está frenando")

    def Girar(self):
        return self.Girar() + print ("el vehículo está girando")

    def Derrapar(self):
        return self.Derrapar() + print ("el vehículo está derrapando")

    def MarchaAtras(self):

        return self.MarchaAtras() + print ("el vehículo está funcionandop Marcha Atras")




class Motor(Transporte):
    def __init__(self,Color,Ruedas,Ancho,Alto,Asientos,Carga,Cilindrada,Marchas,AireAcondicionado,encendido):
        Transporte.__init__(self,Color,Ruedas,Ancho,Alto,Asientos,encendido)
        self.carga=Carga
        self.Cilindrada=Cilindrada
        self.Marcha=Marchas
        self.Aire=AireAcondicionado
        self.encendido=encendido


    def encendido(self):
        if (self.encendido==1):
             print("el coche está encendido")
        else:
            print("el coche está apagado")


    def Acelerar(self):
       return Transporte.Acelerar(self)

    def Frenar(self):
        return Transporte.Frenar(self)

    def Girar(self):
       return Transporte.Girar(self)

    def Derrapar(self):
       return Transporte.Derrapar(self)

    def MarchaAtras(self):
       return Transporte.MarchaAtras(self)

    def Arrancar(self):
       return Motor.Arrancar(self) + print("el vehículo está arrancado")




class vehiculo(Motor):
    def __init__(self,Color,Ruedas,Ancho,Alto,Asientos,Carga,Cilindrada,Marchas,AireAcondicionado,encendido):
        Motor.__init__(self,Color,Ruedas,Ancho,Alto,Asientos,Carga,Cilindrada,Marchas,AireAcondicionado,encendido)

    def Acelerar(self):
       return Motor.Acelerar(self)

    def Frenar(self):
        return Motor.Frenar(self)

    def Girar(self):
       return Motor.Girar(self)

    def Derrapar(self):
       return Motor.Derrapar(self)

    def MarchaAtras(self):
       return Motor.MarchaAtras(self)

    def Arrancar(self):
       return Motor.Arrancar(self)

  #  def Datos(self):
   #     return self.Color + self.Ruedas + self.Ancho + self.Alto + self.




Transporte1=Transporte("rojo",str(4),str(20),str(220),str(4),1)

print(Transporte1)