Password Hasher
A simple, cross-platform password hashing application built with Python and PyQt5. This tool allows you to securely hash passwords using various algorithms locally on your machine, without the need for an internet connection. Executables are available for Windows and macOS. Feel free to use the code, fork it, or contribute to its development.

Features
Multiple Hashing Algorithms: Supports MD5, SHA-1, SHA-256, SHA-512, and more.
User-Friendly Interface: Simple and intuitive GUI built with PyQt5.
Dark and Light Mode: Switch between themes to suit your preference.
Copy to Clipboard: Easily copy the hashed password for use elsewhere.
Offline Usage: All operations are performed locally for enhanced security. (Intended to be downloaded/used offline)
Cross-Platform: Available as an executable for Windows and an app for macOS.
Open Source: Code is available for modification and improvement.

###Security Notice###
Please be aware that this application is not digitally signed, which may result in security warnings when you attempt to run it. Downloading and using the application is at your own discretion. For full transparency and peace of mind, the complete source code is available within this repository, allowing you to review and verify its functionality.

## Running the Application on macOS

After downloading `Password.Hasher.zip`, follow these steps to run the application:

1. **Extract the Application:**
   - Double-click `Password.Hasher.zip` to extract `Password.Hasher.app`.

2. **Open the Application:**
   - Double-click `Password.Hasher.app`.
   - If you see a warning stating that the app cannot be opened because the developer cannot be verified:
     - **Right-Click Method:**
       - Right-click (or Control-click) on `Password.Hasher.app`.
       - Select **"Open"**.
       - In the dialog that appears, click **"Open"** again.
   
     - **System Preferences Method:**
       - Open **System Preferences** > **Security & Privacy** > **General**.
       - Click **"Open Anyway"** next to the warning about `password_hasher.app`.

3. **Run the Application:**
   - The app should now launch without further warnings.




## Running the Application on Windows

After downloading `PasswordHasher.exe`, you might encounter a security warning from Windows Defender SmartScreen.

**To Run the Application:**

1. Double-click the `PasswordHasher.exe` file.
2. In the SmartScreen warning dialog, click on **"More info"**.
3. Click on **"Run anyway"** to launch the application.

**Note:** This warning appears because the application is not digitally signed. Ensure you trust the source before proceeding.
