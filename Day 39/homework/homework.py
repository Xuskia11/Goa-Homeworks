#Duplicate Encoder

def duplicate_encode(word):
    word = word.lower()
    x = ""
    for i in word:
        if word.count(i) > 1:
            x += ")"
        elif word.count(i) == 1:
            x += "("
    return x


#Detect pangram
def is_pangram(s):
    s = s.lower()
    is_true = True
    x = "abcdefghijklmnopqrstuvwxyz"
    for i in x:
        if i in s:
            is_true = True
        else:
            is_true = False
            break
    return is_true

#Whats A Name In?
def name_in_str(text, name):
    for c in text.lower():
        if c == name[0].lower():
            name = name[1:]
            if not name:
                return True
    return False


#First non-repeating character
def first_non_repeating_letter(s):
    list = [i.lower() for i in s]
    
    for i in range(len(list)):
        if list.count(list[i]) == 1:
            return s[i]
    return ""