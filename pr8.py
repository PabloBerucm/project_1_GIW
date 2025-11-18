"""
TODO: rellenar

Asignatura: GIW
Práctica 8
Grupo: XXXXXXX
Autores: XXXXXX 

Declaramos que esta solución es fruto exclusivamente de nuestro trabajo personal. No hemos
sido ayudados por ninguna otra persona o sistema automático ni hemos obtenido la solución
de fuentes externas, y tampoco hemos compartido nuestra solución con otras personas
de manera directa o indirecta. Declaramos además que no hemos realizado de manera
deshonesta ninguna otra actividad que pueda mejorar nuestros resultados ni perjudicar los
resultados de los demás.
"""

###
### <DEFINIR AQUÍ LAS CLASES DE MONGOENGINE>
###

#importamos la librería y la conectamos a la base de datos
from mongoengine import *
connect("giw_mongoengine")

"""
chuleta de comprobaciones con regex
    ^ -> inicio de la cadena
    \d -> un dígito
    {} -> repeticiones de un elemento
    $ -> final de cadena
"""

#creamos la clase tarjeta
#se le aporta EmbeddedDocument porque es un atributo de un usuario, es decir, está comprendido en los datos del usuario
class Tarjeta(EmbeddedDocument):
    nombre = StringField(required=True, min_length=2)
    #con regex damos un patrón especial que debe cumplir el texto.
    #con el número validamos que tenga exactamente 16 dígitos
    numero = StringField(required=True, regex=r"^\d{16}$")
    mes = StringField(required=True, regex=r"^\d{2}$")
    year = StringField(required=True, regex=r"^\d{2}$")
    cvv = StringField(required=True, regex=r"^\d{3}$")

    #Las validaciones inteligentes se implementan por separado sobreescribiendo el método clean que se ejecuta antes de save y cuando se ejecuta validate
    def clean(self):
        #aquí solo tendremos que comprobar que nombre sea un string
        if not isinstance(self.nombre, str):
            raise ValidationError("Nombre debe ser str")
        

#crearemos una función para validar el dni del usuario evitando una función de usuario excesivamente extensa
def validar_dni(dni):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"   #secuencia oficial del DNI español
    #si la longitud no es válida, los 8 primeros dígitos no son números o el último dígito no está en mayúscula el dni no es válido
    if len(dni) != 9 or not dni[:8].isdigit() or not dni[-1].isalpha():
        return False
    numero = int(dni[:8])
    #si la letra es válida se devuelve true
    return dni[-1].upper() == letras[numero % 23]


#creamos el usuario, es un documento que se guarda en una colección
class Usuario(Document):
    dni = StringField(required=True, unique=True)
    nombre = StringField(required=True, min_length=2)
    apellido1 = StringField(required=True, min_length=2)
    apellido2 = StringField()
    f_nac = StringField(required=True)  #los tests trabajan con string, no datetime
    #el usuario puede tener varias tarjetas por lo que lo almacenamos en una lista
    tarjetas = EmbeddedDocumentListField(Tarjeta)
    pedidos = ListField(ReferenceField("Pedido"))

    def clean(self):
        #dni
        if not isinstance(self.dni, str) or not validar_dni(self.dni):
            raise ValidationError("DNI incorrecto")

        #f_nac, usaremos datetime para comprobar el formato de la fecha directamente
        import datetime
        try:
            datetime.datetime.strptime(self.f_nac, "%Y-%m-%d")
        except:
            raise ValidationError("Fecha incorrecta")
        
        #validar tarjetas
        #si ya está el método clean de las tarjetas sobreescrito para validarlas podemos una a una ir ejecutando el método validate
        if self.tarjetas:
            if not isinstance(self.tarjetas, list):
                raise ValidationError("tarjetas debe ser lista")
            for t in self.tarjetas:
                t.validate()

        #validar pedidos
        if self.pedidos:
            if not isinstance(self.pedidos, list):
                raise ValidationError("pedidos debe ser lista")
            for p in self.pedidos:
                p.validate()


