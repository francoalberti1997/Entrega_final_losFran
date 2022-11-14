

class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def __str__(self):
        return("esta es la clase Persona") 
    

class Experiencia():
    def __init__(self, evaluacion="buena"):
        self.evaluacion = evaluacion
    
    def __str__(self):
        return("esta es la clase Experiencias") 

    def crear_experiencia(self):
        


class Crud(Experiencia, Persona):
    objeto = Persona        

    def __str__(objeto):
        return print(objeto)

a = Crud()

print(a)

