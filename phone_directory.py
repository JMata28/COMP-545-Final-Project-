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
        self.wordEnd = False

root = TrieNode()

#Part of the code for function "trie_add" was obtained from https://www.geeksforgeeks.org/trie-insert-and-search/ and modified to fit the needs of this program 
#This is the function that adds an name entry to the trie data structure
def trie_add(root, name):
    print("Executing trie_add function in the name: ", name)
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

def hasmap_add():
    #This is the function that adds an entry to the hashmap data structure
    print("hashmap_add function sucessfully executed")

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

def hashmap_lookup():
    #This is the manual implementation of a hash map to store the saved names. 
    print("hashmap_ lookup function successfully executed")

dummy_data = [('Arnold Mpiima', '123-456-7890'), ('Lalitha Bhavanand', '123-123-1231'), ('Jose Mata', '504-123-4567')]

for name, number in dummy_data:
    trie_add(root, name)

user_answer = input("Enter the name of the person that you're looking for in the phonebook directory.\n")
found_status = trie_lookup(root, user_answer)
if found_status == True:
    print("Name " + user_answer + " was found.")
else:
    print("Name " + user_answer + " was NOT found.")

