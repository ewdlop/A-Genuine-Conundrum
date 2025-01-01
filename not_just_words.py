from psychopy import visual, event, core

# Set up window
win = visual.Window([800, 600])

# Text elements
question = visual.TextStim(win, text="The trolley is approaching. What do you do?")
option1 = visual.TextStim(win, pos=(-0.5, -0.5), text="Press '1' to save the group (sacrifice 1 person).")
option2 = visual.TextStim(win, pos=(0.5, -0.5), text="Press '2' to save 1 person (sacrifice the group).")

# Draw the screen
question.draw()
option1.draw()
option2.draw()
win.flip()

# Wait for user input
keys = event.waitKeys(keyList=['1', '2'])

# Outcome
if '1' in keys:
    result = "You saved the group but sacrificed one person."
elif '2' in keys:
    result = "You saved one person but sacrificed the group."
else:
    result = "No decision made. Default action taken."

# Display the result
result_text = visual.TextStim(win, text=result)
result_text.draw()
win.flip()
core.wait(3)  # Display for 3 seconds
win.close()
