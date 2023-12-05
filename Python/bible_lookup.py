import csv
"""
Author      : Anderson Levasseur
Date        : 11-12-23
Description :  This program can be used to find verses in the bible
"""


print("Welcome to the Bible Lookup Program")
#imports csv into a dictionary
abrev = dict()
for row in csv.reader(open('BibleLookup/Bible_Abbreviations.csv', 'r')):
      abrev[row[0].upper()] = row[1].upper()

#Returns the start location of the book
def find_book(book, bible):
    book = "THE BOOK OF " + book
    for line in bible:
        if line[:-1] == book:
            return False
    return "book"

#Returns the line of the chapter
def find_chapter(chapter, bible):
    if book == "PSALMS":
        chapter = "PSALM " + chapter
    else:
        chapter = "CHAPTER " + chapter
    
    for line in bible:
        if line[:-1] == chapter:
            return False
        if 'THE BOOK OF' in line:
            return "chapter"
    return "chapter"

#Returns the line of the verse
def find_verse(verse, bible):
    for line in bible:
        if '\n' == line:
            return "verse"
        elif line.split()[0] == verse:
            return line
    return "verse"

#Prints the verse to the console with no more than 80 chars per line
def pretty_print(verse_err, book, chapt, verse):
    # handles error cases
    errs = {
        "book" : f"'{book}' not in the bible",
        "chapter" : f"{book} doesn't contain chapter {chapt}",
        "verse" : f"{book} {chapt} doesn't contain verse {verse}"
    }

    # if err print error
    if verse_err in errs:
        return errs.get(verse_err)

    verse_out = f"{book} {chapt}:{verse_err}"
    open('Biblelookup/verses.txt', 'a').write(verse_out)
    last_index = 0
    # find beginning of word before 80 and insert \n
    while last_index + 80 < len(verse_out):
        last_index = verse_out[:80 + last_index].rfind(' ')
        verse_out = verse_out[:last_index] + "\n" + verse_out[last_index:]
    return verse_out[:-1]

yes_no = { "Y" : True, "YES" : True, "N" : False, "NO" : False}

cont = True
while cont:
    bible = open('BibleLookup/Bible.txt', 'r') 

    book = input("What book would you like to read from : ")
    chapt = input("What chapter would you like : ")
    verse = input("What verse would you like : ")

    book = book.upper()
    book = abrev.get(book, book)

    verse_err = find_book(book, bible)
    if verse_err is False:
        verse_err = find_chapter(chapt, bible)
    if verse_err is False:
        verse_err = find_verse(verse, bible)
    
    print(pretty_print(verse_err, book, chapt, verse))
    
    valid_ans = False
    
    while not valid_ans:
        valid_ans = True
        ans = input("Would you like to look up another verse (Y/N)? ")
        cont = yes_no.get(ans.upper(), None)
        if cont == None:
            valid_ans = False
            print("Invalid response...\nLet's try this again")