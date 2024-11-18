import threading

datosSesion = threading.local()

class SesionUsuario:

    def iniciar_sesion(self,nombreUsuario):
        datosSesion.usuario = nombreUsuario

    def mostrarSesion(self):
        print(f"Sesión iniciada para el usuario: {datosSesion.usuario}")

def gestionarSesion(nombreUsuario):
    datosSesion.sesionUsuario = SesionUsuario()
    datosSesion.sesionUsuario.iniciar_sesion(nombreUsuario)
    datosSesion.sesionUsuario.mostrarSesion()

usuarios = ["Ana","Carolos","Beatriz","David","Elena"]

hilos = []

for usuario in usuarios:
    hilo = threading.Thread(target=gestionarSesion, args=(usuario,))
    hilo.start()
    hilos.append(hilo)

for hilo in hilos:
    hilo.join()



