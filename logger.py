from datetime import datetime

def log(message):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    formatted_message = f"{timestamp} {message}"
    
    with open("project.log", "a") as log_file:
        log_file.write(formatted_message + "\n")