import re
import operator
from collections import Counter
msg = "PPQCAXQVEKGYBNKMAZUYBNGBALJONITSZMJYIMVRAGVOHTVRAUCTKSGDDWUOXITLAZUVAVVRAZCVKBQPIWPOU"

msg = msg.upper().strip().replace(" ","")   # to convert the cipher text into capital letters and remove all spaces
msg = re.sub(r'\W', '', msg)  #to remove all non alpha numeric characters
print(msg)

def findRepeatedSequences():
    seqspace= []
    dictOfElems = dict()
    for seqlen in range(3,6):                  #loop through the different lenghts of the key
        for itervar in range(0,len(msg)):      #lopp from start to end of the message
            temp = msg[itervar:itervar+seqlen]  #chop up the cipher text into chunks equivalent to the lenght of the key
            print(temp)
            if(len(temp)==seqlen):
                seqspace.append(temp)           #get a list of the chopped down cipher text which can then be used to find the max repeating sequences
    print(seqspace)

    dictOfElems = dict(Counter(seqspace))      #get the count of all the sequences that are repeated
    print(dictOfElems)
    myDict = {key:value for key, value in dictOfElems.items() if value != 1}  # remove all the entries in the dictionary that are occuring only once
    print(myDict)


    space_list = []
    # to get the index of the repeating sequences in the cipher text
    for elem in myDict:
        matches = re.finditer(elem,msg)
        match_position=[match.start() for match in matches]
        print(match_position)
        space_list.append(match_position)
    print(space_list)
    seq_distance(space_list)


    # to find the difference between indices of the different repeating sequences, this yields the distance between the different repeating sequences
def seq_distance(space_list):
    diff_list = []
    for lst in range(0,len(space_list)):
        for i in range(1,len(space_list[lst])):
            print(i)
            for j in range(i-1,len(space_list[lst])):
                print(j)
                temp1 = space_list[lst][len(space_list[lst]) - i]
                temp2 = space_list[lst][len(space_list[lst]) - i - j]
                print(temp1)
                print(temp2)
                temp = temp1 -temp2
                if(temp >= 0):
                    diff_list.append(temp)
                else:
                    diff_list.append(-temp)

    print(diff_list)
    nondup_list = list(set(diff_list))
    print(nondup_list)
    nonzero_list = list(filter(lambda a:a !=0,nondup_list))
    print(nonzero_list)
    factors = findFactors(nonzero_list)
    print(factors)
    findProbableKeyLength(factors)


def findProbableKeyLength(factors):
    dictofFactors = dict()
    dictofFactors=dict(Counter(factors))
    print(dictofFactors)
    dictofFactors={key: value for key, value in dictofFactors.items() if (value != 1 and value != 2)}
    print(dictofFactors)

    probable_key_lengths = dictofFactors.keys()
    print(probable_key_lengths)


def findFactors(input_list):
    factors = []
    for position in range(0,len(input_list)):
        for i in range(2,input_list[position]+1):
            if (input_list[position] % i == 0):
                factors.append(i)
    return(factors)





findRepeatedSequences()
