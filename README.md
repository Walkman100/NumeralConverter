# NumeralConverter
Convert [Arabic Numerals](https://en.wikipedia.org/wiki/Arabic_numerals) to [Roman Numerals](https://en.wikipedia.org/wiki/Roman_numerals)

## Program Usage
### Windows
You can download the [NumeralConverter.bat](https://github.com/Walkman100/NumeralConverter/blob/master/numeralconverter.bat) file and put it in the same folder as the executable to use the program without opening a command prompt first.

To use from the command prompt, from the program folder:
```sh
> numeralconverter 543
DXLIII
> numeralconverter
Enter Arabic number: 543
DXLIII
> numeralconverter 543 > output.txt
```
Contents of `output.txt` will be `DXLIII`.

### Linux (Mono)
See the [MonoTests](https://github.com/Walkman100/VBNCW/tree/master/MonoTests) folder in `VBNCW` to make sure you have `mono` and `vbnc` up and running, then from the program folder:
```sh
> mono numeralconverter.exe 543
DXLIII
> mono numeralconverter.exe
Enter Arabic number: 543
DXLIII
> mono numeralconverter.exe 543 > output
> cat output
DXLIII
```
