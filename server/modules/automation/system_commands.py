import os
import platform
import subprocess
import webbrowser

def execute_command(command):
    try:
        command = command.lower()

        if "open youtube" in command:
            webbrowser.open("https://www.youtube.com")
            return "Opening YouTube"

        elif "open google" in command:
            webbrowser.open("https://www.google.com")
            return "Opening Google"

        elif "open chrome" in command:
            return launch_application("chrome")

        elif "open vscode" in command:
            return launch_application("code")

        elif "open spotify" in command:
            # Option 1: If installed from Microsoft Store or in PATH
            return launch_application("spotify")

            # Option 2: If that doesn't work, use full path:
            # return subprocess.Popen("C:\\Users\\YourUsername\\AppData\\Roaming\\Spotify\\Spotify.exe")

        elif "shutdown" in command:
            return shutdown_system()

        elif "play music" in command:
            return play_music()

        else:
            return "Sorry, I don't recognize that command yet."

    except Exception as e:
        return f"System command error: {str(e)}"


# === Launch Applications Based on OS ===
def launch_application(app_name):
    system = platform.system()

    if system == "Windows":
        try:
            subprocess.Popen(app_name, shell=True)
            return f"Launching {app_name}"
        except Exception as e:
            return f"Error launching {app_name}: {str(e)}"

    elif system == "Darwin":  # macOS
        return subprocess.Popen(["open", "-a", app_name])
    elif system == "Linux":
        return subprocess.Popen([app_name])
    else:
        return "Unsupported OS for launching applications."


# === Shutdown OS ===
def shutdown_system():
    system = platform.system()

    if system == "Windows":
        os.system("shutdown /s /t 1")
    elif system == "Linux" or system == "Darwin":
        os.system("sudo shutdown now")
    return "Shutting down system..."

# === Play Default Music ===
def play_music():
    music_path = os.path.expanduser("~/Music")  # Change this to your default music folder
    try:
        files = os.listdir(music_path)
        if not files:
            return "No music files found in Music folder."
        music_file = os.path.join(music_path, files[0])
        os.startfile(music_file) if platform.system() == "Windows" else subprocess.call(["open", music_file])
        return "Playing music"
    except Exception as e:
        return f"Error playing music: {str(e)}"
