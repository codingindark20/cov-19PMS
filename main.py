#ROCHAK RUPAKHETI   
#NP000534


#This is sourcecode of COVID-19 Patient Management System 
#This system handles, display and edit patient data


#FILE
file = open('data.txt','a')


#This is function for New Patient Registration
from datetime import date
import time
import itertools
today = date.today()
t = time.localtime()
now = time.strftime("%H:%M:%S",t)
counter = itertools.count()
def patientRegistration():
    file.write("\nDate : "+str(today)+"\tTime : "+str(now)+"\n")
    print("\nThis is New Patient Registration System\n")
    noOfEntry = int(input("Enter number of registration to be made : "))
    i=1
    while i<=noOfEntry:
        id = next(counter)
        print("\n")
        patientName = input("Enter Patient's Fullname : ")
        patientAge = input("Enter patient's age : ")
        bloodGrp = input("Enter blood group : ")
        priorityGrp = input("Enter priority group among ATO/ACC/AEO/SID/AHS : ")
        
        #Writing data to the file
        file.write("Data\t")
        file.write(str(id))
        file.write("\t"+patientName)
        file.write("\t"+patientAge)
        file.write("\t"+bloodGrp)
        file.write("\t"+priorityGrp)
        i+=1

        if priorityGrp == "ATO" or priorityGrp == "ACC" or priorityGrp == "AEO":
            testrslt()

        elif priorityGrp == "SID":
            testSID()

        elif priorityGrp == "AHS":
            testAHS()

        else:
            print("You entered invalid Priority Group.")
            return
#END OF FUNCTION     




#Function for SID (Symptomatic Individuals)
def testSID():
    def T1SID():
        print("\n")
        T1result = input("Enter the Test1 result (+ve/-ve) : ")
        file.write("\tT1 : "+T1result)
        if T1result == "+ve":
            NWICU = input("Enter the quarantine of the patient (NW/ICU) : ")
            file.write("\t"+NWICU)
            print("Patient is in : "+NWICU)
            file.write("\tACTIVE\n")
        elif T1result == "-ve":
            file.write("\tHQFR")
            print("Patient is in Home Quarantine.\n")
            T2SID()
        else:
            print("Sorry! Invalid Input")
    
    def T2SID():
        T2result = input("Enter Test2 result (+ve/-ve) : ")
        file.write("\tT2 : "+T2result)
        if T2result == "+ve":
            NWICU = input("Enter the quarantine of the patient (NW/ICU) : ")
            file.write("\t"+NWICU)
            file.write("\tACTIVE\n")
            print("Patient is in : "+NWICU)
        elif T2result == "-ve":
            file.write("\tHQFR")
            print("Patient is in Home Quarantine.\n")
            T3SID()
        else: 
            print("Sorry! Invalid Input")

    def T3SID():
        T3result = input("Enter Test3 result (+ve/-ve) : ")
        file.write("\tT3 : "+T3result)  
        if T3result == "+ve":
            NWICU = input("Enter the quarantine of the patient (NW/ICU) : ")
            file.write("\t"+NWICU)
            file.write("\tACTIVE\n")
            print("Patient is in : "+NWICU)
        elif T3result == "-ve":
            file.write("\tRU")
            print("Patient is in Home")
            file.write("\tRECOVERED\n")
        else:
            print("Sorry! Invalid Input.")
    
    T1SID()
#END OF FUNCTION         



#Function for AHS (Asymptomatic Hospital Staff)
def testAHS():
    def T1AHS():
        print("\n")
        T1result = input("Enter Test1 result (+ve/-ve) : ")
        file.write("\tT1 : "+T1result)
        if T1result == "+ve":
            file.write("\tHQNF")
            file.write("\tACTIVE\n")
            print("Patient is in Home Quarantine.")
        elif T1result == "-ve":
            file.write("\tCWFR")
            print("Continue working and follow up test is required.\n")
            T2AHS()
        else:
            print("Sorry! Invalid Input.")
    
    def T2AHS():
        T2result = input("Enter Test2 result (+ve/-ve) : ")
        file.write("\tT2 : "+T2result)
        if T2result == "+ve":
            file.write("\tHQNF")
            file.write("\tACTIVE\n")
            print("Patient is in Home Quarantine.\n")
        elif T2result == "-ve":
            file.write("\tCWFR")
            print("Continue working and follow up test is required.\n")
            T3AHS()
        else:
            print("Sorry! Invalid Input.")
    

    def T3AHS():
        T3result = input("Enter Test3 result (+ve/-ve) : ")
        file.write("\tT3 : "+T3result)
        if T3result == "+ve":
            file.write("\tHQNF")
            file.write("\tACTIVE\n")
            print("Patient is in Home Quarantine.")
        elif T3result == "-ve":
            file.write("\tCW")
            file.write("\tRECOVERED\n")
            print("Continue working.")
        else:
            print("Sorry! Invalid Input.")
     
    T1AHS()
#END OF FUNCTION 




