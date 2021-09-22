def lengthOfLastWord(s: str) -> int:
    wordList = s.strip().split(' ')
    print("wordList=",wordList)
    lastWord = wordList[-1]
    return len(lastWord)

print(lengthOfLastWord('Hello World'))