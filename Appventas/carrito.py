class carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session["carrito"]
        if not carrito:                                     #Si no hay carrito asociado a la session 
            self.session["carrito"] = {}                    #Se crea un diccionario vacio
            self.carrito = self.session[carrito]
        else:
            self.carrito = carrito                          #Si no, muestra carrito 

    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():                   #Si no se encuentra el ID de producto dentro del carrito 
            self.carrito[id] = {                            #Crear diccionario con las keys que queremos y que esten en nuestro modelo
            "producto_id": producto.id,
            "nombre": producto.nombre,
            "acumulado": producto.precio,
            "cantida": 1,
        }
        else:
            self.carrito[id]["cantida"] += 1                 #Si el producto existe se agrega la cantidad de 1
            self.carrito[id]["acumulado"] += producto.precio
        self.guardar_carrito()  

    def guardar_carrito(self):
        self.sessions["carrito"] = self.carrito
        self.session.modified = True


    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()                            #Crear diccionario con las keys que                        

    def restar(self, producto):                                
        id = str(producto.id)                                  
        if id in self.carrito.keys():                          
            self.carrito[id]["cantidad"] -= 1                 #si encuentra el ID en carrito le resta 1
            self.carrito[id]["acumulado"] -= producto.precio  #resta del acumulado de productos el precio
            if self.carrito[id]["cantidad"] <= 0:             #Si la cantidad en el carrito es 0 o menor eliminar producto
                self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.sessions["carrito"] = {}
        self.session.modified = True


                            




