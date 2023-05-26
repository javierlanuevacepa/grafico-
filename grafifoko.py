import matplotlib.pyplot as plt
import numpy as np

p1=0
p2=0
elpepegrafico = []
elkakegrafico = []
tilingrafico = []
ventasgrafico = []

clientos = {}
cliente = []

ventastri=""

elpepe=0
elkake=0
tilin=0
ventastotales=0

while True:
    ventastri=""
    p1=0
    p2=0
    elpepe=0
    elkake=0
    tilin=0


    print("(1) Realizar venta")
    print("(2) Ver datos")
    selection=input("Que deseas hacer:")
    if selection=="1":
        while p1==0:
            nombre=input("Ingrese nombre del cliente:")
            if nombre=="":
                p1+=1
                print("Ingrese un nombre valido! ")
            else:
                
                print("Nombre ingresado correctamente")
                while p2==0:
                    print("(1) ELPEPE")
                    print("(2) ELKAKE")
                    print("(3) Tilin")
                    print("(4) Realizar venta")
                    
                    sele=input("Que llevara el cliente:")
                    if sele=="1":
                        ventastri=ventastri + "ELPEPE "
                        elpepe+=1
                        ventastotales=+1
                        print(f"--El cliente lleva {elpepe} ELPEPE--")
                    if sele=="2":
                        ventastri=ventastri + "ELKAKE "
                        elkake+=1
                        ventastotales=+1
                        print(f"--El cliente lleva {elkake} ELKAKE--")
                    if sele=="3":
                        ventastri=ventastri + "TILIN "
                        tilin+=1
                        ventastotales=+1
                        print(f"--El cliente lleva {tilin} TILIN--")
                    if sele=="4":
                        if elpepe>0:
                            elpepegrafico.append(elpepe)
                        if elkake>0:
                            elkakegrafico.append(elkake)
                        if tilin>0:
                            tilingrafico.append(tilin)
                        if ventastotales>0:
                            ventasgrafico.append(ventastotales)
                        clientos = {nombre : ventastri}
                        cliente.append(nombre)
                        p2+=1
                        p1+=1
                        print("Venta realizada correctamente !")
                        




        #ypoints.append(x)
    if selection=="2":
        print("(1) ELPEPE")
        print("(2) ELKAKE")
        print("(3) Tilin")
        print("(4) Ventas Totales")
        print("(5) Clientes y ventas")
        elpepler=input("Que datos deseas ver:")
        if elpepler=="1":
            plt.plot(elpepegrafico, marker = 'p')
            plt.show()
        if elpepler=="2":
            plt.plot(elkakegrafico, marker = '^')
            plt.show()
        if elpepler=="3":
            plt.plot(tilingrafico , marker = 'x')
            plt.show()
        if elpepler=="4":
            plt.plot(ventasgrafico , marker = 'x')
            plt.show()
        if elpepler=="5":
            print(cliente)
            clientela=input("Ingrese el cliente que desea ver: ")
            if clientela not in (clientos):
                print("No se a encontrado cliente")
            else:
                print(clientos[clientela])
