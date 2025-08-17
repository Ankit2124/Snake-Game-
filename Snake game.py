import tkinter as tk
import random

MOVE_INCREMENT = 20
GAME_SPEED = 100

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(root, width=400, height=400, bg="yellow")
        self.canvas.pack()
        self.snake = [(100, 100)]
        self.snake_direction = "Right"
        self.food = None
        self.score = 0
        self.running = True
        self.draw_snake()
        self.place_food()
        self.root.bind("<Key>", self.change_direction)
        self.move_snake()

    def draw_snake(self):
        self.canvas.delete("snake")
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0]+20, segment[1]+20,
                                         fill="green", tags="snake")

    def move_snake(self):
        if not self.running: return
        x, y = self.snake[0]
        if self.snake_direction == "Left":
            x -= MOVE_INCREMENT
        elif self.snake_direction == "Right":
            x += MOVE_INCREMENT
        elif self.snake_direction == "Up":
            y -= MOVE_INCREMENT
        elif self.snake_direction == "Down":
            y += MOVE_INCREMENT

        new_head = (x, y)
        if (x < 0 or y < 0 or x >= 400 or y >= 400 or new_head in self.snake):
            self.running = False
            self.canvas.create_text(200, 200, text="Game Over", fill="red", font=("Arial", 24))
            return

        self.snake = [new_head] + self.snake
        if new_head == self.food:
            self.score += 1
            self.place_food()
        else:
            self.snake.pop()

        self.draw_snake()
        self.root.after(GAME_SPEED, self.move_snake)

    def place_food(self):
        while True:
            x = random.randint(0, 19) * 20
            y = random.randint(0, 19) * 20
            if (x, y) not in self.snake:
                break
        self.food = (x, y)
        self.canvas.delete("food")
        self.canvas.create_oval(x, y, x+20, y+20, fill="red", tags="food")

    def change_direction(self, event):
        directions = {"Left", "Right", "Up", "Down"}
        if event.keysym in directions:
            opposites = {"Left":"Right", "Right":"Left", "Up":"Down", "Down":"Up"}
            if self.snake_direction != opposites[event.keysym]:
                self.snake_direction = event.keysym

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
