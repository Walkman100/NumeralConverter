Public Class NumeralConverter
    Shared tmpString As String = ""

    Public Shared Sub Main(args As String())
        If args.Length = 0 Then
            Console.Write("Input Arabic or Roman number? (a/r) ")
            tmpString = Console.ReadKey().Key.ToString
            Console.Writeline()
            If tmpString = "A"
                Console.Write("Enter Arabic number: ")
                tmpString = Console.Readline()
                If IsNumeric(tmpString) Then
                    OutputRomanNumeral(tmpString)
                Else
                    Console.Writeline("""" & tmpString & """ is not an Arabic number!")
                End If
            ElseIf tmpString = "R"
                Console.Write("Enter Roman number: ")
                tmpString = Console.Readline()
                'OutputArabicNumber(tmpString)
            Else
                Console.Writeline("""" & tmpString & """ isn't 'a' or 'r'!")
            End If
        Else
            Select case args(0)
                Case "-h"
                    Console.Writeline("NumeralConverter - github.com/Walkman100/NumeralConverter")
                    Console.Writeline("Usage: " & System.Diagnostics.Process.GetCurrentProcess.ProcessName & ".exe [-h|-r (roman number)|-a (arabic number)]")
                Case "-a"
                    If IsNumeric(args(1)) Then
                        OutputRomanNumeral(args(1))
                    Else
                        Console.Writeline("""" & args(1) & """ is not an Arabic number!")
                    End If
                Case "-r"
                    'OutputArabicNumber(args(1))
                Case Else
                    Console.Writeline("Unrecognised flag """ & args(0) & """!")
                    Console.Writeline("Usage: " & System.Diagnostics.Process.GetCurrentProcess.ProcessName & ".exe [-h|-r (roman number)|-a (arabic number)]")
            End Select
        End If
    End Sub

    Shared Sub OutputRomanNumeral(number As Integer)
        Do Until (number - 1000) < 0
            number = number - 1000
            Console.Write("M")
        Loop
            Do Until (number - 900) < 0
                number = number - 900
                Console.Write("CM")
            Loop
        Do Until (number - 500) < 0
            number = number - 500
            Console.Write("D")
        Loop
            Do Until (number - 400) < 0
                number = number - 400
                Console.Write("CD")
            Loop
        Do Until (number - 100) < 0
            number = number - 100
            Console.Write("C")
        Loop
            Do Until (number - 90) < 0
                number = number - 90
                Console.Write("XC")
            Loop
        Do Until (number - 50) < 0
            number = number - 50
            Console.Write("L")
        Loop
            Do Until (number - 40) < 0
                number = number - 40
                Console.Write("XL")
            Loop
        Do Until (number - 10) < 0
            number = number - 10
            Console.Write("X")
        Loop
            Do Until (number - 9) < 0
                number = number - 9
                Console.Write("IX")
            Loop
        Do Until (number - 5) < 0
            number = number - 5
            Console.Write("V")
        Loop
            Do Until (number - 4) < 0
                number = number - 4
                Console.Write("IV")
            Loop
        Do Until (number - 1) < 0
            number = number - 1
            Console.Write("I")
        Loop
        Console.Writeline()
    End Sub
End Class

#If RomanNumerals = True
I   1
V   5
X   10
L   50
C   100
D   500
M   1000
#End If
