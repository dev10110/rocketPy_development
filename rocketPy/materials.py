from . import ureg, Q_

class Material():

    def __init__(self, name):

        self.name = name

        self.density = 0*ureg.km/(ureg.m**3)


    def __repr__(self):

        return f'{self.name}: (Material))'

class Aluminium(Material):

    def __init__(self, name='Al-6061-T6'):

        super().__init__(name=name)

        self.density = 2.7*ureg.g/(ureg.cm**3)
        self.tensile_mod = 69*ureg.GPa
        self.tensile_strength = 270*ureg.MPa
        self.max_temp = 420*ureg.degK


class PLA(Material):

    def __init__(self, name='PLA'):

        super().__init__(name=name)

        self.density = 1.05*ureg.g/(ureg.cm**3)


class Phenolic(Material):

    def __init__(self, name='Phenolic'):

        super().__init__(name=name)

        self.density = 0.95*ureg.g/(ureg.cm**3)

class Acrylic(Material):

    def __init__(self, name='Acrylic'):

        super().__init__(name=name)

        self.density = 1.19*ureg.g/(ureg.cm**3)

class Plywood(Material):

    def __init__(self, name='Plywood'):

        super().__init__(name=name)

        self.density = 0.63*ureg.g/(ureg.cm**3)

class Polycarbonate(Material):

    def __init__(self, name='Polycarbonate'):

        super().__init__(name=name)

        self.density = 1.2*ureg.g/(ureg.cm**3)
