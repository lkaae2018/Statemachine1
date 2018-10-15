#Statemachine til beskrivelse af livets gang
import time

y=0
tid=1

def Home(x):
    global y
    global tid
    y=y+1
    print("Y="+str(y))
    if y==50:
        return
    if x=="wake":
        x="take train"
        print("Tager toget på arbejde")
        time.sleep(tid)
        return Work(x)
    elif x=="take train":
        x="sleep"
        print("Går i seng")
        time.sleep(tid)
        return Bed(x)

def Work(x):
    if x=="take train":
        x="take train"
        print("Tager toget hjem fra arbejde")
        time.sleep(tid)
        return Home(x)

def Bed(x):
    if x=="sleep":
        x="wake"
        print("Vågner")
        time.sleep(tid)
        return Home(x)


state=Home(x="wake")
while state: state=Home(x="wake")
print("Død of færdig!!!!")




