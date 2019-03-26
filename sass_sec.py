import os,time
import signal,datetime
from threading import Timer
c=True
notme=True
thx=None
lines=[]
ftimesetup=not os.path.isfile("usdata.txt")
if ftimesetup:
 print("Welcome to SASS_SEC!")
 usdata=open("usdata.txt","w")
 usdata.write(input("Please enter your username: ")+"\n")
 usdata.write(input("Please enter a password: ")+"\n")
 usdata.close()
usdata=open("usdata.txt","r")
for line in usdata:
 lines.append(line.strip())
uname=lines[0]
pword=lines[1]
usdata.close()
print("Welcome to "+uname+"'s Rapsberry Pi.\nHe has been notified of your arrival with a loud annoying beep")
print("Also you have a *special* terminal now. No need to thank me! :)")
firsttime= os.path.isfile("RecentConnections.txt")
f=open("RecentConnections.txt","a")
if firsttime==False:
 f.write("WELCOME TO SASS_SEC!\n\n")
def ctrlz():
 print("\nOops, that's a no from me")
def isbad(inp):
  global notme,thx,f
  bad=False
  if "sudo" in inp:
   bad=True
   print("sudo ain't allowed buddy")
  elif "startx" in inp:
   bad=True
   print("No graphics for you buddy!")
  elif "sh" in inp:
   bad=True
   print("Some people just want to see the world burn")
  elif "halt" in inp or "reboot" in inp:
   bad=True
   print("yikes, hard luck chum")
  elif pword in inp:
   bad=True
   print("Apologies "+uname)
   notme=False
  elif "nano" in inp:
   bad=True
   print("KERNEL ERROR AT MEMORY ADRESS 0x00SCR3W_U")
  elif "cat" in inp:
   bad=True
   print("No kitties today ",thx)
  elif ":(){ :|: & };:" in inp:
   bad=True
   print("Oh dear "+thx+", i had no idea you'd stoop that low")
   f.write("This guy tried to fork bomb you^\n")
  elif "rm" in inp:
   bad=True
   print("I'll remove you if you keep that up")
  elif "poweroff" in inp:
   bad=True
   print("Unlucky bro")
  elif "init" in inp:
   bad=True
   print("We don't do that here")
  elif "shutdown" in inp:
   bad=True
   print("Stop trying fool")
  elif "mv" in inp:
   bad=True
   print("Yup, That's an error")
  elif "python" in inp:
   bad=True
   print("Sorry, Inception 2 has not been released yet") 
  return bad
b='SSH_CLIENT' in os.environ or 'SSH_TTY' in os.environ
if b:
 thx=os.environ.get("SSH_CLIENT")
 thx=thx.split(" ")[0]
 now=datetime.datetime.now()
 ctime=str(now.hour)+":"+str(now.minute)+":"+str(now.second)
 cdate=str(now.day)+"/"+str(now.month)+"/"+str(now.year)
 stri=thx+" Connected at "+ctime+" GMT on "+ cdate+"\n"
 f.write(stri) 
 f.close()
 if b and c: 
    c=False
    while notme:
     signal.signal(signal.SIGTSTP, ctrlz)
     try:
      command=input("stoopid@dumdum:~ $ ")
      if isbad(command)==False:
       os.system(command)
     except:
      print("\nYou ain't getting out that easy")
    f=open("RecentConnections.txt","a")
    f.write("^Access Granted^\n")
    f.close()
else:
 pass
