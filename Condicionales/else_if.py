ingreso_mensual = 81000
gasto_mesnual = 80000

# if anidados y el if (elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mesnual < 0:
        print("estas en la ruina")
    elif ingreso_mensual - gasto_mesnual > 3000:
        print("vas bien loco")
    else:
        print("Te quedaste de hambre")    
    
elif ingreso_mensual > 1000:
    print("Tu ingreso es bueno para Latinoamerica")

elif ingreso_mensual > 500:
    print("Tu ingreso es bueno para Peru")

elif ingreso_mensual > 200:
    print("Tu ingreso es bueno para Venezuela")    

else:
    print("eres un pobre")