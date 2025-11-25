import subprocess
import ctypes
import winsound

# Popup Function (Windows Message Box)
def popup(title, text, button):
    return ctypes.windll.user32.MessageBoxW(0, text, title, button)

def updates_available():
    try:
        result = subprocess.check_output(
            ["powershell", "-Command", "Import-Module PSWindowsUpdate; (Get-WindowsUpdate).Count"],
            text=True
        ).strip()

        print("Result:", result)
        return int(result) > 0

    except Exception as e:
        print("Error:", e)
        return False

def install_updates():
    subprocess.call([
        "powershell",
        "-Command",
        "Import-Module PSWindowsUpdate; Get-WindowsUpdate -Install -AcceptAll -AutoReboot"
    ])

print("Check for Windows updates...")

if updates_available():
    print("UPDATE FOUND!")

    # alarm
    winsound.PlaySound("C:\\Windows\\Media\\Alarm01.wav", winsound.SND_FILENAME)

    # Popup with YES/NO
    result = popup("UPDATE!!!", "Updates available! Install now?", 4)

    # If YES is pressed (result 6)
    if result == 6:
        print("Press Enter twice")
        install_updates()

else:
    popup("Info", "No updates found.", 0)
