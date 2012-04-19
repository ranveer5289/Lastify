import subprocess
from Tkinter import Label
from Tkinter import Tk

class checkgrowl():

        def showdialog(self):
                root = Tk()
                w = Label(root, text="Growl not running")
                w.pack()
                root.mainloop()
        

        def checkrunning(self):
                output = subprocess.Popen(['tasklist'], stdout=subprocess.PIPE).communicate()[0]

                if "Growl" in output:
                        print "growl is running "
                else:
                        self.showdialog()
                        return False


#cg = checkgrowl()
#cg.checkrunning()
