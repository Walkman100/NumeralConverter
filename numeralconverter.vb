Public Class NumeralConverter
    Shared tmpString As String = ""

    Public Shared Sub Main(args As String())
        If args.Length = 0 Then
            Console.Write("Enter Arabic number: ")
            tmpString = Console.Readline()
        Else
            tmpString = args(0)
        End If
        
        If IsNumeric(tmpString) Then
            OutputRomanNumeral(tmpString)
        Else
            Console.Writeline(tmpString & " is not an Arabic number!")
        End If
    End Sub

    Shared Sub OutputRomanNumeral(number As Integer)
        Do Until (number - 1000) < 0
            number = number - 1000
            Console.Write("M")
        Loop
        Do Until (number - 500) < 0
            number = number - 500
            Console.Write("D")
        Loop
        Do Until (number - 100) < 0
            number = number - 100
            Console.Write("C")
        Loop
        Do Until (number - 50) < 0
            number = number - 50
            Console.Write("L")
        Loop
        Do Until (number - 10) < 0
            number = number - 10
            Console.Write("X")
        Loop
        Do Until (number - 5) < 0
            number = number - 5
            Console.Write("V")
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
