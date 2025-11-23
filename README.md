Small utility for devs; I needed it for my own usage so I figured I'd learn some extra python, then share it on my portfolio for others if they find it useful.

This is a simple tool that you can load paragraphs into, then type them and output your timed keystrokes as a JSON.
Then you can use the JSON file as a ghost representation of the typing you recorded, for whatever future projects you made need that for. This was made as a helper for my race-me online portfolio app.

Note, I don't know much tkinter and didn't put too much into making this pretty; pretty barebones functionality just as a fair warning. 


# Pseudocode plan
# Create main window: Typing Recorder

# Inside the window:
#   - Add paragraph to type
#   - Add text boxto type in
#   - Add three buttons:
#         [Start] → begins recording keystrokes
#         [Stop] → ends recording
#         [Export JSON] → saves the data to a file

# When [Start] is clicked:
#     - Clear previous typing data, start timer
#     - Begin listening to key presses

# Every time a key is typed:
#     - Save the character
#     - Save how many seconds since beginning

# When [Stop] is clicked:
#     - Stop saving new key presses, stop timer

# When [Export JSON] is clicked:
#     - Save the recorded list of characters and times as a JSON file