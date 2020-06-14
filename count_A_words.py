def get_words(sentence):
    words=[]
    sow_index=0
    for i in range (0,len(sentence)):
        if (sentence[i]==' ' or sentence[i]=='.'or sentence[i]==','):
            words.append(sentence[sow_index:i])
            sow_index=i+1
    return words

def find_A_words(words):
    word_a=0
    for word in words:
        if (word[0]=="a" or word[0]=="A"):
            word_a=word_a+1
    return word_a

sentence="World is round."
words=get_words(sentence)
word_a=find_A_words(words)
print(word_a)
