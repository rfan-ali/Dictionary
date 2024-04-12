from Api import getMeaningApi
word = input("enter the word find ats meaning :")
meaningList = getMeaningApi(word)
meaning = meaningList[0]["meanings"]
for pos in meaning:
    print(meaning)