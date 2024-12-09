import tkinter as tk
import random

# Function to load jokes from the file
def load_jokes(filename='randomJokes.txt'):
    with open(filename, 'r') as file:
        jokes = file.readlines()
    return jokes

# Function to show a joke setup and punchline
def show_joke(jokes):
    joke = random.choice(jokes).strip()
    setup, punchline = joke.split('?')

    # Create a new window for the joke
    joke_window = tk.Toplevel()
    joke_window.title("Alexa Tell Me a Joke")

    # Display setup
    setup_label = tk.Label(joke_window, text=f"{setup}?", font=("Arial", 16))
    setup_label.pack(pady=10)

    # Function to display the punchline
    def reveal_punchline():
        punchline_label.config(text=punchline)

    # Button to reveal punchline
    reveal_button = tk.Button(joke_window, text="Reveal Punchline", command=reveal_punchline)
    reveal_button.pack(pady=5)

    # Punchline label (initially empty)
    punchline_label = tk.Label(joke_window, text="", font=("Arial", 14))
    punchline_label.pack(pady=5)

    # Button to request a new joke
    new_joke_button = tk.Button(joke_window, text="New Joke", command=lambda: [joke_window.destroy(), show_joke(jokes)])
    new_joke_button.pack(pady=5)

    # Button to quit
    quit_button = tk.Button(joke_window, text="Quit", command=joke_window.destroy)
    quit_button.pack(pady=5)

# Main function to create the GUI and display the first joke
def main():
    jokes = load_jokes()

    # Main application window
    root = tk.Tk()
    root.title("Joke Teller")

    # Button to start telling jokes
    start_button = tk.Button(root, text="Alexa, tell me a Joke", font=("Arial", 16),
                             command=lambda: show_joke(jokes))
    start_button.pack(pady=20)

    # Button to exit the application
    exit_button = tk.Button(root, text="Exit", font=("Arial", 16), command=root.destroy)
    exit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
