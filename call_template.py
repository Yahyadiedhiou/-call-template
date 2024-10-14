import os

def escribir_script():
    entrada = input("Escribe algo: ")
    if entrada == "#call":
        with open("call_template.txt", "w", encoding="utf-8") as file:
            file.write("...\n")  # Escribe puntos o cualquier otro texto deseado
        print("Archivo 'call_template.txt' creado con el texto predefinido.")
    else:
        print("La entrada no es '#call'. No se ha creado ningún archivo.")

# Llamada a la función
escribir_script()
