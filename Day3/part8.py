#creating Exceptin with intention

try:
    raise Exception('spam','eggs')
except Exception as inst:
        print(type(inst))
        print(inst.args)
        print(inst)