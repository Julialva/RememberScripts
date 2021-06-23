import random
ReasonPhrase = ["OK","Created","No Content","Moved Permanently","Found","Not Modified","Bad Request",
                "Unauthorized","Forbidden","Not Found","proxy authentication required","multiple resource use conflict",
                "Unsupported media type","Too many requests - rate limit reached","Internal Server Error","Not Implemented",
                "bad gateway","Service Unavailable","gateway timeout"]
ResponseCode = [200,201,204,301,302,304,400,401,403,404,407,409,415,429,500,501,502,503,504]
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