from django.test import TestCase

#from django.contrib.auth import get_user_model#podemos crear usuarios para hacer nuestros tests

# User=get_user_model()
# class CanalTestCase(TestCase):
#     def setUp(self):
#         self.usuarios_a = User.objects.create(username='Martin',password='alto')
#         self.usuarios_b = User.objects.create(username='Milo',password='perro')
#         self.usuarios_c = User.objects.create(username='Ayelen',password='petisa')
#         #son crados en la memoria corta, se eliminan al hacer el test

#     def test_usuarios_count(self):#para verificar que sean 3 usuarios
#        qs=User.objects.all()#agarra todos los usuarios creados
#        self.assertEqual(qs.count(),3)
#        #assertEqual verifica que dos variables sean iguales. va a verificar qe se creen 3 usuarios y lo compare con el numero 3 que colocamos.

#     def test_cada_usuario_canal(self):
#         qs=User.objects.all()#se agarran todos los usuarios
#         for usuario in qs: #se agrega un usuario a un canal q creamos
#             canal_obj = Canal.objects.create()
#             canal_obj.usuarios.add(usuario)

#         canal_qs = Canal.objects.all()
#         self.assertEqual(canal_qs.count(), 3)
#         canal_qs_1 = canal_qs.solo_uno()
#         self.assertEqual(canal_qs_1.count(), canal_qs.count())
    
#     def prueba_dos_usuarios(self):
#         canal_obj = Canal.objects.create()
#         CanalUsuario.objects.create(usuario=self.usuario_a, canal=canal_obj)
#         CanalUsuario.objects.create(usuario=self.usuario_b, canal=canal_obj)

#         canal_obj2 = Canal.objects.create()
#         CanalUsuario.objects.create(usuario=self.usuario_c, canal=canal_obj2)

#         qs = Canal.objects.all()
#         self.assertEqual(qs.count(), 2)
#         solo_dos = qs.solo_dos()
#         self.assertEqual(solo_dos.count(), 1)

