# NumeralConverter
Convert between [Arabic Numerals](https://en.wikipedia.org/wiki/Arabic_numerals) and [Roman Numerals](https://en.wikipedia.org/wiki/Roman_numerals)

## Program Usage
### Windows
You can download the [NumeralConverter.bat](https://github.com/Walkman100/NumeralConverter/blob/master/numeralconverter.bat) file and put it in the same folder as the executable to use the program without opening a command prompt first.

To use from the command prompt, from the program folder:
```sh
> numeralconverter -h
Usage: numeralconverter.exe [-h|-r (roman number)|-a (arabic number)]
> numeralconverter -r CMXCIX
999
> numeralconverter -a 543
DXLIII
> numeralconverter
Input Arabic or Roman number? (a/r): a
Enter Arabic number: 543
DXLIII
> numeralconverter -a 543 > output.txt
```
Contents of `output.txt` will be `DXLIII`.

### Linux (Mono)
See the [MonoTests](https://github.com/Walkman100/VBNCW/tree/master/MonoTests) folder in `VBNCW` to make sure you have `mono` and `vbnc` up and running, then from the program folder:
```sh
> mono numeralconverter.exe -h
Usage: numeralconverter.exe [-h|-r (roman number)|-a (arabic number)]
> mono numeralconverter.exe -r CMXCIX
999
> mono numeralconverter.exe -a 543
DXLIII
> mono numeralconverter.exe
Input Arabic or Roman number? (a/r): a
Enter Arabic number: 543
DXLIII
> mono numeralconverter.exe -a 543 > output
> cat output
DXLIII
```
