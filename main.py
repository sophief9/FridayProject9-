import tkinter as tk
from tkinter import scrolledtext
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch the OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_completion():
    """Fetch the completion based on the user's input."""
    try:
        prompt = input_box.get("1.0", tk.END).strip()  # Get user input
        if not prompt:
            output_box.insert(tk.END, "Error: Prompt cannot be empty.\n")
            return

        # Call OpenAI Completion API with the new model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Using gpt-3.5-turbo model
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=150  # Adjust max_tokens as needed
        )
        completion = response['choices'][0]['message']['content'].strip()
        output_box.insert(tk.END, f"Input: {prompt}\nOutput: {completion}\n\n")
    except Exception as e:
        output_box.insert(tk.END, f"Error: {str(e)}\n")

# Create the main GUI window
root = tk.Tk()
root.title("OpenAI Completion Generator")

# Input Label and Text Box
input_label = tk.Label(root, text="Enter your prompt:")
input_label.pack(pady=5)

input_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=5)
input_box.pack(pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=generate_completion)
submit_button.pack(pady=5)

# Output Label and Output Box
output_label = tk.Label(root, text="Output:")
output_label.pack(pady=5)

output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
output_box.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
