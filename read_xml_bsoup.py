from bs4 import BeautifulSoup


def read_xml_bsoup(xml_filename):
    contents = open(xml_filename).read()
    soup = BeautifulSoup(contents, "xml")

    body = soup.find("body")

    head = body.find("head")
    title = ""
    if head:
        # head.name = "h1"
        title = head.text
        head.decompose()

    for lb in body.find_all("lb"):
        lb.name = "br"
        lb.attrs.clear()

    for p in body.find_all("p"):
        p.attrs.clear()
        p["class"] = "tei-p"

    for pb in body.find_all("pb"):
        pb.string = pb["n"]
        pb.attrs.clear()
        pb["class"] = "tei-pb"
        pb.name = "span"

    epigraph = body.find("epigraph")
    if epigraph:
        epigraph.name = "div"
        epigraph["class"] = "tei-epigraph"

    for supplied in body.find_all("supplied"):
        supplied.attrs.clear()
        supplied["class"] = "tei-supplied"
        supplied.name = "span"

    for surplus in body.find_all("surplus"):
        surplus.attrs.clear()
        surplus.name = "span"

    for note in body.find_all("note"):
        # note_text = note.text
        # footnote_number = note["n"].split("-", 1)[1]
        # note.string = footnote_number
        # note.attrs.clear()
        # note["class"] = "note"
        # note["rel"] = "footnote"
        # note["href"] = "#cite_note-" + footnote_number
        # note.name = "a"
        # note.name = "span"
        # create a new tag
        # ref = soup.new_tag("ref")
        # ref.append(note_text)

        # insert the new tag after the current tag
        # note.insert_after(ref)
        note.attrs.clear()
        note.name = "ref"
        note.string = note.text

    trailer = body.find("trailer")
    trailer.name = "div"
    trailer["class"] = "tei-trailer"

    content = str(body.find("div"))
    content += "<br/><hr/><br/>"
    content += "<references />"
    return (title, content)


xml_filename = "./SARIT-corpus-master/arunadatta-sarvangasundara.xml"

title, content = read_xml_bsoup(xml_filename)
print(title)
print(content)