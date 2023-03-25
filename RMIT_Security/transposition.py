text = "CMOBBZLXHR, EHTMPMDUKL XZMDLTHTQR MUL ZLDULMZ XDZ ZCCKMKZLMR, UMMOBUMR ULF GZMOBKXR TC U SKFZ BULQZ TC KLFOGXBKZG ULF XDZKB GOWWHR MDUKL CBTY YULOCUMXOBZB XT MTLGOYZB. MYULR KLFOGXBKZG KLMHOFKLQ XDZ UOXTYTXKNZ, ZHZMXBTLKM MTYYZBMZ ULF YZFKMUH KLFOGXBKZG MUL OXKHKGZ XDZ EZLZCKXG TC EHTMPMDUKL KL NUBKTOG XUGPG GOMD UG WBTNKLQ XDZ UOXDZLXKMKXR TC UOXTYTXKNZ WUBXG, NUHKFUXKLQ U XBULGCZB TC WURYZLXG TB YUKLXUKLKLQ XDZ AOUHKXR TC WDUBYUMZOXKMUH WBTFOMXG. OTLZ KYWTBXULX KLFOGXBR SDKMD UCCZMXG WZTWHZ QHTEUHHR KG XDZ CTTF WBTFOMXKTL KLFOGXBR, SDKMD BZAOKBZG WBTFOMXG GOMD UG NZQZXUEHZG, CBOKXG, WTOHXBR ULF YZUXG LZZF XT EZ GTOBMZF CBTY CUBYG ULF EZ TC XTW AOUHKXR ER XDZ XKYZ XDZR BZUMD MTLGOYZBG. TXDOG XDZ CTTF WBTFOMXKTL KLFOGXBR MTOHF EZ ZLDULMZF SKXD EHTMPMDUKL ULF EZMTYZG U GYUBX KLFOGXBR, KYWBTNKLQ XDZ AOUHKXR TC XDZKB WBTFOMXG."





# 1 get the count of each set of letters in the string
from collections import Counter
org_text_freq = (Counter(text))

# print(type(text_freq))

# for x in text_freq:
#     print(x)

# 2 iterate over the dictionary of letter fequencies and map them in order of the alphabet frequency
letter_freq = 'etaoinshrdlcumwfgypbvkj'

text_freq = 'ZXKULTMBGODFCHYRWEQNAPS'

print len(letter_freq)
print len (text_freq)


converted_text = []
converted_string = ""

for letter in text:
    print ("checking letter" + letter)
    if letter == ' ':
        converted_text.append(letter)
        converted_string = converted_string + letter
    elif letter == ',':
        converted_text.append(letter)
        converted_string = converted_string + letter
    elif letter == '.':
        converted_text.append(letter)
        converted_string = converted_string + letter
    else:

        counter = 0
        for item in text_freq:
            print("against item" + item)

            if letter.lower() == item.lower():
                print("match " + letter.lower() + " is the same as " + item.lower())
                converted_text.append(letter_freq[counter])
                converted_string = converted_string + letter_freq[counter]
                counter += 1

            else:
                counter += 1


    # converted_text.append(letter)
print (converted_text)
print (converted_string)


print(org_text_freq)

# Counter({' ': 122, 'Z': 63, 'X': 62, 'K': 55, 'U': 52, 'L': 50, 'T': 50, 'M': 46, 'B': 44, 'G': 41, 'O': 39, 'D': 30, 'F': 28, 'C': 22, 'H': 22, 'Y': 21, 'R': 20, 'W': 17, 'E': 11, 'Q': 9, ',': 8, 'N': 7, '.': 4, 'A': 4, 'P': 4, 'S': 4})

#
# list = list(text_freq.items())
# # print(list)
#
# for item in list:
#     print (item)
# my_dict = {Z': 63, 'X': 62, 'K': 55, 'U': 52, 'L': 50, 'T': 50, 'M': 46, 'B': 44, 'G': 41, 'O': 39, 'D': 30, 'F': 28, 'C': 22, 'H': 22, 'Y': 21, 'R': 20, 'W': 17, 'E': 11, 'Q': 9, ',': 8, 'N': 7, '.': 4, 'A': 4, 'P': 4, 'S': 4}
#
# }

# for letter in text:
#     print letter
