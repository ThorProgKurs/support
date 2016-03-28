On Error Resume Next

Sub SetEnvVar
    Set objEnv = CreateObject("WScript.Shell").Environment("System")
    objEnv("PATH") = objEnv("PATH") & ";c:\cygwin\bin"
End Sub

If WScript.Arguments.Count = 0 then
    Set fso = CreateObject("Scripting.FileSystemObject") 
    fld = fso.GetParentFolderName(WScript.ScriptFullName) & "\packages"
    CreateObject("WScript.Shell").Run "cygwin.exe -q -L -R c:\cygwin -l " & chr(34) & fld & chr(34)
    SetEnvVar
    If Err.Number <> 0 Then
        currentDirectory = left(WScript.ScriptFullName,(Len(WScript.ScriptFullName))-(len(WScript.ScriptName)))
        Set UAC = WScript.CreateObject("Shell.Application")
        UAC.ShellExecute "wscript.exe", currentDirectory + "install.vbs /setPathOnly", "", "runas", 0
    End If
ElseIf WScript.Arguments(0) = "/setPathOnly" Then
    SetEnvVar
End If
