# Import necessary libraries
import tkinter as tk  # Import the Tkinter library for GUI
import requests  # Import the requests library to make HTTP requests
from threading import Thread  # Import the Thread class for asynchronous operations

# Define the API URL to fetch random quotes
api = "http://api.quotable.io/random"

# Initialize an empty list to store quotes
quotes = []

# Initialize a variable to keep track of the current quote being displayed
quote_number = 0

# Create the main window of the application
window = tk.Tk()
window.geometry("920x270")  # Set the window size
window.title("Quote Generator")  # Set the window title
window.grid_columnconfigure(0, weight=1)  # Configure grid column
window.resizable(False, False)  # Disable window resizing
window.configure(bg="grey")  # Set window background color

# Function to preload quotes upon initialization
def preload_quotes():
    global quotes
    
    # Print a message indicating that more quotes are being loaded
    print("***Loading more Quotes***")
    # Fetch 10 random quotes from the API and add them to the list
    for x in range(10):
        random_quotes = requests.get(api).json()
        content = random_quotes["content"]
        author = random_quotes["author"]
        quote = content + "\n\n" + "By" + author
        print(content)  # Print the fetched quote to console
        quotes.append(quote)  # Add the quote to the list

    # Print a message indicating that quote loading is finished
    print("***Finished loading more quotes!***")    

# Preload quotes upon program execution
preload_quotes()

# Function to get a random quote and display it
def get_random_quote():
    global quote_label
    global quotes
    global quote_number

    # Update the quote label with the current quote
    quote_label.configure(text=quotes[quote_number])
    quote_number = quote_number + 1  # Increment the quote number

    # If the third-to-last quote is reached, start a new thread to preload more quotes
    if quotes[quote_number] == quotes[-3]:
        thread = Thread(target=preload_quotes)
        thread.start()

# Create the UI elements
quote_label = tk.Label(window, text="Click on the button to generate a random number!",
                       height=6,
                       pady=10,
                       wraplength=800,
                       font=("Helvetica", 14)
                       )
quote_label.grid(row=0, column=0, stick="WE", padx=20, pady=10)  # Place the quote label on the window

# Create a button to generate random quotes
button = tk.Button(text="Generate", command=get_random_quote, bg="#0052cc", fg="#ffffff",activebackground="grey", font=("Helvetica", 14))
button.grid(row=1, column=0, stick="WE", padx=20, pady=10)  # Place the button on the window

# Execute the GUI application
if __name__ == "__main__":
    window.mainloop()
