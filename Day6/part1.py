# Adapter class in python(Adpter class interfaces with mutiple class)

class Computer:
    def __init__(self,n):
        self.name=n
    def __str__(self):
        return 'the {} computer'.format(self.name)
    def execute(self):
        return 'execute a program'

class Synthesizer:
    def __init__(self,n):
        self.name = n
    def __str__(self):
        return 'the {} synthesizer'.format(self.name)
    def play(self):
        return 'can play a song'

class Human:
    def __init__(self,n):
        self.name=n
    def __str__(self):
        return "the  {} human".format(self.name)
    def speak(self):
        return 'can speak works'
# adapter class can inteface with multiple class
class Adapter:
    def __init__(self,o,adapter_methods):
        self.obj = o # object variable is created
        self.__dict__.update(adapter_methods) # inbuit dict function is used as variable
    def __str__(self):
        return str(self.obj)

objects = [Computer('Asus')]

synth = Synthesizer('moog')
objects.append(Adapter(synth, dict(execute=synth.play)))

human = Human('bob')
objects.append(Adapter(human, dict(execute=human.speak)))
for i in objects:
    print('{}  {}'.format(str(i), i.execute()))