import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from stegano import lsb

# Create the main application window
root = tk.Tk()
root.title("Image Steganography")
root.geometry("400x300")

# Function to open and display an image
def open_image():
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        img = Image.open(file_path)
        img.show()

# Function to encode a message into an image
def encode():
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("PNG files", "*.png")])
    if not file_path:
        return

    secret_message = input_text.get("1.0", tk.END).strip()
    if not secret_message:
        messagebox.showerror("Error", "Please enter a message to encode")
        return

    try:
        encoded_image = lsb.hide(file_path, secret_message)
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            encoded_image.save(save_path)
            messagebox.showinfo("Success", "Message encoded and image saved successfully")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to decode a message from an image
def decode():
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("PNG files", "*.png")])
    if not file_path:
        return

    try:
        secret_message = lsb.reveal(file_path)
        if secret_message:
            messagebox.showinfo("Secret Message", secret_message)
        else:
            messagebox.showwarning("Warning", "No hidden message found")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create input text area
input_text = tk.Text(root, height=5, width=40)
input_text.pack(pady=10)

# Create open image button
open_image_button = tk.Button(root, text="Open Image", command=open_image)
open_image_button.pack(pady=5)

# Create encode button
encode_button = tk.Button(root, text="Encode Message", command=encode)
encode_button.pack(pady=5)

# Create decode button
decode_button = tk.Button(root, text="Decode Message", command=decode)
decode_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
