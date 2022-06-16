'''
단어정렬
'''
words = []
for _ in range(int(input())):
    word = input()
    length = len(word)
    if (length, word) not in words:
        words.append((length, word))
words = sorted(words, key= lambda x : (x[0],x[1]))
for word in words:
    print(word[1])