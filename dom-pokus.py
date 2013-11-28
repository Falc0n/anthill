file = open('foobar.htm').read()
#dom = dom.parse(file)

foo = dom.getElementsByTagName('Bar')

def content(element): #idk whether this works or not
    return element.text, element.attrib
