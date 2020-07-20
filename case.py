import os
import shutil
import subprocess

## Reading the parameters and setting the variables 
path = os.environ.get ("ospath")
caseid = input ("CaseID: ")
casetype = input ("chat/call/e-mail: ")
customername = input ("Customer name: ")
productname = input ("Product name: ")
source_chat = path+"chat.txt"
source_call = path+"call.txt"
source_email = path+"email.txt"
destination = path + str(caseid) + "/" 
mailfile = os.path.join (destination, "correspondence.txt")
text_editor = "vscode"
text_editor_args = "-n"

## Defining the function to create case folder
def createcasefolder (caseid):
    try:
        os.mkdir(destination)
    except:
        print ("Folder has failed to be created")
    else:
        print (caseid + " folder created successfully")

## Calling the funcion createcasefolder
createcasefolder (caseid)

## Branching the case based on the case type
if casetype == "chat" or casetype == "Chat":
    shutil.copyfile(source_chat,mailfile)
    subprocess.Popen([text_editor,text_editor_args,mailfile])
elif casetype == "call" or casetype == "Call":
    shutil.copyfile(source_call,mailfile) 
    subprocess.Popen([text_editor,text_editor_args,mailfile])
else:
    shutil.copyfile(source_email,mailfile)
    subprocess.Popen([text_editor,text_editor_args,mailfile])
