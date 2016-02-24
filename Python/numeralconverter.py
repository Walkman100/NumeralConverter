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
    
    while number > 500:
        number = number - 500
        print("D")
    while number > 400:
        number = number - 400
        print("CD")
    
    while number > 100:
        number = number - 100
        print("C")
    while number > 90:
        number = number - 90
        print("XC")
    
    while number > 50:
        number = number - 50
        print("L")
    while number > 40:
        number = number - 40
        print("XL")
    
    while number > 10:
        number = number - 10
        print("X")
    while number > 9:
        number = number - 9
        print("IX")
    
    while number > 5:
        number = number - 5
        print("V")
    while number > 4:
        number = number - 4
        print("IV")
    
    while number > 1:
        number = number - 1
        print("I")
    print("\n")

def outputArabicNumber(RomanNumber):
    RomanNumber = RomanNumber.upper
    for i=0 to len(RomanNumber):
        select case RomanNumber(i):
            case "I":
                RomanNumber(i) = 1
            case "V":
                RomanNumber(i) = 2
            case "X":
                RomanNumber(i) = 3
            case "L":
                RomanNumber(i) = 4
            case "C":
                RomanNumber(i) = 5
            case "D":
                RomanNumber(i) = 6
            case "M":
                RomanNumber(i) = 7
            case else:
                print("\"" + RomanNumber(i) + "\" is not a valid Roman Numeral character!")
                exit()
    next
    # Now we have the roman number in arabic numbers (so we can use < and >), we just add it all
    ArabicNumber = 0
    RomanNumber = RomanNumber + "0" # Because loops, length calculation and next letter calculation
    for i=0 to len(RomanNumber) - 1:
        if i < len(RomanNumber) - 1 andalso RomanNumber(i) >= RomanNumber(i + 1):
            select case RomanNumber(i):
                case "1":
                    ArabicNumber = ArabicNumber + 1
                case "2":
                    ArabicNumber = ArabicNumber + 5
                case "3":
                    ArabicNumber = ArabicNumber + 10
                case "4":
                    ArabicNumber = ArabicNumber + 50
                case "5":
                    ArabicNumber = ArabicNumber + 100
                case "6":
                    ArabicNumber = ArabicNumber + 500
                case "7":
                    ArabicNumber = ArabicNumber + 1000
        elif i < len(RomanNumber) - 1:
            select case RomanNumber(i)
                case "1":
                    ArabicNumber = ArabicNumber - 1
                case "2":
                    ArabicNumber = ArabicNumber - 5
                case "3":
                    ArabicNumber = ArabicNumber - 10
                case "4":
                    ArabicNumber = ArabicNumber - 50
                case "5":
                    ArabicNumber = ArabicNumber - 100
                case "6":
                    ArabicNumber = ArabicNumber - 500
                case "7": # logic says this can't be possible, but no real reason to leave it out...
                    ArabicNumber = ArabicNumber - 1000
    next
    print(ArabicNumber)

main(sys.argv[1:])
