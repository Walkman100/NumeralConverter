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
        If (number - 1000) > 0 Then
            number = number - 1000
            Console.Write("M")
        End If

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
