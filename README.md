# NumeralConverter
Convert between [Arabic Numerals](https://en.wikipedia.org/wiki/Arabic_numerals) and [Roman Numerals](https://en.wikipedia.org/wiki/Roman_numerals)

## Compiling
To compile and test the latest source code:
- open a command prompt or terminal in the parent folder of where you want to download NumeralConverter to
```sh
git clone https://github.com/Walkman100/NumeralConverter.git
cd NumeralConverter
# on windows:
compile
numeralconverter -h
# on linux:
./compile.sh
mono numeralconverter.exe -h
```

- On Linux, either:
  - rename the file to `numeralconverter` to be able to just do `mono numeralconverter -h`
  - create a `numeralconverter` script in `/usr/bin` (or `/bin`) with the contents of:
```sh
#!/bin/sh

mono /full/path/to/numeralconverter.exe $@
```
then `chmod 777` it and you should be able to just do `numeralconverter -h` from any folder.

## Program Usage
### Windows
You can download the [NumeralConverterWindows.bat](https://github.com/Walkman100/NumeralConverter/blob/master/NumeralConverterWindows.bat) file and put it in the same folder as the executable to use the program without opening a command prompt first.

To use from the command prompt, from the program folder:
```sh
> numeralconverter -h
Usage: numeralconverter.exe [-h|-r [roman number]|-a [arabic number]]
> numeralconverter -r CMXCIX
999
> numeralconverter -a
Enter Arabic number: 543
DXLIII
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
Usage: numeralconverter.exe [-h|-r [roman number]|-a [arabic number]]
> mono numeralconverter.exe -r CMXCIX
999
> mono numeralconverter.exe -a
Enter Arabic number: 543
DXLIII
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
