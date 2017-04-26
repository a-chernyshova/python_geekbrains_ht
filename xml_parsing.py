# -*- coding: utf-8 -*-
import xml.etree.ElementTree as etree

def get_to_for(file):
    tree = etree.parse(file)
    #get root element
    root = tree.getroot()
    for child in root:
        if child.tag == 'to':
            print(child.tag, ':', child.text)
        elif child.tag == 'from':
            print(child.tag, ':', child.text)
        elif child.tag == 'body':
            body = child.text
        else:
            print('Extra node:', child.tag)
    return body

try:
    print('Test1:')
    get_to_for('temp/test.xml')
except etree.ParseError as ParseError:
    print('Check file structure:', ParseError)

try:
    print('Test2:')
    get_to_for('temp/test3.xml')
except etree.ParseError as ParseError:
    print('Check xml file structure:', ParseError)

# print('Root:', root)
# #print root tag
# print(root.tag)
# print(root.attrib)
# #print attrib any element by number
# print(root[3].attrib)
# print(len(root))
# tag_list = []
# for child in root:
#     print(child, child.tag)
#     tag_list.append(child.tag)
# print(tag_list)
# #todo: learn how does work findall
# print(len(root.findall('{http://www.w3.org/XML/1998/namespace}lang')))
# print(root[2].text)
# #todo: learn how to parse broken xml
