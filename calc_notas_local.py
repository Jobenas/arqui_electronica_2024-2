
def ingresa_nota_manual(nombre_eval: str) -> int:
    input_correcto = False
    while not input_correcto:
        resultado = input(f"Por favor ingrese la nota para {nombre_eval}: ")
        try:
            nota = int(resultado)
            if -1 < nota < 21:
                input_correcto = True
            else:
                print("Ingrese un valor de nota valido (entre 0 y 20)")
        except ValueError:
            print("No se ingreso un valor numerico") 
    
    return nota


if __name__ == '__main__':
    notas_labs = list()
    nombre_labs = [f"lab_{i + 1}" for i in range(12)]
    for nombre_lab in nombre_labs:
        nota_lab = ingresa_nota_manual(nombre_lab)
        notas_labs.append(nota_lab)

    e1 = ingresa_nota_manual("Examen parcial")
    e2 = ingresa_nota_manual("Examen final")

    nota_lab = sum(notas_labs) / len(notas_labs)

    nota_final = ((5 * nota_lab) + (2.5 * e1) + (2.5 * e2)) / 10

    print(f"La nota final del curso es: {nota_final}")
    
