# fetching paragraphs
def FetchPara(filename):
    Filename_1 = open(filename)
    text_1 = ''
    for i in Filename_1:
        text_1 += i
    text_1 = text_1.split('\n\n')
    Filename_1 = [x.strip() for x in text_1]
    return Filename_1
    
if __name__ =='__main__':
    print(FetchPara('temp.txt'))