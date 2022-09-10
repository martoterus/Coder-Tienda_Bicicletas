<!--CoderHouse-Python Enlace al video : https://youtu.be/hQ9E2Jeh7Bs
    Proyecto Final Coder House

    Decidimos hacer una aplicación web de "Artículos para una bicicletería". 
    
    Podras crearte un usuario permitiendote:
                 usar la tienda para poder poder comprar. 
                 chatear con los demas usuarios.
                 cargar una foto de avatar.
                 modificar datos de tu usuario.
                 contactarse con la pagina por medio de "contacto" y se enviará junto al mensaje el usuario que lo envia.
    Si no es usuario:
                 ver los articulos de la tienda.
                 contactarse con la pagina via correo. 
                 ver las zolapas de "home", "about" y "formularios" 
    
    Tambien el administrador podra crear empleados que podran hacer:
                 Cargar nuevos articulos, modificar los actuales. 
                 Chatear en el chat de usuarios.


    Algunos de los problemas que surgieron:
    
    Problema n°1:
    En Contacto, en el envío de mensaje no nos validaban los campos y por esto apareció el error de que se enviaba el mensaje vacío. 
    Esto ocurría por la falta de conocimiento en html y css, ya que la carga de datos se realizaba por medio del nombre(name="")
    del campo del html a la view. 
    Para corregir esto decidimos cargar un formulario y retornar el renderizado con el html y el formulario como contexto en el método get.
    Y cuando enviamos los datos y entramos con el método post recuperamos los datos del formulario a una variable, y si son válidos, se 
    guarda cada campo especifico en distintas variables preseleccionadas (variable=form.cleande_data["campo"])
    Para enviar el mensaje por  correo es necesario transformar el render a string, se utiliza la función predeterminada,
    importada de django.template.loader, con las variables que queremos enviar. Y luego, con un objeto importado de django 
    le cargamos los datos necesarios, y enviamos el correo con la función "send", y se envia el mensaje al correo que colocamos en la configuración de la app.

    Para usar class Meta: Utilizamos un formulario basado en modelos class ModeloX (models.ModelForm):

    Problema n°2:
    En avatar de usuario: Al cambiar el avatar con el mismo usuario, saltaba un error y no mostraba ninguna imagen ya que se 
    dirigía a la excepción. 
    ¿Qué sucedía? El filtro nos trae la imagen asociada a el usuario, al haber más de una imagen se pisaban entre sí y ocurría un error.
    Para solucionar esto pensamos lo siguiente: cuando usamos el manager object con el método filtro creamos un QuerySet, es decir una lista.
    Entonces decidimos contar la cantidad de elementos de la lista, restarle 1 y ese número colocarlo como ubicación en la lista del contexto:
    avatar=Avatar.objects.filter(user=request.user.id)                    
    filtro=len(avatar)-1

    return render ..... {"url":avatar[filtro].imagen.url}...

    Problema 3: 

    En la pestaña about no nos permita cargar la foto de nosotros. Intentamos colocando el código img con la direccione de la carpeta donde 
    están todas las fotos y la foto en sí que queríamos subir, pero terminaba fallando y aparecía la imagen rota.
    Para esto decidimos utilizar el medio inicial que usamos para el avatar. 
    Creamos un modelo llamado "about", donde creamos un campo de imagen, lo cargamos en la base de datos, y también modificamos el admin
    para poder cargar las fotos manualmente con el administrador. Finalmente, en views.py en la función que renderiza el "about" 
    tomamos todos los objectos del modelo About y enviamos como contexto en el renderizado la ubicación de la imagen con su url.

    
    

        -->
