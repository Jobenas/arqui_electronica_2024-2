

if __name__ == '__main__':
    input_correcto = False
    while not input_correcto:
        resultado = input("Por favor ingrese una nota: ")
        try:
            nota = int(resultado)
            if -1 < nota < 21:
                input_correcto = True
            else:
                print("Ingrese un valor de nota valido (entre 0 y 20)")
        except ValueError:
            print("No se ingreso un valor numerico") 
    print(f"Lo que se ingreso fue: {resultado}")

