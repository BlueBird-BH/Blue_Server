from logica import funcionesBash as bash
import getpass


def mostrarUsuarios():
    bash.ejecutarComando("cut -d: -f1 /etc/passwd", "Usuarios en el sistema")


def crearUsuario():
    usuario = input("╠═─[Nombre de usuario]→ ")
    clave = getpass.getpass(prompt="╚═─[Clave]→ ")

    bash.ejecutarComando(f"useradd {usuario}", "Creando usuario...")

    bash.ejecutarComando(f"echo {usuario}:{clave} | chpasswd",
                         "Configurando clave del usuario")


def eliminarUsuario():
    usuario = input("╚═─[Nombre de usuario]→ ")

    bash.ejecutarComando(f"killall -KILL -u {usuario}",
                         "Deteniendo procesos del usuario...")

    bash.ejecutarComando(f"userdel {usuario}", "Eliminando usuario...")
