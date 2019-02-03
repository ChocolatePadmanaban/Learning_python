#count the xml tags in a file

from xml.dom.minidom import parseString

def Count_Tags(filename_1='test.xml',tagname_1= 'out'):
    file = open(filename_1,'r')
    data = file.read()
    file.close()
    dom= parseString(data)
    return len(dom.getElementsByTagName(tagname_1))

if __name__ == '__main__':
    print(Count_Tags())