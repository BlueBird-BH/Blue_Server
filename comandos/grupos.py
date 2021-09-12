from logica import funcionesBash as bash


def crearGrupo():
    grupo = input("╚═─[Nombre del grupo]→ ")

    comando = f"groupadd {grupo}"
    mensaje = "Creando grupo..."
    bash.ejecutarComando(comando, mensaje)


def eliminarGrupo():
    grupo = input("╚═─[Nombre del grupo]→ ")

    comando = f"groupdel {grupo}"
    mensaje = "Eliminando grupo..."
    bash.ejecutarComando(comando, mensaje)

def agregarUsuario():
    usuario = input("╠═─[Nombre de usuario]→ ")
    grupo = input("╚═─[Nombre del grupo]→ ")

    comando =  f"usermod -aG {grupo} {usuario}"
    mensaje = "Agregando usuario al grupo..."
    bash.ejecutarComando(comando, mensaje)

def retirarUsuario():
    usuario = input("╠═─[Nombre de usuario]→ ")
    grupo = input("╚═─[Nombre del grupo]→ ")

    comando =  f"gpasswd -d {usuario} {grupo}"
    mensaje = "Retirando usuario del grupo..."
    bash.ejecutarComando(comando, mensaje)