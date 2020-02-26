import tkinter as tk
import math
import threading

window = tk.Tk()
window.title('Decode')
window.geometry('800x600')
window.configure(background='black')

result = {}


def dynamic_processing():
    result_text = ''

    input_stream = input_entry.get()

    for i in range(0, 256):
        new_string = ''
        for letter_num in range(0, len(input_stream)-1):
            new_string = new_string + chr((ord(input_stream[letter_num])+i) % 256)
        if FLAG_entry.get() in new_string:
            if len(new_string.split(FLAG_entry.get())) > 2:
                result_text = result_text + "Many result of +"+str(i)+"\n"
            split_symbol = new_string.split(FLAG_entry.get())[1][0]
            result_text = result_text+FLAG_entry.get()+split_symbol+\
                          new_string.split(split_symbol)[1]+split_symbol

    # result_type = ''
    result_label.configure(text=result_text)


header_label = tk.Label(window, text='Decode fo CTF_Tools')
header_label.pack()

input_frame = tk.Frame(window)
input_frame.pack(side=tk.TOP)
input_label = tk.Label(input_frame, text='Input text:')
input_label.pack(side=tk.LEFT)
input_entry = tk.Entry(input_frame)
input_entry.pack(side=tk.LEFT)

FLAG_frame = tk.Frame(window)
FLAG_frame.pack(side=tk.TOP)
FLAG_label = tk.Label(FLAG_frame, text='FLAG:')
FLAG_label.pack(side=tk.LEFT)
FLAG_entry = tk.Entry(FLAG_frame)
FLAG_entry.pack(side=tk.LEFT)

result_label = tk.Label(window)
result_label.pack()

calculate_btn = tk.Button(window, text='', command=dynamic_processing)
calculate_btn.pack()

dynamic_process = threading.Thread(target=dynamic_processing)
dynamic_process.start()

window.mainloop()