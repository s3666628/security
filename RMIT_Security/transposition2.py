encrypt_text = "MOBBZLXHR, EHTMPMDUKL XZMDLTHTQR MUL ZLDULMZ XDZ ZCCKMKZLMR, UMMOBUMR ULF GZMOBKXR TC U SKFZ BULQZ TC KLFOGXBKZG ULF XDZKB GOWWHR MDUKL CBTY YULOCUMXOBZB XT MTLGOYZB. YULR KLFOGXBKZG KLMHOFKLQ XDZ UOXTYTXKNZ, ZHZMXBTLKM MTYYZBMZ ULF YZFKMUH KLFOGXBKZG MUL OXKHKGZ XDZ EZLZCKXG TC EHTMPMDUKL KL NUBKTOG XUGPG GOMD UG WBTNKLQ XDZ UOXDZLXKMKXR TC UOXTYTXKNZ WUBXG, NUHKFUXKLQ U XBULGCZB TC WURYZLXG TB YUKLXUKLKLQ XDZ AOUHKXR TC WDUBYUMZOXKMUH WBTFOMXG. TLZ KYWTBXULX KLFOGXBR SDKMD UCCZMXG WZTWHZ QHTEUHHR KG XDZ CTTF WBTFOMXKTL KLFOGXBR, SDKMD BZAOKBZG WBTFOMXG GOMD UG NZQZXUEHZG, CBOKXG, WTOHXBR ULF YZUXG LZZF XT EZ GTOBMZF CBTY CUBYG ULF EZ TC XTW AOUHKXR ER XDZ XKYZ XDZR BZUMD MTLGOYZBG. XDOG XDZ CTTF WBTFOMXKTL KLFOGXBR MTOHF EZ ZLDULMZF SKXD EHTMPMDUKL ULF EZMTYZG U GYUBX KLFOGXBR, KYWBTNKLQ XDZ AOUHKXR TC XDZKB WBTFOMXG."

# 1 get the count of each set of letters in the string
from collections import Counter
org_text_freq = (Counter(encrypt_text))

# 2 iterate over the dictionary of letter fequencies and map them in order of the alphabet frequency
# lett_freq = 'etaoinshrdlcumwfgypbvkj'
# text_freq = 'ZXKULTMBGODFCHYRWEQNAPS'
#
# lett_freq = 'ethorasundclgybkifmvpqw'
# text_freq = 'ZXDTBUGOLFMHQREPKCYNWAS'

lett_freq = 'etohafndclgyiurbksmvqpw'
text_freq = 'ZXTDUCLFMHQRKOBEPGYNAWS'

def convert_text_to_freq(encypt_text, text_alpha_freq_list, letter_freq_list):

    if len(text_alpha_freq_list) != len(letter_freq_list):
        return "Error - lists must be the same length"

    def find_replace(encrypt_letter):
        converted_text = ""
        counter = 0
        for letter in text_alpha_freq_list:
            if encrypt_letter.lower() == letter.lower():
                converted_letter = letter_freq_list[counter]
                return converted_text + converted_letter
            else:
                counter += 1
        return converted_text + encrypt_letter

    final_text =""
    for item in encypt_text:
        final_text = final_text + find_replace(item)
    return final_text

changed_text = convert_text_to_freq(encrypt_text, text_freq, lett_freq)


print (org_text_freq)
print (changed_text)

