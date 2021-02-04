Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "D:\PythonProjects\extras\youtube_downloader\runner_multi_with_notification.bat" & Chr(34), 0
Set WinScriptHost = Nothing