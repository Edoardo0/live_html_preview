import argparse
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from selenium import webdriver

parser = argparse.ArgumentParser() # Instantiates an ArgumentParser object for parsing command-line arguments.
parser.add_argument("filepath") # Defines a mandatory string positional argument named 'filepath'.
args = parser.parse_args() # Parses sys.argv and returns a Namespace object containing the extracted arguments.

html_path = os.path.abspath(args.filepath) # Returns a normalized absolute version of the passed string path.
target_dir = os.path.dirname(html_path) # Extracts and returns the parent directory string from the provided path.

driver = webdriver.Chrome() # Initializes and returns a WebDriver instance for inter-process control of the Chrome browser.
driver.get(f"file:///{html_path}") # Executes an HTTP GET request to navigate to the generated local URI.

class ReloadHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith((".html", ".css", ".js")): # Evaluates that the event is not a directory and the path string ends with the specified extensions.
            relative = os.path.relpath(event.src_path, target_dir) # Calculates the relative path of the modified file with respect to the parent directory.
            print(f"[{time.strftime('%H:%M:%S')}] Modification in: {relative}. Refreshing...") # Formats and prints a string containing the timestamp and path to standard output.
            driver.refresh() # Sends a command to the WebDriver to reload the currently active web document.

event_handler = ReloadHandler() # Instantiates an object of the custom ReloadHandler class.
observer = Observer() # Creates an instance of the Observer class to manage background monitoring threads.
observer.schedule(event_handler, path=target_dir, recursive=True) # Associates the event handler with the specified path, enabling recursive traversal of subdirectories.
observer.start() # Spawns and starts the asynchronous thread to listen for file system events.

print(f"Monitoring active on: {target_dir}")
print("Press CTRL+C to stop the script.")

try:
    while True:
        time.sleep(1) # Suspends the execution of the calling thread for 1 second to avoid saturating CPU clock cycles.
except KeyboardInterrupt:
    print("\nShutting down...")
    observer.stop() # Sets the observer's internal flag to signal the thread termination request.
    driver.quit() # Closes the communication sockets and terminates the WebDriver executable process.
observer.join() # Blocks the execution of the main thread until the observer thread has completely terminated.
