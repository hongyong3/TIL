# def shortcut(text):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     for vowel in vowels:
#         text = text.replace(vowel, "")
#     print(text)

# shortcut('tejrktriiiqjrkqfdsfjksdl')

def start_end(text):
    while type(text) == str:
        count = 0
        for i in text:
            if len(i) > 2 and i[0] == i[-1]:
                count += 1

print(start_end(['level', 'asdwe', 's', 'abceda', 'gsdwrtfg']))