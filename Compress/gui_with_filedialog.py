import tkinter as tk
from compressmodule import compress_file, decompress_file
from tkinter import filedialog


def open_file():
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File", 
                                          filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
    return filename 
    


def compression(input_file, output_file):
    compress_file(input_file, output_file)
    
def decompression(input_file, output_file):
    decompress_file(input_file, output_file)


window = tk.Tk()
window.title("Compression Enginge")
window.geometry("400x300")



compressed_button = tk.Button(window, text="Compress",command=lambda : compression(open_file(), "compress_ouput1.txt"))
decompressed_button = tk.Button(window, text="DeCompress",command=lambda : decompression(open_file(), "decompress_output1.txt"))

compressed_button.grid(row=2,column=1)
decompressed_button.grid(row=5,column=1)

window.mainloop()


