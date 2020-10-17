def distinct(s):
    s=s.lower()
    my_dict = {i:s.count(i) for i in s}
    return my_dict

#print(distinct("BrownBro"))

def areanagrams(s1,s2):
    lst1 = list(s1.lower())
    lst2 = list(s2.lower())
    lst1.sort()
    lst2.sort()
    print(lst1,lst2)
    return lst1 == lst2

#print(areanagrams("bacdbba","dcbabba"))


def content_word(filename):
    count = 0
    my_words={}
    with open(filename,"r") as myFile:
        for fileContent in myFile:
            fileContent = fileContent.lower()
            list_f = fileContent.split()
            my_words={i:list_f.count(i) for i in list_f}
        popular_word=sorted(my_words,key=my_words.get,reverse=True)
        top_20=popular_word[:20]
    return top_20

print(content_word("new2.txt"))


def extract(text):
    output = ""
    count = 0
    wordlist=text.split(" ")
    for word in wordlist:
        count = count + 1
        if count%5==0:
            output = output+word[0]

    return output

print(extract("Yesterday I saw an aardvark while walking my pet tortoise, Frank. What a sight this was! Aarvarks are nocturnal animals appearing in daylight with caution. Make sure to bring kippers when you visit."))
