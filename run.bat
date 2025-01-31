start powershell.exe -NoExit -ExecutionPolicy Bypass -Command "$env:TERM='xterm-256color'; & '%~dp0hex2ascii\Scripts\Activate.ps1'; python '%~dp0Hex2ASCII.py'"
