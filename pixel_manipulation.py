from PIL import Image
import numpy as np

def load_image(image_path):
    """Load an image and convert it to a numpy array."""
    image = Image.open(image_path)
    return np.array(image)

def save_image(np_array, output_path):
    """Save a numpy array as an image."""
    image = Image.fromarray(np_array.astype('uint8'))
    image.save(output_path)

def encrypt_image(np_array, key):
    """Encrypt the image using a simple XOR operation."""
    encrypted_array = np_array ^ key
    return encrypted_array

def decrypt_image(np_array, key):
    """Decrypt the image using a simple XOR operation."""
    decrypted_array = np_array ^ key
    return decrypted_array

# Example usage:
input_image_path = '/Users/karthik/Desktop/wallpapers/GT3.jpeg'
encrypted_image_path = '/Users/karthik/Desktop/wallpapers/GT3_encrypted.jpeg'
decrypted_image_path = '/Users/karthik/Desktop/wallpapers/GT3_decrypted.jpeg'
encryption_key = 123  # A simple encryption key

# Load the original image
image_array = load_image(input_image_path)

# Encrypt the image
encrypted_array = encrypt_image(image_array, encryption_key)
save_image(encrypted_array, encrypted_image_path)

# Decrypt the image
decrypted_array = decrypt_image(encrypted_array, encryption_key)
save_image(decrypted_array, decrypted_image_path)

print(f"Image encrypted and saved to {encrypted_image_path}")
print(f"Image decrypted and saved to {decrypted_image_path}")
