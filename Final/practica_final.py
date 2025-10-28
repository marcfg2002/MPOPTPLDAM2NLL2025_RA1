import csv #per llegir i escriure arxius csv
import datetime #per treballar amb dates i hores

RUTA_BASE = 'ra1/final/data/' #constant amb la ruta base dels arxius de dades

#classe per representar una venda de ticket
class Venta:
    id_actual = 1 #variable de classe per anar donant ids unics
    #el constructor de la classe
    def __init__(self, cliente, email, fecha_registro, evento, fecha_evento, precio, categoria, fecha_venta):
        self.id = Venta.id_actual #assignem l'id
        Venta.id_actual += 1 #incrementem el comptador d'ids per la seguent venda
        self.cliente = cliente
        self.email = email
        self.fecha_registro = self.parse_fecha(fecha_registro) 
        self.evento = evento
        self.fecha_evento = self.parse_fecha(fecha_evento)
        self.precio = float(precio) #el preu el guardem com a float
        self.categoria = categoria
        self.fecha_venta = self.parse_fecha(fecha_venta)

    #funcio per convertir un string de data a objecte date
    def parse_fecha(self, fecha_str):
        try:
            #intentem fer la conversio amb el format any-mes-dia
            return datetime.datetime.strptime(fecha_str, "%Y-%m-%d").date()
        except:
            #si falla retornem none
            return None

    #calcula quants dies falten per a l'event
    def dias_hasta_evento(self):
        if self.fecha_evento:
            hoy = datetime.date.today() #agafem la data d'avui
            return (self.fecha_evento - hoy).days #la resta de dates dona un timedelata, agafem els dies
        return None

    #calcula quants dies fa que el client es va registrar
    def antiguedad_cliente_dias(self):
        if self.fecha_registro:
            hoy = datetime.date.today()
            return (hoy - self.fecha_registro).days
        return 0 #si no hi ha data de registre, diem 0 dies

    def __str__(self):
        return f"[{self.id}] {self.cliente} compro {self.evento} ({self.precio}€)"


#funcio per cargar totes les dades dels tres arxius csv
def cargar_datos(clientes_file, eventos_file, ventas_file):
    clientes = {} #diccionari per clients
    eventos = {} #diccionari per events
    registros_ventas = [] #llista per guardar els objectes venta

    #bloc per cargar clients
    try:
        with open(clientes_file, 'r', encoding='utf-8') as archivo_clientes:
            lector = csv.reader(archivo_clientes, delimiter=';')
            next(lector, None) #saltem la capcalera
            for fila in lector:
                if len(fila) < 4:
                    continue #saltem files incompletes, per si de cas
                id_cliente, nombre_cliente, email_cliente, fecha_registro = fila
                clientes[int(id_cliente)] = (nombre_cliente, email_cliente, fecha_registro) #guardem al diccionari
    except:
        print("No es va poder obrir clients") #error si no es troba o s'obra malament
        return [], {}

    #bloc per cargar events
    try:
        with open(eventos_file, 'r', encoding='utf-8') as archivo_eventos:
            lector = csv.reader(archivo_eventos, delimiter=';')
            next(lector, None) #saltem la capcalera
            for fila in lector:
                if len(fila) < 5:
                    continue
                id_evento, nombre_evento, fecha_evento, precio_evento, categoria = fila
                eventos[id_evento] = (nombre_evento, fecha_evento, precio_evento, categoria) #guardem al diccionari
    except:
        print("No es va poder obrir events")
        return [], {}

    #bloc per cargar vendes
    try:
        with open(ventas_file, 'r', encoding='utf-8') as archivo_ventas:
            lector = csv.reader(archivo_ventas, delimiter=';')
            next(lector, None) #saltem la capcalera
            for fila in lector:
                if len(fila) < 4:
                    continue
                _, id_cliente, id_evento, fecha_venta = fila
                #busquem les dades del client, si no el trobem, posem valors per defecte, en aquest cas, desconegut
                datos_cliente = clientes.get(int(id_cliente), ("desconegut", "", ""))
                #busquem les dades de l'event, si no el trobem, posem valors per defecte
                datos_evento = eventos.get(id_evento, ("desconegut", "", "0", ""))
                #creem l'objecte venta ajuntant totes les dades
                registro = Venta(
                    datos_cliente[0], datos_cliente[1], datos_cliente[2], #dades client
                    datos_evento[0], datos_evento[1], datos_evento[2], datos_evento[3], #dades event
                    fecha_venta #data de la venta
                )
                registros_ventas.append(registro) #guardem l'objecte
    except:
        print("No es va poder obrir vendes")
        return [], {}

    print("dades carregades:", len(registros_ventas))
    return registros_ventas, clientes #retornem la llista de vendes i el diccionari de clients


