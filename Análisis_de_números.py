"""
Ejercicio 3. Análisis de números. Pide números al usuario
Muestra mayor, menor, promedio, cantidad de pares, cantidad de impares
funciones para cada cálculo
"""

def pedir_numero(mensaje, lista):
    while True:
        try:
            numero = float(input(mensaje))
            if numero in lista:
                print("\nEl número ya está en la lista.")
                continue
            else:
                lista.append(numero)
                return numero
        except ValueError:
            print("\nSolo números.")
            
def mayor_numero(lista):
    mayor = float('-inf')
    for numero in lista:
        if numero > mayor:
            mayor = numero
    return mayor
    
def menor_numero (lista):
    menor = float('inf')
    for numero in lista:
    	if numero < menor:
         menor = numero
    return menor

def promedio(lista):
	promedio = (sum(lista))/len(lista)
	return promedio

def cantidad_de_pares(lista):
    contador = 0
    for numero in lista:
    	if numero % 2 == 0:
            contador += 1
    return contador

def cantidad_de_impares(lista):
	contador = 0
	for numero in lista:
		if numero %2 != 0:
			contador += 1
			return contador

def escoger_opcion(mensaje, opciones):
	while True :
		try:
			opcion = int(input(mensaje))
			if opcion in opciones:
				print("\nFuera de rango.")
				continue
			return opcion
		except ValueError:
			print("\nSolo números.")

def menu():
	print("\n___MENU___")
	print ("1. Añadir número.")
	print("2. Listar números.")
	print("3. Determinar número mayor.")
	print("4. Determinar número menor.")
	print ("5. Determinar promedio.")
	print("6. Cantidad de pares.")
	print("7. Cantidad de impares.")
	print ("8. Salir.")

def jugar(lista):
	while True:
		print("\nJuego sobre números en una lista.")
		menu()
		opcion = escoger_opcion("\nEscoja una opción: ", [1,2,3,4,5,6,7,8])
		if opcion== 1:
			numero = pedir_numero("\nIntroduzca un número: ", lista)
			print (f"\nHa introducido el número {numero} satisfactoriamente.")
		elif opcion == 2:
			if not lista:
				print("\nAún no hay ningún elemento en la lista.")
			else:
				print("\nLa lista está compuesta por los siguientes números ordenados de menor a mayor: ")
				ordenados = sorted(lista)
				for i, número in enumerate (ordenados, start = 1):
					print(f"{i}. {número}")
		elif opcion == 3:
					mayor = mayor_numero(lista)
					print(f"\nEl mayor número de la lista es {mayor}.")
		elif opcion == 4:
					menor = menor_numero(lista)
					print(f"\nEl menor número de la lista es {menor}.")
		elif opcion == 5:
					media = promedio (lista) 
					print(f"\nEl promedio de la lista es {media:.2f}.")
					
		elif opcion == 6:
					pares = cantidad_de_pares(lista)
					print(f"\nHay {pares} elementos pares.")
		elif opcion == 7:
					contador = cantidad_de_impares(lista)
					print(f"\nHay {contador} elementos impares.")
		else:
			return

def main():
	lista = []
	jugar(lista)
	print("\nHa salido satisfactoriamente del programa\n")
	
if __name__ == "__main__":
	main()

				
				