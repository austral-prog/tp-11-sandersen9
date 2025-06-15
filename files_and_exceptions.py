def read_file_to_dict(filename):
    ventas = {}

    with open(filename, "r") as archivo:
        try:
            linea = archivo.readline().strip()
            registros = linea.split(";")

            for item in registros:
                if item:
                    producto, valor = item.split(":")
                    valor = float(valor)

                    if producto in ventas:
                        ventas[producto].append(valor)
                    else:
                        ventas[producto] = [valor]

        except Exception as e:
            print("Error al procesar el archivo:", e)

    return ventas


def process_dict(ventas):
    for producto, montos in ventas.items():
        total = sum(montos)
        promedio = total / len(montos)
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
    
