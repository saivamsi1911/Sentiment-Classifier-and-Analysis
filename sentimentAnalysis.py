projectTwitterDataFile = open("project_twitter_data.csv","r")
resultingDataFile = open("resulting_data.csv","w")

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(n):
    for i in n:
        if i in punctuation_chars:
            n=n.replace(i,"")
    return n

def get_neg(n):
    count=0
    
    for i in n.split(" "):
        if strip_punctuation(i.lower()) in negative_words:
            count+=1
    
    return count

def get_pos(n):
    count=0
    
    for i in n.split(" "):
        if strip_punctuation(i.lower()) in positive_words:
            count+=1
    
    return count


# This function will write to the file and we will be provided with the needed data.
def writeInDataFile(resultingDataFile):
    resultingDataFile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    resultingDataFile.write("\n")

    linesPTDF =  projectTwitterDataFile.readlines()
    headerDontUsed= linesPTDF.pop(0)
    for linesTD in linesPTDF:
        listTD = linesTD.strip().split(',')
        resultingDataFile.write("{}, {}, {}, {}, {}".format(listTD[1], listTD[2], get_pos(listTD[0]), get_neg(listTD[0]), (get_pos(listTD[0])-get_neg(listTD[0]))))    
        resultingDataFile.write("\n")

        

writeInDataFile(resultingDataFile)
projectTwitterDataFile.close()
resultingDataFile.close()