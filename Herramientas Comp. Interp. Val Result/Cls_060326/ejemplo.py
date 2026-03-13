#Programa para registrar estudiantes y cursos con while
#solicitar al usuario la cantidad de estudiantes a registrar

N = int(input("Solicitar que ingrese la cantidad de estudiantes: "))

#crear una lista vacia para guardar la inf de los estudiantes
estudiantes = []

# contador para recorrer a los estudiabntes
i = 1

#ciclo while quese ejecute hasta que i sea igual al num de estudiantes

while i <= N:
    #mostrar en pantalla que estudiante se esta registrando
    print("\n Registro del estudiante", i)

    #solicitar el nombre del estudiante
    #.format inserta la variable en el texto en donde se coloquen las llaves {}
    nombre = input("ALUMNO {}: ".format(i))

    #Slicite la cantidad de cursos que va a matricular el estudiante
    M = int(input("Solicitar que ingrese la cantidad de cursos : "))

    #crear una lista vacia para guardar la inf de los cursos
    cursos = []
    #contador para recorrer los cursos
    j = 1

    #while para ingresar la inf de los cursos
    while j <= M:
       #solicitar el nombre del curso
       curso_nombre = input("CURSO {}: ".format(j))

       #agregar el nombre del curso a la lista de cursos
       cursos.append(curso_nombre)

       #incrementar el contador de cursos
       j += 1

    #crear un diccionario con la informacion del estudiante
    #guardar los datos: el nombre y la lista de cursos
    estudiante ={
        "nombre": nombre,
        "cursos": cursos
    }

    #agregamos el diccionario del estudiante a la lista de estudiantes
    estudiantes.append(estudiante)

    # incrementar el contador de estudiantes
    i += 1

#mostrar la infomacion 
print("\n ***** LISTADO DE ESTUDIANTES *****")

#reiniiar el contador para recorrer los estudiantes registrados
i= 0
# ciclo para recorrer los estudiantes registrados
while i < len(estudiantes):
    #mostrar nombre del estudiante 
    print("\n Estudiante: ", estudiantes[i]["nombre"])
    
    #reiniciar contador para recorrer a los cursos
    j = 0

    #ciclo while para recorrer a la lista de cursos
    while j < len(estudiantes[i]["cursos"]):
        #mostrar el numero del curso y su nombre
        print("Curso", j+1, ":", estudiantes[i]["cursos"][j])

        #incrementamos el contador de cursos
        j += 1

    #incrementamos el contador de estudiantes
    i += 1