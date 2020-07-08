
import os
import random
#Initalise
print("""
~~~~~~~~~~~~~[Windog command line for Windows 10 Version 2004.]~~~~~~~~~~~~~~~~~

   \###\   /##\   /###//  /###//          /#####//
    \###\ /####\ /###//  ____            /#/ /#// 
     \######/\######//  /###// /#####// /#/ /#// /####// /#####//
      \####/  \####//  /###// /#/ /#// /#/ /#// /#//#// /#/ /#//
       \##/    \##//  /###// /#/ /#// /#####// /####// /#####//
                                                          /#//
                                                      |####//   /v1.2/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

                                                                                       """) 


def ep():
    print("[ep - every program]")
    print("get a list of every program on the system")
    print("This can include programs that can't be found on the program manager")
    print("eg, add or remove programs. Note: first time running may take some time...")
    print("starting operation...")
    os.startfile("epcmd.cmd")
    index()
def tr():
    print("[tr - tracecert]")
    print(" traces the 'hops' to the website [note: This may take some time...]")
    tri = input("(target website)> ")
    print("starting operation")
    temptr = open("temptr.cmd","w")
    temptr.write("title windog tr \n")
    temptr.write("color 02 \n")
    temptr.write("tracert " + tri + " \n")
    temptr.write("cmd /k")
    temptr.close()
    os.startfile("temptr.cmd")
    inp = input("(Process done, press anything to continue)")
    index()


def dr():
    print("[dr - directory encryptor]")
    print(""" A simple file encryptor, Just select what
    file you want to be encrypted.
    [Warning: If file path is entered in correctly the command
    will encrypt windog, this can be easyly reversed by going into
    cmd, typing: cd [filepath of windog] cipher /d.]""")
    con = input("(Do you want to encrypt files) Y/N ")
    if con == 'Y':
        dri = input("(File path)> ")
        if dri == "":
            print("Must put correct file path")
            index()
        print("Starting operation (writting tempory file)...")
        tempdr = open("tempwincommmand.cmd","w")
        tempdr.write("cd  " + dri +"\n")
        tempdr.write("cipher /e \n" )
        tempdr.write("cmd /k \n" )
        tempdr.close()
        os.startfile("tempwincommmand.cmd")
        print("operation complete!")
        print("removing tempory file")
        Conis = input("(Process done, press anything to continue)")
        if Conis == "f":
            print("Done, files in ", dri,  " have been encrypted, see cmd console for more info")
        print("Done, files in ", dri,  " have been encrypted, see cmd console for more info")

    if con == 'N':
        print("operation cancelled ")
        index()

    else: index()

def pas():
    print("[pas - windog password generator]")
    print(""" This is a tool that enables the user to generate 
    a secure random pattern of letters and numbers for a password
    of the chosers length. [Its recommended that you copy and paste
    this into a notepad document or on a piece of paper!!!]""")
    Data = ['a','A','B','b','C','c','D','d','E','e','F','f',',','/','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z','1','2','3','4','5','6','7','8','9']
    Password = []
    Leng = int(input("(length of password)> "))
    for i in range (Leng):
        a = random.choice(Data)
        Password.append(a)

    
    print("Password is :  ", "".join(Password))
    index()
    

def no():
    print("[no - network overview, starting...]")
    os.startfile("nocmd.cmd")

def ta():
    print("[ta - tasks, displaying system info and current tasks...]")
    os.startfile("tacmd.cmd")


def ipn():
    print("[ipn - Asking for new ip...]")
    os.startfile("ipncmd.cmd")


def ipconfig():
    print("""[if - Complete network]
             Gives the user detailed infomation
             on the users ip. Plus any connected
             IP's will be shown here.
             With the speed of a connection to google's sever.
             And connnections in the network
             Do you want run this program?""")

    input1 = input("(if)> Y/N ")

    if input1 == 'Y':
        print("opening file.....")
        os.startfile("ifcmd.cmd")
        print("operation completed!")
        index()
    if input1 == 'y':
        print("opening file.....")
        os.startfile("ifcmd.cmd")
        print("operation completed!")
        index()
    else: index()
    



def repair():
    print("""[wp - WinRepair]
             This option will open a new cmd command line
             that will run commands to help detect and
             repair corruption in the os (windows only).
             - a command line will open and use two commands
             (sfc and DISM)
             - estimated time, 30 - 1 hour depending on system
             Do you want run this program?""")
    input1 = input("(wp)> Y/N  ")
    if (input1 == "N" or "n"):
        print("operation cancelled") 
        index()
         
    if (input1 == "Y" or "y"):
        
        print("opening file.....")
        os.startfile("wpcmd.cmd")
        print("operation completed!")
        index()
    



def help():
    print("""[help]
          Windog is command line tool box for windows 2004,
          Helping to solve a wide range of problems plus simplifying 
          the cmd command line into easy understand mini commands.
          These commands open files which run multiable commands all at once!
          And are all built in to the windows operating system. 

            The functionality of windog is being constantly changed and added too.
          For now these are some simple commands you can use to help fix some common
          issues. [These commands will NOT damage the system unless a violation of the on screen
          instuctions!!!]
          [Commands]
          {Network related}
          - if [A command to give a complete overview of users current network]
          - ipn [A command to generate a new ip]
          - no [Displays all networks and connected network password]
          - tr [tracert, shows the path that packets take from your computer untill it reaches your destination]
          
          {System related}
          - ta [Displays all system hardware and current tasks + driver info]
          - dr [simple file encrypter]
          - ep [Displays every program on the system.]
          
          {advanced system related, Open these through search and select run as admin!!!}
          <These are not found in windog command!>
          - prokey.cmd [scipt that shows your windows 10 product key]
          - rpcmd.cmd [widows repair through DISM + sfc]
          
          ----------------------------------[non cmd]----------------------------------
          - pas [Simple password generator]
          - exit [exits program]
          

          """)
    index()

def index():
        #command checker
        import os
        
        print("Type: help. For all the commands to the system")
        Input1 = input("(win)> ")

        if Input1 == 'wp': #wp
            repair()
        

        if Input1 == 'help': #help
            help()

        if Input1 == 'if': #ipconfig
            ipconfig()

        if Input1 == 'ipn': #ipn
            ipn()

        if Input1 == 'ta': #tasks
            ta()

        if Input1 == 'no': #network overview
            no()

        if Input1 == 'dr': #Directory explorer
            dr()

        if Input1 == 'tr': #tracer
            tr()

        if Input1 == 'ep': #every program
            ep()



        #non-cmd related stuff

        if Input1 == 'pas':
            pas()
        
        if Input1 == 'exit':
            exit()




        
        print("invalid command")
        index()
        

#start
index()
#notes, template
"""if (Input1 == '???'): #wp
        ???()
    """