#Array plus array
def array_plus_array(arr1,arr2):
    
    return sum(arr1) + sum(arr2)

#Rock Paper Scissors!
def rps(p1, p2):
    if p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    elif p1 == "rock" and p2 == "scissors":
         return "Player 1 won!"
    
    
    
    if p1 == "scissors" and p2 == "rock":
        return "Player 2 won!"
    elif p1 == "rock" and p2 == "paper":
        return "Player 2 won!"
    elif p1 == "paper" and p2 == "scissors":
        return "Player 2 won!" 
    elif p1 == p2:
        return "Draw!"
    
#Area or perimeter
def area_or_perimeter(l , w):
    if l == w:
        return l * w
    else:
        return (l + w) * 2
    
#Remove anchor from URL
def remove_url_anchor(url):
    x =  url.split("#")
    return x[0]

#Anagram Detection
def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    x = sorted(test)
    y = sorted(original)
    if x == y:
        return True
    else:
        return False
    
#Greatest common divisor
def mygcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x

#Write Number in Expanded Form
def expanded_form(num):
    s = []
    i = len(str(num)) -1
    for n in str(num):
        if n != "0":
            s.append(n + "0" * i)
        i -= 1
    return " + ".join(s)

#Collatz
def collatz(n):
    lists = [str(n)]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        lists.append(str(int(n)))
    return "->".join(lists)

#Simple Pig Latin
def pig_it(text):
    
    texts = text.split(" ")
    word = ""
    
    for i in texts:
        if i in "!%&.?":
            word = word + i
        else:
            i= i[1:]+ i[0] + "ay"
            word = word + i + " "
            
    return word.strip()

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

#Kebabize
def kebabize(st):
    word = ""
    for i in st:
        if i.isalpha() == False:
            i = ""
        if i.isupper():
            i = i.lower()
            word +="-" + i
        else:
            word += i
    return word.strip("-")


