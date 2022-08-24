from datetime import datetime
import csv

def pedir_nombre():
    name = input("Elija un archivo csv: ")
    contenido = openFile(name)
    return contenido

def openFile(name):
    path = name + ".csv"
    with open(path, "r") as file:
        contenido = list()
        reader = csv.DictReader(file)
        for i in reader:
            contenido.append(i)
    return contenido

def createFile(name):
    path = name + ".csv"
    with open(path, "w", newline='') as file:
        encabezado = ['NroCheque','CodBanco','CodSucursal','NroCuentaOrigen','NroCuentaDestino','Valor','FechaOrigen','FechaPago','DNI','Estado','Tipo']
        writer = csv.DictWriter(file, fieldnames = encabezado)
        writer.writeheader()
        for row in arrayFiltrada:
            writer.writerow(row)
        file.close()

def filtro(array, clave, valor):
    resultado = list()
    if not valor:
        return array
        
    for i in array:
        if i[clave] == valor:
            resultado.append(i)
    if not resultado:
        print('No se encontro datos en el archivo')
    return resultado

def filtrarFecha(eleccion):
    fecha1 = datetime.strptime(input("Fecha 1 (Formato: DAY-MONTH-YEAR): "),('%d-%m-%Y'))
    fecha2 = datetime.strptime(input("Fecha 2 (Formato: DAY-MONTH-YEAR): "),('%d-%m-%Y'))
    fecha1 = int(datetime.timestamp(fecha1))
    fecha2 = int(datetime.timestamp(fecha2))
    fechasFiltradas = list()
    for i in contenido:
        fechasContenido = i[eleccion]
        fechasDateTime = datetime.strptime(fechasContenido, '%d-%m-%Y')
        fechasDateTime = int(datetime.timestamp(fechasDateTime))
        comparacion = fecha1 <= fechasDateTime and fecha2 >= fechasDateTime
        if comparacion:
            fechasFiltradas.append(i)
    return fechasFiltradas

def pantalla():
    for i in range(len(arrayFiltrada)):
                    print('Numero de Cheque: ' + arrayFiltrada[i]['NroCheque'])
                    print('Codigo de Banco: '+ arrayFiltrada[i]["CodBanco"])
                    print('Codigo de sucursal: '+ arrayFiltrada[i]["CodSucursal"])
                    print('Cuenta Origen: '+ arrayFiltrada[i]["NroCuentaOrigen"])
                    print('Cuenta Destino: '+ arrayFiltrada[i]["NroCuentaDestino"])
                    print('Valor: '+ arrayFiltrada[i]["Valor"])
                    print('Fecha de Origen: '+ arrayFiltrada[i]["FechaOrigen"])
                    print('Fecha de Pago: '+ arrayFiltrada[i]["FechaPago"])
                    print('DNI: '+ arrayFiltrada[i]["DNI"])
                    print('Estado: '+ arrayFiltrada[i]["Estado"])
                    print('Tipo: '+ arrayFiltrada[i]["Tipo"])

if __name__ == '__main__':
    while True:
        print('ITCheck Procesamiento de cheques')
        while True:
            try:
                contenido = pedir_nombre()
                break
            except:
                continue
    
        while True:
            print('Filtar por: \n1. ESTADO \n2. TIPO\n3. DNI \n4. RANGO DE FECHAS')
            opcion = input('==> ')
            match opcion:
                case '1':
                    while True:
                        print('Filtrar como: \n1. PENDIENTE \n2. APROBADO \n3. RECHAZADO')
                        opcion = input('==> ')
                        match opcion:
                            case '1':
                                opcion = 'PENDIENTE'
                            case '2':
                                opcion = 'APROBADO'
                            case '3':
                                opcion = 'RECHAZADO'
                            case _:
                                continue                     
                        arrayFiltrada=  filtro(contenido,'Estado',opcion )
                        break
                case '2':
                    while True:
                        print('Filtar como: \n1. EMITIDO \n2. RECHAZADO')
                        opcion = input('==> ')
                        match opcion:
                            case '1':
                                opcion = 'EMITIDO'
                            case '2':
                                opcion = 'DEPOSITADO'
                            case _:
                                continue    
                        arrayFiltrada=  filtro(contenido,'Tipo',opcion )
                        break
                case '3':
                    dni = input('DNI a buscar: ')
                    arrayFiltrada=  filtro(contenido,'DNI',dni )
                case '4':
                    opcion = 'RANGO DE FECHAS'
                    while True:
                        print("Filtrar como: \n1. Fecha de Origen \n2. Fecha de pago")
                        eleccion = input()
                        if eleccion == str(1):
                            eleccion = 'FechaOrigen'
                        elif eleccion == str(2):
                            eleccion = 'FechaPago'
                        else:
                            continue
                        print('Ingrese un rango de fechas: ')
                        arrayFiltrada = filtrarFecha(eleccion)
                        break
                case '_':
                    continue
            break
        
        if arrayFiltrada:    
            while True:
                print('Ver archivo como:  \n1. PANTALLA \n2. CSV')
                opcion = input('==> ')
                match opcion:
                    case'1':
                        pantalla()
                    case'2':
                        createFile(f"{arrayFiltrada[0]['DNI']} {datetime.timestamp(datetime.now())}")
                    case '_':
                        continue
                break

        print('Quiere continuar?: \n1. SI \n2. NO \n')
        opcion = input('==> ')
        if int(opcion) != int(1):
            break