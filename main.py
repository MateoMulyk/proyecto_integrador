'''Este es un comentario
    de varias lineas de texto
'''
print("Cual es tu nombre?")
player = input() 
bienvenida = f"bienvenido {player}, vamos a empezar!"
print(bienvenida)
print("que edad tienes?")
edad = int(input())
print("tu edad es", edad) 
while True:
    print("Eres soltero? s/n")

    estado_civil = input()
    if estado_civil == "s":
        print("Vea pues, veo que eres soltero.")
        break
    elif estado_civil == "n": 
        print("Vea pues, veo que estas casado.")
        break     
    else:
        print("esa no es una respuesta valida")    
        
 #Hasta aca todo funcionan
print("En que nivel de dificultad quieres jugar?")
dificultad = input()

while dificultad == "Alta" and edad < 30:
    print("Estas seguro?")
    verificacion = input()
    if verificacion == "no":
       print("Bueno, entonces cambia la dificultad") 
       dificultad = input()
    elif verificacion == "si":
       print("Bueno vamos a continuar entoces") 
       break     
    else:
        print("Error, Esa no es una respuesta valida")

#print(list(range(edad+1,-1,-1)))
print("tu partida empieza en...")
for i in range(edad+1,-1,-1):
    
    print(i)