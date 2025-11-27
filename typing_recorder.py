from tkinter import *
from tkinter import ttk
import json
import time

recording = False
startTime = 0
keystrokes = []
# Default paragraph ID
current_p_id = "p1"

def start():
    # Clear keystrokes,  start recording, note start time
    global recording, startTime, keystrokes
    typing_box.delete("1.0", END)
    typing_box.focus_set()
    keystrokes = []
    recording = True
    startTime = time.perf_counter()

def stop():
    # Stop recording
    global recording
    recording = False

def export():
    # Export keystrokes and timing to ghost.json
    global keystrokes, current_p_id
    # Add paragraph ID to file name
    with open(f"ghost_{current_p_id}.json", "w") as f:
        json.dump(keystrokes, f, indent=2)

def record(event):
    # Record a keystroke with elapsed time
    global recording, startTime, keystrokes
    # Only record when recording is active
    if not recording:
        return
    
    elapsed = time.perf_counter() - startTime
    keystrokes.append({
        # Record key ID
        "keysym": event.keysym,
        "time": elapsed
    })

# Function to set current paragraph and its ID
def set_p(text, p_id):
    global current_p_id
    currentP.config(text=text)
    current_p_id = p_id

root = Tk()
root.title("Typing Recorder")

p1 = "calm river gentle breeze quiet morning slow footsteps soft sunlight peaceful thoughts drifting along",
p2 = "bright meadow warm coffee quiet laughter soft music open windows simple comfort steady hands",
p3 = "small moments matter more than big plans practice patience focus clearly breathe slowly keep moving",
p4 = "Not all those who wander are lost.",
p5 = "To be, or not to be, that is the question.",
p6 = "The only thing we have to fear is fear itself.",
p7 = "In the middle of difficulty lies opportunity.",
p8 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness.",
p9 = "When you have eliminated the impossible, whatever remains, no matter how improbable, must be the truth.",
p10 = "Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.",

# GUI Layout
frm = ttk.Frame(root, padding=320)
frm.grid()

currentP = ttk.Label(frm, text=p1, wraplength=500)
currentP.grid(column=0, row=0, columnspan=5)


typing_box = Text(frm, width=50, height=10)
typing_box.grid(column=0, row=1, columnspan=4)
typing_box.bind("<Key>", record)

ttk.Button(frm, text="Start Recording", command= start).grid(column=0, row=2)
ttk.Button(frm, text="Stop Recording", command= stop).grid(column=1, row=2)
ttk.Button(frm, text="Export JSON", command= export).grid(column=2, row=2)

ttk.Button(frm, text="P1", command=lambda: set_p(p1, "p1")).grid(column=0, row=4)
ttk.Button(frm, text="P2", command=lambda: set_p(p2, "p2")).grid(column=1, row=4)
ttk.Button(frm, text="P3", command=lambda: set_p(p3, "p3")).grid(column=2, row=4)
ttk.Button(frm, text="P4", command=lambda: set_p(p4, "p4")).grid(column=3, row=4)
ttk.Button(frm, text="P5", command=lambda: set_p(p5, "p5")).grid(column=4, row=4)
ttk.Button(frm, text="P6", command=lambda: set_p(p6, "p6")).grid(column=0, row=5)
ttk.Button(frm, text="P7", command=lambda: set_p(p7, "p7")).grid(column=1, row=5)
ttk.Button(frm, text="P8", command=lambda: set_p(p8, "p8")).grid(column=2, row=5)
ttk.Button(frm, text="P9", command=lambda: set_p(p9, "p9")).grid(column=3, row=5)
ttk.Button(frm, text="P10", command=lambda: set_p(p10, "p10")).grid(column=4, row=5)
root.mainloop()