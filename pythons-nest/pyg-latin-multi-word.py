# Codewar's Multi Word Pyg Latin

def pyg_latin(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    list_of_words = str.split()
    space = ' '

    translated_words = [];

    for word in list_of_words:
        if word[0].lower() in vowels:
            translated_words.append(word.lower() + "way")
        elif word[0:2].lower() not in vowels and len(word) >= 4:
            translated_words.append(word[2:].lower() + word[0:2].lower() + "ay")
        else:
            translated_words.append(word[1:].lower() + word[0:1].lower() + "ay")

    return space.join(translated_words)

print(pyg_latin("This does indeed work"))
print(pyg_latin("Adventures with the Scary Hissy Boi"))
print(pyg_latin("The throw went through the old thatch roof"))
