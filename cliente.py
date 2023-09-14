class DB():
    data_clientes = {
        "Cliente1": {
            "nombre": "",
            "mail": "",
            "edad": 32
        },
        "Cliente2": {
            "nombre": "",
            "mail": "",
            "edad": 21
        }

    }
    data_productos = {
        "local": "",
        "producto": "",
    }

class Cliente: 
    def __init__ (self, nombre, mail, edad):
        self.nombre = nombre
        self.mail = mail
        self.edad = edad
    
    def mostrar_cliente(self):
        print(f"El usuario de {self.nombre} se ha creado")
    
    def __str__(self):
        print(self.mostrar_cliente)
