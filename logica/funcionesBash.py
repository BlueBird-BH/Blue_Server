import os


# Funciones de comandos
def ejecutarProceso(comando):
    proceso = os.system(comando)
    return proceso


def ejecutarComando(comando, mensaje):
    try:
        mostrarMensaje(mensaje)
        ejecutarProceso(comando)
    except Exception as error:
        mostrarError(error)


def limpiarPantalla():
    return ejecutarProceso("clear")


# Funciones para mensajes
def mostrarMensaje(mensaje):
    print(f"\n  » {mensaje}")


def mostrarError(error):
    mostrarMensaje(f"Ha ocurrido un error inesperado: {error}")