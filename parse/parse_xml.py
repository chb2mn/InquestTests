import urllib2
import json
import re
import xml.etree.ElementTree as ET
import types
from pprint import pprint

def get_data(url):
    response = urllib2.urlopen(url)
    data = response.read()
    return data

def form_dict(root):
    json_dict = {}
    if root.text is not None and len(root.text.strip()) > 0:
        json_dict["text"] = root.text
    if len(root.attrib) > 0:
        json_dict["attributes"] = root.attrib
    for child in list(root):
        if child.tag in json_dict:
            try:
                json_dict[child.tag].append(form_dict(child))
            except AttributeError:
                json_dict[child.tag] = [json_dict[child.tag], form_dict(child)]
        else:            
            json_dict[child.tag] = form_dict(child)
    return json_dict

if __name__ == '__main__':
    #xml = get_data('http://www.malwaredomainlist.com/hostslist/mdl.xml')
    xml = open("mdl.xml", 'rb').read()
    root = ET.fromstring(xml)
    my_dict = form_dict(root)
    fout = open("mdl.json", 'wb')
    json.dump(my_dict, fout)
    pprint(my_dict)
