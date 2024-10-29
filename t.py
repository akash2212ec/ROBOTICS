import tkinter as tk
from tkinter import messagebox
import random
import math

class GoatSimulation:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Who is the GOAT?")
        self.root.geometry("400x300")
        
        # Main label
        tk.Label(
            self.root, 
            text="Who is the GOAT?", 
            font=("Arial", 16, "bold")
        ).pack(pady=20)
        
        # Buttons frame
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(expand=True, fill='both')
        
        # Messi button (the one that will dodge)
        self.messi_btn = tk.Button(
            self.button_frame,
            text="Messi",
            width=10,
            state='disabled',  # Make it impossible to click
            fg='green',        # Green text
            font=("Arial", 10, "bold")
        )
        self.messi_btn.place(x=150, y=100)
        
        # Ronaldo button (the one that shows SUIIIII)
        self.ronaldo_btn = tk.Button(
            self.button_frame,
            text="Ronaldo",
            width=10,
            command=self.show_suiii,
            fg='red',          # Red text
            font=("Arial", 10, "bold")
        )
        self.ronaldo_btn.place(x=150, y=150)
        
        # Window dimensions
        self.width = 400
        self.height = 300
        
        # Store last cursor position
        self.last_cursor_x = 0
        self.last_cursor_y = 0
        
        # Bind mouse movement to continuously track cursor
        self.root.bind('<Motion>', self.avoid_cursor)
        
    def avoid_cursor(self, event):
        # Get cursor and button positions
        cursor_x = event.x
        cursor_y = event.y
        button_x = self.messi_btn.winfo_x()
        button_y = self.messi_btn.winfo_y()
        
        # Calculate distance between cursor and button
        distance = math.sqrt((cursor_x - button_x) ** 2 + (cursor_y - button_y) ** 2)
        
        # If cursor gets too close, move the button
        if distance < 150:
            # Calculate movement vector
            dx = cursor_x - self.last_cursor_x
            dy = cursor_y - self.last_cursor_y
            
            # Move in the opposite direction of cursor movement
            move_distance = 80
            if abs(dx) > 0 or abs(dy) > 0:
                angle = math.atan2(dy, dx)
                new_x = button_x - move_distance * math.cos(angle)
                new_y = button_y - move_distance * math.sin(angle)
                
                # Ensure button stays within window bounds with wrapping
                new_x = (new_x + self.width) % (self.width - 60)
                new_y = (new_y + self.height) % (self.height - 60)
                
                # Keep button visible by enforcing minimum margins
                margin = 10
                new_x = max(margin, min(self.width - 80, new_x))
                new_y = max(margin, min(self.height - 40, new_y))
                
                self.messi_btn.place(x=new_x, y=new_y)
        
        # Update last cursor position
        self.last_cursor_x = cursor_x
        self.last_cursor_y = cursor_y
        
    def show_suiii(self):
        suiii_window = tk.Toplevel(self.root)
        suiii_window.title("Suiiiiiiiiii!")
        suiii_window.geometry("300x200")
        
        label = tk.Label(
            suiii_window,
            text="Suiiiiiiiiii!",
            font=("Arial", 24, "bold")
        )
        label.pack(expand=True)
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = GoatSimulation()
    app.run()