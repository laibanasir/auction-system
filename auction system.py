#________________Importing Modules_______________


import tkinter as tk
import uuid
import logging
from tkinter import IntVar
from tkinter import StringVar
from tkinter import messagebox
from functools import partial
from tkinter import *
import random


#_______________Global variables declaration_______________


global idWin 
global registrationDict
global name
global registrationNumber
registrationDict = {'Laiba' : '1234566',
                    'Kainat' : '1234556'}


#_______________Main Window with buttons_______________


def main() :
    system = tk.Tk()
    system.configure(background = "#addbd9")
    system.geometry("1000x700")
    system.title("Auction System")
    label = tk.Label(system,
                   text = "Welcome to the auction system",
                   fg = "white",
                   bg = "#addbd9",
                   font = "Helvita 36 bold italic").place(anchor = 'center', relx = 0.5, rely = 0.05)


    logInButton = tk.Button(system, text = "Manage id", 
        width = 18,
        activebackground = "#adb7db",
        activeforeground = "white",
        anchor = "center",
        cursor = "heart",
        height = 1,
        relief = "sunken",
        fg = "white",
        bg = "#898787",
        command = manageId ,
        font = "Times 30 bold").place(anchor = 'center', relx = 0.5, rely = 0.21)

               
    toBidButton = tk.Button(system, text = "Call a bid", 
        width = 18,
        activebackground = "#adb7db",
        activeforeground = "white",
        anchor = "center",
        cursor = "heart",
        height = 1,
        relief = "sunken",
        fg = "white",
        bg = "#898787",
        command =  callABid,
        font = "Times 30 bold").place(anchor = 'center', relx = 0.5, rely = 0.37)

    
    viewbidsbutton = tk.Button(system, text = "View Bids", 
        width = 18,
        activebackground = "#adb7db",
        activeforeground = "white",
        anchor = "center",
        cursor = "heart",
        height = 1,
        relief = "sunken",
        fg = "white",
        bg = "#898787",
        command = viewBids,
        font = "Times 30 bold").place(anchor = 'center', relx = 0.5, rely = 0.53)


    companyButton = tk.Button(system, text = "Authorized Pesons Only", 
        width = 18,
        activebackground = "#adb7db",
        activeforeground = "white",
        anchor = "center",
        cursor = "heart",
        height = 1,
        relief = "sunken",
        fg = "white",
        bg = "#898787",
        command = company ,
        font = "Times 30 bold").place(anchor = 'center', relx = 0.5, rely = 0.69)

    
    exit = tk.Button(system, text = "Exit", command = system.destroy,
        width = 18,
        activebackground = "#adb7db",
        activeforeground = "white",
        anchor = "center",
        cursor = "heart",
        height = 1,
        relief = "sunken",
        fg = "white",
        bg = "#898787",
        font = "Times 30 bold").place(anchor = 'center', relx = 0.5, rely = 0.85)
    tk.mainloop()








    
    #_______________View Bids Window_____________________________________
    

