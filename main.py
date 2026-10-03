lista_total = []
opciones_menu = 1,2,3,4,5
indice = 0

colores_titulos = "\033[31m"
reset = "\033[0m"
color_éxito = "\033[92m"
advertencias = "\033[91m"
errores_alertas = "\033[93m"
datos_importantes = "\033[1;96m"
textos_secundarios  = "\033[37m"
negrita = "\033[1m"
celdas = "\033[33m"
subrayado = "\033[4m"


print(f"📋{negrita}--- Bienvenido/a al listado de productos ---{reset}📋")

while True:

    print(f"\n{negrita}1- Agregar producto 📥\n2- Mostrar producto 📄\n3- Buscar producto 🔎\n4- Eliminar producto 🗑️\n5- Salir ⭕")
    menu = input(f"\n{datos_importantes}Seleccione alguna de las anteriores opciones: {reset}").strip()

    if menu.isdigit() and menu != " ":

        menu_int = int(menu)

    else:
        menu_int = 0

    if menu_int in opciones_menu :

        if menu_int == opciones_menu[0]:

            print(f"\n{negrita}   ----- Agregar un precio al sistema -----{reset}")

            agregar_producto = input(f"{datos_importantes}Ingrese el nombre del producto a agregar: {reset}").strip().capitalize()

            while not agregar_producto.replace(" ","").isalpha() or agregar_producto == "" :

                print(f"\n{errores_alertas}El producto no puede contener números, símbolos o espacios vacíos.{reset}")
                agregar_producto = input(f"\n{datos_importantes}Ingrese el nombre del producto a agregar: {reset}").strip().capitalize()

            agregar_catalogo = input(f"\n{datos_importantes}Ingrese a que categoría corresponde el producto agregado: {reset}").strip().capitalize()

            while not agregar_catalogo.replace(" ","").isalpha() or agregar_catalogo == "" :

                print(f"\n{errores_alertas}La categoria no puede contener números, símbolos o espacios vacíos.{reset}")
                agregar_catalogo = input(f"\n{datos_importantes}Ingrese el nombre del producto a agregar: {reset}").strip().capitalize()
            
            agregar_precio_str = input(f"\n{datos_importantes}Ingrese el precio del producto a agregar: {reset}").strip()

            while not agregar_precio_str.isdigit() or agregar_precio_str == "0" :

                print(f"\n{errores_alertas}El valor del precio debe ser solo números postivos y no puede contener espacios.{reset}")
                agregar_precio_str = input(f"\n{datos_importantes}Ingrese el precio del producto a agregar: {reset}").strip()

            indice += 1
            precio_int = int(agregar_precio_str)
            lista_total.append([agregar_producto,agregar_catalogo,precio_int])
            print(f"\n{color_éxito}¡Producto {reset}'{datos_importantes}{agregar_producto}{reset}' {color_éxito}agregado con éxito!{reset}")
            print(f"\n{negrita}Con que opcion desea continuar: {reset}")


        elif menu_int == opciones_menu[1]:

            if not lista_total :

                print(f"\n{advertencias}No hay productos existentes en la lista, agrega un producto primero.{reset}")

            else:

                indice = 0
                print(f"\n{celdas}┌────────────────────────────────{reset}{negrita} Lista de productos {celdas}────────────────────────────────────┐{reset}\n{celdas}│                                                                                        │{reset}")
                for i in range(len(lista_total)) :

                    indice += 1
                    nombre = lista_total[i][0]
                    categ = lista_total[i][1]
                    precio = lista_total[i][2]
                    print(f"{celdas}├{reset}ID{datos_importantes}{indice}{reset}- {subrayado}Categoría{reset} : {datos_importantes}{categ}{reset}, {subrayado}Producto{reset} : {datos_importantes}{nombre}{reset}, {subrayado}Precio{reset} : ${datos_importantes}{precio}{reset}                 ")
                    print(f"{celdas}└────────────────────────────────────────────────────────────────────────────────────────┘{reset}")

                print(f"\n{negrita}Con que opcion desea continuar: {reset}")

        elif menu_int == opciones_menu[2]:

            print(f"\n{negrita}     ---- Buscador de productos ----{reset}")

            busqueda_productos = input(f"{datos_importantes}Ingrese el nombre del producto que desea buscar: {reset}").strip().capitalize()

            if busqueda_productos.isalpha():
            
                if not lista_total:

                    print(f"\n{advertencias}No hay productos registrados con ese nombre en el sistema.{reset}")

                else:

                    for i in range(len(lista_total)):

                        if busqueda_productos == lista_total[i][0]:

                            print(f"\nProducto '{datos_importantes}{busqueda_productos}{reset}' {color_éxito}coincide{reset} con el registro; Su categoría es : {datos_importantes}{lista_total[i][1]}{reset}; Su precio : {datos_importantes}${lista_total[i][2]}{reset} ; Su ID es {datos_importantes}{indice}{reset}.")
                            print(f"\n{negrita}Con que opcion desea continuar: {reset}")        
                            break

                    else :
                        print(f"\n{errores_alertas}No existe {datos_importantes}{busqueda_productos}{reset} en la lista.{reset}")


            else:

                print(f"\n{errores_alertas}No pueden ingresarse números o espacios vacíos.{reset}")

        elif menu_int == opciones_menu[3]:

            print(f"\n{negrita}            --- Eliminar producto ---{reset}")
            if len(lista_total) == 0:

                print(f"\n{advertencias}Todavia no hay productos cargados.{reset}")


            else:

                for i in range(len(lista_total)):
                    print(f"ID{datos_importantes}{i+1}{reset}- Producto : '{datos_importantes}{lista_total[i][0]}{reset}' - Categoría : '{datos_importantes}{lista_total[i][1]}{reset}' - Precio : '{datos_importantes}${lista_total[i][2]}{reset}'")  

                id_elminar = input(f"\n{datos_importantes} Ingrese número de producto a eliminar: {reset}").strip()
                while not id_elminar.isdigit():

                    print(f"\n{errores_alertas}Debe ingresar un número valido.{reset}")
                    id_elminar = input(f"\n{datos_importantes}Número de producto a eliminar: {reset}").strip()

                posicion = int(id_elminar) - 1
                # ["algo",[nombre,categoria,precio]].pop(1) -> [nombre,categoria,precio]
                eliminado = lista_total.pop(posicion)
                print(f"\n'{datos_importantes}{eliminado[0]}{reset}' {color_éxito}eliminado con éxito.{reset}")


        elif menu_int == opciones_menu[4]:

            print(f"\n{color_éxito}Salió de la lista de productos con éxito.👋{reset} {negrita}¡GRACIAS POR ELEGIRNOS!👋{reset}")
            break

    else: 
        print(f"\n{errores_alertas}Debe ingresar una opcion correcta (1/2/3/4/5){reset}")