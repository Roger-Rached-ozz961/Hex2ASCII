import sys
from termcolor import colored
from colorama import init


init(autoreset=True)

# Pastel colors (lighter shades)
LIGHT_PASTEL_GREEN = '\033[38;5;152m'  # Pastel Green
LIGHT_PASTEL_RED = '\033[38;5;217m'    # Pastel Red
LIGHT_PASTEL_BLUE = '\033[38;5;153m'   # Pastel Blue
LIGHT_PASTEL_YELLOW = '\033[38;5;227m' # Pastel Yellow
LIGHT_PASTEL_PURPLE = '\033[38;5;177m' # Pastel Purple
RESET_COLOR = '\033[0m'      # Reset color

def print_banner():
    banner = """
    =================================
        Hex to ASCII Converter
    =================================
    Author: Roger Rached
    Description: This script converts hexadecimal values to human-readable ASCII text.
    Simply input hex values separated by spaces, and the script will return the
    corresponding ASCII characters. The results will also be saved to 'conversion_results.txt'.
    =================================
    """
    print(f"{LIGHT_PASTEL_PURPLE}{banner}{RESET_COLOR}")  # Reset color after banner

def hex_to_ascii(hex_string):
    try:
        hex_values = hex_string.split()
        print(f"{LIGHT_PASTEL_BLUE}\n[INFO] Processing {len(hex_values)} hex values...{RESET_COLOR}")
        ascii_text = ''.join(chr(int(h, 16)) for h in hex_values)
        print(f"{LIGHT_PASTEL_GREEN}[SUCCESS] Conversion completed successfully!{RESET_COLOR}")
        return ascii_text
    except ValueError:
        print(f"{LIGHT_PASTEL_RED}[ERROR] Invalid hex input detected!{RESET_COLOR}")
        return "Error: Invalid hex input. Ensure you enter valid hex numbers separated by spaces."

def save_to_file(hex_input, ascii_output):
    try:
        with open("conversion_results.txt", "a", encoding="utf-8") as file:
            file.write(f"Hex Input: {hex_input}\nASCII Output: {ascii_output}\n{'-'*40}\n")
        print(f"{LIGHT_PASTEL_BLUE}\n[INFO] Result saved to conversion_results.txt{RESET_COLOR}")
    except Exception as e:
        print(f"{LIGHT_PASTEL_RED}[ERROR] Failed to save result to file: {e}{RESET_COLOR}")

def main():
    print_banner()
    try:
        while True:
            if len(sys.argv) > 1:
                hex_string = ' '.join(sys.argv[1:])
                print(f"{LIGHT_PASTEL_BLUE}\n[INFO] Received input from command line.{RESET_COLOR}")
                ascii_output = hex_to_ascii(hex_string)
                print(f"{LIGHT_PASTEL_GREEN}ASCII Output:", f"{LIGHT_PASTEL_YELLOW}{ascii_output}{RESET_COLOR}")
                save_to_file(hex_string, ascii_output)
            else:
                hex_string = input(f"{LIGHT_PASTEL_BLUE}Enter hex values separated by spaces (or type 'exit' to quit): ").strip()
                if hex_string.lower() == 'exit':
                    print(f"{LIGHT_PASTEL_PURPLE}\n[INFO] User requested exit. Shutting down gracefully...{RESET_COLOR}")
                    print(f"{LIGHT_PASTEL_PURPLE}Gracefully exiting... Have a wonderful day!{RESET_COLOR}")
                    break
                if not hex_string:
                    print(f"{LIGHT_PASTEL_YELLOW}[WARNING] No input provided. Please enter valid hex values.{RESET_COLOR}")
                    continue
                ascii_output = hex_to_ascii(hex_string)
                print(f"{LIGHT_PASTEL_GREEN}ASCII Output:", f"{LIGHT_PASTEL_YELLOW}{ascii_output}{RESET_COLOR}")
                save_to_file(hex_string, ascii_output)

    except KeyboardInterrupt:
        # Handle the graceful exit on CTRL+C
        print(f"\n{LIGHT_PASTEL_BLUE}\n[INFO] Program interrupted by user.{RESET_COLOR}")
        print(f"Gracefully exiting...{RESET_COLOR}")

if __name__ == "__main__":
    main()
