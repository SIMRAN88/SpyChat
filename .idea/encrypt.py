from steganography.steganography import Steganography

def send_message():
    original_image = raw_input("What is the name of the image?")
    output_path = 'output.jpg'
    text = raw_input("What do you want to say?")
    Steganography.encode(original_image, output_path, text)

def read_message():
    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)

    return secret_text

read_message()

