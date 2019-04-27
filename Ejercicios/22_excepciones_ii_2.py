# -*- coding: utf-8 -*-
def divide():
    try:
    
        opt1=(float(input("Introduce el primer número: ")))
        opt2=(float(input("Introduce el segundo número: ")))

        print("La división es: " + str(opt1/opt2))

    # except:
    #     print("Ha ocurrido un error.")
    except ValueError:
        print("Valor introducido erróneo.")

    except ZeroDivisionError:
        print("No se puede dividir entre 0.")

    finally:
        print("Cálculo finalizado.")

divide()