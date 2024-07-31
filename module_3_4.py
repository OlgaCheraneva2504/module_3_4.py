def single_root_words(root_word, *other_words):
    same_words = []
    lower_root_word = root_word.lower()
    list_other_words = list(other_words)

    for i in list_other_words:
        if i.lower() in lower_root_word or lower_root_word in i.lower():
            same_words.append(i)

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
result3 = single_root_words('ма', 'МАКар', 'мАмА', 'дубИНа', 'МашинА')
print(result1)
print(result2)
print(result3)