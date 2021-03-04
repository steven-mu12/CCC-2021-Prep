
#input and array setup
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']

S = input()

sentence = S.split()

sentence_pos = 0

for ok in sentence:
    sentence[sentence_pos] = list(ok)
    sentence_pos  = sentence_pos + 1

sentence_pos = 0

#code
for word in sentence:
    if word[0] in vowels:
        word.append("ma")

        if sentence[0] == sentence[0]:
            sentence_pos = sentence_pos + 1
        
        elif (sentence[sentence_pos - 1])[-1] == "ma":
            sentence[sentence_pos - 1].append("a")
        
        elif (sentence[sentence_pos - 1])[-1] == "aa":
            sentence[sentence_pos - 1].append("a")
        
        elif (sentence[sentence_pos - 1])[-1] == "a":
            sentence[sentence_pos - 1].append("a")
        
        else:
            continue

    else:
        added_word = word.pop(0)
        word.append(added_word)
        word.append("ma")

        if sentence[0] == sentence[0]:
            sentence_pos = sentence_pos + 1
        
        elif (sentence[sentence_pos - 1])[-1] == "ma":
            sentence[sentence_pos - 1].append("a")
        
        elif (sentence[sentence_pos - 1])[-1] == "aa":
            sentence[sentence_pos - 1].append("a")
        
        elif (sentence[sentence_pos - 1])[-1] == "a":
            sentence[sentence_pos - 1].append("a")
        
        else:
            continue
    
anotherpos = 0
glue = ''
for word in sentence:
    new_word = glue.join(word)
    sentence[anotherpos] = new_word
    anotherpos = anotherpos + 1

final_sentence = ''
for x1 in range(sentence):
    final_sentence = sentence[x1]

print (sentence)