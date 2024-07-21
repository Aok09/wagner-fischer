def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]
dictionary = load_dictionary("words.txt")

def wagner_fischer(s1, s2):
    len_s1, len_s2 = len(s1), len(s2)
    if len_s1 > len_s2:
        s1, s2 = s2, s1
        len_s1, len_s2 = len_s2, len_s1

    current_row = range(len_s1 + 1)
    for i in range(1, len_s2 + 1):
        previous_row, current_row = current_row, [i] + [0] * len_s1
        for j in range(1, len_s1 + 1):
            add, delete, change = previous_row[j] + 1, current_row[j-1] + 1, previous_row[j-1]
            if s1[j-1] != s2[i-1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[len_s1]

def spell_check(word, dictionary, Max = 5):
    suggestions = []

    for correct_word in dictionary:
        distance = wagner_fischer(word, correct_word)
        suggestions.append((correct_word, distance))

    suggestions.sort(key=lambda x: x[1])
    return suggestions[:Max]


def corrections(misspelled_word, dictionary = dictionary):
    suggestions = spell_check(misspelled_word, dictionary)


    for word, distance in suggestions:
        print(f"{word} (Distance: {distance}) from: {misspelled_word}")






import tkinter as tk

def on_change(*args):
    user_input = user_input_var.get()
    corrections(user_input)

# Create the main window
root = tk.Tk()
root.title("Input Example")

# Create a StringVar to hold the user input
user_input_var = tk.StringVar()

# Attach a trace to the StringVar to call on_change whenever the input changes
user_input_var.trace_add("write", on_change)

# Create a label
label = tk.Label(root, text="Enter something:")
label.pack()

# Create an entry widget and associate it with the StringVar
entry = tk.Entry(root, textvariable=user_input_var)
entry.pack()

# Run the application
root.mainloop()
