mySentence=['Ali came here to visit us. He did not want to disturb my friend Sofia']


newSentence=[]
for sentence in mySentence:
    split_sentence=sentence.split()
    newSentence.append(split_sentence)

print(newSentence)