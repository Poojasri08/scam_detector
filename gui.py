import tkinter as tk
from detector import analyze_text


def scan_text():

    text = input_box.get("1.0", tk.END)

    result, flags, score, risk_percent = analyze_text(text)

    output = f"Result: {result}\n"
    output += f"Risk Score: {score}\n"
    output += f"Risk Percentage: {risk_percent}%\n\n"

    if flags:

        output += "Flags:\n"

        for f in flags:
            output += f"- {f}\n"

    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, output)


root = tk.Tk()

root.title("Scam Detector")
root.geometry("600x500")

label = tk.Label(root, text="Enter Job or Internship Message")
label.pack()

input_box = tk.Text(root, height=10, width=70)
input_box.pack()

scan_button = tk.Button(root, text="Analyze", command=scan_text)
scan_button.pack()

result_box = tk.Text(root, height=15, width=70)
result_box.pack()

root.mainloop()