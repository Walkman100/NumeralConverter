#!/bin/sh
vbnc "-out:numeralconverter.exe" -nologo -utf8output -quiet -rootnamespace:numeralconverter -target:exe /win32icon:"VB/doc-convert-arabic-to-roman-numbers2.ico" "VB/numeralconverter.vb" "VB/AssemblyInfo.vb"
