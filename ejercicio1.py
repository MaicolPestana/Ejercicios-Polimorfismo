class Transporte():
    def Tipo_transporte(self):

        pass

class Coche(Transporte):
    def Tipo_transporte(self):
        return "Este es un transporte terrestre"
    
class Avion(Transporte):
    def Tipo_transporte(self):
        return "Este es un transporte Aereo"
    
class Barco(Transporte):
    def Tipo_transporte(self):
        return "Este es un transporte Maritimo"
    
        


jet = Avion()
Ferrari = Coche()
Yate = Barco()


print(jet.Tipo_transporte())
print(Ferrari.Tipo_transporte())
print(Yate.Tipo_transporte())

