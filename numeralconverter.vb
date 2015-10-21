Public Class NumeralConverter
    Shared tmpString as String = ""

    Public Shared Sub Main(args as String())
        If args.Length = 0 Then
            Console.Write("Enter Arabic number: ")
            tmpString = Console.Readline()
        Else
            tmpString = args(0)
        End If


    End Sub
End Class
