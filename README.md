# Windows Update Checker (Python)

This Python script checks for available Windows updates, shows a popup warning, plays an alert sound, and installs the updates if the user agrees.  
The popup buttons automatically follow the **Windows system language** (e.g., YES/NO, JA/NEIN).

---

## Features

- Checks for available Windows updates using PowerShell  
- Plays an alert sound if updates are found  
- Displays a system-language popup (YES/NO or equivalent)  
- Installs updates automatically if confirmed  
- Uses `PSWindowsUpdate` PowerShell module  

---

## Requirements

Install the required PowerShell module:
```bash
Install-Module PSWindowsUpdate
```

---

## Start 

To start it, you have to double-click UTCode.bat and accept the prompt.
