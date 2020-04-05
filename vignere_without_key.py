import re
from collections import Counter
letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
msg = "PPQCAXQVEKGYBNKMAZUYBNGBALJONITSZMJYIMVRAGVOHTVRAUCTKSGDDWUOXITLAZUVAVVRAZCVKBQPIWPOU"
from vignere import decrypt



englishLetterFreq = {'A': 8.17, 'B': 1.29, 'C': 2.78,'D': 4.25,'E': 12.70, 'F': 2.23,'G': 2.02,'H': 6.09,'I': 6.97, 'J': 0.15,'K': 0.77, 'L': 4.03, 'M': 2.41,'N': 6.75, 'O': 7.51,'P': 1.93,'Q': 0.10,'R': 5.99,'S': 6.33,'T': 9.06,'U': 2.76, 'V': 0.98, 'W': 2.36, 'X': 0.15,    'Y': 1.97,    'Z': 0.07}
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
msg = msg.upper().strip().replace(" ","")   # to convert the cipher text into capital letters and remove all spaces
msg = re.sub(r'\W', '', msg)  #to remove all non alpha numeric characters
print(msg)

def findrepeatedsequences():
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
    factors = findfactors(nonzero_list)
    print(factors)
    findprobablekeylength(factors)


def findprobablekeylength(factors):
    dictofFactors = dict()
    dictofFactors=dict(Counter(factors))
    print(dictofFactors)
    dictofFactors={key: value for key, value in dictofFactors.items() if (value != 1 and value != 2)}
    print(dictofFactors)

    probable_key_lengths = dictofFactors.keys()
    print(probable_key_lengths)
    getnlettersfromstring(probable_key_lengths)


#to break down the cipher such that we have a set of characters which are all encoded with the same key index
def getnlettersfromstring(probable_key_lengths):
    str_list = []
    for elem in probable_key_lengths:

        print(elem)
        for start in range(0,4):       #can replace 4 with elem to loop through all the possible key lengths
            sub_str = ''
            for seq in range(start,len(msg),4):         #can replace 4 with elem to loop through all the possible key lengths
                sub_str=sub_str + msg[seq]
            str_list.append(sub_str)
            str_list = list(set(str_list))
    print(str_list)
    frequency_analysis("PAEBABANZIAHAKDXAAAKIU")

def frequency_analysis(str_list):

    freq_list = {}
    distro_list = {}
    length_of_str = len(str_list)
    print(length_of_str)
    for char in str_list:
        if char in freq_list:
            freq_list[char] +=1
        else:
            freq_list[char] = 1
    print(freq_list)

    for char in letters:
        if char not in freq_list:
            freq_list[char] = 0
    print(freq_list)


    for elem in freq_list:
        distro_list[elem] = freq_list[elem]/length_of_str
    print(distro_list)

    for dict_value in distro_list:
        distro_list[dict_value] = round(distro_list[dict_value],3)

    print(distro_list)

    sortedDict = sorted(distro_list.items())
    findKey(sortedDict)

def findKey(sortedDict):
    print(sortedDict)


def findfactors(input_list):
    factors = []
    for position in range(0,len(input_list)):
        for i in range(2,input_list[position]+1):
            if (input_list[position] % i == 0):
                factors.append(i)
    return(factors)


findrepeatedsequences()
