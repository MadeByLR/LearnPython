#Working with different IF statements which each statement is self explanetory is what it is asking
isMale = False
isTall = False

if isMale or isTall:
    print("You are either male, tall or both")
elif isMale and not(isTall):
    print("You are a short male")
elif not(isMale) and isTall:
    print("You are not male but are tall")
else:
    print("You are neither male or tall")