#This is function for Test Results and Action Taken
def testrslt():
    def T1():
        print("\n")
        T1result = input("Enter Test1 result (+ve/-ve) : ")
        file.write("\tT1 : "+T1result)
        if T1result == "+ve":
            NWICU = input("Enter the quarantine of the patient (NW/ICU) : ")
            file.write("\t"+NWICU)
            file.write("\tACTIVE\n")
            print("Patient is in : "+NWICU)
        elif T1result == "-ve":
            file.write("\tQDFR")
            print("Patient is in Quarantine Center.\n")
            T2()
        else:
            print("Sorry! Invalid Input")

    def T2():
        T2result = input("Enter Test2 result (+ve/-ve) : ")
        file.write("\tT2 : "+T2result)
        if T2result == "+ve":
            NWICU = input("Enter the quarantine of the patient (NW/ICU) : ")
            file.write("\t"+NWICU)
            file.write("\tACTIVE\n")
            print("Patient is in : "+NWICU)
        elif T2result == "-ve":
            file.write("\tQDFR")
            print("Patient is in Quarantine Center.\n")
            T3()
        else:
            print("Sorry! Invalid Input.")


            
    def T3():
        T3result = input("Enter Test3 result (+ve/-ve) : ")
        file.write("\tT3 : "+T3result)  
        if T3result == "+ve":
            NWICU = input("Enter the quarantine of the patient (NW/ICU) : ")
            file.write("\t"+NWICU)
            file.write("\tACTIVE\n")
            print("Patient is in : "+NWICU)
        elif T3result == "-ve":
            file.write("\tRU")
            file.write("\tRECOVERED\n")
            print("Patient is in Home\n")
        else:
            print("Sorry! Invalid Input.")

    T1()
#END OF FUNCTION 




#This is function for Setting and Changing Patient Status(ACTIVE/RECOVERED/DECEASED)
import sys
import fileinput
def settingChng():
    print("\n\tSetting and Changing Patient Status\n")
    # with is like your try .. finally block in this case
    with open('data.txt') as file:

# read a list of lines into data
        data = file.read()

    print(data)
    
    print("\nYou can change case status ACTIVE to RECOVERED\n")
    lineno = int(input("Enter 1 to change case status ACTIVE to RECOVERD : "))
    if lineno == 1:

# replace all occurrences of 'ACTIVE' with 'RECOVERED' 
        for i, line in enumerate(fileinput.input('data.txt', inplace=1)):
            sys.stdout.write(line.replace('ACTIVE', 'RECOVERED'))  
    print("\nData changed succesfully!\n")
    view = int(input("Press 1 to view new data : "))
    if view == 1:
        with open('data.txt') as file:
            newdata = file.read()
            print(newdata)

#END OF FUNCTION       




#This is Function for Statiscal Information on Tests Carried Out
def statsInfo():
    print("\n\tStatistical Information\n")
    
    with open("data.txt") as f:
        readfile = f.read()


    totalTests = 0
    PatientTested = 0
    RecoveredCases = 0
    ActiveCases = 0

    
    for line in readfile:
        stats = readfile.split(",")
        if stats == 'T1' or 'T2' or 'T2' :
            totalTests += 1
        elif stats == 'Data' :
            PatientTested += 1
        elif stats == 'ACTIVE' :
            ActiveCases += 1
        elif stats == 'RECOVERED':
            RecoveredCases += 1

    print("There are ", totalTests, " Total Tests done.")
    print("There are ", PatientTested, " patient tested.")
    print("There are ", ActiveCases, " active cases.")
    print("There are ", RecoveredCases, " recovered cases.")
#END OF FUNCTION

    


#This function is for Searching Functionalities
def searching():
    print("\tSearch\n")
    print("\n1. Search by ID\n2. Search By Name\n")
    searchOption = int(input("Choose a option (1/2) : "))
    searchfile = open("data.txt")
    
    if searchOption == 1:
        searchId = int(input("Enter ID : "))

        for line in searchfile:
            if line.startswith(str(searchId)):
                print(line)
                break
            else:
                print("Sorry! Data is not found.")
        
    
    elif searchOption == 2:
        searchName = input("Enter patients name : ")
       
        for line in searchfile:
            if line.startswith(searchName):
                print(line)
                break
            else:
                print("Sorry! Data is not found!")

    else:
        print("Sorry! your input is wrong! Please try again.")
#END OF FUNCTION


#Output window starts here
print("\t\tCOVID-19 Patient Management System\n")
print("1. New Patient Registration\n2. Setting and Changing Patient Status\n3. Statistical Information\n4. Search\n ")
option = int(input("Choose a option (1/2/3/4) : "))

if option == 1:
    patientRegistration()

#elif option == 2:
    #testrslt()

elif option == 2:
    settingChng()

elif option == 3:
    statsInfo()

elif option == 4:
    searching()

else:
    print("Sorry! your input is wrong! Please try again.")
    
   
   #END OF PROGRAM
   #Created by : Rochak Rupakheti
   #website >> www.rochakrupakheti.com.np
    
