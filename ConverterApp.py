from __future__ import print_function

try:  # python 3: default
    import tkinter as tk
    from tkinter import ttk
except ImportError:  # python 2
    import Tkinter as tk
    import ttk

import csv

"""
RTAC CSV Converter
Made by Brian Ward, '21
        brianmward99@gmail.com
Converts the output of a Google form into individual lighting files.
"""

class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.rownum = 0

        tk.Label(self.master, text="Please enter the input filename (without extension)").grid(row=self.row(),column=1)
        self.file_text = tk.Entry(self.master)
        self.file_text.grid(row=self.row(),column=1)

        tk.Label(self.master, text="Please enter the preamble information").grid(row=self.row(),column=1)
        self.pream_text = tk.Entry(self.master, width=100)
        self.pream_text.grid(row=self.row(),column=1)
        self.pream_text.insert(tk.END, "time, bcemail, Song, Contact Name, Email, Costume Color, Costume Texture, Music Length")

        tk.Label(self.master, text="Which preamble field should the files be named after?").grid(row=self.row(),column=1)
        self.outn_text = tk.Entry(self.master,)
        self.outn_text.grid(row=self.row(),column=1)
        self.outn_text.insert(tk.END, "Song")

        tk.Label(self.master, text="Which preamble information should be put in the header?").grid(row=self.row(),column=1)
        self.outf_text = tk.Entry(self.master, width=100)
        self.outf_text.grid(row=self.row(),column=1)
        self.outf_text.insert(tk.END, "Song, Contact Name, Email, Costume Color, Costume Texture, Music Length")

        tk.Label(self.master, text="Please enter the information provided for each cue").grid(row=self.row(),column=1)
        self.cue_text = tk.Entry(self.master, width=100)
        self.cue_text.grid(row=self.row(),column=1)
        self.cue_text.insert(tk.END, "Time, Fade, Feeling, Cyc, Happening")

        tk.Label(self.master, text="Maximum number of cues").grid(row=self.row(),column=1)
        self.cue_slider = tk.Scale(self.master, from_=5, to=100, orient='horizontal')
        self.cue_slider.grid(row=self.row(), column=1)
        self.cue_slider.set(25)

        tk.Button(self.master, text='Convert!', command=self.out).grid(row=self.row(), column=1)

    def row(self):
        row = self.rownum
        self.rownum += 1
        return row

    def out(self):
        filename = self.file_text.get()
        preamble = list(map(str.strip, self.pream_text.get().split(',')))
        cue_info = list(map(str.strip, self.cue_text.get().split(',')))
        num_cues = self.cue_slider.get()
        out_field = self.outn_text.get().strip()
        out_format = list(map(str.strip, self.outf_text.get().split(',')))
        convert(filename,preamble,cue_info,num_cues, out_field, out_format)

def convert(filename, preamble, cue_info, num_cues, out_field, out_info):
    cue_function = lambda x: [f'Cue {x} {i}' for i in cue_info]
    cuedata = [q for sub in [cue_function(x) for x in range(1, num_cues+1)] for q in sub]
    started = False
    with open(f'{filename}.csv', newline='') as incsv:
        reader = csv.DictReader(incsv, fieldnames=preamble + cuedata)

        for row in reader:
            if not started:
                started = True
                continue

            print('Writing', row[out_field])

            with open(f'{row[out_field]}.csv', 'w', newline='') as outcsv:
                writer = csv.writer(outcsv, quoting=csv.QUOTE_MINIMAL)

                # blank line at top of file
                writer.writerow([''])
                # create the header
                header = [['', info +":", row[info]] for info in out_info]
                writer.writerows(header)

                # blank line before cues
                writer.writerow([''])
                labels = ['', 'Cue #'] + cue_info + ['Notes']
                writer.writerow(labels)

                writer.writerows([['', ''] + [row[item] for item in cue_function(i)] + [' '] for i in range(1, num_cues)])

# Create the application window
root = tk.Tk()
root.minsize(width=600, height=300)
root.title("RTAC CSV Converter")
app = Application(master=root)
app.mainloop()