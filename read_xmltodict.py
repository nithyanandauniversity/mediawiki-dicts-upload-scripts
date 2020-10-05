# import xml.etree.ElementTree as ET
# import xmltodict

# # import json

# tree = ET.parse("./SARIT-corpus-master/jitari-nairatmyasiddhi.xml")
# xml_data = tree.getroot()
# print(xml_data)
# for e in tree.xpath("//text"):
#     print(e)

# xml_data = tree.getroot()

# xmlstr = ET.tostring(xml_data, encoding="utf8", method="xml")


# data_dict = dict(xmltodict.parse(xmlstr))

# print(data_dict)

# # with open("new_data_2.json", "w+") as json_file:
# #     json.dump(data_dict, json_file, indent=4, sort_keys=True)

# from xml.dom import minidom

import xmltodict
import pprint

pp = pprint.PrettyPrinter(indent=2)


contents = open("./SARIT-corpus-master/jitari-nairatmyasiddhi.xml").read()
# print(contents)
data_dict = dict(xmltodict.parse(contents))

# xmldoc = minidom.parse("./SARIT-corpus-master/jitari-nairatmyasiddhi.xml")
# print(data_dict)
# print(data_dict["TEI"]["text"])
pp.pprint(data_dict["TEI"]["text"])
