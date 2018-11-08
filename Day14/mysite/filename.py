# execute python manage.py shell < filename.py


from django.template import Context
from django.template import Template
t = Template("My name is {{name}}")
c = Context({"name": "Pradeep"})
List1 = ["Pradeep",'dinesh','ezhil']
for i in List1:
    print(t.render(Context({'name':i})))
person1 = {'name': 'Pradeep', 'age':23}
t = Template('{{person.name}} is {{person.age}} years old.')
c= Context({"person":person1})
print(t.render(c))

class Person(object):
    def __init__(self,first_name,last_name):
        self.first_name,self.last_name= first_name, last_name

t= Template('Hello, {{person.first_name}} {{person.last_name}}')
c = Context({'person':Person('Pradeep','Padmanaban')})
print(t.render(c))

t= Template("{{var}} -- {{var.upper}} -- {{var.isdigit}}")
print(t.render(Context({'var':'Hello'})))

t= Template("Item 2 is {{items.2}}.")
c = Context({'items': ["apples",'bananas','carrots']})
print(t.render(c))

t=Template('My name is {{person.first_name}}.')

class SilentAssertionError(AssertionError):
    silent_variable_failure = True
    
class PersonClass3:
    def first_name(self):
        raise SilentAssertionError
p = PersonClass3()
print(t.render(Context({'person':p})))