from create_page import create_page
from get_definitions_from_sqlite_db import get_definitions_from_sqlite_db
from read_xml_bsoup import read_xml_bsoup


def format_content():
    for book_name, definitions in definitions.items():
        content += "<table><tr><th>" + book_name + "</th></tr>"
        for definition in definitions:
            content += "<tr><td>" + definition + "</td></tr>"
        content += "</table>"


title = "a"
# content = get_definitions_from_sqlite_db(WORD)

title, content = read_xml_bsoup()
create_page(title, content)