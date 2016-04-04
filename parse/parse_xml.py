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

#recursively go through the ET tree and at each level add the info if it is there
def form_dict(root):
    json_dict = {}
    #check if the text for the label is empty, if not, add it
    if root.text is not None and len(root.text.strip()) > 0:
        json_dict["text"] = root.text
    #check if there are a attributes and add them to the level
    if len(root.attrib) > 0:
        json_dict["attributes"] = root.attrib
    #Recurse for every child of this node
    for child in list(root):
        #If the child is already in our dictionary (like in the series of items), try to append or make a list
        if child.tag in json_dict:
            try:
                json_dict[child.tag].append(form_dict(child))
            except AttributeError:
                json_dict[child.tag] = [json_dict[child.tag], form_dict(child)]
        else:            
            json_dict[child.tag] = form_dict(child)
    return json_dict

if __name__ == '__main__':
    print "connecting..."
    xml = get_data('http://www.malwaredomainlist.com/hostslist/mdl.xml')
    #xml = open("mdl.xml", 'rb').read()
    print "done, parsing tree"
    root = ET.fromstring(xml)
    my_dict = form_dict(root)
    #now that we have a dict, dump it to a file
    fout = open("mdl.json", 'wb')
    json.dump(my_dict, fout)
    #pretty print out the dict for simpler reading
    pprint(my_dict)
