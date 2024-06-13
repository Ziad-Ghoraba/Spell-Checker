import difflib , time

# open dictionary text file D:\Programming\Projects\Data\Spell_Checker\
# with open (r"C:\Users\DataOnLine\.vscode\projects\uni_project\Dictionary.txt" , 'r') as file :
with open (r"D:\Programming\Projects\Data\Spell_Checker\Project_Dictionary.txt" , 'r') as file :
    dic= file.read().split()

# function to check over the dictionary

def binary_search(word_list, item):
    low = 0
    high = len(word_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if item == word_list[mid]:
            return True
        elif item > word_list[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False

# Function to check if the word exists in the dictionary
def check_word(word):
    # remove non-alphabetic characters except coma (')
    new_word = ''.join(c for c in word if c.isalpha() or c=="'")

    # If the new word is empty, then all characters were non-alphabetic
    if not new_word :
        return True

    # Otherwise, perform a binary search with the new word
    return binary_search(dic, new_word)
            
        

# function to draw red underline 
def red_line (word) :
    return f"\x1b[31m\x1b[4m{word}\x1b[0m"


# Function to predict three words

def matches(word , n):
    
    suggestions=[]
    
    # creat an object of SequenceMatcher class 
    # SequenceMatcher is used to compare 2 sequences 
    # it takes 3 arguments (isJunk, seq1, seq2)
    # passing only one argument seq2  
    match = difflib.SequenceMatcher(None,None ,word)
    
    # passing all words in dictionary one by one to seq1 
    for w in dic :
        match.set_seq1(w) 
    
        # using quick_ratio method to indicate the similarty between the 2 sequences quickly
        # condition > 0.6 for taking the closest words not all words from dictionary 
        if  match.quick_ratio() > 0.6  :
            
            # append list of [word and its values of ratio()] not quick_ratio bc it's more accurate
            suggestions.append([ w , match.ratio() ])
        
    match = select_sort(suggestions , n)
    return word + ": " + ", ".join(match) + '\n'
        

    # selection sort 
def select_sort(list_of_lists , passes_num) :
    n=len(list_of_lists)
    
    # check if there are any predicted words in the list
    if n == 0 :
        return ["does not seem like an English word"]
    
    # if there are, make sure that the n.of words is equal or more than desired number 
    else :
        if n < passes_num :
            passes_num = n
    
        # modified selection sort to make number of passes = number of word I want 
        for i in range (passes_num-1):
            max = list_of_lists[i][1]
            max_position = i
        
            for j in range (i+1 , n-1):
                if list_of_lists[j][1] > max:        
                    max = list_of_lists[j][1]
                    max_position =j
            
            list_of_lists[i] , list_of_lists[max_position] = list_of_lists[max_position] , list_of_lists[i]
        
    suggestions =[]
    for i in range (passes_num) : 
        suggestions.append (f"\x1b[32m{list_of_lists[i][0]}\x1b[0m")
        #suggestions.append (list_of_lists[i][0])
    return suggestions 

        
# input and processing 
text = input("Enter the text: ").split()
start = time.time()
out_list =[]
suggestions =[]
for w in text :
    w=w.lower()
    if check_word(w):
        out_list.append(w)
    else :
        out_list.append(red_line(w))
        suggestions.append(matches( w , 3 ))

print('\n' , *out_list)

print('\n'"----------------------SUGGESTIONS------------------------")
print(*suggestions, sep='')

end = time.time()
print("The time of execution of above program is :", (end - start))
