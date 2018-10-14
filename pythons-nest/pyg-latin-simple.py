# Codewar's single word Pyg Latin

def pyg_latin(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if str.lower() in vowels:
        return str.lower() + "way"
    elif str[0:3].lower() not in vowels and len(str) >= 4:
        return str[3:].lower() + str[0:3].lower() + "ay"
    elif str[0:2].lower() not in vowels and len(str) >= 4:
        return str[2:].lower() + str[0:2].lower() + "ay"
    else:
        return str[1:].lower() + str[0:1].lower() + "ay"


print(pyg_latin("dog"))
print(pyg_latin("Moth"))
print(pyg_latin("Ellie"))
print(pyg_latin("China"))
print(pyg_latin("throw"))
print(pyg_latin("pyg"))
print(pyg_latin(raw_input("Type in word to translate: ")))
