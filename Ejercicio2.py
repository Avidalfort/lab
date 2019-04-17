a=int(input("cual departamento le interesa: "))
a=str(a)
p=a[0:2]
num=a[2:4]
if p==20:
    if num==7 or num==3 :
        print ("total a pagar 460")
    elif num==0 or num==4:
        print ("totla a pagar 320")
    else:
        print ("total a pagar 400")
elif p==1:
    print ("total a pagar 115")
elif num==7 or num==3:
    print ("total a pagar 80")
elif num==0 or num==4:
    print ("total a pagar 100")    
else: 
    if num==7 or num==3:
        print("total a pagar 288")
    elif num==0 or num==4:
        print ("total a pagar 200") 
    else:
        print ("total a pagar 250")
