import tkinter as tk
import random


class Square:
    def __init__(self, canvas, size, color):
        self.canvas = canvas
        self.size = size
        self.color = color
        self.x = random.randint(0, canvas.winfo_width() - size)
        self.y = random.randint(0, canvas.winfo_height() - size)
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])
        self.shape = canvas.create_rectangle(self.x, self.y, self.x + size, self.y + size, fill=color)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.canvas.move(self.shape, self.dx, self.dy)

        # Bounce from the walls
        if self.x <= 0 or self.x + self.size >= self.canvas.winfo_width():
            self.dx *= -1
        if self.y <= 0 or self.y + self.size >= self.canvas.winfo_height():
            self.dy *= -1

    def check_collision(self, other):
        x1, y1, x2, y2 = self.canvas.coords(self.shape)
        x3, y3, x4, y4 = self.canvas.coords(other.shape)
        if (x1 < x4 < x2 or x1 < x3 < x2) and (y1 < y4 < y2 or y1 < y3 < y2):
            return True
        return False


class SquaresApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Squares")
        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack()
        self.num_squares = 0
        self.squares = []
        self.square_size = 40
        self.colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown"]

        self.entry_label = tk.Label(root, text="Enter number of squares:")
        self.entry_label.pack()
        self.entry = tk.Entry(root)
        self.entry.pack()
        self.entry.focus_set()

        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack()

        self.root.after(100, self.move_squares)

    def start(self):
        self.num_squares = int(self.entry.get())
        self.generate_squares()

    def generate_squares(self):
        for _ in range(self.num_squares):
            color = random.choice(self.colors)
            square = Square(self.canvas, self.square_size, color)
            self.squares.append(square)

    def move_squares(self):
        for square in self.squares:
            square.move()

        for i, square in enumerate(self.squares):
            for other_square in self.squares[i + 1:]:
                if square.check_collision(other_square):
                    if square.color == other_square.color:
                        self.generate_new_square(square)
                    else:
                        self.bounce(square, other_square)

        self.root.after(50, self.move_squares)

    def generate_new_square(self, square):
        color = square.color
        new_square = Square(self.canvas, self.square_size, color)
        self.squares.append(new_square)

    def bounce(self, square1, square2):
        square1.dx *= -1
        square1.dy *= -1
        square2.dx *= -1
        square2.dy *= -1


if __name__ == "__main__":
    root = tk.Tk()
    app = SquaresApp(root)
    root.mainloop()
