
![Gif showing the automation in use](https://github.com/user-attachments/assets/ea315205-8a20-41ef-b682-4d244a6ecdbe)

# Simple Python Live Reloader for front-end website development

A lightweight, dependency-minimal Python script to automate browser refreshing during front-end web development. 

If you prefer coding in minimalist text editors (like Sublime Text) or environments designed for quick scripting rather than bloated IDEs, the lack of a built-in "Live Server" can be a bottleneck. This tool solves the manual refresh problem by directly observing the file system and controlling the browser externally.

## Core Features & Advantages

* **Editor Agnostic:** It monitors the actual `.html`, `.css`, and `.js` files on your drive using filesystem events. It works perfectly regardless of the application you use to write your code.
* **Instant Visual Feedback:** The script triggers a browser refresh milliseconds after it detects a modification event (like hitting `Cmd+S` or `Ctrl+S`).
* **Frictionless Workflow:** Setup takes about 3 minutes the first time. After that, launching your development environment is just a single double-click away.

## Installation & Setup

1.  Download the `livehtml.py` script and the specific launcher file for your operating system: `.command` for macOS, `.sh` for Linux, or `.bat` for Windows.
2.  Open the launcher file in a text editor and replace the placeholder strings with the absolute path to where you saved `livehtml.py`, and the absolute path to your target `index.html`.
3.  Place this launcher file directly inside your website's project folder for easy access.
4.  **For macOS/Linux only:** Open your terminal and navigate to your project folder using the `cd` command.
5.  **For macOS/Linux only:** Grant execution permissions to the launcher script by running `chmod +x your_launcher_name.command` on macOS (or `.sh` on Linux). Windows users can skip this step.
6.  Close the terminal. The setup is complete.

### Using it on a New Project
To use this live reloader for a different website, you have two simple options:
1. **Edit:** Open your existing launcher file (`.command`, `.bat`, or `.sh`) in a text editor and replace the old `index.html` path with the path to your new project. (and move the file to the new project's folder for quick access)
2. **Duplicate:** Copy the launcher file, paste it into your new project's folder, update the HTML path inside it, and use this new dedicated launcher.

## How to Use and Terminate

* **Start:** Double-click the launcher file in your project folder. A terminal window will open in the background, followed by an automated Chrome instance displaying your site.
* **Stop:** To cleanly terminate the session, bring the active terminal window to the foreground and press `Ctrl+C`. This intercepts the background process, safely kills the browser session, and stops the filesystem observer. You can then safely close the terminal window.

## Prerequisites

Ensure you have Python 3 installed along with the following libraries:
`pip install watchdog selenium`
*(Note: A compatible version of Google Chrome must be installed on your machine for the WebDriver to function).*
