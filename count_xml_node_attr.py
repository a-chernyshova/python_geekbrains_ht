# -*- coding: utf-8 -*-
import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    amount = len(node.attrib)
    return amount + len(list((get_attr_number(child)) for child in node))

if __name__ == '__main__':
    tree = etree.parse('temp/test.xml')
    root = tree.getroot()
    print(get_attr_number(root))

# <feed xml:lang='en'>
#     <title>HackerRank</title>
#     <subtitle lang='en'>Programming challenges</subtitle>
#     <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
#     <updated>2013-12-25T12:00:00</updated>
# </feed>
