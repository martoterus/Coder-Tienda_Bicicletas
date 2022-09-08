def total_carrito(request):
    total = 0                                             
    if request.user.is_authenticated:                               #Si el ususario es autenticado                    #Si el carrito esta vinculado a una sesion
        for key, value in request.session['carrito'].items():   #Entonces, iterar y guardar clave valor de los items dentro del carrito
            total =total + (float(value["precio"]))             #Se suman todos los productos
    return{'total_carrito': total}                                  #Se devuelve un diccionario con el total