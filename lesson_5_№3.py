import random
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox


class FilmPickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Случайный фильм по жанру")
        self.root.geometry("600x400")

        self.films = None
        self.genre_to_titles = {}
        self.genre_display = {}

        # Кнопка загрузки файла
        self.load_btn = tk.Button(root, text="Загрузить CSV", command=self.load_file)
        self.load_btn.pack(pady=10)

        self.file_label = tk.Label(root, text="Файл не загружен")
        self.file_label.pack()

        # Ввод жанра
        frame = tk.Frame(root)
        frame.pack(pady=20)

        tk.Label(frame, text="Жанр:").pack(side=tk.LEFT)

        self.genre_entry = tk.Entry(frame, width=20)
        self.genre_entry.pack(side=tk.LEFT, padx=5)

        self.find_btn = tk.Button(frame, text="Найти фильм", command=self.find_random)
        self.find_btn.pack(side=tk.LEFT)

        # Результат
        self.result_label = tk.Label(root, text="", wraplength=560, justify="center")
        self.result_label.pack(pady=15)

        self.info_label = tk.Label(root, text="", wraplength=560, justify="center")
        self.info_label.pack()

    def load_file(self):
        path = filedialog.askopenfilename(
            title="Выберите imdb_top_250.csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )

        if not path:
            return

        try:
            self.films = pd.read_csv(path)

            if "Title" not in self.films.columns or "Genre" not in self.films.columns:
                raise ValueError("В файле должны быть столбцы 'Title' и 'Genre'")

            self.build_genre_index()

            self.file_label.config(text=f"Загружено фильмов: {len(self.films)}")
            genres = ", ".join(sorted(self.genre_display.values()))
            self.info_label.config(text=f"Доступные жанры: {genres}")
            self.result_label.config(text="")

        except Exception as e:
            messagebox.showerror("Ошибка загрузки", str(e))
            self.films = None
            self.genre_to_titles = {}
            self.genre_display = {}
            self.file_label.config(text="Файл не загружен")

    def build_genre_index(self):
        self.genre_to_titles = {}
        self.genre_display = {}

        for _, row in self.films.iterrows():
            if pd.isna(row["Title"]) or pd.isna(row["Genre"]):
                continue

            title = str(row["Title"]).strip()
            genres_raw = str(row["Genre"])

            # Жанры в файле записаны как "Action | Crime | Drama"
            genres = [g.strip() for g in genres_raw.split("|") if g.strip()]

            for genre in genres:
                key = genre.lower()
                self.genre_to_titles.setdefault(key, []).append(title)
                self.genre_display[key] = genre

    def find_random(self):
        if self.films is None:
            messagebox.showwarning("Нет данных", "Сначала загрузите CSV-файл.")
            return

        genre = self.genre_entry.get().strip().lower()

        if not genre:
            messagebox.showwarning("Жанр не указан", "Введите жанр фильма.")
            return

        titles = self.genre_to_titles.get(genre)

        if not titles:
            messagebox.showinfo(
                "Жанр не найден",
                f"Жанр «{genre}» не найден. Попробуйте другой."
            )
            return

        title = random.choice(titles)
        display_genre = self.genre_display.get(genre, genre)

        self.result_label.config(text=f"{title} ({display_genre})")
        self.info_label.config(text=f"Найдено фильмов этого жанра: {len(titles)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = FilmPickerApp(root)
    root.mainloop()