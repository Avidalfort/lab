N=input("cual es el nombre del participante")
D=float(input("cual fue la dificultad del piquero"))
j=7
x=0
I=0
p=[]
for i in range(0,j) :
    x=float(input("puntaje del juez: "))
    x=x+I
    p.append(x)
    if I==0:
        I=1/2
p.sort()
p.pop(-1)
p.pop(0)
r=(p[0]+p[1]+p[2]+p[3]+p[4])*(3/5)
r=r*D
print("El puntaje total de",N,"es: ",r)

