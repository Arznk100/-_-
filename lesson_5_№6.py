import tkinter as tk
from tkinter import filedialog, messagebox

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class LeastSquaresApp:
    def __init__(self, root):
        self.root = root
        self.root.title("МНК: аппроксимация данных")
        self.root.geometry("520x260")
        self.root.configure(bg="#1e1e2e")

        self.data = None          # DataFrame
        self.path = None          # путь к файлу

        # --- Кнопка загрузки CSV ---
        self.load_btn = tk.Button(
            root, text="Выбрать CSV", command=self.load_csv,
            bg="#89b4fa", fg="#1e1e2e",
            activebackground="#74c7ec",
            font=("Arial", 12, "bold"),
            padx=10, pady=5
        )
        self.load_btn.pack(pady=20)

        # --- Кнопка расчёта ---
        self.calc_btn = tk.Button(
            root, text="Посчитать МНК и сохранить график",
            command=self.compute_and_plot,
            bg="#a6e3a1", fg="#1e1e2e",
            activebackground="#94e2d5",
            font=("Arial", 12, "bold"),
            padx=10, pady=5
        )
        self.calc_btn.pack(pady=5)

        # --- Статус ---
        self.status = tk.Label(
            root, text="Файл не загружен",
            bg="#1e1e2e", fg="#cdd6f4",
            font=("Arial", 11), wraplength=480, justify="center"
        )
        self.status.pack(pady=20)

    # ---------- 1. Загрузка CSV ----------
    def load_csv(self):
        path = filedialog.askopenfilename(
            title="Выберите CSV для лабораторной",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        if not path:
            return

        try:
            self.data = pd.read_csv(path)
            self.path = path
            cols = ", ".join(self.data.columns)
            self.status.config(
                text=f"Загружено: {len(self.data)} строк\nСтолбцы: {cols}"
            )
        except Exception as e:
            messagebox.showerror("Ошибка загрузки", str(e))
            self.data = None
            self.path = None
            self.status.config(text="Файл не загружен")

    # ---------- 2. МНК + график ----------
    def compute_and_plot(self):
        if self.data is None:
            messagebox.showwarning("Нет данных", "Сначала загрузите CSV.")
            return

        # Ожидаем минимум два столбца: x и y
        if self.data.shape[1] < 2:
            messagebox.showerror("Ошибка", "В файле нужно минимум 2 столбца: x и y")
            return

        try:
            # Берём первые два столбца как x и y
            x = self.data.iloc[:, 0].astype(float).to_numpy()
            y = self.data.iloc[:, 1].astype(float).to_numpy()

            # ---- МНК для y = k*x + b ----
            # k = (n*Σxy - Σx*Σy) / (n*Σx² - (Σx)²)
            # b = (Σy - k*Σx) / n
            n = len(x)
            sx = np.sum(x)
            sy = np.sum(y)
            sxy = np.sum(x * y)
            sx2 = np.sum(x * x)

            k = (n * sxy - sx * sy) / (n * sx2 - sx ** 2)
            b = (sy - k * sx) / n

            # ---- График ----
            plt.figure(figsize=(8, 5))
            plt.scatter(x, y, color="#89b4fa", label="Данные", zorder=3)
            plt.plot(x, k * x + b, color="#f38ba8", linewidth=2,
                     label=f"МНК: y = {k:.4f}x + {b:.4f}")
            plt.title("Аппроксимация МНК")
            plt.xlabel(self.data.columns[0])
            plt.ylabel(self.data.columns[1])
            plt.grid(True, alpha=0.3)
            plt.legend()

            # ---- Сохранение ----
            out_path = filedialog.asksaveasfilename(
                title="Сохранить график",
                defaultextension=".png",
                initialfile="approximation.png",
                filetypes=[("PNG image", "*.png"), ("All files", "*.*")]
            )
            if out_path:
                plt.savefig(out_path, dpi=150, bbox_inches="tight")
                self.status.config(
                    text=f"k = {k:.4f}\nb = {b:.4f}\nГрафик сохранён: {out_path}"
                )
            else:
                self.status.config(text=f"k = {k:.4f}\nb = {b:.4f}")

            plt.show()

        except Exception as e:
            messagebox.showerror("Ошибка расчёта", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = LeastSquaresApp(root)
    root.mainloop()