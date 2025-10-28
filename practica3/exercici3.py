import csv #per treballar amb arxius CSV

#classe per representar cada registre d'horari
class RegistroHorario:
    def __init__(self, empleado, dia, entrada, salida):
        self.empleado = empleado
        self.dia = dia
        self.entrada = entrada
        self.salida = salida

    #funcio que retorna les hores treballades
    def duracion(self):
        return self.salida - self.entrada


#funcio per carregar les dades del CSV i crear els objectes
def cargar_registros(nombre_archivo):
    registros = [] #llista buida on guardarem tots els registres
    try:
        with open(nombre_archivo, newline='', encoding='utf-8') as f:
            lector = csv.reader(f, delimiter=';')
            next(lector, None)
            for fila in lector:
                nombre, dia, h_entrada, h_salida = fila
                entrada = int(h_entrada)
                salida = int(h_salida)
                registro = RegistroHorario(nombre, dia, entrada, salida)
                registros.append(registro)
        print(f"S'han carregat {len(registros)} registres correctament.\n")
    except FileNotFoundError:
        print(f"Error: no s'ha trobat l'arxiu {nombre_archivo}")
    return registros


#funcio per agrupar els empleats per dia en un diccionari
def empleados_por_dia(registros):
    empleados_dia = {}
    for r in registros:
        #si encara no hem creat cap conjunt per aquest dia, el creem ara.
        #aixo serveix per tenir una llista (sense repetir noms) dels empleats que han treballat aquell dia.
        if r.dia not in empleados_dia:
            empleados_dia[r.dia] = set() #afegim el nom de l'empleat al conjunt del dia corresponent.
        empleados_dia[r.dia].add(r.empleado)
    #mostrem resultats
    print("=== EMPLEATS PER DIA ===")
    for dia, empleados in empleados_dia.items():
        print(f"{dia}: {', '.join(empleados)}")
    print()
    return empleados_dia


#funcio per calcular hores totals per empleat
def resumen_horas(registros):
    hores_totals = {}
    for r in registros:
        if r.empleado not in hores_totals:
            hores_totals[r.empleado] = 0
        hores_totals[r.empleado] += r.duracion()
    return hores_totals


#funcio per guardar el resum al csv
def guardar_resumen(hores_totals):
    try:
        with open('ra1/practica3/resumen_horarios.csv', 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f, delimiter=';')
            escritor.writerow(['Empleado', 'Horas_totales'])
            for empleado, total in hores_totals.items():
                escritor.writerow([empleado, total])
        print("S'ha generat l'arxiu 'resumen_horarios.csv' correctament.\n")
    except Exception as e:
        print("Error al guardar l'arxiu:", e)


#funcio principal
def main():
    registros = cargar_registros('ra1/practica3/horarios.csv')
    if not registros:
        return

    empleados_dia = empleados_por_dia(registros)

    #empleats que van treballar dilluns i divendres
    if 'Lunes' in empleados_dia and 'Viernes' in empleados_dia:
        interseccion = empleados_dia['Lunes'] & empleados_dia['Viernes']
        print("Empleats que van treballar dilluns i divendres:")
        if interseccion:
            for e in interseccion:
                print("-", e)
        else:
            print("Cap empleat coincideix.")
        print()

    #empleats que van treballar dissabte pero no diumenge
    if 'Sábado' in empleados_dia and 'Domingo' in empleados_dia:
        diferencia = empleados_dia['Sábado'] - empleados_dia['Domingo']
        print("Empleats que van treballar dissabte però no diumenge:")
        if diferencia:
            for e in diferencia:
                print("-", e)
        else:
            print("Cap empleat compleix la condició.")
        print()

    #calculem hores totals i les guardem al csv
    hores_totals = resumen_horas(registros)
    guardar_resumen(hores_totals)

    print("--- Fi de la pràctica 3 ---")


#codi que s'executa quan arranca el programa
if __name__ == '__main__':
    main()