import json #per poder treballar amb arxius json

#funcio per cargar les hores dels treballadors des d'un json
def cargar_horarios_json(nombre_archivo):
    horarios = {} #diccionari buit per guardar les hores
    try:
        #obrim l'arxiu en mode lectura
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            datos = json.load(f) #carguem tot el contingut del json a la variable datos
            #iterem sobre cada diccionari dins de la llista datos i agafem les dades
            for persona in datos:
                nombre = persona['Nombre']
                entrada = persona['Entrada']
                salida = persona['Salida']
                horarios[nombre] = (entrada, salida)
    #si l'arxiu no existeix saltem aqui
    except FileNotFoundError:
        print(f"Error: No es va trobar l'arxiu {nombre_archivo}")
    #si el json esta malament saltem aqui
    except json.JSONDecodeError:
        print(f"Error: l'arxiu {nombre_archivo} no te un format JSON valid.")
    return horarios #retornem el diccionari amb les dades cargades


#funcio per validar si una hora es correcta i la convertim a minuts totals
def validar_hora(hora_str):
    try:
        #mirem si l'hora te el format hh:mm
        if ":" in hora_str:
            #separem hores i minuts
            horas, minutos = hora_str.split(":")
            #convertim a int
            horas, minutos = int(horas), int(minutos)
        else:
            #si nomes hi ha un numero, assumim que son hores i els minuts son zero
            horas, minutos = int(hora_str), 0

        #comprovem que hores estigui entre 0-23 i minuts entre 0-59
        if 0 <= horas <= 23 and 0 <= minutos < 60:
            return horas * 60 + minutos #retornem els minuts totals
        else:
            return None #si no es valida, retornem none
    #si el text que ens passen no es pot convertir a int
    except ValueError:
        return None


#funcio per mostrar tots els registres carregats
def mostrar_registros(horarios):
    #iterem amb enumerate per tenir un index
    for i, (nombre, (entrada, salida)) in enumerate(horarios.items(), start=0):
        #mostrem l'index, nom, entrada i sortida
        print(f"{i}. {nombre}: entra a les {entrada} i surt a les {salida}")
    print()


#funcio per demanar una hora i dir quantes persones ja han arribat
def contar_entradas(horarios):
    hora_input = input("Introdueix una hora (ex: 9 o 08:30): ").strip() #demanem l'hora
    hora_usuario = validar_hora(hora_input) #la convertim a minuts

    #si validar_hora ens ha tornat none es que l'hora esta malament
    if hora_usuario is None:
        print("Error: hora no valida.\n")
        return

    contador = 0 
    #iterem nomes pels valors del diccionari
    for entrada, _ in horarios.values():
        entrada_minutos = validar_hora(entrada) #convertim l'hora d'entrada a minuts
        #mirem si es valida
        if entrada_minutos is not None and entrada_minutos <= hora_usuario:
            contador += 1 #sumem al comptador

    #mostrem el resultat
    print(f"A aquesta hora, {contador} persones ja han arribat.\n")


#funcio principal amb el menu
def menu(horarios):
    while True: 
        print("========== MENU ==========")
        print("1) Mostrar registres")
        print("2) Comptar entrades")
        print("3) Sortir")
        opcion = input("Tria una opcio (1-3): ").strip() #demanem l'opcio

        if opcion == '1':
            mostrar_registros(horarios) #cridem a mostrar
        elif opcion == '2':
            contar_entradas(horarios) #cridem a comptar
        elif opcion == '3':
            print("Fins aviat!")
            break #trenquem el bucle per sortir del programa
        else:
            print("Opcio no valida. Intenta de nou.\n") #si no tria 1, 2 o 3


#codi que s'executa quan el script arranca
if __name__ == '__main__':
    #intentem carregar les dades de l'arxiu
    horarios = cargar_horarios_json('ra1/practica2/horarios.json')
    #si el diccionari te dades, mostrem el menu
    if horarios:
        menu(horarios)