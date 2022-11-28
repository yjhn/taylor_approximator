from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from matplotlib import pyplot as plt
import sympy
from sympy import sin, cos, tan, cot, asin, acos, atan, acot
from sympy import log, sqrt, root, exp
from sympy import Derivative
from sympy.abc import x
import re

from math import pi, e

class Taylor:
    
    def __init__(self, root):
        root.title("Funkcijos aproksimavimas Teiloro eilute")

        # Window setup.
        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        # Make frame expand to fit the window if it is resized.
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        
        # Frame for everything except the approximated function.
        self.big_frame = ttk.Frame(self.mainframe)
        self.big_frame.grid(column=1, row=2, sticky=(W, N))
        
        self.create_label_input_frame(self.big_frame)
        
        # Grafikas
        # pl = plt.plot()
        # plt.savefig("empty_plot.png")
        
        self.plot = ttk.Label(self.big_frame)
        self.plot.grid(column=2, row=1, sticky=(W, N))
        self.plot_img = ImageTk.PhotoImage(file="empty_plot.png")
        self.plot["image"] = self.plot_img
        
        # Sugeneruota funkcija
        self.taylor_frame = ttk.Frame(self.mainframe)
        self.taylor_frame.grid(column=1, row=1, sticky=(W, N))
        
        self.output_fn_label_label = ttk.Label(self.taylor_frame, text="Teiloro eilutė:  ")
        self.output_fn_label_label.grid(column=1, row=1, sticky=(E, N))
        self.output_fn_label_label.grid_remove()
        
        self.output_fn = StringVar()
        self.output_fn_label = ttk.Label(self.taylor_frame, textvariable=self.output_fn)
        self.output_fn_label.grid(column=2, row=1, sticky=(W, N))
        
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        
        root.bind("<Return>", self.calculate_taylor)

    def calculate_taylor(self, *args):
        fx = self.input_fn.get()
        der = derivative(fx)
        
        self.output_fn.set(der)
        # Generate and display the plot here
        # self.plot_img = ImageTk.PhotoImage(file="test_image_1.jpg")
        # self.plot["image"] = self.plot_img
        
        # Show function label
        self.output_fn_label_label.grid()
    
    def create_label_input_frame(self, parent):
        self.label_input_frame = ttk.Frame(parent)
        self.label_input_frame.grid(column=1, row=1, sticky=(W, N))
        
        # Labels in column 1, inputs in column 2
        
        # Labels
        self.input_fn_label = ttk.Label(self.label_input_frame, text="f(x) =")
        self.input_fn_label.grid(column=1, row=1, sticky=(E, N))
        
        self.x0_label = ttk.Label(self.label_input_frame, text="x =")
        self.x0_label.grid(column=1, row=2, sticky=(E, N))
        
        self.xmin_label = ttk.Label(self.label_input_frame, text="min x =")
        self.xmin_label.grid(column=1, row=3, sticky=(E, N))
        
        self.xmax_label = ttk.Label(self.label_input_frame, text="max x =")
        self.xmax_label.grid(column=1, row=4, sticky=(E, N))
        
        self.poly_degree_label = ttk.Label(self.label_input_frame, text="polinomo laispnis")
        self.poly_degree_label.grid(column=1, row=5, sticky=(E, N))
        
        # Inputs
        self.input_fn = StringVar()
        self.input_fn_field = ttk.Entry(self.label_input_frame, width=15, textvariable=self.input_fn)
        self.input_fn_field.grid(column=2, row=1, sticky=(W, N))
        
        self.x0 = StringVar()
        self.x0_field = ttk.Entry(self.label_input_frame, width=10, textvariable=self.x0)
        self.x0_field.grid(column=2, row=2, sticky=(W, N))
        
        self.xmin = StringVar()
        self.xmin_field = ttk.Entry(self.label_input_frame, width=10, textvariable=self.xmin)
        self.xmin_field.grid(column=2, row=3, sticky=(W, N))
        
        self.xmax = StringVar()
        self.xmax_field = ttk.Entry(self.label_input_frame, width=10, textvariable=self.xmax)
        self.xmax_field.grid(column=2, row=4, sticky=(W, N))
        
        self.poly_degree = StringVar()
        self.poly_degree_field = ttk.Entry(self.label_input_frame, width=5, textvariable=self.poly_degree)
        self.poly_degree_field.grid(column=2, row=5, sticky=(W, N))
        
        # "Aproksimuok" mygtukas
        self.approximate_btn = ttk.Button(self.label_input_frame, text="Aproksimuok", command=self.calculate_taylor)
        self.approximate_btn.grid(column=2, row=6, sticky=(N, E))
        
        for child in self.label_input_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

# syntax: root(x, 5) = 5th degree root of x
# log(x, a) = log_a(x)
# otherwise the syntax is standard as used in Lithuania
def derivative(fx):
    # Replacements to be made in the input:
    # ln -> log
    # arcsin -> asin
    # arccos -> acos
    # tg -> tan
    # arctg -> atan
    # ctg -> cot
    # arcctg -> acot
    # e^a -> exp(a)
    # a^b -> a**b
    fx = fx.replace("ln", "log")\
            .replace("arcsin", "asin")\
            .replace("arccos", "acos")\
            .replace("tg", "tan")\
            .replace("arctg", "atan")\
            .replace("ctg", "cot")\
            .replace("arcctg", "acot")\
            .replace("^", "**")\
            .replace("pi", str(pi))\
            .replace("exp", "mmm")\
            .replace("e", str(e))\
            .replace("mmm", "exp")
            # hack to replace e with its value
    
    print(fx)
    return Derivative(fx, x, evaluate=True)

root = Tk()
Taylor(root)
root.mainloop()
