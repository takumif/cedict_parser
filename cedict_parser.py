import sys
import codecs
import sqlite3

class Entry(object):
    def __init__(self, trad, simp, pin, eng):
        self.traditional = trad
        self.simplified = simp
        self.pinyin = pin
        self.english = eng

def write(entries, dbName):
    db = sqlite3.connect(dbName)
    c = db.cursor()

    c.execute("create table entries (traditional text, simplified text, pinyin text, english text)")

    def entryToTuple(entry):
        return (entry.traditional, entry.simplified, entry.pinyin, entry.english)

    entryTuples = map(entryToTuple, entries)
    c.executemany("insert into entries values (?,?,?,?)", entryTuples)

    db.commit()
    db.close()

def parse(fileName):
    entries = []

    with codecs.open(fileName, "r", "utf-8") as f:
        for line in f:
            if (len(line) > 0 and line[0] != "#"):
                split = line.split()
                trad = split[0]
                simp = split[1]
                pin = line[line.index("[") + 1 : line.index("]")]
                eng = line[line.index("/") + 1 :]
                entry = Entry(trad, simp, pin, eng)

                entries.append(entry)

    return entries

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Usage: python cedict_parser.py path_to_cedict_text_file path_to_db_to_create_(optional)")
    else:
        fileName = sys.argv[1]
        dbName = "cedict.db" if len(sys.argv) < 3 else sys.argv[2]
        entries = parse(fileName)

        if (len(entries) == 0):
            print("Invalid cedict text file")
        else:
            write(entries, dbName)
            print("Wrote %d entries into %s" % (len(entries), dbName))