#crear producto
class Producto(Document):
    codigo_barras = StringField(required=True, unique=True)
    nombre = StringField(required=True, min_length=2)
    categoria_principal = IntField(required=True, min_value=0)
    categorias_secundarias = ListField(IntField(min_value=0))

    def clean(self):
        #el código de barras debe ser string
        if not isinstance(self.codigo_barras, str):
            raise ValidationError("EAN debe ser str")

        #el código de barras debe ser un número y tener 13 dígitos
        if len(self.codigo_barras) != 13 or not self.codigo_barras.isdigit():
            raise ValidationError("EAN debe ser un número de 13 dígitos")
        
        """
        Validar el dígito de control:
            suma los dígitos en las posiciones impares, multiplica los dígitos en las posiciones pares por 3 
            y suma ambos resultados. Luego, encuentra la siguiente decena superior al total y réstale el total
        """
        nums = list(map(int, self.codigo_barras))
        suma_dig_imp = sum(nums[i] * (3 if i % 2 == 1 else 1) for i in range(12))
        control = (10 - (suma_dig_imp % 10)) % 10
        if control != nums[12]:
            raise ValidationError("Dígito de control incorrecto")
        
        #Validar categorías
        if self.categorias_secundarias:
            if not isinstance(self.categorias_secundarias, list):
                raise ValidationError("Categorías secundarias debe ser una lista")
            if self.categorias_secundarias[0] != self.categoria_principal:
                raise ValidationError("Categoría principal debe encontrarse en el primer lugar de las categorías secundarias")


class Linea(EmbeddedDocument):
    num_items = IntField(required=True, min_value=1)
    precio_item = FloatField(required=True, min_value=0)
    nombre_item = StringField(required=True, min_length=2)
    total = FloatField(required=True, min_value=0)
    producto = ReferenceField(Producto, required=True)

    def clean(self):
        #Validamos el nombre
        if not isinstance(self.nombre_item, str):
            raise ValidationError("nombre del item debe ser str")

        #validación del total
        if abs(self.total - (self.num_items * self.precio_item)) > 0.0001:
            raise ValidationError("total incorrecto")

        #nombre_item no coincide con producto.nombre
        if self.producto and self.nombre_item != self.producto.nombre:
            raise ValidationError("nombre_item no coincide con producto.nombre")


class Pedido(Document):
    total = FloatField(required=True, min_value=0)
    fecha = StringField(required=True)
    lineas = EmbeddedDocumentListField(Linea, required=True)

    def clean(self):
        #fecha debe ser str
        if not isinstance(self.fecha, str):
            raise ValidationError("fecha debe ser str")

        #lineas debe ser una lista no vacía
        if not isinstance(self.lineas, list) or len(self.lineas) == 0:
            raise ValidationError("lineas debe ser una lista no vacía")
        
        #validar cada línea (lo que llama a su método clean)
        for l in self.lineas:
            l.validate()

        #calcular suma total
        suma = sum(l.total for l in self.lineas)
        if abs(self.total - suma) > 0.0001:
            raise ValidationError("total incorrecto")

        #comprobar que no haya productos repetidos
        prods = [l.producto for l in self.lineas]
        if len(prods) != len(set(prods)):
            raise ValidationError("no puede haber productos repetidos")



"""
Tenemos un último problema, cuando se borra un Pedido, este debe desaparecer de la lista de pedidos del usuario.
Esto lo podemos lograr con una señal pre_delete para borrar el pedido de la lista del usuario antes de borrar el objeto pedido.
"""
from mongoengine import signals

def borrar_pedido(sender, document, **kwargs):
    #document es el pedido que se está borrando
    usuarios = Usuario.objects(pedidos=document)
    for u in usuarios:
        u.pedidos = [p for p in u.pedidos if p != document]
        u.save()

#conectamos la señal al pre_delete para que se ejecute nuestra función auxiliar
signals.pre_delete.connect(borrar_pedido, sender=Pedido)
