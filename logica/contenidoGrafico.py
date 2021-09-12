# Menu principal
def menuPrincipal():
    print("╔═════════════════════════════════════════════════╗")
    print("║                       Menu                      ║")
    print("╠═════════════════════════════════════════════════╣")
    print("║ [1] Gestionar usuarios                          ║")
    print("║ [2] Gestionar grupos                            ║")
    print("║ [3] Gestionar servicio SFTP                     ║")
    print("╠═════════════════════════════════════════════════╣")
    print("║ » Presione Ctrl + C para salir                  ║")
    print("╠═════════════════════════════════════════════════╝")


# Titulos
def tituloCerrando():
    print("╔═════════════════════════════════════════════════╗")
    print("║                   Cerrando...                   ║")
    print("╠═════════════════════════════════════════════════╝")


def tituloError():
    print("╔═════════════════════════════════════════════════╗")
    print("║                      Error                      ║")
    print("╠═════════════════════════════════════════════════╝")


def tituloGestionUsuarios():
    print("╔═════════════════════════════════════════════════╗")
    print("║                Gestionar usuarios               ║")
    print("╠═════════════════════════════════════════════════╣")


def tituloGestionGrupos():
    print("╔═════════════════════════════════════════════════╗")
    print("║                Gestionar grupos                 ║")
    print("╠═════════════════════════════════════════════════╣")


def tituloGestionServicio():
    print("╔═════════════════════════════════════════════════╗")
    print("║             Gestionar servicio SFTP             ║")
    print("╠═════════════════════════════════════════════════╣")


def tituloOpcion1():
    print("╔═════════════════════════════════════════════════╗")
    print("║                       [1]                       ║")
    print("╠═════════════════════════════════════════════════╝")


def tituloOpcion2():
    print("╔═════════════════════════════════════════════════╗")
    print("║                       [2]                       ║")
    print("╠═════════════════════════════════════════════════╝")


# Mensajes
def mensajeContinuar():
    print("╠═════════════════════════════════════════════════╗")
    print("║ » Presione Enter para continuar                 ║")
    input("╚═════════════════════════════════════════════════╝")


def mensajeOpcionIncorrecta():
    print("╠═─[Ocurrio un error]→ La opcion marcada no se     ")
    print("║                      encuentra en la lista de    ")
    print("║                      opciones presentada         ")


def mensajeGestionUsuarios():
    print("║ [1] Mostrar usuarios                            ║")
    print("║ [2] Crear usuario                               ║")
    print("║ [3] Eliminar usuario                            ║")
    print("║ [4] Volver al menu principal...                 ║")
    print("╠═════════════════════════════════════════════════╣")


def mensajeGestionGrupos():
    print("║ [1] Crear grupo                                 ║")
    print("║ [2] Eliminar grupo                              ║")
    print("║ [3] Agregar usuario a grupo                     ║")
    print("║ [4] Retirar usuario de grupo                    ║")
    print("║ [5] Volver al menu principal...                 ║")
    print("╠═════════════════════════════════════════════════╣")


def mensajeGestionServicio():
    print("║ [1] Establecer configuracion predeterminada     ║")
    print("║ [2] Añadir usuario al servicio                  ║")
    print("║ [3] Retirar usuario del servicio                ║")
    print("║ [4] Volver al menu principal...                 ║")
    print("╠═════════════════════════════════════════════════╣")