def viewBids():
    
    viewBidsWin = tk.Tk()
    viewBidsWin.configure(background = "#addbd9")
    viewBidsWin.geometry("1000x700")
    viewBidsWin.title("Bids")



    
    #________________Check entry____________________


    
                
    def tobid():

         def checkEntry():

            global registrationCheck

            registrationCheck = str(entry1.get())

        
            if registrationCheck in registrationDict.values():
                currentpage = 1
                pagecount = 1
                currentpage += 1
 
                if currentpage >= pagecount:
                    buttonReg.config(state=DISABLED)

        
            else:
                messagebox.showerror("error", "try again")
                return 'Invalid.'
        
         v = StringVar()
         x = StringVar()
         labelReg = Label(viewBidsWin,text = "Registration Number: ",
                   fg = "white",
                   bg = "#addbd9",
                   font = "Helvita 7 bold italic").place(anchor = 'center', relx = 0.5, rely = 0.6)

         entry1 = tk.Entry(viewBidsWin, textvariable=v)
         entry1.place(anchor = 'center', relx = 0.7, rely = 0.6)
         
         buttonReg = tk.Button(viewBidsWin, text="Enter", width = 13,
            activebackground = "#adb7db",
            activeforeground = "white",
            anchor = "center",
            cursor = "heart",
            height = 1,
            relief = "sunken",
            fg = "white",
            bg = "#898787",
            command = checkEntry,
            font = "Times 10 bold")
         buttonReg.place(anchor = 'center', relx = 0.9, rely = 0.6)


         labelReg = Label(viewBidsWin,text = "Bid Amount ",
                   fg = "white",
                   bg = "#addbd9",
                   font = "Helvita 7 bold italic").place(anchor = 'center', relx = 0.5, rely = 0.5)
         def bidcheck():
            global entrybid

            entrybid = str(entry2.get())
            entryRegis = str(entry1.get())

        
            if not(entrybid.isdigit()):
                messagebox.showerror("error", "Enter digits only.")
                return 'Invalid Entry'
            else:
                currentpage = 1
                pagecount = 1
                currentpage += 1
 
                if currentpage >= pagecount:
                    buttonReg.config(state=DISABLED)
                    

#___________________Highest Bid____________________

                    
            bid = [0]
            bid.append(entrybid)
            bids = bid.sort(reverse = True)
            global highestbid

            highestbid = bids[0]
            bidders = [0]
            bidders.append(entryRegis)

            global companyGets
            companyGets = highestbid*10/100

            bidcount = 0
            if not(int(entrybid == 0) and int(entryRegis == 0)):
                bidcount += 1
        
             
         label0 = Label(viewBidsWin,text = "",
                   fg = "white",
                   bg = "#addbd9",
                   font = "Helvita 8 bold italic")
         label0.place(anchor = 'center', relx = 0.15, rely = 0.4)

             
         ##label0.config(text = "The product has been bought for $ Company gets $" )


         entry2 = tk.Entry(viewBidsWin, textvariable=x)
         entry2.place(anchor = 'center', relx = 0.7, rely = 0.5)

         buttonReg = tk.Button(viewBidsWin, text="Enter", width = 13,
            activebackground = "#adb7db",
            activeforeground = "white",
            anchor = "center",
            cursor = "heart",
            height = 1,
            relief = "sunken",
            fg = "white",
            bg = "#898787",
            command = bidcheck,
            font = "Times 10 bold")
         buttonReg.place(anchor = 'center', relx = 0.9, rely = 0.5)





    
             

         
    
    def bid1():

        labelname = Label(viewBidsWin,text = "Item name: Custom Artwork",
                   fg = "white",
                   bg = "#addbd9",
                   font = "Helvita 8 bold italic").place(anchor = 'center', relx = 0.15, rely = 0.2)
        labelbids = Label(viewBidsWin,text = "Number of bids: 2",
                   fg = "white",
                   bg = "#addbd9",
                   font = "Helvita 8 bold italic").place(anchor = 'center', relx = 0.15, rely = 0.3)
        labelbids = Label(viewBidsWin,text = "Item Description: A piece of antique artwork from the greek civilization.",
                   fg = "white",
                   bg = "#addbd9",
                   font = "Helvita 8 bold italic").place(anchor = 'center', relx = 0.15, rely = 0.4)
        labelbids = Label(viewBidsWin,text = "Minimum bid: $25",
                   fg = "white",
                   bg = "#addbd9",
                   font = "Helvita 8 bold italic").place(anchor = 'center', relx = 0.15, rely = 0.5)

        buttonbid = tk.Button(viewBidsWin, text="Bid", width = 13,
            activebackground = "#adb7db",
            activeforeground = "white",
            anchor = "center",
            cursor = "heart",
            height = 1,
            relief = "sunken",
            fg = "white",
            bg = "#898787",
            command = tobid,
            font = "Times 12 bold")
        buttonbid.place(anchor = 'center', relx = 0.5, rely = 0.2)

        
