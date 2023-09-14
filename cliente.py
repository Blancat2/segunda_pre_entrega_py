class Cliente: 
     

    def __init__ (self, nombre, mail, edad):
        self.nombre = nombre
        self.mail = mail
        self.edad = edad
        

    def guardar_datos(self):

    
    def mostrar_cliente(self):
        print(f"El usuario de {self.nombre} se ha creado")
    
    def compra(self):
        pass
    
    def __str__(self):
        print(self.mostrar_cliente)
