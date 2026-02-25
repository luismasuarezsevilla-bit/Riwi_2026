print("calculadora cientifica")
print("1.suma\n2.resta\n3.multiplicasion\n4.division\n5.potenciacion\n6.radicacion\n7.porcentaje\n8.modulo\n9.promedio")
operacion=int(input("ingrese la operacion a realizar: "))
a=int(input("ingrese un  primer valor a operar"))
b=int(input("ingrese un segundo valor a operar"))
while operacion > 0 and operacion <= 9:
    if operacion==1:
        resultado=a+b
        print(resultado)
        break
    elif operacion==2:
        resultado=a-b
        print(resultado)
        break
    elif operacion==3:
        resultado=a*b
        print(resultado)
        break
    elif operacion==4:
        if b==0:
            print("respuesta no definida")
            break
        else:
            resultado=a/b
            print(resultado)
            break
    if operacion==5:
        resultado=a**b
        print(resultado)
        break
    elif operacion==6:
        resultado=a**(1/b)
        print(resultado)
        break
    elif operacion==7:
        resultado=(a*b)/100
        print(resultado)
        break
    elif operacion==8:
        resultado=a%b
        print(resultado)
        break
    else:
        resultado=(a+b)/2
        print(resultado)
        break
print("gracias por usar la calculadora cientfica")