#_____________________________________________________________________________

        
    v = StringVar
    
   

    buttonReg1 = tk.Button(viewBidsWin, text="Bid1", width = 13,
            activebackground = "#adb7db",
            activeforeground = "white",
            anchor = "center",
            cursor = "heart",
            height = 1,
            relief = "sunken",
            fg = "white",
            bg = "#898787",
            command = bid1,
            font = "Times 12 bold")
    buttonReg1.place(anchor = 'center', relx = 0.5, rely = 0.2)






    viewBidsWin.mainloop()


#_______________Call a bid screen with functions_______________


def callABid():
    callABidWin = tk.Tk()
    callABidWin.configure(background = "#addbd9")
    callABidWin.geometry("1000x700")
    callABidWin.title("Call A Bid")


    label6 = tk.Label(callABidWin,
                   text = "Call a bid",
                   fg = "white",
                   bg = "#addbd9",
                   font = "Helvita 30 bold italic").place(anchor = 'center', relx = 0.5, rely = 0.05)


    labelCat = tk.Label(callABidWin, text = 'Category',width = 10,
        activebackground = "#adb7db",
        activeforeground = "white",
        anchor = "center",
        cursor = "heart",
        height = 1,
        relief = "sunken",
        fg = "white",
        bg = "#898787",
        font = "Times 18 bold").place(anchor = 'n', relx = 0.1, rely = 0.1)

    
    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    CheckVar3 = IntVar()
    CheckVar4 = IntVar()
    CheckVar5 = IntVar()
    CheckVar6 = IntVar()
    CheckVar7 = IntVar()
    

    CategoryCheckButton1 = tk.Checkbutton(callABidWin,
                                             text = 'Technology',
                                             variable = CheckVar1,
                                             onvalue = 1,
                                             offvalue = 0,
                                             height = 1,
                                             width = 10,
                                             bg = "#addbd9",
                                             selectcolor="white").place(anchor = 'center',
                                                               relx = 0.1,
                                                               rely = 0.215)

    
    CategoryCheckButton2 = tk.Checkbutton(callABidWin,
                                             text = 'Travel',
                                             variable = CheckVar2,
                                             onvalue = 1,
                                             offvalue = 0,
                                             height = 1,
                                             width = 10,
                                             bg = "#addbd9",
                                             selectcolor="white").place(anchor = 'center',
                                                               relx = 0.1,
                                                               rely = 0.25)

    
    CategoryCheckButton3 = tk.Checkbutton(callABidWin,
                                             text = 'Sports Tickets',
                                             variable = CheckVar3,
                                             onvalue = 1,
                                             offvalue = 0,
                                             height = 1,
                                             width = 10,
                                             bg = "#addbd9",
                                             selectcolor="white").place(anchor = 'center',
                                                               relx = 0.1,
                                                               rely = 0.28)

    
    CategoryCheckButton4 = tk.Checkbutton(callABidWin,
                                             text = 'Food',
                                             variable = CheckVar4,
                                             onvalue = 1,
                                             offvalue = 0,
                                             height = 1,
                                             width = 10,
                                             bg = "#addbd9",
                                             selectcolor="white").place(anchor = 'center',
                                                               relx = 0.1,
                                                               rely = 0.31)

    
    CategoryCheckButton5 = tk.Checkbutton(callABidWin,
                                             text = 'Music',
                                             variable = CheckVar5,
                                             onvalue = 1,
                                             offvalue = 0,
                                             height = 1,
                                             width = 10,
                                             bg = "#addbd9",
                                             selectcolor="white").place(anchor = 'center',
                                                               relx = 0.1,
                                                               rely = 0.34)

    
    CategoryCheckButton6 = tk.Checkbutton(callABidWin,
                                             text = 'Education',
                                             variable = CheckVar6,
                                             onvalue = 1,
                                             offvalue = 0,
                                             height = 1,
                                             width = 10,
                                             bg = "#addbd9",
                                             selectcolor="white").place(anchor = 'center',
                                                               relx = 0.1,
                                                               rely = 0.37)

    
    CategoryCheckButton7 = tk.Checkbutton(callABidWin,
                                             text = 'Sports',
                                             variable = CheckVar7,
                                             onvalue = 1,
                                             offvalue = 0,
                                             height = 1,
                                             width = 10,
                                             bg = "#addbd9",
                                             selectcolor = "white").place(anchor = 'center',
                                                               relx = 0.1,
                                                               rely = 0.41)


    #_________Check Entry Function___________________


    def checkEntry():
    

        entrye = str(entry3.get())

        
        if not(entrye.isdigit()):
            messagebox.showerror("error", "Enter digits only.")
            return 'Invalid Entry'
        else:
            currentpage = 1
            pagecount = 1
            currentpage += 1
 
            if currentpage >= pagecount:
                button3.config(state=DISABLED)

    def checkEntry1():


        entrye = str(entry3.get())

        
        if not(entrye.isdigit()):
            messagebox.showerror("error", "Enter digits only.")
            return 'Invalid Entry'
        else:
            currentpage = 1
            pagecount = 1
            currentpage += 1
 
            if currentpage >= pagecount:
                button3.config(state=DISABLED)


        


    #__________Entry Validation______________________

    def combine():


        entryValid()
        returnValue()
        
        
    def returnValue(arg = None):
        display1 = entry3.get()
        return display1

    
    def ad():
            adWin = tk.Tk()
            adWin.configure(background = "#addbd9")
            adWin.geometry("1000x700")
            adWin.title("Auction")
            adWin.mainloop()
            display1 = returnValue()
            v = StringVar()
            displayLabel1 = tk.Label(adWin, textvariable = v, text = "")
            diplayLabel1.config(text=display1)
            displayLabel1.pack(fill=X)

    def entryValid():
        if len(entry3.get()) == 0 or len(entry4.get()) == 0 or len(auctioneer.get("1.0",END)) == 0 or len(item.get("1.0",END)) == 0 :
            messagebox.showerror("error", "Fill in the empty field.")
            return 'Invalid Entry'

        else:
            currentpage = 1
            pagecount = 1
            currentpage += 1
 
            if currentpage >= pagecount:
                button7.config(state=DISABLED)
        ad()


        


    
    #__________Minimum bid___________________________

    
    label5 = tk.Label(callABidWin,
                   text = "Minimum bid",
                   fg = "white",
                   bg = "#addbd9",
                   font = "Helvita 18 bold italic").place(anchor = 'center', relx = 0.3, rely = 0.2)

        
    v = StringVar

    
    entry3 = tk.Entry(callABidWin, textvariable=v)
    entry3.place(anchor = 'center', relx = 0.5, rely = 0.2)

    
    button3 = tk.Button(callABidWin, text="Set", width = 13,
            activebackground = "#adb7db",
            activeforeground = "white",
            anchor = "center",
            cursor = "heart",
            height = 1,
            relief = "sunken",
            fg = "white",
            bg = "#898787",
            command = checkEntry,
            font = "Times 12 bold")
    button3.place(anchor = 'center', relx = 0.7, rely = 0.2)


    #____________________Back Button_________________________


    back = tk.Button(callABidWin, text = "Back", command = callABidWin.destroy,
        width = 10,
        activebackground = "#adb7db",
        activeforeground = "white",
        anchor = "center",
        cursor = "heart",
        height = 1,
        relief = "sunken",
        fg = "white",
        bg = "#898787",
        font = "Times 18 bold").place(relx = 0.8, rely = 0.9)

    
    #_____________Number of bids_____________

    
    def checkEntry5():
        currentpage = 1
        pagecount = 1
        currentpage += 1
        bidnum = str(entry4.get())
        
        if not(bidnum.isdigit()) :
             messagebox.showerror("error", "Enter digits")
 
        elif currentpage >= pagecount:
             button10.config(state=DISABLED)
            

    



    label6 = tk.Label(callABidWin,
                   text = "Number of bids",
                   fg = "white",
                   bg = "#addbd9",
                   font = "Helvita 18 bold italic").place(anchor = 'center', relx = 0.3, rely = 0.3)

        
    v = StringVar

    
    entry4 = tk.Entry(callABidWin, textvariable=v)
    entry4.place(anchor = 'center', relx = 0.5, rely = 0.3)

    
    button10 = tk.Button(callABidWin, text="Set", width = 13,
            activebackground = "#adb7db",
            activeforeground = "white",
            anchor = "center",
            cursor = "heart",
            height = 1,
            relief = "sunken",
            fg = "white",
            bg = "#898787",
            command=checkEntry5,
            font = "Times 12 bold")
    button10.place(anchor = 'center', relx = 0.7, rely = 0.3)



    #__________________Check registration Number_____________________

    def checkEntry2():


        registrationCheck = str(entry4.get())

        
        if registrationCheck not in registrationDict.values():
            messagebox.showerror("error", "Registration Number not found.")
            return 'The number you have entered is invalid.'

        else:
            currentpage = 1
            pagecount = 1
            currentpage += 1
 
            if currentpage >= pagecount:
                button4.config(state=DISABLED)

    #_______________On click______________

    def onclick():
        
            currentpage = 1
            pagecount = 1
            currentpage += 1
 
            if currentpage >= pagecount:
                button5.config(state=DISABLED)

                
            if currentpage >= pagecount:
                button6.config(state=DISABLED)



    #__________Registration Number_____________

    
    label6 = tk.Label(callABidWin,
                   text = "Registration Number",
                   fg = "white",
                   bg = "#addbd9",
                   font = "Helvita 10 bold italic").place(anchor = 'center', relx = 0.3, rely = 0.4)

        
    v = StringVar

    
    entry4 = tk.Entry(callABidWin, textvariable=v)
    entry4.place(anchor = 'center', relx = 0.5, rely = 0.4)

    
    button4 = tk.Button(callABidWin, text="Enter", width = 13,
            activebackground = "#adb7db",
            activeforeground = "white",
            anchor = "center",
            cursor = "heart",
            height = 1,
            relief = "sunken",
            fg = "white",
            bg = "#898787",
            command = checkEntry2,
            font = "Times 12 bold")
    button4.place(anchor = 'center', relx = 0.7, rely = 0.4)



    #__________auctioneer's description__________


    label7 = tk.Label(callABidWin,
                   text = "Auctioneer details",
                   fg = "white",
                   bg = "#addbd9",
                   font = "Helvita 14 bold italic").place(anchor = 'center', relx = 0.3, rely = 0.55)

        
    v = StringVar

    
    auctioneer = tk.Text(callABidWin, height=5, width=20)
    auctioneer.place(anchor = 'center', relx = 0.5, rely = 0.55)
    auctioneer.insert(tk.END, auctioneer)

    
    button5 = tk.Button(callABidWin, text="Enter", width = 13,
            activebackground = "#adb7db",
            activeforeground = "white",
            anchor = "center",
            cursor = "heart",
            height = 1,
            relief = "sunken",
            fg = "white",
            bg = "#898787",
            command = onclick,
            font = "Times 12 bold")
    button5.place(anchor = 'center', relx = 0.7, rely = 0.55)


    #___________Item details____________



    label6 = tk.Label(callABidWin,
                   text = "Item Description",
                   fg = "white",
                   bg = "#addbd9",
                   font = "Helvita 16 bold italic").place(anchor = 'center', relx = 0.3, rely = 0.75)

        
    v = StringVar


    item = tk.Text(callABidWin, height=5, width=20)
    item.place(anchor = 'center', relx = 0.5, rely = 0.75)
    item.insert(tk.END, item)


    
    button6 = tk.Button(callABidWin, text="Enter", width = 13,
            activebackground = "#adb7db",
            activeforeground = "white",
            anchor = "center",
            cursor = "heart",
            height = 1,
            relief = "sunken",
            fg = "white",
            bg = "#898787",
            command = onclick,
            font = "Times 12 bold")

    button6.place(anchor = 'center', relx = 0.7, rely = 0.75)


    #_____________________Place Ad button____________________


    button7 = tk.Button(callABidWin, text="Place Ad", width = 13,
            activebackground = "#adb7db",
            activeforeground = "white",
            anchor = "center",
            cursor = "heart",
            height = 1,
            relief = "sunken",
            fg = "white",
            bg = "#898787",
            command = entryValid,
            font = "Times 22 bold")


    button7.place(anchor = 'center', relx = 0.5, rely = 0.92)

    


    callABidWin.mainloop()

    
        


