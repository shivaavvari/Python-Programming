import tkinter as tk
from compressmodule import compress_file, decompress_file

def compression(input_file, output_file):
    compress_file(input_file, output_file)
    
def decompression(input_file, output_file):
    decompress_file(input_file, output_file)


window = tk.Tk()
window.title("Compression Enginge")
window.geometry("400x300")


input_entry = tk.Entry(window)
output_entry = tk.Entry(window)
input_label = tk.Label(window, text="File to be Compressed")
ouput_label = tk.Label(window, text="Name of the Compressed File")
compressed_button = tk.Button(window, text="Compress",command=lambda : compression(input_entry.get(), output_entry.get()))
compressed_label = tk.Label(window, text="File to be DeCompressed")
compressed_entry = tk.Entry(window)
decompressed_label = tk.Label(window, text="Name of the  DeCompressed File")
decompressed_entry = tk.Entry(window)
decompressed_button = tk.Button(window, text="DeCompress",command=lambda : decompression(compressed_entry.get(), decompressed_entry.get()))

input_label.grid(row=0, column=0)
input_entry.grid(row=0, column=1)
ouput_label.grid(row=1, column=0)
output_entry.grid(row=1, column=1)
compressed_button.grid(row=2,column=1)
compressed_label.grid(row=3, column=0)
compressed_entry.grid(row=3, column=1)
decompressed_label.grid(row=4, column=0)
decompressed_entry.grid(row=4, column=1)
decompressed_button.grid(row=5,column=1)

window.mainloop()


