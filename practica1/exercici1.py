#demanem quants treballadors hi ha i ho guardem
treballadors = input("¿Cuántos trabajadores? ")
#mirem si es un numero i si es positiu. si no ho es, el tornem a demanar
while not treballadors.isdigit() or int(treballadors) <= 0:
    print("Error: numero de treballadors invalid. Ha de ser un enter positiu.")
    treballadors = input("¿Cuántos trabajadores? ")

#convertim a enter
num_treballadors = int(treballadors)

#demanem l'hora de referencia
hora_referencia = input("Selecciona hora de referencia (0-23): ")
#mirem si es un numero i si esta entre 0 i 23
while not hora_referencia.isdigit() or not (0 <= int(hora_referencia) <= 23):
    print("Error: la hora ha de ser un numero entre 0 i 23.")
    hora_referencia = input("Selecciona hora de referencia (0-23): ")

#convertim a enter
hora_referencia = int(hora_referencia)

#inicialitzem variables per als resultats finals
contador_entradas = 0
salida_mas_temprana = 24 #posem 24 per que qualsevol hora sera mes petita
empleado_mas_temprano = ""

#bucle per demanar les dades de cada treballador
while num_treballadors > 0:
    #demanem el nom
    nombre_empleado = input("Nombre del empleado: ")

    #demanem l'hora d'entrada
    hora_entrada = input("Hora de entrada (0-23): ")
    #validem que sigui un numero entre 0 i 23
    while not hora_entrada.isdigit() or not (0 <= int(hora_entrada) <= 23):
        print("Error: la hora de entrada ha d'estar entre 0 i 23.")
        hora_entrada = input("Hora de entrada (0-23): ")
    hora_entrada = int(hora_entrada)

    #demanem l'hora de sortida
    hora_salida = input("Hora de salida (0-23): ")
    #validem que sigui un numero entre 0 i 23 i que sigui mes gran que l'hora d'entrada
    while (not hora_salida.isdigit() or 
            not (0 <= int(hora_salida) <= 23) or 
            int(hora_salida) <= hora_entrada):
        print("Error: la hora de sortida ha d'estar entre 0 i 23 i ser mes gran que la d'entrada.")
        hora_salida = input("Hora de salida (0-23): ")
    hora_salida = int(hora_salida)

    #comprovem si ha entrat a temps
    if hora_entrada <= hora_referencia:
        contador_entradas += 1

    #comprovem si la seva sortida es la mes temprana
    if hora_salida < salida_mas_temprana:
        salida_mas_temprana = hora_salida #actualitzem la hora minima
        empleado_mas_temprano = nombre_empleado #guardem el nom

    #restem un treballador per acabar el bucle
    num_treballadors -= 1
    print("Trabajadores restantes:", num_treballadors)

#mostrem els resultats
print("\n--- RESULTATS ---")
#primer el numero d'empleats que han entrat a temps
print("Numero d'empleats que van entrar abans o a la hora de referencia:", contador_entradas)

#si hem trobat algun que hagi sortit, mostrem qui i a quina hora
if empleado_mas_temprano != "":
    print("l'empleat que va sortir mes d'hora va ser", empleado_mas_temprano, 
          "a les", salida_mas_temprana, "hores.")
else:
    #si no hi ha dades
    print("No es va registrar cap sortida valida.")