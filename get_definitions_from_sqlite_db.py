from pathlib import Path
import sqlite3

from create_page import create_page

SQLITE_DB_FILE = Path("./data/sanskrit-dictionary.sqlite")

# needed to enable tuples indices access through their name not index
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_definitions_from_sqlite_db(word):
    conn = sqlite3.connect(SQLITE_DB_FILE)
    # enable access tuples indices through their name not index
    conn.row_factory = dict_factory
    c = conn.cursor()

    # word = "a"
    # Do this instead
    t = (word,)

    query = """
        SELECT key, lnum, data, name as book_name
        FROM data da
        INNER JOIN dictionaries di
        ON da.source = di.id
        WHERE key=? AND da.source = 'WIL'
        ORDER BY name, lnum
    """
    c.execute(query, t)
    # print(c.fetchall()['data'])

    definitions = {}
    for row in c.execute(query, t):
        if row["book_name"] not in definitions:
            definitions[row["book_name"]] = []
        # print()
        # print(row)
        definitions[row["book_name"]].append(row["data"])
        # print(row["data"])
        # break

    content = ""
    for book_name, definitions in definitions.items():
        content += "<table><tr><th>" + book_name + "</th></tr>"
        for definition in definitions:
            content += "<tr><td>" + definition + "</td></tr>"
        content += "</table>"

    # create_page(WORD, content)

    # c.execute('SELECT DISTINCT source FROM data')
    # print(c.fetchall())

    # Save (commit) the changes
    # conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()

    return content