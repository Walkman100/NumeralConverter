#!/bin/sh
vbnc "-out:numeralconverter.exe" -nologo -utf8output -quiet -rootnamespace:numeralconverter -target:exe  "numeralconverter.vb" "AssemblyInfo.vb"
