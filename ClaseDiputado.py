'''Declara una clase abstracta Legislador que herede de la clase Persona, con un atributo
provinciaQueRepresenta (tipo String) y otros atributos.
Declara un método abstracto getCamaraEnQueTrabaja.
Crea dos clases concretas que hereden de Legislador: la clase Diputado y la clase Senador
que sobreescriban los métodos abstractos necesarios.
Crea una lista de legisladores y muestra por pantalla la cámara en que trabajan haciendo uso
del polimorfismo.'''

from abc import abstractmethod
from ClaseLegislador import legislador

class diputado(legislador):
    
    def __init__(self, nombre, apellido, documento, provincia):
        super().__init__(nombre, apellido, documento, provincia)
                
    def camara_que_trabaja(self):
        print("trabaja en camara 1")