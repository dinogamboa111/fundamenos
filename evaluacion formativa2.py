import os
import time

print("Bienvenido a nuestra tienda de sushi\nNuestra Carta es la sigiente: ")

inicialmenu1 = 1
inicialmenu2 = 1
pikachu = 0 
otaku = 0
pulpo = 0
anguila = 0

while inicialmenu1 == 1:
    print(" ")
    print(" Seleccine la opcion que desea: ")
    try:
        print("_"*60)
        print("1.- Pikachu Roll            $4500")
        print("2.- Otaku Roll              $5000")
        print("3.- Pulpo Venenoso Roll    $5200")
        print("4.- Anguila Electrica Roll  $4500")
        print("5.- Borrar pedido actual/comenzar de 0")
        print("6.- Finalizar mi pedido")
        print("_"*60)
        pedido= int(input(" indique su eleccion: "))
        print("_"*60)
    except ValueError:
        print(" Recuerde ingresar una opcion valida, numero entre 1 y 6 ")
        continue
    if pedido ==1:
        pikachu = pikachu+1
        print("_"*60)
        print(f"ha seleccionado una unidad de Pikachu Roll, su pedido actual es: ")
        print(f"Pikachu Roll: {pikachu} por un  valor de: ${pikachu*4500}")
        print(f"Otaku Roll: {otaku} por un  valor de: ${otaku*5000}")
        print(f"Pulpo Venenoso Roll: {pulpo} por un  valor de: ${pulpo*5200}")
        print(f"Anguila Electrica Roll: {anguila} por un  valor de: ${anguila*4800}")
        print("_"*60)
        continue
    if pedido ==2:
        otaku = otaku+1
        print("_"*60)
        print(f"ha seleccionado una unidad de Otaku Roll, su pedido actual es: ")
        print(f"Pikachu Roll: {pikachu} por un  valor de: ${pikachu*4500}")
        print(f"Otaku Roll: {otaku} por un  valor de: ${otaku*5000}")
        print(f"Pulpo Venenoso Roll: {pulpo} por un  valor de: ${pulpo*5200}")
        print(f"Anguila Electrica Roll: {anguila} por un  valor de: ${anguila*4800}")    
        print("_"*60)       
        continue
    if pedido==3:
        pulpo= pulpo+1
        print("_"*60)
        print(f"ha seleccionado una unidad de Pulpo Venenoso Roll, su pedido actual es: ")
        print(f"Pikachu Roll: {pikachu} por un  valor de: ${pikachu*4500}")
        print(f"Otaku Roll: {otaku} por un  valor de: ${otaku*5000}") 
        print(f"Pulpo Venenoso Roll: {pulpo} por un  valor de: ${pulpo*5200}")
        print(f"Anguila Electrica Roll: {anguila} por un  valor de: ${anguila*4800}")
        print("_"*60)
        continue
    if pedido==4:
        anguila = anguila+1
        print("_"*60)
        print(f"ha seleccionado una unidad de Anguila electrica Roll, su pedido actual es: ")
        print(f"Pikachu Roll: {pikachu} por un  valor de: ${pikachu*4500}")
        print(f"Otaku Roll: {otaku} por un  valor de: ${otaku*5000}")
        print(f"Pulpo Venenoso Roll: {pulpo} por un  valor de: ${pulpo*5200}")
        print(f"Anguila Electrica Roll: {anguila} por un  valor de: ${anguila*4800}")
        print("_"*60)
        continue
    if pedido==5:
        anguila = anguila+1
        print("_"*60)
        print(f"Se ha borrado su pedido actual, comenzara de 0 ")
        print("_"*60)
        pikachu = 0
        anguila= 0
        pulpo = 0
        otaku = 0
        continue
    if pedido ==6:
        print("_"*60)
        print(" ha finalizado de seleccionar su pedido, el resumen es: ")
        print(" ")
        print(f"ha seleccionado una unidad de Anguila electrica Roll, su pedido actual es: ")
        print(f"Pikachu Roll: {pikachu} por un  valor de: ${pikachu*4500}")
        print(f"Otaku Roll: {otaku} por un  valor de: ${otaku*5000}")
        print(f"Pulpo Venenoso Roll: {pulpo} por un  valor de: ${pulpo*5200}")
        print(f"Anguila Electrica Roll: {anguila} por un  valor de: ${anguila*4800}")
        valor = (pikachu*4500)+(otaku*5000)+(pulpo*5200)+(anguila*4800)
        print(f"Valor del pedido: ${valor}")
        print("_"*60)
        inicialmenu1 = 2
    while inicialmenu2 == 1:
        tienecodigo=int(input("Usted posee algun codigo de descuento? si=1/no=2"))
        if tienecodigo==1:
            codigo=input("por favor ingrese su codigo")
            if codigo == "soyotaku":
                print("_"*60)
                print("se ha aplicado su descuento, el resumen es: ")
                print(" ")
                print(f"ha seleccionado una unidad de Anguila electrica Roll, su pedido actual es: ")
                print(f"Pikachu Roll: {pikachu} por un  valor de: ${pikachu*4500}")
                print(f"Otaku Roll: {otaku} por un  valor de: ${otaku*5000}")
                print(f"Pulpo Venenoso Roll: {pulpo} por un  valor de: ${pulpo*5200}")
                print(f"Anguila Electrica Roll: {anguila} por un  valor de: ${anguila*4800}")
                valor = (pikachu*4500)+(otaku*5000)+(pulpo*5200)+(anguila*4800)
                print(f"Valor del pedido con 10% de descuento: ${valor*0.9}")
                print("_"*60)
                volver2=int(input("desea realizar otro pedido si=1/no=2, en caso de 2 se terminara el pedido: "))
                if volver1 ==1:
                    inicialmenu1=1
                    inicialmenu2=2
                    break
                elif volver1 ==2:
                    inicialmenu2=2
                    inicialmenu=2
                    break
            elif codigo != "soyotaku":
                volver=int(input("Codigo no valido, si desea voler a ingresar un codigo, precione 1, si desea volver al menu inicial precione 2"))
                if volver == 1:
                    continue
                elif volver==2:
                    inicialmenu1= 1
                    break
        elif tienecodigo ==2:
            print("_"*60)
            print("Su pedido no posee descuentos: ")
            print(" ")
            print(f"ha seleccionado una unidad de Anguila electrica Roll, su pedido actual es: ")
            print(f"Pikachu Roll: {pikachu} por un  valor de: ${pikachu*4500}")
            print(f"Otaku Roll: {otaku} por un  valor de: ${otaku*5000}")
            print(f"Pulpo Venenoso Roll: {pulpo} por un  valor de: ${pulpo*5200}")
            print(f"Anguila Electrica Roll: {anguila} por un  valor de: ${anguila*4800}")
            valor = (pikachu*4500)+(otaku*5000)+(pulpo*5200)+(anguila*4800)
            print(f"Valor del pedido final: ${valor}")
            print("_"*60)
            volver1=int(input("desea realizar otro pedido si=1/no=2, en caso de 2 se terminara el pedido: "))
            if volver1 ==1:
                inicialmenu1=1
                break
            elif volver1 ==2:
                inicialmenu=2
                break
        print("_"*60)
        print("se ha aplicado su descuento, el resumen es: ")
        print(" ")
        print(f"ha seleccionado una unidad de Anguila electrica Roll, su pedido actual es: ")
        print(f"Pikachu Roll: {pikachu} por un  valor de: ${pikachu*4500}")
        print(f"Otaku Roll: {otaku} por un  valor de: ${otaku*5000}")
        print(f"Pulpo Venenoso Roll: {pulpo} por un  valor de: ${pulpo*5200}")
        print(f"Anguila Electrica Roll: {anguila} por un  valor de: ${anguila*4800}")
        valor = (pikachu*4500)+(otaku*5000)+(pulpo*5200)+(anguila*4800)
        print(f"Valor del pedido con 10% de descuento: ${valor*0.9}")
        print("_"*60)
        volver2=int(input("desea realizar otro pedido si=1/no=2, en caso de 2 se terminara el pedido: "))
        if volver1 ==1:
            inicialmenu1=1
            break
        elif volver1 ==2:
            inicialmenu=2
            break
print(" ")
