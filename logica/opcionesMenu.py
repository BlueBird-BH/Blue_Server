from logica import contenidoGrafico as menu
from logica import funcionesBash as bash
from comandos import usuarios, grupos, servicio_sftp


# Pantallas de tareas
def cerrarPrograma():
    bash.limpiarPantalla()
    menu.tituloCerrando()
    menu.mensajeContinuar()
    bash.limpiarPantalla()


def procesoFinalizado():
    print("\n╔═→ Proceso finalizado")
    menu.mensajeContinuar()
    bash.limpiarPantalla()


# Pantallas de error
def opcionIncorrecta():
    bash.limpiarPantalla()
    menu.tituloError()
    menu.mensajeOpcionIncorrecta()
    menu.mensajeContinuar()
    bash.limpiarPantalla()


def errorInesperado(error):
    bash.limpiarPantalla()
    menu.tituloError()
    print(f"╠═─[Ocurrio un error inesperado]→ {error}")
    menu.mensajeContinuar()


# Pantallas de submenus
def mostrarSubmenu(parametro):
    getattr(menu, f"tituloGestion{parametro}")()
    getattr(menu, f"mensajeGestion{parametro}")()
    return input("╚═─[Ingrese una opcion]→ ")


def gestionUsuarios(opcion):
    funciones = {
        "1": usuarios.mostrarUsuarios,
        "2": usuarios.crearUsuario,
        "3": usuarios.eliminarUsuario
    }
    bash.limpiarPantalla()
    menu.tituloGestionUsuarios()
    funciones[opcion]()
    procesoFinalizado()


def gestionGrupos(opcion):
    funciones = {
        "1": grupos.crearGrupo,
        "2": grupos.eliminarGrupo,
        "3": grupos.agregarUsuario,
        "4": grupos.retirarUsuario
    }
    bash.limpiarPantalla()
    menu.tituloGestionGrupos()
    funciones[opcion]()
    procesoFinalizado()


def gestionServicio(opcion):
    funciones = {
        "1": servicio_sftp.establecerConfiguracion,
        "2": servicio_sftp.permitirUsuario,
        "3": servicio_sftp.denegarUsuario
    }
    bash.limpiarPantalla()
    menu.tituloGestionServicio()
    funciones[opcion]()
    procesoFinalizado()


# Ejecucion principal
def buclePrincipal():
    try:
        while True:
            bash.limpiarPantalla()
            menu.menuPrincipal()
            opcionMenu = input("╚═─[Ingrese una opcion]→ ")
            bash.limpiarPantalla()

            # Gestion usuarios
            if opcionMenu == "1":
                while True:
                    opcion = mostrarSubmenu("Usuarios")
                    opcionesValidas = ["1", "2", "3"]

                    if opcion in opcionesValidas:
                        gestionUsuarios(opcion)
                    elif opcion == "4":
                        break
                    else:
                        opcionIncorrecta()

            # Gestion grupos
            elif opcionMenu == "2":
                while True:
                    opcion = mostrarSubmenu("Grupos")
                    opcionesValidas = ["1", "2", "3", "4"]

                    if opcion in opcionesValidas:
                        gestionGrupos(opcion)
                    elif opcion == "5":
                        break
                    else:
                        opcionIncorrecta()

            # Gestion servicio SFTP
            elif opcionMenu == "3":
                while True:
                    opcion = mostrarSubmenu("Servicio")
                    opcionesValidas = ["1", "2", "3"]

                    if opcion in opcionesValidas:
                        gestionServicio(opcion)
                    elif opcion == "4":
                        break
                    else:
                        opcionIncorrecta()

            else:
                opcionIncorrecta()

    except KeyboardInterrupt:
        cerrarPrograma()

    except Exception as error:
        errorInesperado(error)
