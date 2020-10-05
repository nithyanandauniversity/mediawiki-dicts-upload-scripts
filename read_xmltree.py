# import parsel

# xml = open("./SARIT-corpus-master/jitari-nairatmyasiddhi.xml").read()
# selector = parsel.Selector(xml)
# text_content = selector.xpath("//text").get()


# def replace_tag_by_div(str, tag_name):
#     str.replace("<" + tag_name + ">", '<div class="' + tag_name + '">')
#     str.replace("</" + tag_name + ">", "</" + tag_name + ">")


# text_content.replace('<lb ed="gb" />', "<br />")
# replace_tag_by_div(text_content, "epigraph")
# replace_tag_by_div(text_content, "trailer")

from lxml import etree as ET
import pprint

pp = pprint.PrettyPrinter(indent=2)

tree = ET.parse("./SARIT-corpus-master/jitari-nairatmyasiddhi.xml")

root = tree.getroot()

# replace all <lb /> line-break tags by <br /> tags
lb_list = tree.findall("//body//lb", root.nsmap)
print(len(lb_list))
for lb in lb_list:
    lb.tag = "br"
    lb.attrib.clear()
    lb.attrib["class"] = "tei-lb"

p_list = tree.findall("//body//p", root.nsmap)
print(len(p_list))
for p in p_list:
    p.attrib.clear()
    p.attrib["class"] = "tei-p"

pbN_list = tree.findall("//body//pb", root.nsmap)
print(len(pbN_list))
for pbN in pbN_list:
    pbN.text = pbN.get("n")
    pbN.attrib.clear()
    pbN.attrib["class"] = "tei-pb"
    pbN.tag = "span"

head = tree.find("//body//head", root.nsmap)
head.tag = "h1"

epigraph = tree.find("//body//epigraph", root.nsmap)
epigraph.tag = "div"
epigraph.attrib["class"] = "tei-epigraph"

supplied_list = tree.findall("//body//supplied", root.nsmap)
for supplied in supplied_list:
    supplied.attrib.clear()
    supplied.attrib["class"] = "tei-supplied"
    supplied.tag = "span"

surplus_list = tree.findall("//body//surplus", root.nsmap)
for surplus in surplus_list:
    surplus.attrib.clear()
    surplus.tag = "span"

notes_list = tree.findall("//body//note", root.nsmap)
for note in notes_list:
    note.text = note.get("n").split("-", 1)[1]
    note.attrib.clear()
    note.attrib["class"] = "note"
    note.attrib["rel"] = "footnote"
    # note.attrib["href"] = "TODOx"
    note.tag = "a"


trailer = tree.find("//body//trailer", root.nsmap)
trailer.tag = "div"
trailer.attrib["class"] = "tei-trailer"

tree = tree.find("//body", root.nsmap)
xml_string = ET.tostring(tree).decode("UTF-8")
print(xml_string)