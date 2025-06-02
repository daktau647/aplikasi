import ttkbootstrap as tb
from tkinter import StringVar, messagebox, LEFT

def solve():
    try:
        a1 = float(a1_var.get())
        b1 = float(b1_var.get())
        c1 = float(c1_var.get())
        a2 = float(a2_var.get())
        b2 = float(b2_var.get())
        c2 = float(c2_var.get())

        det = a1 * b2 - a2 * b1
        if det == 0:
            result_var.set("No unique intersection (lines are parallel or coincident).")
        else:
            x = (c1 * b2 - c2 * b1) / det
            y = (a1 * c2 - a2 * c1) / det
            result_var.set(f"Intersection at (x={x:.2f}, y={y:.2f})")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

app = tb.Window(themename="superhero")
app.title("Intersection of Two Linear Equations")
app.geometry("400x300")

a1_var = StringVar()
b1_var = StringVar()
c1_var = StringVar()
a2_var = StringVar()
b2_var = StringVar()
c2_var = StringVar()
result_var = StringVar()

tb.Label(app, text="Equation 1: a1*x + b1*y = c1").pack(pady=5)
tb.Entry(app, textvariable=a1_var, width=5).pack(side=LEFT, padx=5, pady=5)
tb.Label(app, text="x +").pack(side=LEFT)
tb.Entry(app, textvariable=b1_var, width=5).pack(side=LEFT, padx=5)
tb.Label(app, text="y =").pack(side=LEFT)
tb.Entry(app, textvariable=c1_var, width=5).pack(side=LEFT, padx=5)

frame1 = tb.Frame(app)
frame1.pack(pady=10)
tb.Label(frame1, text="Equation 2: a2*x + b2*y = c2").pack(pady=5)
tb.Entry(frame1, textvariable=a2_var, width=5).pack(side=LEFT, padx=5)
tb.Label(frame1, text="x +").pack(side=LEFT)
tb.Entry(frame1, textvariable=b2_var, width=5).pack(side=LEFT, padx=5)
tb.Label(frame1, text="y =").pack(side=LEFT)
tb.Entry(frame1, textvariable=c2_var, width=5).pack(side=LEFT, padx=5)

tb.Button(app, text="Find Intersection", command=solve, bootstyle="success").pack(pady=20)
tb.Label(app, textvariable=result_var, font=("Segoe UI", 12)).pack(pady=10)

app.mainloop()