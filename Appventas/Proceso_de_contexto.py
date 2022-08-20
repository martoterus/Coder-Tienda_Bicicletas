def total_carrito(request):
    total = 0                                                     
    if request.user.is_authenticated:                               #Si el ususario es autenticado
        if "carrito" in request.session.keys():                              #Si el carrito esta vinculado a una sesion
            for key, value in request.session["carrito"].items():   #Entonces, iterar y guardar clave valor de los items dentro del carrito
                total += int(value["acumulado"])                    #Se suman todos los productos
    return{"total_carrito": total}                                  #Se devuelve un diccionario con el total