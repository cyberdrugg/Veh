class Engine:
    def __init__(self, volume, title, mileage ):
        self.volume = volume
        self.title = title
        self.mileage = mileage

    def __str__(self):
        return f'volume - {self.volume} \n' \
               f'title - {self.title} \n' \
               f'mileage - {self.mileage} '
    def drive(self):
        return f'This engine can good drive for moto and auto'



class moto(Engine):
    def __init__(self, volume, title, mileage):
        super().__init__(volume, title, mileage)

    def __str__(self):
        return super(moto, self).__str__()


moto1 = moto(volume=1.6 , title='suzuki', mileage=584)
print(moto1)

class Auto(Engine):
    def __init__(self, volume, title, mileage):
        super().__init__(volume, title, mileage)

    def __str__(self):
        return super(Auto, self).__str__()

print('-'*50)
auto1 = Auto(volume=2.5,title='Hgjjgds',mileage=252)
print(auto1)

class Sportcar(Engine):
    def __init__(self, volume, title, mileage):
        super().__init__(volume, title, mileage)

    def __str__(self):
        return super(Sportcar, self).__str__()

print('-'*50)
sportcar = Sportcar(volume=4.5,title='porsche model x',mileage=556)
print(sportcar)