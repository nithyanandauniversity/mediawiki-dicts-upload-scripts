from create_page import create_page
from get_definitions_from_sqlite_db import get_definitions_from_sqlite_db

WORD = "a"
definitions = get_definitions_from_sqlite_db(WORD)
create_page(WORD, definitions)