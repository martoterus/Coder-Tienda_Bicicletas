class carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:                         #Si no hay carrito asociado a la session 
             carrito = self.session["carrito"] = {}               #Se crea un diccionario vacio 
       
        self.carrito = carrito                      #Si no, muestra carrito 

    def agregar(self, producto):
        if str(producto.id) not in self.carrito.keys():                  #Si no se encuentra el ID de producto dentro del carrito 
            self.carrito[producto.id] = {                            #Crear diccionario con las keys que queremos y que esten en nuestro modelo
            "producto_id": producto.id,
            "nombre": producto.nombre,
            "precio": str(producto.precio),
            "cantida": 1
            }
        else:
            for key, value in self.carrito.items():               #Si el producto existe se agrega la cantidad de 1
                if key == str(producto.id):
                    value ["cantida"] = value["cantida"] + 1
                    value ["precio"] = float(value["precio"])+ producto.precio
                    break
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True


    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()                            #Crear diccionario con las keys que                        

    def restar(self, producto):                                
        for key, value in self.carrito.items():
            if key == str(producto.id):                  #si encuentra el ID en carrito le resta 1
                value ["cantida"] = value["cantida"] - 1
                value ["precio"] = float(value["precio"]) - producto.precio    #resta del acumulado de productos el precio
                if value["cantida"] < 1:                     #Si la cantidad en el carrito es 0 o menor eliminar producto
                    self.eliminar(producto)
                break
        self.guardar_carrito()
                                  
                    
    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True


                            




