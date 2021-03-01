'''
Spreadsheets often use this alphabetical encoding for its columns:
 "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Given a column number, return its alphabetical column id. 
For example, given 1, return "A". Given 27, return "AA".
'''
def columns(id, curStr):
    sheet= {}
    alphabet = "ZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i,j in enumerate(alphabet):
        sheet[i] = j
    if id < 27:
        newStr = sheet[id] + curStr
        return newStr
    newLetter = sheet[(id % 26)]
    newStr = newLetter + curStr
    return columns((id-1) // 26, newStr)

print(columns(999,''))
    
    