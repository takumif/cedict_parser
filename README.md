# cedict_parser
A small Python script for converting CC-CEDICT text file into a SQLite database. Sample data obtained from the [MDBG website](http://www.mdbg.net/chindict/chindict.php?page=cc-cedict), and licensed under [Creative Commons Attribution-Share Alike 3.0](http://creativecommons.org/licenses/by-sa/3.0/).

## Usage

`python cedict_parser.py path_to_cedict_text_file path_to_db_to_create_(optional)`

If no database file name is given, it defaults to `cedict.db`.

## Database Format

Table: **Entries**

|Attribute|Type|
|---------|----|
|traditional|TEXT|
|simplified|TEXT|
|pinyin|TEXT|
|english|TEXT|

Example data:

|Attribute|Value|
|---------|----|
|traditional|龜|
|simplified|龟|
|pinyin|gui1|
|english|tortoise/turtle|
