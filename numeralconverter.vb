Public Class NumeralConverter
    Shared tmpString As String = ""

    Public Shared Sub Main(args As String())
        If args.Length = 0 Then
            Console.Write("Input Arabic or Roman number? (a/r): ")
            tmpString = Console.ReadKey().Key.ToString
            Console.Writeline()
            If tmpString = "A"
                Console.Write("Enter Arabic number: ")
                CheckAndOutputRomanNumeral(Console.Readline())
            ElseIf tmpString = "R"
                Console.Write("Enter Roman number: ")
                OutputArabicNumber(Console.Readline())
            Else
                Console.Writeline("""" & tmpString & """ isn't 'a' or 'r'!")
            End If
        Else
            Select case args(0)
                Case "-h"
                    Console.Writeline("NumeralConverter - github.com/Walkman100/NumeralConverter")
                    WriteUsage()
                Case "-a"
                    If args.length > 1 Then : CheckAndOutputRomanNumeral(args(1))
                    Else : Console.Write("Enter Arabic number: ")
                           CheckAndOutputRomanNumeral(Console.Readline())
                    End If
                Case "-r"
                    If args.length > 1 Then : OutputArabicNumber(args(1))
                    Else : Console.Write("Enter Roman number: ")
                        OutputArabicNumber(Console.Readline())
                    End If
                Case Else
                    Console.Writeline("Unrecognised flag """ & args(0) & """!")
                    WriteUsage()
            End Select
        End If
    End Sub

    Shared Sub WriteUsage()
        Dim flags as String = " [-h|-r [roman number]|-a [arabic number]]"
        If My.Computer.Info.OSPlatform = "Unix" Then
            Console.Writeline("Usage: mono " & System.Diagnostics.Process.GetCurrentProcess.ProcessName & flags)
        ElseIf My.Computer.Info.OSPlatform = "Win32NT" Then
            Console.Writeline("Usage: " & System.Diagnostics.Process.GetCurrentProcess.ProcessName & flags)
        Else
            Console.Writeline("Unrecognised platform """ & My.Computer.Info.OSPlatform & """! Please report at https://github.com/Walkman100/NumeralConverter/issues/new")
            Console.Writeline("Default usage info: " & System.Diagnostics.Process.GetCurrentProcess.ProcessName & ".exe " & flags)
        End If
    End Sub

    Shared Sub CheckAndOutputRomanNumeral(input as String)
        If IsNumeric(input) Then
            If input.Length < 20 Then
                OutputRomanNumeral(input)
            Else
                Console.Writeline("""" & input & """ is " & (input.Length - 19) & " digit(s) too long! Maximum size for UInt64 is 19 digits")
            End If
        Else
            Console.Writeline("""" & input & """ is not an Arabic number!")
        End If
    End Sub

    Shared Sub OutputRomanNumeral(number As ULong)
        If number > 1000
            Dim i As Long
            For i = 1 to number \ 1000
                Console.Write("M")
            Next
            number -= (number \ 1000) * 1000
        End If
REM        Do Until number < 1000
REM            number -= 1000
REM            Console.Write("M")
REM        Loop
            Do Until number < 900
                number -= 900
                Console.Write("CM")
            Loop
        Do Until number < 500
            number -= 500
            Console.Write("D")
        Loop
            Do Until number < 400
                number -= 400
                Console.Write("CD")
            Loop
        Do Until number < 100
            number -= 100
            Console.Write("C")
        Loop
            Do Until number < 90
                number -= 90
                Console.Write("XC")
            Loop
        Do Until number < 50
            number -= 50
            Console.Write("L")
        Loop
            Do Until number < 40
                number -= 40
                Console.Write("XL")
            Loop
        Do Until number < 10
            number -= 10
            Console.Write("X")
        Loop
            Do Until number < 9
                number -= 9
                Console.Write("IX")
            Loop
        Do Until number < 5
            number -= 5
            Console.Write("V")
        Loop
            Do Until number < 4
                number -= 4
                Console.Write("IV")
            Loop
        Do Until number < 1
            number -= 1
            Console.Write("I")
        Loop
        Console.Writeline()
    End Sub

    Shared Sub OutputArabicNumber(RomanNumber As String)
        RomanNumber = RomanNumber.ToUpper
        Dim i As Long
        For i = 0 to RomanNumber.Length - 1
            Select Case RomanNumber(i)
                Case "I" ' below basically does RomanNumber.Char(i) = "1"
                    RomanNumber = RomanNumber.Remove(i) & "1" & RomanNumber.Substring(i + 1)
                Case "V"
                    RomanNumber = RomanNumber.Remove(i) & "2" & RomanNumber.Substring(i + 1)
                Case "X"
                    RomanNumber = RomanNumber.Remove(i) & "3" & RomanNumber.Substring(i + 1)
                Case "L"
                    RomanNumber = RomanNumber.Remove(i) & "4" & RomanNumber.Substring(i + 1)
                Case "C"
                    RomanNumber = RomanNumber.Remove(i) & "5" & RomanNumber.Substring(i + 1)
                Case "D"
                    RomanNumber = RomanNumber.Remove(i) & "6" & RomanNumber.Substring(i + 1)
                Case "M"
                    RomanNumber = RomanNumber.Remove(i) & "7" & RomanNumber.Substring(i + 1)
                Case Else
                    Console.Writeline("""" & RomanNumber(i) & """ is not a valid Roman Numeral character!")
                    End
            End Select
        Next
        ' Now we have the roman number in arabic numbers (so we can use < and >), now we just add it all
        Dim ArabicNumber as Long = 0
        RomanNumber = RomanNumber & "0" ' Because loops, length calculation and next letter calculation
        For i = 0 to RomanNumber.Length - 1
            If i < RomanNumber.Length - 1 AndAlso RomanNumber(i) >= RomanNumber(i + 1)
                Select Case RomanNumber(i)
                    Case "1"
                        ArabicNumber += 1
                    Case "2"
                        ArabicNumber += 5
                    Case "3"
                        ArabicNumber += 10
                    Case "4"
                        ArabicNumber += 50
                    Case "5"
                        ArabicNumber += 100
                    Case "6"
                        ArabicNumber += 500
                    Case "7"
                        ArabicNumber += 1000
                End Select
            ElseIf i < RomanNumber.Length - 1
                Select Case RomanNumber(i)
                    Case "1"
                        ArabicNumber -= 1
                    Case "2"
                        ArabicNumber -= 5
                    Case "3"
                        ArabicNumber -= 10
                    Case "4"
                        ArabicNumber -= 50
                    Case "5"
                        ArabicNumber -= 100
                    Case "6"
                        ArabicNumber -= 500
                    Case "7" ' logic says this can't be possible, but no real reason to leave it out...
                        ArabicNumber -= 1000
                End Select
            End If
        Next
        Console.Writeline(ArabicNumber)
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
