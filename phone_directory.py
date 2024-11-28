#This is our submission for COMP 545-001 Analysis of Algorithms - Final Project 
#Group members: Arnold Mpiima, Lalitha Bhavanand, and Jose Mata

#Menu:
#1. look for person
#2. add person
#3. display names and numbers in phonebook
#3. (if time allows, delete person)

#Steps: 
#Create dummy data in tuple format to save to phonebook. 
#Save dummy data in phonebook. For each tuple saved in phone book: 
    #Create the entry for the name in the trie data structure. 
    #Save the tuple in the hash map. 
#Display names and numbers in phonebook
#Add menu options for the user.
    #To look for a person: 
        #perform the trie_lookup function to see if the name of the person is in the trie data structure. If it is, then proceed with the hash map lookup
        #then the hashmap_lookup function takes place and returns the tuple information
        #the point here is that the hashmap_lookup will not happen if the name is not found in the trie data structure. The fact that there is a 
        #entry for the name in the trie data structure means that it will for sure be in the hashmap and therefore the hashfunction will not happen unnecesarily. 
    #To add a person:
        #ask the user for the first and last names and number of the person
        #create the entry in the trie data structure by using the trie_add function
        #create the entry in the hashmap data structure by using the hashmap_add function
    #To display names and numbers in the phonebook:
        #print out the hashmap list. If necessary, add code to make sure that only the non-empty items of the list print out. 

#The code for the class "TrieNode" was obtained from https://www.geeksforgeeks.org/trie-insert-and-search/ and modified to fit the needs of this program
#This class is used to represent nodes in the trie data structure and their functionality
class TrieNode:
    def __init__(self):
        self.child = [None] * 27 #Creates a list of 27 indexes containing the object None: 26 letters of the English alphabet and an additional index for spaces. 
        self.word_end = False

root = TrieNode() #the root node for the trie data structure is one that always starts completely empty (no characters in its children and the wordEnd attribute is False)

hashmap = [None]*100 #The hashmap consists of a list of 100 items (indexes 0 to 99) that is initialized with all-zero values 

#This is a hash function that simply calculates the sum of the equivalent ascii value of each character, then divides it by a hundred, and returns the remainder as the hash code (index)
def hash_function(name):
    #Convert the name to only lowercase letters
    name = name.lower()
    #Remove leading and trailing whitespace characters
    name = name.strip()
    total_value_of_name = 0
    for character in name:
        total_value_of_name = total_value_of_name + ord(character)
    index = total_value_of_name%100 #returns a value from 0 to 99 which is the remainder of the sum of all ascii equivalents divided by 100
    return index


#Part of the code for function "trie_add" was obtained from https://www.geeksforgeeks.org/trie-insert-and-search/ and modified to fit the needs of this program 
#This is the function that adds an name entry to the trie data structure
def trie_add(root, name):
    #Convert the name to only lowercase letters
    name = name.lower()
    #Remove leading and trailing whitespace characters
    name = name.strip()
    # Initialize the curr pointer with the root node
    curr = root
    # Iterate across the length of the string
    for character in name:
        if character == ' ': 
            index = 26 #spaces will always have the index 26
        else:
            index = ord(character) - ord('a') #orc('a') has a value of 97, so the index for 'a' is 0, for 'b' is 1, and so on
        # Check if the node exists for the current character in the Trie
        if curr.child[index] is None:
            # If node for current character does not exist then make a new node
            new_node = TrieNode()
            # Keep the reference for the newly created node
            curr.child[index] = new_node
        # Move the curr pointer to the newly created node or the node that already existed for that character
        curr = curr.child[index]
    # Mark the end of the word
    curr.word_end = True

#This is the function that adds an entry to the hashmap data structure
def hashmap_add(name, number):
    index = hash_function(name)
    hashmap[index] = (name, number)

#Part of the code for function "trie_lookup" was obtained from https://www.geeksforgeeks.org/trie-insert-and-search/ and modified to fit the needs of this program 
#This is the implementation of the Trie data structure to check if a name is already included in the phonebook. 
def trie_lookup(root, name):
    #Covert the name to use only lowercase letters
    name = name.lower()
    #Remove leading and trailing whitespace characters
    name = name.strip()
    # Initialize the curr pointer with the root node
    curr = root
    # Iterate across the length of the string
    for character in name:
        if character == ' ': 
            index = 26 #spaces will always have the index 26
        else:
            index = ord(character) - ord('a') #orc('a') has a value of 97, so the index for 'a' is 0, for 'b' is 1, and so on
        # Check if the node exists for the current character in the trie data structure
        if curr.child[index] is None:
            return False
        # Move the curr pointer to the already existing node for the current character
        curr = curr.child[index]
    # Return true if the word exists and is marked as ending
    return curr.word_end

#This is the manual implementation of a hash map to retrieve the saved names and numbers. 
def hashmap_lookup(name):
    index = hash_function(name)
    name_and_number = hashmap[index]
    return name_and_number

#This is the function that looks for a person in the phonebook directory.
#First, it uses the trie data structure to see if the name exists in the phonebook directory. If it does, then it retrieves it in the hashmap along with the phone number.
def option_1():
    user_answer_1 = input("Enter the name of the person that you're looking for in the phonebook directory. Type their first name, then a space, and then their last name.\n")
    found_status = trie_lookup(root, user_answer_1)
    if found_status == True:
        print("Name " + user_answer_1 + " was found in the phonebook directory.")
        name_and_number = hashmap_lookup(user_answer_1)
        print("Name: " + name_and_number[0] + "\nNumber: " + name_and_number [1] + "\n\n")
    else:
        print("Name " + user_answer_1 + " was NOT found in the phonebook directory.\n\n")

def option_2(root):
    user_name = input("Please enter the person's first name, then a space, and then their last name.\n")
    user_number = input("Please enter the person's phone number in the following format: xxx-xxx-xxxx\n")
    trie_add(root, user_name)
    hashmap_add(user_name, user_number)
    print("User '" + user_name +"' has been succesfully added to the phonebook directory.\n\n")

def option_3(hashmap):
    print("Here is a list of all the names and numbers in the phonebook directory:")
    for pair in hashmap:
        if pair != None:
            print(pair)
    print("\n\n")
dummy_data = [('Arnold Mpiima', '123-456-7890'), ('Lalitha Bhavanand', '123-123-1231'), ('Jose Mata', '504-123-4567')]

for name, number in dummy_data:
    trie_add(root, name)
    hashmap_add(name, number)

print("Welcome to our group's phone directory simulator using hashmap and trie data structures.")
while True: 
    user_answer_0 = input("Please choose one of the four options below:\nEnter '1' to look for a person in the phonebook directory.\nEnter '2' to add a new person to the phonebook directory.\nEnter '3' to display all the names and numbers in the phonebook.\nEnter '4' to end the program.\n")
    if user_answer_0 == '1':
        option_1()
    elif user_answer_0 == '2':
        option_2(root)
    elif user_answer_0 == '3':
        option_3(hashmap)
    elif user_answer_0 == '4':
        print("Exiting program...")
        break
    else:
        print("Answer is invalid")