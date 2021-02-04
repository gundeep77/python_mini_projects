Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "D:\PythonProjects\extras\hack\system.bat" & Chr(34), 0
Set WinScriptHost = Nothing