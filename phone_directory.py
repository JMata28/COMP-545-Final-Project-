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

def trie_add():
    #This is the function that adds an entry to the trie data structure
    print("trie_add function successfully executed")

def hasmap_add():
    #This is the function that adds an entry to the hashmap data structure
    print("hashmap_add function sucessfully executed")

def trie_lookup():
    #This is the implementation of the Trie data structure to check if a name is included in the phonebook. 
    print("trie_lookup function successfully executed")

def hashmap_lookup():
    #This is the manual implementation of a hash map to store the saved names. 
    print("hashmap_ lookup function successfully executed")

dummy_data = [('Arnold Mpiima', '123-456-7890'), ('Lalitha Bhavanand', '123-123-1231'), ('Jose Mata', '504-123-4567')]
