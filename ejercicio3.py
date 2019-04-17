print("ingrese 2 angulos")
a1=int(input("Ingrese angulo 1: "))
a2=int(input("Ingrese angulo 2: "))
z=180-(a1+a2)
if (a1==90) or (a2==90) or (z==90):
    print("triangulo Rectangulo")
elif (a1<90) and (a2<90) and (z<90):
    print("triangulo acutangulo")
elif (a1>90) or (a2>90) or (z>90):
    print ("triangulo obstusangulo")


