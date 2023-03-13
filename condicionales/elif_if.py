
#if, elif, else y anidación

ingreso_mensual = 11000
gasto_mensual = 9000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("estas ahorrando")
    else:
        print('estas gasatando mucho, no se si te alcanza')
elif ingreso_mensual > 1000:
    print('estas bien en america latina')
elif ingreso_mensual > 500:
    print('estas bien en argentina')
elif ingreso_mensual > 200:
    print('estas bien en cordoba')
else:
    print('no te alcanza para vivir')
    