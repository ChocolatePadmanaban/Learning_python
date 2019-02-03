# getting data from xml file


from xml.sax.handler import ContentHandler
from xml.sax import make_parser

# make_parser() --> to parse the streaming events

class Bfhandler(ContentHandler):
    def startElement(self,name,attr):
        if (name == "food"):
            self.name = attr.get("menuid");

    def endElement(self,name):
        if (name == "food"):
            print("%-8s " % (self.name))


food = Bfhandler()
saxparser = make_parser()
saxparser.setContentHandler(food)
datasource = open("breakfast.xml","r")
saxparser.parse(datasource)
datasource.close()