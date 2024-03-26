import tkinter as tk
import speech_recognition as sr  #used for converting the voice into text
from tkinter import messagebox

# Initialize the recognizer
recognizer = sr.Recognizer()

#to open a new window with voice command button
def open_window():
    voice_window = tk.Toplevel(A)
    voice_window.title("Voice Assistant")
    voice_window.geometry("300x100")
    listen_button = tk.Button(voice_window, text="***SPEAK***", command=listen)
    listen_button.pack()

A = tk.Tk()
A.title(" Voice Assistant")
A.geometry("300x200")
button = tk.Button(A,text="Open Voice Assistant", command=open_window)
button.pack()

# to listen to the user's voice command
def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        messagebox.showinfo("Listening...", "Speak something")
        try:
            audio = recognizer.listen(source, timeout=10)
            text = recognizer.recognize_google(audio)
            messagebox.showinfo("Command recognized", f"You said: {text}")
        except sr.UnknownValueError:
            messagebox.showwarning("Warning", "Could not understand audio")
        except sr.RequestError as e:
            messagebox.showerror("Error", f"Could not request results: {e}")
A.mainloop()
