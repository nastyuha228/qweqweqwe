class Human:
    def __init__(self, n, a, h):
        self.__name = n
        self.__age = a 
        self.__height = h 
        
    def print(self):
        print(f'Имя: {self.__name}')
        print(f'Возраст: {self.__age}')
        print(f'Рост: {self.__height}')
        print('-'*30)
        
    @property
    def name(self):
        return self.__name.upper()
        
    @name.setter
    def name(self, n):
        self.__name = n.capitalize()
        
    @property
    def age(self):
        return self.__age
        
    @age.setter
    def age(self, a):
        self.__age = a
    @property
    def height(self):
        return self.__height
        
    @height.setter
    def height(self, h):
        self.__height = h
        
p1 = Human ('да' , 11, 111)

p1.print()
p1.name = 'олег'
p1.age = 5
p1.height = 500
print(p1.name)
print(p1.age)
print(p1.height)
