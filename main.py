from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import matplotlib
# If the below line is not included, the app hangs after closing the window.
matplotlib.use('agg')
from matplotlib import pyplot as plt
from sympy import Derivative
from sympy.abc import x
from sympy import lambdify
import numpy as np

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
        san_fx = sanitize(fx)
        der = derivative(san_fx)
        rev_san_der = reverse_sanitize(der)
        
        self.output_fn.set(rev_san_der)
        
        fx_lambda = lambdify(x, san_fx)
        fx_der_lambda = lambdify(x, der)
        array = self.arrange()
        fx_arr = list(map(fx_lambda, array))
        fx_der_arr = list(map(fx_der_lambda, array))
        
        # Generate and display the plot here
        pl = plt.plot(array, fx_arr, array, fx_der_arr)
        plt.savefig("plot.png")
        self.plot_img = ImageTk.PhotoImage(file="plot.png")
        self.plot["image"] = self.plot_img
        plt.clf()
        
        # Show function label
        self.output_fn_label_label.grid()
    
    def arrange(self):
        # Arrange 1000 steps in the interval [xmin; xmax)
        xmin = self.xmin.get()
        xmax = self.xmax.get()
        step_size = (xmax - xmin) / 1000.0
        arr = np.arange(xmin, xmax, step_size)
        return arr
    
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
        
        self.x0 = DoubleVar()
        self.x0_field = ttk.Entry(self.label_input_frame, width=10, textvariable=self.x0)
        self.x0_field.grid(column=2, row=2, sticky=(W, N))
        
        self.xmin = DoubleVar()
        self.xmin_field = ttk.Entry(self.label_input_frame, width=10, textvariable=self.xmin)
        self.xmin_field.grid(column=2, row=3, sticky=(W, N))
        
        self.xmax = DoubleVar()
        self.xmax_field = ttk.Entry(self.label_input_frame, width=10, textvariable=self.xmax)
        self.xmax_field.grid(column=2, row=4, sticky=(W, N))
        
        self.poly_degree = IntVar()
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
def sanitize(fx):
    # Replacements to be made in the input:
    # ln -> log
    # arcsin -> asin
    # arccos -> acos
    # tg -> tan
    # arctg -> atan
    # ctg -> cot
    # arcctg -> acot
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
    
    return fx

def reverse_sanitize(fx):
    # Replacements to be made in the input:
    # ln <- log // cannot do this, log can take one or two args
    # arcsin <- asin
    # arccos <- acos
    # tg <- tan
    # arctg <- atan
    # ctg <- cot
    # arcctg <- acot
    # a^b <- a**b
    fx = str(fx)
    fx = fx.replace("asin", "arcsin")\
            .replace("acos", "arccos")\
            .replace("tan", "tg")\
            .replace("atan", "arctg")\
            .replace("cot", "ctg")\
            .replace("acot", "arcctg")\
            .replace("**", "^")\
    
    return fx

# fx can be a string or sympy expression
def derivative(fx):
    return Derivative(fx, x, evaluate=True)

root = Tk()
Taylor(root)
root.mainloop()
