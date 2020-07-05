
import os
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
    if input1 == 'l':
        print("llll")

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
          - if [A command to give a complete overview of users current network]
          - ipn [A command to generate a new ip]
          - ta [Displays all system hardware and current tasks]
          - no [Displays all networks and connected network password]
          """)
    index()

def index():
        #command checker
        import os
        print("Windog commandline 2020") 
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

        
        print("invalid command")
        index()
        

#start
index()
#notes, template
"""if (Input1 == '???'): #wp
        ???()
    """