VBC = vbnc
VBCFLAGS = -nologo -quiet -utf8output -rootnamespace:numeralconverter -target:exe /win32icon:VB/doc-convert-arabic-to-roman-numbers2.ico
VBFILES = VB/numeralconverter.vb VB/AssemblyInfo.vb

numeralconvertervb: numeralconverter.exe
# two rules so it doesn't recompile if the VB files haven't been changed since compile
numeralconverter.exe: $(VBFILES)
	$(VBC) $(VBCFLAGS) -out:numeralconverter.exe $(VBFILES)

clean:
	$(RM) numeralconverter.exe
	$(RM) -r VB/bin
# in case you had been using MonoDevelop
