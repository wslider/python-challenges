import os

def word_frequency(sample_text):

    #create empty dictionary
    #open file in reading mode
    word_dict = {}
    with open(sample_text, 'r') as text:
    
        #loop through each line 
        for line in text:
            line = line.strip().lower()
            words = line.split(" ")
            #loop through words in each line 
            for word in words:
                #check if each word is already in the dictionary
                #add 1 to count if it is
                # Remove punctuation from each word
                clean_word = ''.join(char for char in word if char.isalnum())

                if clean_word in word_dict:
                    word_dict[clean_word] = word_dict[clean_word] + 1
                #if not, add word to dictionary with a count of 1
                else: 
                    word_dict[clean_word] = 1

        for key in sorted(word_dict.keys()):
            print(f"{key} : {word_dict[key]}")

        #add sort by frequency later
        
sample_text = 'sample.txt'
word_frequency(sample_text)


