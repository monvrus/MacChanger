import subprocess
import optparse
import re

def getUserInput():
    parseObject = optparse.OptionParser()
    parseObject.add_option("-i","--interface",dest="interface",help="interface to change")
    parseObject.add_option("-m","--mac",dest="macAdress",help="new mac adress")

    return parseObject.parse_args()


def changeMacAdress(userInterface,userMacadres):
    subprocess.call(["ifconfig",userInterface,"down"])
    subprocess.call(["ifconfig",userInterface,"hw","ether",userMacadres])
    subprocess.call(["ifconfig",userInterface,"up"])

def controlNewMac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))

    if new_mac:
        return new_mac.group(0)
    else:
        return None

print("mymacchanger started")
(userInput,arguments) = getUserInput()
changeMacAdress(userInput.interface,userInput.macAdress)
finalized_mac = controlNewMac(str(userInput.interface))

if finalized_mac == userInput.macAdress:
    print("Succes ! ")
else:
    print("Error !")