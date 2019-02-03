# Align with four space

def Alignment_of_file(filename_1):
    Filename_1 = open(filename_1)
    Input_1 = ['    '+ i.strip()+'\n' for i in Filename_1]
    Filename_1.close()
    Filename_2 = open('Output_1.txt','w')
    Filename_2.writelines(Input_1)
    Filename_2.close()


def Alignment_using_Genrator(filename_1):
    Filename_1 = open(filename_1)
    def gen_a(Filename_1):    
        for i in Filename_1:
            yield '    '+i.strip()+'\n'
    x = gen_a(Filename_1)
    Filename_2 = open('Output_1.txt','w')
    for i in x:
        Filename_2.write(next(x))
    Filename_2.close()
    Filename_1.close()

def Alignment_with_limit(filename_1, n):
    Filename_1 = open(filename_1)
    filename_1 = Filename_1.readlines()
    Input_1 = [i.strip() for i in filename_1]
    Input_1 = ''.join(Input_1)
    lenght_1 = (len(Input_1)//n) +1
    Filename_2 = open('Output_1.txt','w')
    for i in range(lenght_1):
        Filename_2.write('    '+Input_1[i*n: (i+1)*n]+'\n')
    Filename_2.write('    '+Input_1[(lenght_1+1)*n:]+'\n')
    Filename_2.close()        

if __name__ == "__main__":
    Alignment_with_limit('Input__1.txt', 50)