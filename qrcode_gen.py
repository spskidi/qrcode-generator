import qrcode

def main():
    print("Welcome to the QR Code Generator!")
    
    while True:
        ask = input("Type 'start' to start the program or 'exit' to quit: ").strip().lower()
        
        if ask == 'start':
            while True:
                try:
                    # Get the link or exit command
                    query = input("Enter the link to make QR code or type 'exit' to quit: ").strip()
                    if query.lower() == "exit":
                        print("Exiting program. Goodbye!")
                        return
                    
                    # Get file name
                    filename = input("Enter the file name (include .png at the end): ").strip()
                    if not filename.endswith(".png"):
                        print("Invalid file name. Please include '.png'.")
                        continue
                    
                    # Get colors
                    color1 = input("Enter the fill color: ").strip()
                    color2 = input("Enter the background color: ").strip()#for background of qr 
                    
                    # QR Code generation
                    qr = qrcode.QRCode(
                        version=2,#Ranges from 1 to 40.
                        error_correction=qrcode.constants.ERROR_CORRECT_M,# M Recovers 15% of the code.  (Use higher error correction (M, Q, or H) if the QR code might be partially obscured or damaged.)
                        box_size=7,#Increase or decrease for a larger or smaller QR code.
                        border=8#Increase for a thicker border, or decrease for minimal space around the QR code (minimum is 4).
                    )
                    qr.add_data(query)
                    qr.make(fit=True)
                    
                    # Create and save the image
                    img = qr.make_image(fill_color=color1, back_color=color2)
                    img.save(filename)
                    print(f"QR code saved as {filename}.")
                except Exception as e:
                    print(f"Something went wrong: {e}. Try again.")
        elif ask == 'exit':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid input. Please type 'start' or 'exit'.")

if __name__ == "__main__":
    main()
