# -*- coding: utf-8 -*-

# imported libraries
import os
import pymysql
from time import sleep
from datetime import date 
import csv


# Set up the connection to MySQL from Python
try: # connection
    connection = pymysql.connect(host = '127.0.0.1', database = 'employees', user = 'root', passwd = 'Merciful#100')
    cursor = connection.cursor()
    
    print('')
    print('\033[0;32mCONNECTION ESTABLISHED\033[m')
    
    established = 1
    sleep(2)
    os.system('cls')
    
except:
    print('')
    print('\033[0;31mERROR CONNECTING DATABASE...\033[m')
    
    sleep(1)
    established = 0


# Check if connection worked
if established == 1: # if connection is established
    try:
        while True:
            os.system('cls')
            
            print('')
            print('CRUD - RECORDS LIST')
            print('')
            
            menu = ['VIEW RECORDS LIST', 'RECORDS SEARCH', 'ADD NEW RECORD', 'CHANGE RECORD', 'DELETE RECORD', 'EXPORT TABLE', 'IMPORT TABLE']
            
            for index, listItems in enumerate(menu):
                print(f'\033[0;36m[{index + 1}]\033[m {listItems}')
                
            print('\033[0;31m[0]\033[m EXIT PROGRAM')
            print('')
            
            selectOption = int(input('SELECT AN OPTION TO PERFORM: '))

            if selectOption in [0, 1, 2, 3, 4, 5, 6, 7]: # Options

                # records list
                if selectOption == 1: 
                    os.system('cls')
                    print('')
                    
                    try:
                        result = cursor.execute('SELECT * FROM employees')
                        
                        for result in cursor:
                            print(result)
                            
                    except:
                        print('\033[0;31mTABLE NOT FOUND CHECK CONNECTION\033[m')
                        
                    print('')
                    recordBreak = str(input('\033[0;33mPress ENTER or any key and enter to exit...\033[m '))

                # records search
                if selectOption == 2: 
                    os.system('cls')
                    
                    print('')
                    searchRecord = int(input('SELECT ID TO SEARCH: '))
                    print('')
                    
                    try:
                        searchID = cursor.execute(f'SELECT * FROM employees WHERE id = {searchRecord}')
                        connection.commit()
                        resultSearch = cursor.fetchone()
                        
                        if resultSearch == None:
                            print('\033[0;31mRECORD NOT FOUND SEE RECORD LIST\033[m')     
                            
                        else:
                            print(resultSearch)
                            
                    except:
                        print('\033[0;31mRECORD NOT FOUND, CHECK YOUR INPUT OR CONNECTION\033[m')
                        
                    print('')
                    searchBreak = str(input('\033[0;33mPress ENTER or any key and enter to exit...\033[m '))
                
                # add new record
                if selectOption == 3: 
                    os.system('cls')
                    
                    print('')
                    print('FILL IN TO ADD A NEW RECORD...')
                    print('')
                    1
                    id = int(input('ID (empty to self fill):  '))
                    name = str(input('FULL NAME: '))
                    email = str(input('ADDRESS EMAIL: '))
                    age = int(input('AGE: '))
                    designation = str(input('DESIGNATION: '))
                    createdDate = str(input('CREATED DATE [yyyy-mm-dd]: '))
                    
                    print('')
                    confirmInclusion = str(input('CONFIRM INCLUSION OF RECORDS \033[0;31m[Y/N]\033[m? ')).strip().upper()
                    
                    if confirmInclusion == 'Y':
                        try:
                            cursor.execute("INSERT INTO employees(id, name, email, age, designation, created)   \
                                            VALUES (%s, %s, %s, %s, %s, %s)", (id, name, email, age, designation, createdDate))
                            connection.commit()
                            
                            print('')
                            print('\033[0;32mSUCCESSFUL INCLUSION\033[m')
                            
                        except:
                            print('')
                            print('\033[0;31mNOT DONE INCLUSION, CHECK YOUR INPUT OR CONNECTION\033[m')
                            
                    else:
                        print('')
                        print('\033[0;31mUNREALIZED INCLUSION\033[m')
                        
                    print('')
                    sleep(2)


                # change record
                if selectOption == 4: 
                    os.system('cls')
                    
                    print('')
                    changeID = int(input('REGISTRATION ID FOR CHANGE: ')) 
                    print('')
                    
                    print('LOOKING FOR RECORD...') 
                    print('')
                    sleep(2)
                    
                    try:
                        searchChangeID = cursor.execute(f'SELECT * FROM employees WHERE id = {changeID}')
                        connection.commit()
                        resultChangeSearch = cursor.fetchone()
                        
                        if resultChangeSearch == None:
                            print('\033[0;31mRECORD NOT FOUND SEE RECORD LIST\033[m')
                            changeIDConnection = 0      
                            
                        else:
                            print(resultChangeSearch)
                            changeIDConnection = 1
                            
                    except:
                        print('\033[0;31mRECORD NOT FOUND, CHECK YOUR INPUT OR CONNECTION\033[m')
                        changeIDConnection = 0
                        
                    if changeIDConnection == 1:
                        print('')
                        
                        listOptions = ['ID', 'FULL NAME', 'ADDRESS EMAIL', 'AGE', 'DESIGNATION', 'CREATED DATE [yyyy-mm-dd]']
                        
                        for index, listItems in enumerate(listOptions):
                            print(f'\033[0;36m[{index + 1}]\033[m {listItems}')
                            
                        print('')
                        
                        changeColumn = int(input('SELECT THE COLUMN NUMBER YOU WISH TO MODIFY: '))
                        
                        if changeColumn == 1:
                            changeColumn = 'id'
                            
                        elif changeColumn == 2:
                            changeColumn = 'name'
                            
                        elif changeColumn == 3:
                            changeColumn = 'email'
                            
                        elif changeColumn == 4:
                            changeColumn = 'age'
                            
                        elif changeColumn == 5:
                            changeColumn = 'designation'
                            
                        elif changeColumn == 6:
                            changeColumn = 'created'
                            
                        print('')
                        newChange = str(input('NEW INPUT: '))
                        
                        try:
                            changeModify = cursor.execute(f"UPDATE employees SET {changeColumn} = '{newChange}' WHERE id = {changeID}")
                            connection.commit()
                            
                            print('')
                            print('\033[0;32mSUCCESSFUL MODIFICATION\033[m')
                            
                        except:
                            print('')
                            print('\033[0;31mERROR TRYING TO MODIFY, CHECK TABLE OR CONNECTION\033[m')
                            
                    print('')
                    sleep(2)


                # delete record
                if selectOption == 5: 
                    os.system('cls')
                    
                    print('')
                    deleteID = int(input('ID TO DELETE: '))
                    print('')
                    
                    try:
                        deletedID = cursor.execute(f'SELECT * FROM employees WHERE id = {deleteID}')
                        connection.commit()
                        resultDeleteSearch = cursor.fetchone()
                        deleteRecordConnection = 1
                        
                        if resultDeleteSearch == None:
                            deleteRecordConnection = 0
                            print('\033[0;31mRECORD NOT FOUND SEE RECORD LIST\033[m')   
                            
                        else:
                            print(resultDeleteSearch)
                            print('')
                            
                    except:
                        deleteRecordConnection = 0
                        print('\033[0;31mRECORD NOT FOUND, CHECK YOUR INPUT OR CONNECTION\033[m')
                        
                    if deleteRecordConnection == 1:
                        confirmDelete = str(input('DO YOU REALLY WANT TO DELETE THIS RECORD? \033[0;31m[Y/N]\033[m ')).strip().upper()
                        
                        if confirmDelete == 'Y':
                            try:
                                deletedID = cursor.execute(f'DELETE FROM employees WHERE id = {deleteID}')
                                connection.commit()
                                
                                print('')
                                print('\033[0;32mSUCCESSFULLY DELETE RECORD, SEE LIST OF RECORDS TO VIEW\033[m')
                                
                            except:
                                print('')
                                print('\033[0;31mERROR DELETING RECORD, CHECK INPUT OR CONNECTION\033[m')
                                
                        else:
                            print('')
                            print('\033[0;31mREGISTRATION NOT DELETED\033[m')
                            
                    print('')
                    sleep(2)
                

                # export table
                if selectOption == 6: 
                    os.system('cls')
                    
                    print('')
                    nameExport = str(input('EXPORT FILE NAME: '))
                    
                    try:
                        result = cursor.execute('SELECT * FROM user')
                        wayExport = ('C:' + os.sep + 'Users' + os.sep + os.getlogin() + os.sep + 'Desktop' + os.sep)
                        newFile = wayExport + f'{nameExport}.txt'
                        
                        with open(newFile, 'w', newline='') as exitLines:
                            writerFile = csv.writer(exitLines)
                            
                            for row in cursor:
                                writerFile.writerow(row)
                                
                        print('')
                        print('\033[0;32mFILE SUCCESSFULLY EXPORTED\033[m')
                        sleep(2)
                        
                    except:
                        print('')
                        print('\033[0;31mUNEXPECTED ERROR, FILE NOT EXPORTED\033[m')
                        sleep(2)
                        
                    print(' ')


                # import table
                if selectOption == 7:  
                    os.system('cls')
                    
                    print('')
                    importFile = str(input('ENTER FILE.TXT NAME TO IMPORT: '))
                    
                    try:
                        wayImport = ('C:' + os.sep + 'Users' + os.sep + os.getlogin() + os.sep + 'Desktop' + os.sep)
                        fileImport = wayImport + f'{importFile}.txt'
                        
                        with open(fileImport, 'r') as inputLines:
                            readFile = csv.reader(inputLines)
                            
                            for row in readFile:
                                numberID = int(row[0])
                                fullName = str(row[1])
                                profession = str(row[2])
                                birth = str(row[3])
                                genre = str(row[4])
                                bodyweight = float(row[5])
                                height = float(row[6])
                                nationality = str(row[7])
                                
                                try:
                                    cursor.execute("INSERT INTO employees (id, fullname, profession, birth, genre, bodyweight, height, nationality)   \
                                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (numberID, fullName, profession, birth, genre, bodyweight, height, nationality))
                                    connection.commit()
                                    importStatus = 1
                                    
                                except:
                                    importStatus = 0
                                    
                        if importStatus == 1:
                            print('')
                            print('\033[0;32mSUCCESSFUL IMPORT FILE\033[m')
                            
                        else:
                            print('')
                            print('\033[0;31mFILE NOT IMPORTANT, CHECK INPUT FILE\033[m')
                            
                    except:
                        print('\033[0;31mUNEXPECTED ERROR, CHECK FILE OR CONNECTION\033[m')
                        print('')
                        
                    sleep(2)


                # exit program
                if selectOption == 0: 
                    print('')
                    print('\033[0;31mPROGRAM FINISHED\033[m')
                    print('')
                    
                    sleep(1)
                    break
                
            # invalid option
            else: 
                print('')
                print('\033[0;31mINVALID OPTION TRY AGAIN\033[m')
                sleep(1)

    except KeyboardInterrupt:
        print('\033[0;33mProgram terminated by the user!\033[m')
        print('')
        
# if connection is not established
elif established == 0: 
        print('')
        print('\033[0;31mCHECK DATABASE CONNECTION AND TRY AGAIN\033[m')
        print('')
