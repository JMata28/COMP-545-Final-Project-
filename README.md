# COMP-545-Final-Project
This is our submission for COMP 545-001 Analysis of Algorithms - Final Project 
Group members: Arnold Mpiima, Lalitha Bhavanand, and Jose Mata

Fall 2024, Bridgewater State University

## Instructions for Running the Python File
Run the "phone_directory.py" file with Python 3.12.2 64-bit
No additional Python packages need to be installed for the program to work correctly

## What the Program Does
This program simulates a phonebook directory, containing people's names and the corresponding phone number. Upon running the program, you'll be prompted to select one of the following options (or steps). Simply choose a number from 1 to 4 to select an option. You'll be able to choose as many options as desired until you choose option 4, which terminates the program. The following are the choices, each of which is explained in further detail below: 
* Enter '1' to look for a person in the phonebook directory.
* Enter '2' to add a new person to the phonebook directory.
* Enter '3' to display all the names and numbers in the phonebook.
* Enter '4' to end the program.

Any input besides a number from 1 to 4 will result in an "Answer is invalid." message. 

## How the Program Uses the Hashmap and Trie Data Structures
The program uses the hashmap data structure in the following way: The hashmap is represented by a list of 100 items that contains all the pairs of names and phone numbers as Python tuples. The hashmap uses a hash function that simply calculates the sum of the equivalent ascii value of each character, then divides it by a hundred, and returns the remainder as the hash code (the index to locate each pair in the hashmap). So the list of possible indexes goes from 0 to 99. 

Collisions in the hashmap (names that result in the same hash code and are therefore save in the same index) are handled the following way: Pairs of names and phone numbers are stored in the same index location, but as items of a list of tuples instead of individual tuples. An example of names that cause a collision (for demonstrating purposes): 'Lalitha Bhavanand' and 'Anna Cruz', which are both saved in a collision list of tuples in index 98.

The program uses the trie data structure in the following way: For a name to be added to the phonebook directory, the name is first added to the trie data structure. Whenever a name is searched for using Option 1, the trie data structure is checked first to see if the name is in it. If the name exists, then the name and phone number have been included in the phonebook directory. This way, the program doesn't need to check the hashmap directly every time a name is looked up, only in the times where the name is in the phonebook directory. 


### Dummy Data
At the beginning of the program, the following dummy data entries of names and their corresponding number are added to the phonebook directory:
* 'Arnold Mpiima', '123-456-7890'
* 'Lalitha Bhavanand', '123-123-1231'
* 'Jose Mata', '504-123-4567'

More entries can be added to the program using Option 2. 

### Option 1 - Look for a person in the phonebook directory:
This option allows you to input a name to look for in the phonebook directory. You'll be prompted to type the person's first name, then a space, and then their last name.
The program then uses the trie data structure to check if the name is already in it. If it is, then it means that the name is in the phonebook directory because every name that is added to the phonebook directory (the hashmap) is first added to the trie data structure. If found in the trie data structure, then the program retrieves the name and number from the hashmap. If the name is not found in the trie data structure, then we know that the name and number are NOT in the phonebook directory, so the information is not looked for in the hashmap, saving time and computational resources. If the name is found in a hashmap collision it will be retrieved from the list of tuples in the corresponding index of the hashmap. 

### Option 2 - Add a new person to the phonebook directory:
This option allows you to add a name a the corresponding number to the phonebook directory. ou'll be prompted to type the person's first name, then a space, and then their last name. You'll also be prompted to enter the corresponding phone number. The program then adds the name to the trie data structure and then adds the name and number to the hashmap, using a hash function to calculate the index. If a collision is found in the hashmap, it will be handled by storing multiple names and numbers in the same index of the hashmap at the same time. 
**Please note that exiting the program will delete all the phonebook directory entries made in previous runs of the program and will start the program again with the dummy data only.**

### Option 3 - Display all the names and numbers in the phonebook directory:
Selecting this option displays all the names and their corresponsing numbers in the phonebook directory. In cases were collisions were found, the colliding entries will appear as part of the same list. If entries in addition to the dummy data entries have been made by the user with Option 2, these entries will appear in the list displayed by Option 3. 

### Option 4 - Terminate the program:
The program terminates. 


