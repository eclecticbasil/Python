#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Rbukhari, 2022-Feb-23, Changing to add 
# script for variables, displaying data,
# creating a 2d list with a dictionaries and 
# functionality to delete an entry. 
#------------------------------------------#
# Declare variables

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# Replacing the list of lists with list of dicts
dicRow = {} # list of data row
strFileName = "CDInventory.txt"  # data storage file
objFile = None  # file obj

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input("l, a, i, d, s or x: ").lower()  # convert choice to lower case at time of input
    print()

    if strChoice == "x":
        # 5. Exit the program if the user chooses so
        break
    if strChoice == "l":
        # Functionality of loading the existing data
        lstTbl.clear()
        objFile = open(strFileName, "r")
        for row in objFile:
            lstRow = row.strip().split(",")
            dicRow = {"ID":lstRow[0], "Artist":lstRow[1],"CD":lstRow[2]}
            lstTbl.append(dicRow)
        objFile.close()
        pass
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        dicRow = {}
        dicRow["ID"] = int(input("Enter an ID: "))
        dicRow["Artist"] = input ("Enter Name of Artist: ")
        dicRow["CD"] = input ("Enter the CD Name:  ")
        lstTbl.append(dicRow)
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print("ID, Artist, CD")
        for row in lstTbl:
            print(row)
    elif strChoice == 'd':
        # Functionality of deleting an entry
        delID = int(input("Please enter the ID of the row you want to delete: "))
        for dicRow in lstTbl:
            if dicRow["ID"] == delID:
                lstTbl.remove(dicRow)
        pass
    elif strChoice == 's':
      # 4. Saving the data to a text file CDInventory.txt if the user chooses so
      objFile = open(strFileName, 'w')
      for row in lstTbl:
          strRow = ""
          for item in row.values():
              strRow += str(item) + ","
          
          strRow = strRow [:-1] + "\n"
          objFile.write(strRow)
      objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')