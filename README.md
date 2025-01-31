# Hex2ASCII Converter

## Description
Hex2ASCII Converter is a Python-based script that converts hexadecimal values into human-readable ASCII text. The script supports both command-line and interactive inputs. Additionally, the results of the conversion are saved into a `conversion_results.txt` file for easy reference.

## Requirements

- **Python 3.x** (Recommended: Python 3.7+)
- **Termcolor** and **Colorama** Python libraries

### Install the necessary Python libraries
To install the required libraries, run the following command:

```bash
pip install termcolor colorama
```

---

## Usage

### Option 1: Running the script directly
1. Clone or download this repository.
2. Open a terminal or PowerShell window.
3. Navigate to the directory where the script is saved.
4. Run the Python script with:

```bash
python Hex2ASCII.py
```

Alternatively, you can pass hex values directly via command line:

```bash
python Hex2ASCII.py 48 65 78 20 32 41 53 43 49 49
```

The script will output the converted ASCII values and save the results in `conversion_results.txt`.

### Option 2: Running the script with the batch file (`run.bat`)

To simplify the process, you can use the `run.bat` batch file to automatically activate the Python virtual environment and run the script in PowerShell with the correct settings.

#### Steps:
1. **Ensure you have created and activated your Python virtual environment** and installed the required dependencies as mentioned earlier.

2. **Create the batch file**:
   Save the following content as `run.bat` in the same directory as `Hex2ASCII.py`.

   ```bat
   start powershell.exe -NoExit -ExecutionPolicy Bypass -Command "$env:TERM='xterm-256color'; & '%~dp0hex2ascii\Scripts\Activate.ps1'; python '%~dp0Hex2ASCII.py'"
   ```

#### Running the batch file:
1. Double-click the `run.bat` file to start the script in a PowerShell window.
2. The PowerShell terminal will remain open and activate the virtual environment automatically, allowing you to enter hexadecimal values or run the script with command-line arguments.
3. If you are prompted, input the hex values in the terminal. The ASCII output will be shown, and the results will be saved in `conversion_results.txt`.

---

## Script Features
- Converts hexadecimal input to ASCII text.
- Supports both interactive and command-line inputs.
- Provides color-coded output using the `termcolor` and `colorama` libraries for better readability.
- Saves the input and output to a file named `conversion_results.txt` for future reference.

---

## Example Output
```text
=================================
        Hex to ASCII Converter
=================================
Author: Roger Rached
Description: This script converts hexadecimal values to human-readable ASCII text.
Simply input hex values separated by spaces, and the script will return the
corresponding ASCII characters. The results will also be saved to 'conversion_results.txt'.
=================================
[INFO] Processing 10 hex values...
[SUCCESS] Conversion completed successfully!
ASCII Output: Hello World!

[INFO] Result saved to conversion_results.txt
```

The output will be saved in `conversion_results.txt`:

```text
Hex Input: 48 65 78 20 32 41 53 43 49 49
ASCII Output: Hello World!
----------------------------------------
```

---

## Troubleshooting
- **Terminal not displaying colors**: Ensure that your terminal supports ANSI color codes. If you're using a Windows terminal, `PowerShell` should be configured to support them by default.
- **Permission Issues with PowerShell scripts**: If PowerShell script execution is restricted, make sure you have the correct execution policy. You can run this command in PowerShell to allow script execution:

  ```powershell
  Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```

- **Invalid hex input**: Make sure your input consists only of valid hexadecimal characters (0-9, a-f). Separate each hex value with spaces.

---

## Author
Roger Rached

Feel free to open an issue or submit a pull request if you encounter any bugs or have suggestions for improvement.
