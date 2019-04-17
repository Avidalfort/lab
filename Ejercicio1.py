def rut():
    a=[2,3,4,5,6,7,2,3,4,5,6,7]
    rut=input("Ingrese rut sin gion: ")
    rut=rut[::-1]
    b=0
    c=0
    d=12
    suma=0 
    while b<len(rut):
        c=int(rut[b])*int(a[b])
        suma=suma + c
        b=b+1
    print(suma)
    e=11-(suma % 11)
    if 0<e<10:
        d=e
    elif e==11:
        e=0
    elif e==10:
        str(d)
        d="K"
    print ("El numero despues del guion es: ", d)
rut()