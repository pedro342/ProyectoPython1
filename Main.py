'''Declara una clase abstracta Legislador que herede de la clase Persona, con un atributo
provinciaQueRepresenta (tipo String) y otros atributos.
Declara un método abstracto getCamaraEnQueTrabaja.
Crea dos clases concretas que hereden de Legislador: la clase Diputado y la clase Senador
que sobreescriban los métodos abstractos necesarios.
Crea una lista de legisladores y muestra por pantalla la cámara en que trabajan haciendo uso
del polimorfismo.'''

#import ClasePersona, ClaseLegislador, ClaseDiputado, ClaseSenador
from ClasePersona import persona
from ClaseLegislador import legislador
from ClaseDiputado import diputado
from ClaseSenador import senador

legislador1 = legislador("andres","la mama","448283123","cordoba")
diputado1 = diputado("hola","sss","221314","baire")
senador1 = senador("","","","")

print(senador1.get_documento())
print(senador1.get_apellido())
print(senador1.get_nombre())
print(senador1.get_documento())