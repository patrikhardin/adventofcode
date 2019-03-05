#Function that takes a string of text and does the procedure once. We want to call this recursively until result stays same
def scanText(textList):
    i = 0
    while i < len(textList)-1:
        if textList[i].lower() == textList[i+1].lower():
            if textList[i] != textList[i+1]: #This means that the letters are the same but different case
                del textList[i]
                del textList[i] #index updated when removing previous element
                i -= 1
        i += 1
    return textList


#Function that takes a text and and exception character. Returns the length of the result and which chars were removed
def reduce(textList,exceptionChars):
    #First filter the list from unwanted chars
    for char in exceptionChars:
        textList = list(filter(lambda a: a != char, textList))

    #Do the scan
    previousLen = None
    while previousLen != len(textList):
        previousLen = len(textList)
        textList = scanText(textList)
    #One more time just to make sure
    scanText(textList)

    return len(''.join(textList)),exceptionChars

def main():
    pairs = [['',''],['A','a'],['B','b'],['C','c'],['D','d']]

    for pair in pairs:
        with open('input5.txt','r') as file:
            text = file.read()
            text = list(text)

        print(str(reduce(text,pair)[0]) + ' Removed: ' + str(reduce(text,pair)[1][0]) + str(reduce(text,pair)[1][1]))
        #STILL NOT SURE WHY THIS IS ONE TOO LARGE??????

main()
