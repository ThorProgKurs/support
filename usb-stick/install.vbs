Set fso = CreateObject("Scripting.FileSystemObject") 
fld = fso.GetParentFolderName(WScript.ScriptFullName) & "\packages"
CreateObject("WScript.Shell").Run "cygwin.exe -q -L -R c:\cygwin -l " & chr(34) & fld & chr(34)