#_______________Manage Id screen with functions , registration number_______________
#_______________Dictionary or file still missing_____________

def manageId():
    idWin = tk.Tk()
    idWin.configure(background = "#addbd9")
    idWin.geometry("1000x700")
    idWin.title("Manage Id")


    def newRegistration():
        label3 = tk.Label(idWin,
                   text = "Name",
                   fg = "white",
                   bg = "#addbd9",
                   font = "Helvita 20 bold italic").place(anchor = 'center', relx = 0.3, rely = 0.7)

        
        v = StringVar
        entry00 = tk.Entry(idWin, textvariable=v)
        entry00.place(anchor = 'center', relx = 0.5, rely = 0.7)
        button00 = tk.Button(idWin, text="Enter", width = 13,
            activebackground = "#adb7db",
            activeforeground = "white",
            anchor = "center",
            cursor = "heart",
            height = 1,
            relief = "sunken",
            fg = "white",
            bg = "#898787",
            command = DisplayRegistration,
            font = "Times 12 bold")

        button00.place(anchor = 'center', relx = 0.5, rely = 0.8)

        
        name = str(entry00.get())

        registrationNumber = random.randint(1111111, 9999999)
        return 'Your registration number is ' + str(registrationNumber)

        registrationDict[name] = registrationNumber
                    

    def DisplayRegistration():
        result = newRegistration()
        displayRegistration = tk.Text(idWin, height = 2, width = 55)
        displayRegistration.place(anchor = 'center', relx = 0.5, rely = 0.9)
        displayRegistration.insert(tk.END, result)


        currentpage = 1
        pagecount = 1
        currentpage += 1
 
        if currentpage >= pagecount:
                button2.config(state=DISABLED)

        if currentpage >= pagecount:
                button1.config(state=DISABLED)



    
    def checkEntry():


        registrationCheck = str(entry1.get())

        
        if registrationCheck in registrationDict.values():
            return 'Dear user, you are now ready to take part in aunctions.'

        
        else:
            messagebox.showerror("error", "try again")
            return 'The number you have entered is invalid.'


    def checkResult():
        result = checkEntry()
        resultDisplay = tk.Text(idWin, height = 2, width = 55)
        resultDisplay.place(anchor = 'center', relx = 0.5, rely = 0.6)
        resultDisplay.insert(tk.END, result)
        currentpage = 1
        pagecount = 1
        currentpage += 1
 
        if currentpage >= pagecount:
                button1.config(state=DISABLED)

        
    v = StringVar()

    
    label1 = tk.Label(idWin,
                   text = "Do you have a registration number?",
                   fg = "white",
                   bg = "#addbd9",
                   font = "Helvita 32 bold italic").place(anchor = 'center', relx = 0.5, rely = 0.1)

    
    label2 = tk.Label(idWin,
                   text = "Enter here(xxxxxxx): ",
                   fg = "white",
                   bg = "#addbd9",
                   font = "Helvita 26 bold italic").place(anchor = 'center', relx = 0.5, rely = 0.3)


    entry1 = tk.Entry(idWin, textvariable=v)
    entry1.place(anchor = 'center', relx = 0.5, rely = 0.4)



            
    button1 = tk.Button(idWin, text="Enter", width = 10,
        activebackground = "#adb7db",
        activeforeground = "white",
        anchor = "center",
        cursor = "heart",
        height = 1,
        relief = "sunken",
        fg = "white",
        bg = "#898787",
        command = checkResult,
        font = "Times 12 bold")
    button1.place(anchor = 'center', relx = 0.5, rely = 0.5)


    button2 = tk.Button(idWin, text="Get a new one", width = 13,
        activebackground = "#adb7db",
        activeforeground = "white",
        anchor = "center",
        cursor = "heart",
        height = 1,
        relief = "sunken",
        fg = "white",
        bg = "#898787",
        command = newRegistration,
        font = "Times 12 bold")
    button2.place(anchor = 'center', relx = 0.5, rely = 0.6)


    back = tk.Button(idWin, text = "Back", command = idWin.destroy,
        width = 10,
        activebackground = "#adb7db",
        activeforeground = "white",
        anchor = "center",
        cursor = "heart",
        height = 1,
        relief = "sunken",
        fg = "white",
        bg = "#898787",
        font = "Times 18 bold").place(relx = 0.8, rely = 0.9)


