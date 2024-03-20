# Library Management System
import math
import random
import os
import time
import pickle
import csv
print("Welcome to the Library Management System")
time.sleep(0.3)
print("Hello there",end="")
print(".",end="")
time.sleep(0.5)
print(".",end="")
time.sleep(0.5)
print(".")
time.sleep(0.5)
file_exists = os.path.exists('Name.dat')
#Checking File Existence 
if file_exists:
    pass
else:
    f=open("Name.dat","wb")
    l=['admin','admin']
    pickle.dump(l,f)
    f.close()
n=0
while True:
    try:
        
        if n==1:
            pass
        else:
            # Start Of User Interface
            # name_list is used for storing the data of file Name.dat and editing it.
            print("If you are new user press 1 to continue::")
            print("If you are an existing user press 2 to continue::")
            print("If you want to exit the system press 3::")
            time.sleep(0.5)
            n=int(input("Enter your choice::"))
            name_list=[]
    except:
        print("Only integer values.")
    try:
        if n==1:
            f=open("Name.dat","rb")
            while True:
                try:
                    s=pickle.load(f)
                    name_list.append(s)
                except:
                    break
            f.close()  
            f=open("Name.dat","ab+")
            l=[]
            user=input("Create username::")
            # Now we check if username exists in Name.dat
            while True:
                truth=1
                for i in range(len(name_list)):
                    if user==name_list[i][0]:
                        print("The Username already exists...")
                        truth=0
                            
                if truth==1:
                    break
                user=input("Create username::")
            l.append(user)
            ps=input("Create password::")
            l.append(ps)
            l.append([])
            pickle.dump(l,f)
            f.close()
            n=0
            print("Your account has been successfully made.")
        elif n==2:
            while True:
                ttruth=1
                f=open("Name.dat","rb")
                while True:
                    try:
                        s=pickle.load(f)
                        name_list.append(s)
                    except:
                        break  
                user=input("Enter username::")
                # Now we if username is correct
                while True:
                    truth=0
                    for i in range(len(name_list)):
                        if user==name_list[i][0]:
                            truth=1
                            nuser=i
                            # nuser represents position in which that paticular user is in name_list
                            break
                    if truth==1:
                        break
                    else:
                        print("There is no such username...")
                        print("Please remember that username is case sensitive...")
                        q=input("Do you want to create a new username press y or Y to continue::")
                        if q=="y" or q=="Y":
                            ttruth=0
                            n=1
                            break
                        else:    
                            user=input("Enter your username::")
                if ttruth==0:
                    break
                ps=input("Enter your password::")
                while True:
                    if ps==name_list[nuser][1]:
                        print("Your have accessed your account",name_list[nuser][0])
                        break
                    else:
                        print("Your password is wrong")
                        ps=input("Enter your password::")
                if user=="admin":
                    #csv file append and display
                    truth=1
                    sl=0
                    data_backup=[]
                    list_del=[]
                    f=open("csv_file.csv",'r')
                    csvr=csv.reader(f)
                    for line in csvr:
                        print(line)
                        print()
                        #copying data into a temporary storage area from csv file
                        data_backup.append(line)
                        #sl now is the total number of data unit present
                        sl+=1
                    f.close()
                    sl-=1
                    print("Do you want to edit data in the library.. ")
                    ans=input("Enter y or Y if yes... ")
                    if ans=='y'or ans=='Y':
                        f=open("csv_file.csv",'w',newline="")
                        csvw=csv.writer(f)
                        ans2=input("Do you want to keep the records?\n Enter y or Y if yes...  ")
                        if ans2=='y'or ans2=='Y':
                            pass
                        else:
                            #reusing ans2 and not wasting it
                            #we cant use ans as it is being used in the second while loop
                            print("Would you like to delete the full data...")
                            ans2=input("Enter y or Y if yes... ")
                            if ans2=='y'or ans2=='Y':
                                data_backup.clear()
                            else:
                                ans2='y'
                                #reusing ans2
                                for i in data_backup:
                                    print(i)
                                    print()

                                #del_list means it will store no. which user wants deleted    
                                del_list=[]    
                                print("Enter the data no you would like to delete")
                                print("Write an integer more than ",sl," to go out of the loop")
                                print("Or write some number which you have already written")
                                while ans2=='y'or ans2=='Y':
                                    a=int(input("Enter data no "))
                                    if (a>sl or a<=0)or(a in del_list) :
                                        break
                                    else:
                                        del_list.append(a)
                                #now we have all things we need deleted
                                #we sort it in descending order
                                del_list.sort(reverse=True)
                                for i in del_list:
                                    data_backup.pop(i)
                                    sl-=1
                                print("Do you want to update the library also?::")
                                n4=input("Enter y or Y::")
                                if n4=="y" or n4=="Y":
                                    pass
                                else:
                                    truth=0
                        
                        # we write whatever is in data backup
                        while (ans=='y'or ans=='Y') and truth==1:
                            sl+=1
                            l=[]
                            l.append(sl)
                            aname=input("Enter Author's name::")
                            l.append(aname)
                            bname=input("Enter Book's name::")
                            l.append(bname)
                            genre=[]
                            ngenre=int(input("Enter no. Genres::"))
                            for i in range(ngenre):
                                gen=input("Enter Genres::")
                                genre.append(gen)
                            l.append(genre)
                            l.append("y")
                            ans=input("Enter y to continue::")
                            data_backup.append(l)
                        csvw.writerows(data_backup)    
                        f.close()
                    ttruth=0
                if ttruth==0:
                    break
                else:
                    while True:
                        # Interface for accesing library
                        print("Welcome",user,"to the library")
                        print("Press 1 to borrow a book::")
                        print("Press 2 to return a book::")
                        print("Press 3 to exit the library::")
                        try:
                            n2=int(input("Enter your choice::"))
                            if n2==1:
                                while True:
                                    truth=0
                                    data_backup=[]
                                    f=open('csv_file.csv',"r")
                                    csvr=csv.reader(f)
                                    for line in csvr:
                                        print(line)
                                        print()
                                        data_backup.append(line)
                                        # data_backup contains the information of books in the library
                                    f.close()
                                    n4=int(input("Enter the book no of the book you want to borrow ::"))
                                    while truth!=1:
                                        if n4>0 and n4<len(data_backup):
                                            break
                                        try:
                                            n4=int(input("Enter the book no of the book you want to borrow::"))
                                        except:
                                            print("You can only enter integer values.")

                                    l=[n4,time.time()]
                                    data_backup[n4].pop()
                                    data_backup[n4].append("n")
                                    f=open('csv_file.csv','w')
                                    csvw=csv.writer(f)
                                    csvw.writerows(data_backup)
                                    f.close()
                                    name_list[nuser][2].append(l)
                                    f=open("Name.dat","wb")
                                    for i in range(len(name_list)):
                                        pickle.dump(name_list[i],f)
                                    f.close()
                                    print("Do you want to borrow another book?::")
                                    n5=input("Enter y or Y if yes::")
                                    if n5=="y" or n5=="Y":
                                        pass
                                    else:
                                        ttruth=0
                                        break
                            elif n2==2:
                                data_backup=[]
                                f=open('csv_file.csv',"r")
                                csvr=csv.reader(f)
                                for line in csvr:
                                    data_backup.append(line)
                                f.close()
                                try:
                                    c=0
                                    truth2=1
                                    for i in range(len(name_list[nuser][2])):
                                        print("Do you want to return",data_backup[name_list[nuser][2][i-c][0]][2])
                                        n5=input("Enter 1 for yes::")
                                        if n5=="1":
                                            # This is the order of data_backup
                                            # S.no, Author's Name, Book's Name, Genres, Availaibility
                                            data_backup[name_list[nuser][2][i-c][0]].pop(-1)
                                            data_backup[name_list[nuser][2][i-c][0]].append("y")
                                            print("You have borrowed the book for",math.ceil((time.time()-name_list[nuser][2][i-c][1])/(3600*24)),"days")
                                            print("You have to pay",math.ceil((time.time()-name_list[nuser][2][i-c][1])/(3600*24))*5,"rupees")
                                            name_list[nuser][2].pop(0)
                                            f=open("Name.dat","wb")
                                            for i in range(len(name_list)):
                                                pickle.dump(name_list[i],f)
                                            f.close()
                                            f=open('csv_file.csv','w')
                                            csvw=csv.writer(f)
                                            csvw.writerows(data_backup)
                                            f.close()
                                            c=c+1
                                            if len(name_list[nuser][2])==0:
                                                truth2=1
                                                print("You have no other books to return")
                                                break
                                            else:
                                                n6=input("Do you want to return another book?, type y or Y if yes::")
                                                if n6=="y" or n6=="Y":
                                                    continue
                                                else:
                                                    truth2=1
                                                    
                                                
                                        else:
                                            if len(name_list[nuser][2])==1:
                                                truth2=1
                                                print("You have no other books to return")
                                            else:
                                                n6=input("Do you want to return another book?, type y or Y if yes::")
                                                if n6=="y" or n6=="Y":
                                                    pass
                                                else:
                                                    truth2=1
                                        if truth2==1:
                                            break
                                except IOError:
                                    print("You dont have any books to return")
                                truth=1
                            elif n2==3:
                                ttruth=0
                                break
                        except:
                            print("Wrong Input")
                            
                        if truth==1:
                            print("You have no books to return.")
                            ttruth=0
                            pass
                if ttruth==0:
                    break
        elif n==3:
            f=open("bookqt.txt",'r')
            s=f.readlines()
            print("Here is a quote for you:-")
            print(s[random.randint(0,5)],end="")
            print("See you soon...!!!")
            print("Have a nice day.")
            print("Brofist..!!")
            f.close()
            break
        elif n>3:
            print("Wrong input")
    except IOError:
        None
      
   
    
   
    
            
