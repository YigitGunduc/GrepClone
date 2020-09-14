#!/c/Users/gunduc/anaconda3/python

from sys import argv

test = "ge"
punc = "!'^+%&/()=?_-*#$½{[]}., \|1234567890"
strr = ""
with open("a.txt", "r") as f:
    for i in f:
        for j in i:
            if j not in punc:
                strr += j
clear = strr.split()
words = ["apple","car","set"]
test = "get"


def grep(words, test):
    c = test[0]
    sayi = 0
    color_start = "\033[1;31;40m"
    color_end = "\033[0m"
    matched = []
    for word in words:
        if len(word) >= len(test): 
            for i in range(len(word) - len(test)):
                if c == word[i]:
                    indexstart = i
                    counter = 1
                    for j in range(i + 1, i + len(test)):
                        if test[j - i] == word[j]:
                            counter += 1
                            if counter == len(test):
                                print(word[:indexstart] + color_start + test + color_end + word[indexstart + len(test):])
                                
                                matched.append(word)
                                sayi += 1
                                break     
    print("\033[1;32;40m" + str(sayi) + " Eslesme bulundu"+ "\033[0m")
grep(clear,test)
