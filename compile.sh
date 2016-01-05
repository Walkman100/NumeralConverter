#!/bin/sh
vbnc "-out:numeralconverter.exe" -nologo -utf8output -quiet -rootnamespace:numeralconverter -target:exe /win32icon:"doc-convert-arabic-to-roman-numbers2.ico" "numeralconverter.vb" "AssemblyInfo.vb"
