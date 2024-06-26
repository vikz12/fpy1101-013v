import os
libros=[]
personas=[]

#registro_libros
def registros_libros():
    print("\n registre el libro que desea solicitar ")
    titulo_libro =input("ingrese titulo del libro: ")
    autor_libro =input("ingrese el autor del libro: ")
    while True:
        try:
            año_libro = input(int("ingrese el año de publicacion del libro: "))
            sku_libro = input(int("ingrese sku del libro solicitado: "))
            break
        except ValueError:
            print ("solo debe digitar numeros en esta zona ")

        #guardar libros 
    lista_de_libros={
        'titulo_libro':titulo_libro,
        'autor_libro' :autor_libro,
        'año_libro' : año_libro,
        'sku_libro' : sku_libro,
    }
    libros.append(registros_libros) 
    print("libro resgistrasdo exitosamente\n")
 
#funcion listar libros 
def listar_libros():
    print("listar todos los libros ")
    for lista_de_libros in libros:
        print(f"titulo: {listar_libros['titulo_libro']},titulo autor: {listar_libros['autor_libro']}, año libro {listar_libros['año_libro']}, codigo sku libro {listar_libros['sku_libro']} ")

#funcion prestar libro 
def prestar_libros():
    print("rellene los datos solicitados ")
    solicitante_libro=input("ingrese su nombre y apellido")
    sku =input(int("ingrese el sku de libro solicitado"))
    fecha =input("escriba la fecha de solicitud del libro ")
    listar_solicitantes={
        'solicitante_libro' : solicitante_libro,
        'sku' : sku,  
        'fecha' : fecha,  
     }
    personas.append()
#funcion imprimir reporte de prestamos
def imprimir_prestamos():
    solicitantes_de_libros= ['solicitante_libros','sku','fecha']
    print("imprimir planilla de prestamos de libros ")
    for libreria ,solicitante_libro in enumerate (solicitantes_de_libros):
        print(f"{libreria + 1}.{solicitante_libro}")
        planilla_prestamos="planilla_libros.txt"
        with open (solicitantes_de_libros,'w') as f:
            f.write("listar_solicitantes")
            for lista_de_libros in libros:
                f.writeprint(f"solicitante: {prestar_libros['solicitando_libro']},sku libro: {prestar_libros['sku']}, fecha {prestar_libros['fecha']}")
                print("documento subido con exito")

   
        

#funcion salir del programa
def salir_programa():
    print("programa finalizado.... \n desarollado por Victor Rebolledo \n Run: 17.245.7312-0")
    return False
#funcion principal del programa 

def main ():
    print("\nbienvenidos a la biblioteca nacional escoja su opcion en el siguiente menu")
    while True:
        print("1)registrar libro")
        print("2)prestar libro")
        print("3)listar todos los libros")
        print("4)imprimir repoertes de prestamos")
        print("5)salir del programa ")

        try:
            opcion= int(input("\n ingrese el numero de la opcion a realizar"))
            if opcion == 1:
                registros_libros()
            elif opcion == 2:
                prestar_libros()    
            elif opcion == 3:
                listar_libros()
            elif opcion == 4:
                imprimir_prestamos()
            elif opcion == 5:
                salir_programa()
                break
            else: ("opcion invalida intente nuevamente") 
        except ValueError:    
            print("error ingrese un numero valido ")

if __name__=="__main__":
    main()




           


            