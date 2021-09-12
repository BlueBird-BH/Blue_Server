from logica import funcionesBash as bash
import pathlib

# Declaracion de variables
grupo = "grupo_sftp"


# Funciones
def establecerConfiguracion():
    dirTrabajo = pathlib.Path(".").parent.absolute()
    dirArchivo = f"{dirTrabajo}/archivos/sshd_config"
    dirConfig_sftp = "/etc/ssh/sshd_config"
    
    bash.ejecutarComando(f"cp {dirArchivo} {dirConfig_sftp}",
                         "Estableciendo configuracion del servicio SFTP")
    
    bash.ejecutarComando("systemctl restart sshd",
                         "Reiniciando servicio SSH")


def permitirUsuario():
    usuario = input("╠═─[Nombre de usuario]→ ")
    try:
        dirPrincipal = f"/share/{usuario}"
        dirUsuario = f"{dirPrincipal}/sftp"

        bash.ejecutarComando(
            f"groupadd {grupo}",
            "Verificando estado del grupo que controla el servicio")

        bash.ejecutarComando(f"usermod -aG {grupo} {usuario}",
                             "Agregando al usuario al grupo")

        bash.ejecutarComando(f"mkdir -p {dirUsuario}",
                             "Creando carpeta del usuario")

        bash.ejecutarComando(f"chown -R root:root {dirPrincipal}",
                             "Creando carcel Chroot")

        bash.ejecutarComando(f"chown -R {usuario}:{grupo} {dirUsuario}",
                             "Dando permisos de escritura")

    except Exception as error:
        bash.mostrarError(error)


def denegarUsuario():
    usuario = input("╚═─[Nombre de usuario]→ ")
    try:
        dirUsuario = f"/share/{usuario}/sftp"

        bash.ejecutarComando(f"killall -KILL -u {usuario}",
                             "Deteniendo procesos del usuario")

        bash.ejecutarComando(f"gpasswd -d {usuario} {grupo}",
                             "Removiendo al usuario del grupo")

        bash.ejecutarComando(f"rm -rf {dirUsuario}",
                             "Eliminando carpeta del usuario")

    except Exception as error:
        bash.mostrarError(error)