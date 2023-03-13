#calculadora de masa corporal
#ingresa nombre, apellidos y edad
nombre=str(input("ingresa tu nombre:"))
apellido_paterno=str(input("ingresa tu apellido paterno:"))
apellido_materno=str(input("ingresa tu apellido materno:"))
edad=int(input("ingresa tu edad en años:"))
#ingresa la altura y peso
altura=float(input("ingresa tu estatura en Metros:"))
peso= float(input("ingresa tu peso en kg:"))
#calculo de indice de masa corporal
IMC=peso/altura**2
#la Terminal arrojara nombre completo y edad
print("hola",nombre+" "+apellido_paterno+" "+apellido_materno)
print("tu edad",edad)
# la terminal arrojara el calculo de IMC y un comparativo de en que situacion se encuentra
print("Tu indice de masa corporales:",IMC)
if IMC>=16 and IMC<17:
    print("Infra peso")
if IMC>=17 and IMC<18:
    print ('Bajo peso.')
if IMC>=18 and IMC<25:
    print ('Peso normal (saludable).')
if IMC>=5 and IMC<30:
    print ('Sobrepeso (obesidad de grado I).')
if IMC>=30 and IMC<35:
    print ('Sobrepeso cr\u00F3nico (obesidad de grado II).')
if IMC>=35 and IMC<40:
    print ('Obesidad prem\u00F3rbida (obesidad de grado III).')
if IMC>=40:
    print ('Obesidad m\u00F3rbida (obesidad de grado IV).')