#funcio per mostrar totes les vendes cargades
def listar_ventas(registros_ventas):
    if not registros_ventas:
        print("no hi ha dades")
        return
    for venta in registros_ventas:
        print(venta)


#funcio per afegir un nou client al csv i al diccionari
def alta_cliente(file_clientes, clientes_dict):
    #mirem si el nom que volen ja existeix
    nombres_existentes = set([nombre for _, (nombre, _, _) in clientes_dict.items()])
    nombre_nuevo = input("nom: ").strip()
    if nombre_nuevo in nombres_existentes:
        print("el client ja existeix")
        return
    email_nuevo = ""
    #validem que l'email tingui un arroba i un punt
    while "@" not in email_nuevo or "." not in email_nuevo:
        email_nuevo = input("email: ").strip()
        if "@" not in email_nuevo or "." not in email_nuevo:
            print("email malament, ha de tenir @ i .")

    fecha_registro_valida = None
    #validem el format de la data de registre
    while fecha_registro_valida is None:
        fecha_input = input("data registre yyyy-mm-dd: ").strip()
        try:
            #intentem convertirla
            fecha_registro_valida = datetime.datetime.strptime(fecha_input, "%Y-%m-%d").date()
        except:
            print("format malament")
            
    #calculem el nou id, agafant el mes gran que ja tenim i sumant 1
    nuevo_id = max(clientes_dict.keys()) + 1 if clientes_dict else 1
    
    #afegim al csv
    try:
        #obrim en mode añadir (a) per afegir al final
        with open(file_clientes, 'a', encoding='utf-8', newline='') as archivo:
            escritor = csv.writer(archivo, delimiter=';')
            escritor.writerow([nuevo_id, nombre_nuevo, email_nuevo, fecha_input])
        #afegim al diccionari en memoria per tenir-ho actualitzat
        clientes_dict[nuevo_id] = (nombre_nuevo, email_nuevo, fecha_input)
        print("client afegit amb id:", nuevo_id)
    except:
        print("no es va poder guardar al fitxer")


#funcio per buscar vendes dins d'un rang de dates
def filtrar_ventas_por_rango(registros_ventas):
    fecha_inicio = None
    #demanem i validem la data d'inici
    while fecha_inicio is None:
        fecha_input = input("data inici yyyy-mm-dd: ").strip()
        try:
            fecha_inicio = datetime.datetime.strptime(fecha_input, "%Y-%m-%d").date()
        except:
            print("malament")
            
    fecha_fin = None
    #demanem i validem la data final
    while fecha_fin is None:
        fecha_input = input("data fi yyyy-mm-dd: ").strip()
        try:
            fecha_fin = datetime.datetime.strptime(fecha_input, "%Y-%m-%d").date()
        except:
            print("malament")
            
    #comprovem que el rang sigui correcte
    if fecha_fin < fecha_inicio:
        print("la data fi es anterior a la d'inici, es impossible")
        return
    
    contador = 0
    #recorrem les vendes i mirem si la seva data de venda esta dins del rang
    for venta in registros_ventas:
        if venta.fecha_venta and fecha_inicio <= venta.fecha_venta <= fecha_fin:
            print(venta)
            contador += 1
            
    if contador == 0:
        print("no hi ha res en aquest rang")


