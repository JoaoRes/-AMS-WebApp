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
    img = 'images/jante.jpg'
    p = Product(name, price, info0, info1, country, brand, model, weight, unidades, cond, comments, img)
    db.append(p)

    name = "Tire"
    price = 350
    info0 = "Pneu de 450 cm de diaâmetro, adequeada a qualquer tipo de carro para rodas dessas dimensões"
    info1 = "Roda de material de qualidade q apresenta uma longa duração e resistência"
    country = "Portugal"
    brand = "Armstrong"
    model = "TT1"
    weight = 15
    unidades = 1
    cond = "Nova"
    comments = "Não é recomendável o seu uso a não ser que a sua roda tenha precisamente este tamanho"
    img = 'images/tire.png'
    p = Product(name, price, info0, info1, country, brand, model, weight, unidades, cond, comments, img)
    
    db.append(p)

    name = "Radio"
    price = 250
    info0 = "Radio com 10 estações adequado e som de qualidade adequado ao seu carro"
    info1 = "Com um som expansivo e abrangente é a peça ideia para o seu carro"
    country = "Espanha"
    brand = "Blaukpunt"
    model = "AL201"
    weight = 95
    unidades = 2
    cond = "Nova"
    comments = "Rádio adequado a qualquer modelo de carro e fácil de instalar"
    img = 'images/radio.jpeg'
    p = Product(name, price, info0, info1, country, brand, model, weight, unidades, cond, comments, img)
    
    db.append(p)

    name = "Spoiler"
    price = 350
    info0 = "Spoiler adequado à traseira do seu carro"
    info1 = "Ideal para quem quer dar nas vistas na estrada"
    country = "Turquia"
    brand = "Refit"
    model = "122FTP"
    weight = 105
    unidades = 1
    cond = "Usada"
    comments = "Apenas adequado à traseira dos carros da marca audi etc"
    img = 'images/spoiler.jpg'
    p = Product(name, price, info0, info1, country, brand, model, weight, unidades, cond, comments, img)
    
    db.append(p)

    name = "Tail Lights"
    price = 250
    info0 = "Luzes traseiras para os modelos Ford Focus de 2007"
    info1 = "Com uma potência de 200 watts é o produto ideal para garantir a sua segurança na estrada"
    country = "Itália"
    brand = "IPCW"
    model = "model2 gen0"
    weight = 40
    unidades = 1
    cond = "Usada"
    comments = "Importante referir q apenas a use com os modelos especificados"
    img = 'images/tail.jpg'
    p = Product(name, price, info0, info1, country, brand, model, weight, unidades, cond, comments, img)
    
    db.append(p)

    name = "Bateria"
    price = 950
    info0 = "Bateria da marca Traveller para o seu carro"
    info1 = "Ideal para qualquer modelo BMW e Audi"
    country = "Portugal"
    brand = "Traveller"
    model = "T-35"
    weight = 90
    unidades = 1
    cond = "Novo"
    comments = "Nunca antes usada em condição nova"
    img = 'images/traveller.jpeg'
    p = Product(name, price, info0, info1, country, brand, model, weight, unidades, cond, comments, img)
    
    db.append(p)

    name = "Rearviewmirror"
    price = 450
    info0 = "Espelho retrovisor adequado a qualquer modelo de carro"
    info1 = "A segurança na estrada é o mais importante  e este produto é indispensável no seu carro"
    country = "Portugal"
    brand = "RallyPanoramic"
    model = "Non-especified"
    weight = 10
    unidades = 1
    cond = "Novo"
    comments = "Adequado a qualquer modelo e extremamente simples de instalar"
    img = 'images/rearviewmirror.jpg'
    p = Product(name, price, info0, info1, country, brand, model, weight, unidades, cond, comments, img)
    
    db.append(p)

    name = "Motor para carro"
    price = 1500
    info0 = "Motor da honda para modelos da honda"
    info1 = "Motor poderoso de 14 cavalos para aqueles que pretendem demonstrar a potência do seu carro"
    country = "Japão"
    brand = "Honda"
    model = "FF1"
    weight = 900
    unidades = 1
    cond = "Novo"
    comments = "Não tente instalar esta peça sozinho se não souber como"
    img = 'images/engine.jpg'
    p = Product(name, price, info0, info1, country, brand, model, weight, unidades, cond, comments, img)
    
    db.append(p)

    name = "Capô"
    price = 200
    info0 = "Capõ de côr cinzento azulado de 350 cm de largura e 450 de comprimento"
    info1 = "Compativel com modelos golf da volkswagen"
    country = "Alemanha"
    brand = "volkswagen"
    model = "vg5"
    weight = 100
    unidades = 1
    cond = "Novo"
    comments = "Não tente instalar esta peça sozinho se não souber como"
    img = 'images/hood.jpg'
    p = Product(name, price, info0, info1, country, brand, model, weight, unidades, cond, comments, img)
    
    db.append(p)