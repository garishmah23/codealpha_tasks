import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class CrimeDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Crime Analytics Command Center")
        self.root.geometry("1000x600")
        self.root.configure(bg="#1e1e1e")

        self.data = None

        # Title
        title = tk.Label(
            root,
            text="CRIME ANALYTICS COMMAND CENTER",
            font=("Arial", 18, "bold"),
            bg="#1e1e1e",
            fg="white"
        )
        title.pack(pady=10)

        # Sidebar Frame
        sidebar = tk.Frame(root, bg="#2c2c2c", width=200)
        sidebar.pack(side="left", fill="y")

        # Buttons
        tk.Button(sidebar, text="Load Data", command=self.load_data, width=20).pack(pady=10)
        tk.Button(sidebar, text="City Analysis", command=self.city_analysis, width=20).pack(pady=10)
        tk.Button(sidebar, text="Crime Types", command=self.crime_types, width=20).pack(pady=10)
        tk.Button(sidebar, text="Monthly Trends", command=self.monthly_trends, width=20).pack(pady=10)
        tk.Button(sidebar, text="Summary Report", command=self.summary_report, width=20).pack(pady=10)
        tk.Button(sidebar, text="Exit", command=root.quit, width=20).pack(pady=10)

        # Main Frame for Charts
        self.main_frame = tk.Frame(root, bg="#1e1e1e")
        self.main_frame.pack(side="right", fill="both", expand=True)

        self.label = tk.Label(self.main_frame, text="Load dataset to start analysis",
                              bg="#1e1e1e", fg="white", font=("Arial", 14))
        self.label.pack(pady=20)

    # ---------------- LOAD DATA ----------------
    def load_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

        if file_path:
            self.data = pd.read_csv(file_path)
            messagebox.showinfo("Success", "Data Loaded Successfully!")

    # ---------------- CITY ANALYSIS ----------------
    def city_analysis(self):
        if self.data is None:
            messagebox.showerror("Error", "Load dataset first!")
            return

        df = self.data.groupby("City")["Cases"].sum()

        fig, ax = plt.subplots()
        df.plot(kind="bar", ax=ax, color="red")
        ax.set_title("Crime by City")
        ax.set_ylabel("Cases")

        self.show_plot(fig)

    # ---------------- CRIME TYPE ----------------
    def crime_types(self):
        if self.data is None:
            messagebox.showerror("Error", "Load dataset first!")
            return

        df = self.data.groupby("Crime_Type")["Cases"].sum()

        fig, ax = plt.subplots()
        df.plot(kind="pie", autopct="%1.1f%%", ax=ax)
        ax.set_ylabel("")
        ax.set_title("Crime Type Distribution")

        self.show_plot(fig)

    # ---------------- MONTHLY TREND ----------------
    def monthly_trends(self):
        if self.data is None:
            messagebox.showerror("Error", "Load dataset first!")
            return

        self.data["Date"] = pd.to_datetime(self.data["Date"])
        df = self.data.groupby(self.data["Date"].dt.month)["Cases"].sum()

        fig, ax = plt.subplots()
        df.plot(kind="line", marker="o", ax=ax, color="blue")
        ax.set_title("Monthly Crime Trends")
        ax.set_xlabel("Month")
        ax.set_ylabel("Cases")

        self.show_plot(fig)

    # ---------------- SUMMARY REPORT ----------------
    def summary_report(self):
        if self.data is None:
            messagebox.showerror("Error", "Load dataset first!")
            return

        total = self.data["Cases"].sum()
        top_city = self.data.groupby("City")["Cases"].sum().idxmax()
        top_crime = self.data.groupby("Crime_Type")["Cases"].sum().idxmax()

        report = f"""
CRIME ANALYTICS REPORT
--------------------------
Total Cases: {total}
Most Affected City: {top_city}
Most Common Crime: {top_crime}
--------------------------
Generated Successfully
"""

        with open("output.txt", "w") as f:
            f.write(report)

        messagebox.showinfo("Report Generated", "output.txt created successfully!")

    # ---------------- SHOW PLOT ----------------
    def show_plot(self, fig):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=self.main_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    app = CrimeDashboard(root)
    root.mainloop()