#------------------------------------------#
# Title: CDInventory.py
# Desc: Working with classes and functions with binary files and Error Handling.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Sayali, 2022-March-13, Modified the file with the asked TODOs(binary file read/write and Error Handling)
#------------------------------------------#
import pickle
# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.dat'  # data storage file
objFile = None  # file object


# -- PROCESSING -- #
class DataProcessor:
    "Processing the Data in Memory"
    # DONE add functions for processing here
    @staticmethod
    def Process_added_inventory(intID,strTitle,stArtist,table):
        '''
        TO add the added dictionary to the list we use this Process_added_inventory      
        
        Arguemnts/Parameters:
        
        strID : This is the INT ID from Added IO Fucntion.
        
        strTitle : This is the String TITLE from Added IO Fucntion.
        
        stArtist : This is the String ARTIST from Added IO Fucntion.
        
        table : The excisting 2D Table.\.

        Returns:
        
        table : The added row from the IO Function and updates the new 2D List.

        '''
        
        dicRow = {'ID': intID, 'Title': strTitle, 'Artist': stArtist}
        table.append(dicRow)
        return table
   
    @staticmethod
    def delete_inventory(intIDDel,table):
        '''
        Deletes the ID selected by the user to delete
        
        Arguements/ Parameters:
        
        intIDDel : Its the ID the user has input to delete.
        
        table : The 2D Table from which we would delete this ID entered row.

        Returns:
      
        table : The new 2D table after the deleted entry is removed.

        '''
        intRowNr = -1
        blnCDRemoved = False
        for row in table:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del lstTbl[intRowNr]
                blnCDRemoved = True
                
                break
        if blnCDRemoved:
              print('The CD was removed')
        else:
              print('Could not find this CD!')
        return table       
class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file into the data variable.

        Args:
            file_name (string): name of file used to read the data from in this case CDInventory.dat
            

        Returns:
            data : which is whats is stored in the Cdinventory.dat
        """
       
        try:
            with open(file_name,'rb') as objfile:
                data = pickle.load(objfile)
        except FileNotFoundError :
           print("File not found, first add data and write to the file and then read it")
           data = 'Error'
        except EOFError:
            print("File is empty and has no input , write to the file then read")
            data = 'Error'
        return data

    @staticmethod
    def write_file(table,file_name):
       '''
       This function is used to write the 2D Table to the file

       Arguemnts/Parameters:
       
       file_name : The file to which the data must be written.
       
       table : The data in memory which is in the table.

       Returns:
       
       None.

       '''
 
       table_final = ''
       for row in table:
           
           lstValues = list(row.values())
           lstValues[0] = str(lstValues[0])
           table_final = table_final +','.join(lstValues) + '\n'
       with open(file_name,'wb') as objfile:
           pickle.dump(table_final,objfile)  
       
  # -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

    # DONE add I/O functions as needed
    @staticmethod
    def add_inventory():
        '''
        This is used to take the inputs from the user and store to variables which it returns 
        as strID, strTitle, str Artist
        
        Arguemnts/Parameters:
            None
        
        Returns:
        
        strID : The ID entered by the user to add.
        
        strTitle : The String Title entered by the user.
        
        stArtist : The string Artist entered by the user.

        '''
        intID = None
        strTitle = ''
        stArtist = ''
        while type(intID) != int:
            try:
                intID = int(input('Enter ID: ').strip())
            except ValueError :
                print("This ID is not integer type , please enter integer ")
            
        strTitle = input('What is the CD\'s title? ').strip()
        stArtist = input('What is the Artist\'s name? ').strip()
        return intID,strTitle,stArtist
# 1. When program starts, read in the currently saved Inventory
FileProcessor.read_file(strFileName)


# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            print (FileProcessor.read_file(strFileName))
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        # DONE move IO code into function
        # 3.3.2 Add item to the table
        # DONE move processing code into function
        strID, strTitle, stArtist = IO.add_inventory()
        DataProcessor.Process_added_inventory(strID, strTitle, stArtist, lstTbl)
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove
        while True:
            try:
                intIDDel = int(input('Which ID would you like to delete? ').strip())
                break
            except ValueError:
                    print("This is not integer")
            
        # 3.5.2 search thru table and delete CD
        # DONE move processing code into function
        DataProcessor.delete_inventory(intIDDel, lstTbl)
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            FileProcessor.write_file( lstTbl, strFileName)
            # 3.6.2.1 save data
            # DONE move processing code into function
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')




