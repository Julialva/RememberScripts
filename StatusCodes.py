import random
ReasonPhrase = ["Informational","Successful","OK","Created","No Content","Redirection","Moved Permanently","Found","Not Modified",
                "Client Error","Bad Request","Unauthorized","Forbidden","Not Found","Server Error","Internal Server Error","Not Implemented",
                "Service Unavailable"]
ResponseCode = ["1xx","2xx",200,201,204,"3xx",301,302,304,"4xx",400,401,403,404,"5xx",500,501,503]
wrongs = 0
rights = 0
for item in ReasonPhrase:
    Reason = random.choice(ReasonPhrase)
    number = int(input("Guess the response code for the phrase: " + Reason + "\n"))
    try:
        if ReasonPhrase.index(Reason) == ResponseCode.index(number):
            print("You Da Man!")
            rights = rights + 1
        else:
            print("You dumb ass that's wrong... The correct response code was: {0}".format(ResponseCode[ReasonPhrase.index(Reason)]))
            wrongs = wrongs + 1
    except:
        print("That value isn't even in the list")
        wrongs = wrongs + 1
print('Hey boss here is your score...              Correct Answers: {0}     Wrong Answers: {1}'.format(rights,wrongs))