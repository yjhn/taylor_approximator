from tkinter import *
from tkinter import ttk
from PIL import ImageTk

class Taylor:
    
    def __init__(self, root):
        root.title("Funkcijos aproksimavimas Teiloro eilute")

        # Window setup.
        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        # Make frame expand to fit the window if it is resized.
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        
        # Input frame
        self.input_frame = ttk.Frame(self.mainframe)
        self.input_frame.grid(column=1, row=1, sticky=(W, N))
        
        # Function input combobox
        # TODO
        self.input_fn = StringVar()
        input_fn_field = ttk.Entry(self.input_frame, width=15, textvariable=self.input_fn)
        input_fn_field.grid(column=1, row=1, sticky=(W, N))
#         
#         # Funckijos taškas x
#         self.input_fn_point = StringVar()
#         input_fn_point_field = ttk.Entry(self.input_frame, width=7, textvariable=self.input_fn_point)
#         input_fn_point_field.grid(column=1, row=1)
#         
#         # Funkcijos taško aplinka V(x)
#         self.input_fn_point_area = StringVar()
#         point_area = ttk.Entry(self.inputframe, width=15, textvariable=self.input_fn_point_area)
#         point_area.grid(column=1, row=1)
        
        # "Aproksimuok" mygtukas
        self.approximate_btn = ttk.Button(self.input_frame, text="Aproksimuok", command=self.calculate_taylor)
        self.approximate_btn.grid(column=4, row=1, sticky=(N, E))
        
        
        for child in self.input_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)
        
        # Originalios funkcijos grafikas
        self.output_img_source_fn = ttk.Label(self.mainframe)
        self.output_img_source_fn.grid(column=1, row=2, sticky=(W, N))
        
        # Sugeneruota funkcija
        self.output_function = StringVar()
        output_function_label = ttk.Label(self.mainframe, textvariable=self.output_function)
        output_function_label.grid(column=2, row=1, sticky=W)
        
        # Sugeneruotos funkcijos grafikas
        self.output_img_dest_fn = ttk.Label(self.mainframe)
        self.output_img_dest_fn.grid(column=2, row=2, sticky=(W, N))
        
        
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        
        root.bind("<Return>", self.calculate_taylor)

    def calculate_taylor(self, *args):
        self.output_function.set("AAAAA 555555")
        self.source_fn_img = ImageTk.PhotoImage(file="test_image_1.jpg")
        self.dest_fn_img = ImageTk.PhotoImage(file="test_image_2.jpg")
        self.output_img_source_fn["image"] = self.source_fn_img
        self.output_img_dest_fn["image"] = self.dest_fn_img

root = Tk()
Taylor(root)
root.mainloop()
