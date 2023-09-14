class DB():
    data_clientes = {
        1: {
            "user": "Enzo",
            "password": 123
        }

    }


    data_productos = {
        1: {
            "codigo": 1,
            "prod": "Pan",
            "precio": 300,
        },
        2: {
            "codigo": 2,
            "prod": "Arroz",
            "precio": 700,
        },
        3: {
            "codigo": 3,
            "prod": "Cafe",
            "precio": 500,
        },
        4: {
            "codigo": 4,
            "prod": "Fideos",
            "precio": 400,
        },
    }

    def obtener_producto(self, codigo):
        
        try:
            code = int (codigo)
        except ValueError:
            return{}
        
        if code in DB.data:
            return DB.data[code]

class Cliente: 
    def __init__ (self, user, password, ):
        self.user = user
        self.password = password


    

class Producto:

    cantidad = 0

    def __init__(self, codigo, precio, prod):
        self.codigo = codigo
        self.precio = precio
        self.prod = prod
        Producto.cantidad += 1
        
    
    def muestra_producto(self):
        print(f"{self.prod}: $ {self.precio}")
    
    def __add__(self, ):
        self.muestra_producto()
    
    def __del__(self):
       Producto.cantidad -= 1
    

class Pedido:
    def __init__(self):
        self.lista_pedido = []
        self.cantidad_total = 0

    def agrega_producto(self, codigo):
        codigo, precio, prod,   = db.obtener_producto(codigo)
        producto = Producto(codigo, precio, prod)
        self.lista_pedido.append(producto)

    def elimina_producto(self):
        pass

    def lista_final(self):
        pass

    def pagar(self):
        print(f"total a pagar: {self.lista_final()}")

db = DB()
while True:

    pedido = Pedido()

    while True:
        codigo = input("Ingrese codigo o \"P\" para pagar:").strip()

        if codigo.upper() == "P":
            pedido.pagar()
        
        data_productos = db.obtener_producto(codigo)
        if data_productos:
            producto = Producto(data_productos["codigo"], data_productos["precio"], data_productos["prod"])
            print(f"Cantidad de productos añadidos: {Producto.cantidad}")
            pedido.agrega_producto(producto)
        