#______________Company Button Working_______________


def company():


    #______________Log in window__________


    root = Tk()
    root.title("Authorized Persons Only")
    root.configure(background = "#addbd9")
    root.geometry("500x300")
    root.resizable(0, 0)

    #______________Log in variable_________


    PASSWORD = StringVar()

 
    #______________Log in frames____________


    Top = Frame(root, relief=RIDGE, bg = "#addbd9")
    Top.pack(side=TOP, fill=X)
    Form = Frame(root, height=200, bg = "#addbd9")
    Form.pack(side=TOP, pady=20)

 
    #______________Log in labels____________


    lbl_title = Label(Top, text = "Enter password to unlock access", bg = "#addbd9", font = "Helvita 15 bold italic", fg = 'white')
    lbl_title.pack(fill=X)
    lbl_password = Label(Form, text = "Password:", bg = "#addbd9", font = "Helvita 15 bold italic", fg = 'white')
    lbl_password.grid(row=1, sticky="e")
    lbl_text = Label(Form, bg = "#addbd9", font = "Helvita 15 bold italic", fg = 'white')
    lbl_text.grid(row=2, columnspan=2)

 
    #______________Password Entry___________


    password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
    password.grid(row=1, column=1)

    #______________Log In Function__________


    def Login(event=None):
        
        if password.get() == "12345678":
            lbl_text.config(text="Logging in", fg="red")
            HomeWindow()
            
        if password.get() == "":
            lbl_text.config(text="Please complete the required field!", fg="red")

        else:
            lbl_text.config(text="Invalid password", fg="red")
        
    #______________Log In button____________

        
    btn_login = Button(Form, text="Login", width=45, command=Login)
    btn_login.grid(pady=25, row=3, columnspan=2)
    btn_login.bind('<Return>', Login)


    #______________Company Window_____________


    def HomeWindow():

    
        global Home

    
        root.withdraw()
        Home = Toplevel()
        Home.title("Authorized persons only")
        Home.configure(background = "#addbd9")
        width = 600
        height = 500
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        root.resizable(0, 0)
        Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
        lbl_home = Label(Home, text="Successfully Login!", bg = "#addbd9", font = "Helvita 15 bold italic", fg = 'white').pack()
        btn_back = Button(Home, text='Back', command=Back).pack(pady=20, fill=X)


        label01 = tk.Label(Home, text="Account details", bg = "#addbd9", font = "Helvita 15 bold italic", fg = 'white').pack()
        label02 = tk.Label(Home, bg = "#addbd9", font = "Helvita 15 bold italic", fg = 'white').pack()
        label03 = tk.Label(Home, text = "Auctions done: ", bg = "#addbd9", font = "Helvita 15 bold italic", fg = 'white').pack()
        



        
 
    def Back():
        Home.destroy()
        root.deiconify()

    
    #______________Function Calling_____________

    
    if __name__ == '__main__':
        root.mainloop()



    
#_______________Calling main function_______________


main()



