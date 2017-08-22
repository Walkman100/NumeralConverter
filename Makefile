VBC = vbnc
VBCFLAGS = -nologo -quiet -utf8output -rootnamespace:numeralconverter -target:exe /win32icon:VB/doc-convert-arabic-to-roman-numbers2.ico
VBFILES = VB/numeralconverter.vb VB/AssemblyInfo.vb

numeralconvertervb: numeralconverter.exe
# two rules so it doesn't recompile if the VB files haven't been changed since compile
numeralconverter.exe: $(VBFILES)
	$(VBC) $(VBCFLAGS) -out:numeralconverter.exe $(VBFILES)

apo: numeralconverter.apostrophus.exe
apostro: numeralconverter.apostrophus.exe
apostrophus: numeralconverter.apostrophus.exe
numeralconverter.apostrophus.exe: VB/numeralconverter.apostrophus.vb VB/AssemblyInfo.vb
	$(VBC) $(VBCFLAGS) -out:numeralconverter.apostrophus.exe VB/numeralconverter.apostrophus.vb VB/AssemblyInfo.vb

clean:
	$(RM) numeralconverter.exe
	$(RM) numeralconverter.apostrophus.exe
	$(RM) -r VB/bin
# in case you had been using MonoDevelop

all: numeralconvertervb apo
