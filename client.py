class Client:
    def __init__(self, username, address, email, password):
        self.username = username
        self.address = address
        self.email = email
        self.password = password
    def __str__():
        return "CLIENT\nName: "+str(self.username)+" \nAddress: "+str(self.address)+"\nEmail: "+str(self.email)+"\nPassword: "+str(self.password)
    def __eq__(self, other):
        return self.email == other.email


class Product:
    def __init__(self, name, price, info0, info1, country, brand, model, weight, unidades, cond, comments, img):
        self.name = name
        self.price =  price
        self.info0 = info0
        self.info1 = info1
        self.country = country
        self.brand = brand
        self.model = model
        self.weight = weight
        self.unidades = unidades
        self.cond = cond
        self.comments = comments
        self.img = img


def fillDataBase(db):
    name = "Wheel Dine"
    price = 500
    info0 = "Wheel dine de 250 cm de diaâmetro, adequeada a qualquer tipo de carro"
    info1 = "Cor metalizada e resistente a altas temperaturas"
    country = "EUA"
    brand = "Axe Wheels"
    model = "FTP1"
    weight = 45
    unidades = 5
    cond = "Usadas"
    comments = "Apesar se se encontrarem usadas são jantes de muito alta qualidade para elevar o estilo do seu carro a outro nivel"
    img = "images/jante.jpg"
    p = Product(name, price, info0, info1, country, brand, model, weight, unidades, cond, comments, img)
    db.append(p)
    db.append(p)
    db.append(p)