#funcio per calcular i mostrar algunes estadistiques
def estadisticas(registros_ventas):
    if not registros_ventas:
        print("no hi ha dades")
        return
        
    ingresos_totales = 0
    ingresos_por_evento = {} #diccionari per anar sumant ingressos per event
    categorias_existentes = set() #set per trobar categories uniques
    dias_minimos = 9999 #un numero molt gran per trobar el minim
    evento_proximo = "cap"
    precios_ventas = [] #llista per calcular min, max i mitjana de preus
    
    for venta in registros_ventas:
        ingresos_totales += venta.precio
        ingresos_por_evento[venta.evento] = ingresos_por_evento.get(venta.evento, 0) + venta.precio
        categorias_existentes.add(venta.categoria)
        
        dias = venta.dias_hasta_evento() #mirem quants dies falten
        #si falten dies (es positiu o zero) i es menys que el que tenim fins ara
        if dias is not None and dias >= 0 and dias < dias_minimos:
            dias_minimos = dias
            evento_proximo = venta.evento
            
        precios_ventas.append(venta.precio)
        
    print("ingressos totals:", ingresos_totales)
    print("ingressos per event:")
    for evento, total in ingresos_por_evento.items():
        print(evento, ":", total)
    print("categories uniques:", categorias_existentes)
    print("event mes proxim:", evento_proximo, "en", dias_minimos, "dies")
    
    if precios_ventas:
        #calculem i mostrem les dades de preus
        mitjana = sum(precios_ventas)/len(precios_ventas)
        print("preus min,max,mitjana:", min(precios_ventas), max(precios_ventas), mitjana)


#funcio per exportar un informe resumit d'ingressos per event a un csv
def exportar_informe(registros_ventas, ruta_informe):
    ingresos_por_evento = {}
    #calculem els ingressos per event
    for venta in registros_ventas:
        ingresos_por_evento[venta.evento] = ingresos_por_evento.get(venta.evento, 0) + venta.precio
        
    if not ingresos_por_evento:
        print("no hi ha res per exportar")
        return
        
    try:
        #obrim l'arxiu per escriure (w)
        with open(ruta_informe, 'w', encoding='utf-8', newline='') as archivo:
            escritor = csv.writer(archivo, delimiter=';')
            escritor.writerow(['event', 'ingressos']) # capcalera
            for evento, total in ingresos_por_evento.items():
                escritor.writerow([evento, f"{total:.2f}"])
        print("informe guardat")
    except:
        print("no es va poder guardar")


#funcio principal del programa
def main():
    #definim les rutes completes dels arxius
    clientes_file = RUTA_BASE + 'clientes.csv'
    eventos_file = RUTA_BASE + 'eventos.csv'
    ventas_file = RUTA_BASE + 'ventas.csv'
    informe_file = RUTA_BASE + 'informe_resumen.csv'

    #carreguem les dades inicials
    registros_ventas, clientes_dict = cargar_datos(clientes_file, eventos_file, ventas_file)
    if not registros_ventas:
        print("no es va poder carregar dades, sortint...")
        return #si no tenim vendes, sortim

    #bucle infinit del menu
    while True:
        print("1. llistar vendes")
        print("2. alta client")
        print("3. filtrar vendes per data")
        print("4. estadistiques")
        print("5. exportar informe")
        print("6. sortir")
        opcion = input("opcio: ").strip()
        
        #mirem quina opcio ha triat
        if opcion == "1":
            listar_ventas(registros_ventas)
        elif opcion == "2":
            alta_cliente(clientes_file, clientes_dict)
        elif opcion == "3":
            filtrar_ventas_por_rango(registros_ventas)
        elif opcion == "4":
            estadisticas(registros_ventas)
        elif opcion == "5":
            exportar_informe(registros_ventas, informe_file)
        elif opcion == "6":
            print("adeu")
            break #sortim del bucle
        else:
            print("opcio malament")
            
        input("enter per continuar") #pausem per que l'usuari pugui llegir el missatge

#codi que s'executa quan arranca el programa
if __name__ == "__main__":
    main() #cridem la funcio principal