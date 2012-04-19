import subprocess
from Tkinter import Label
from Tkinter import Tk

class checkgrowl():

        def showdialog(self):
                #Instantiate Tk class which displays the main window.
                root = Tk()
                #Add label to main window(root).
                w = Label(root, text="Growl not running")
                w.pack()
                root.mainloop()
        

        def checkrunning(self):
                #Get list of all running processes in windows and check if Growl.exe present or not.
                output = subprocess.Popen(['tasklist'], stdout=subprocess.PIPE).communicate()[0]

                if "Growl" in output:
                        print "growl is running "
                else:
                        self.showdialog()
                        return False

#Testing Purpose
#cg = checkgrowl()
#cg.checkrunning()
