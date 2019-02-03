#Set operations in dictionaries


#union
#intersection
#subraction
#symmetric diff (uncommon elements only)
#is Subset

A = {'a':5, 't': 3,'c':4,'e': 7}
B = {'a': 3,'l': 9, 'e':1, 'd': 6}

#Union

def Union1(a, b):
    answer1 = {}
    seta, setb = set(a), set(b)
    answer2 = list(seta | setb)
    for i in answer2:
        if (i in seta) and (i in setb): 
            answer1[i] = [a[i], b[i]]
        elif i in seta: 
            answer1[i]= a[i]
        elif i in setb: 
            answer1[i]= b[i]
    return answer1

print('the union of A and B is',Union1(A,B))

#Intersection

def Intersection1(a, b):
    answer1 = {}
    seta, setb = set(a), set(b)
    answer2 = list(seta & setb)
    for i in answer2:
        answer1[i]= [a[i],b[i]]
    return answer1

print("Intersection of A and B is ",Intersection1(A,B))

#subraction
def Subraction1(a,b):
    answer1 = {}
    answer2 =list(set(a)-set(b))
    for i in answer2:
        answer1[i]= a[i]
    return answer1

print("A subract B is",Subraction1(A,B))

# Symmetric Difference:

def SymDiff(a,b):
    return Subraction1(Union1(a,b), Intersection1(a,b))

print("Symmetric Difference of A and B is ", SymDiff(A,B))

#Is Subset
def Issubset(a,b):
    seta, setb = set(a),set(b)
    return seta.issubset(setb)

print("Is A subset of B", Issubset(A,B))