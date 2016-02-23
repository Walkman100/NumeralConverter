import sys, getopt

# https://stackoverflow.com/q/354038/2999220
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

tmpString = ""
def main(args):
    if len(args) == 0:
        tmpString = raw_input("Input Arabic or Roman number? (a/r): ")
        tmpString = tmpString.upper()
        if tmpString == "A":
            checkAndOutputRomanNumeral(raw_input("Enter Arabic number: "))
        elif tmpString == "R":
            outputArabicNumber(raw_input("Enter Roman number: "))
        else:
            print("\"" + tmpString + "\" isn't 'a' or 'r'!")
    else:
        select case args(0)
            case "-h":
                print("NumeralConverter - github.com/Walkman100/NumeralConverter")
                printUsage()
            case "-a"
                if len(args) > 1: checkAndOutputRomanNumeral(args(1))
                else: checkAndOutputRomanNumeral(raw_input("Enter Arabic number: "))
            case "-r"
                if len(args) > 1: outputArabicNumber(args(1)
                else: outputArabicNumber(raw_input("Enter Roman number: "))
            case else:
                print("Unrecognised flag \"" + args(0) + "\"!")
                printUsage()

def printUsage():
    flags = " [-h|-r [roman number]|-a [arabic number]]"
    print("python " + sys.argv(0) + flags)

def checkAndOutputRomanNumeral(input):
    if is_integer(input):
        if len(input) < 19:
            outputRomanNumeral(input)
        else:
            print("\"" + input + "\" is " + (len(input) - 18 + " digit(s) too long! Maximum size for \"\\\" operations is 18 digits")
    else:
        print("\"" + input + "\" is not an Arabic number!")

def outputRomanNumeral(number):
    if number > 1000:
        for i=1 to (number \ 1000):
            print("M")
        number = number - (number \ 1000) * 1000
    while number > 900:
        number = number - 900
        print("CM")
    
    while number > :
        number = number - 
        print("D")
    while number > :
        number = number - 
        print("CD")
    
    while number > :
        number = number - 
        print("C")
    while number > :
        number = number - 
        print("XC")
    
    while number > :
        number = number - 
        print("L")
    while number > :
        number = number - 
        print("XL")
    
    while number > :
        number = number - 
        print("X")
    while number > :
        number = number - 
        print("IX")
    
    while number > :
        number = number - 
        print("V")
    while number > :
        number = number - 
        print("IV")
    
    while number > :
        number = number - 
        print("I")
    print("\n")

def outputArabicNumber(RomanNumber):
    RomanNumber = RomanNumber.upper
    

main(sys.argv[1:])