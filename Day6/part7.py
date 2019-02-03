# pickling(a way of storing objects)



class student:
    def __init__(self,name, n=0):
        self.name = name
        self.age = n
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name



import pickle
f=open("student.bin",'wb')
stu1 = student("Pradeep",26)
pickle.dump(stu1,f)
f.close()
f = open("student.bin","rb")
stu5 = pickle.load(f)
print(stu5.get_name()+ "'s age is", stu5.get_age())