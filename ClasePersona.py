'''Declara una clase abstracta Legislador que herede de la clase Persona, con un atributo
provinciaQueRepresenta (tipo String) y otros atributos.
Declara un método abstracto getCamaraEnQueTrabaja.
Crea dos clases concretas que hereden de Legislador: la clase Diputado y la clase Senador
que sobreescriban los métodos abstractos necesarios.
Crea una lista de legisladores y muestra por pantalla la cámara en que trabajan haciendo uso
del polimorfismo.'''

class persona():
    
    def __init__ (self, nombre, apellido, documento):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__documento=documento
    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def get_apellido(self):
        return self.__apellido
    def set_apellido(self, apellido):
        self.__apellido = apellido

    def get_documento(self):
        return self.__documento
    def set_documento(self, documento):
        self.__documento = documento

