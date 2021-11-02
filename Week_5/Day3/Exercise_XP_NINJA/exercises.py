# Exercise 1 : Temperature

class Temperature:
    def __init__(self,temp):
        self.temp = temp

class Celsius(Temperature):
    def __init__(self,temp):
        super().__init__(temp)
    
    def convert(self,unit):
        if unit=="Kelvin":
            return float(self.temp+273.15)
        else:
            return float(self.temp*9/5+32)

class Kelvin(Temperature):
    def __init__(self,temp):
        super().__init__(temp)

    def convert(self,unit):
        if unit=="Celsius":
            return float(self.temp-273.15)
        else:
            return float((self.temp-273.15)*9/5+32)


class Fahrenheit(Temperature):
    def __init__(self,temp):
        super().__init__(temp)

    def convert(self,unit):
        if unit=='Celsius':
            return float((self.temp-32)*5/9)
        else:
            return float((self.temp-32)*5/9+273.15)


cel1 = Celsius(25)
far1 = Fahrenheit(77)
kel1 = Kelvin(298.15)
print(cel1.convert("Kelvin"))
print(cel1.convert("Farheneit"))
print(kel1.convert("Celsius"))
print(kel1.convert("Farheneit"))
print(far1.convert("Kelvin"))
print(far1.convert("Celsius"))

# Exercise 2: In The Quantum Realm
import random

class QuantumParticle:
    def __init__(self, position=500, momentum=0.5, spin=1/2):
        self.x = position
        self.y = momentum
        self.p = spin

    def position(self):
        self.x = random.randint(1,10000)
        print(f'position: {self.x}')
    
    def momentum(self):
        self.y = random.uniform(0,1)
        print(f'momentum: {self.y}')
    
    def spin(self):
        self.p = random.choice([-0.5,0.5])
        print(f'spin:{self.p}')
    
    def disturbance(self):
        self.momentum()
        self.position()
        print('Quantum Interferences!!')
    
    def __repr__(self):
        return f'position:{self.x}\nmomentum:{self.y}\nspin:{self.p}'

    def entangle(self, other):
        if isinstance(other,QuantumParticle):
            if self.p*(-1) == other.p:
                print('Spooky Action at a Distance !!')
            else:
                self.p = other.p*(-1)
                print('Particles are now in quantum entanglement')
        else:
            raise Exception('It must be a quantum particule')


p1 = QuantumParticle(spin=0.5)
p2 = QuantumParticle(spin=-0.5)
p1.momentum()
p1.position()
p1.spin()
p1.disturbance()
p1.entangle(p2)