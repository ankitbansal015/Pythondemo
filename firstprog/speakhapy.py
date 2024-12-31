from win32com.client import Dispatch

def speak(str):
    speak=Dispatch(("SAPI.Spvoice"))
    speak.Speak(str)

if __name__ == '__main__':
    speak("happy birthday brother")