import random
ProtocolName = ['File Tansfer Protocol - data','File Transfer Protocol - control',
'Secure Shell', 'Telnet', 'Simple Mail Transfer Protocol','Domain Name Service',
'Dynamic Host Configuration Protocol - Server', 'Dynamic Host Configuration Protocol - Client',
'Trivial File Transfer Protocol', 'Hypertext Transfer Protocol', 'Post Office Protocol Version 3',
'Internet Message Access Protocol','Simple Network Management Protocol','Hypertext Transfer Protocol Secure']
PortNumber = [20,21,22,23,25,53,67,68,69,80,110,143,161,443]
#TransferMethod =['TCP','TCP','TCP','TCP','TCP','TCP or UDP','UDP',"UDP","UDP",'TCP','TCP','TCP','UDP','TCP']
wrongs = 0
rights = 0
for item in ProtocolName:
    Protocol = random.choice(ProtocolName)
    number = int(input("Guess the PortNum for protocol: " + Protocol + "\n"))
    try:
        if ProtocolName.index(Protocol) == PortNumber.index(number):
            print("You Da Man!")
            rights = rights + 1
        else:
            print("You dumb ass that's wrong... The correct port was: {0}".format(PortNumber[ProtocolName.index(Protocol)]))
            wrongs = wrongs + 1
    except:
        print("That value isn't even valid homie...")
        wrongs = wrongs + 1
print('Hey boss here is your score...              Correct Answers: {0}     Wrong Answers: {1}'.format(rights,wrongs))