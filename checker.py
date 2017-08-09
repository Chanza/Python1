import operator


#selecting dictionary
output = open('small.txt', 'r')
output_list = output.read().strip().split()


#file to check
output2 = open('big.txt', 'r')
output_list2 = output2.read().strip().split()
output2.close()


#searching and counting words
def counter():

 word_count = {}
 clean_word_list = []

 for word in output_list:
    if word in output_list2:
        clean_word_list.append(word)

 print ("\nThe index text file words found from highest to lowest count are:\n")

 for word in output_list2:
    if word in clean_word_list: word_count[word] = word_count.get(word, 0) + 1

 for key, value in sorted(word_count.items(), key=operator.itemgetter(1), reverse=True): print(key, value)

counter()

