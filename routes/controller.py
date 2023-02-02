import subprocess
from dotenv import load_dotenv
import os

load_dotenv()

PYTHON_INTERPRETER = os.getenv("PYTHON_INTERPRETER")
FIRE_DETECTION_SYSTEM_SCRIPT = os.getenv("FIRE_DETECTION_SYSTEM_SCRIPT")

class ControllerFFD():
    def __init__(self):
        self.current_process = None
        self.script = FIRE_DETECTION_SYSTEM_SCRIPT
    
    def is_running(self):
        return self.current_process and self.current_process.returncode is None

    def run(self):
        while self.is_running():
            self.stop()
        
        self.current_process = subprocess.Popen([PYTHON_INTERPRETER, self.script])
        print("current_process: ", self.current_process)    
    
    def stop(self):
        if self.is_running():
            self.current_process.send_signal(subprocess.signal.SIGINT)
            self.current_process = None


if __name__  == "__main__":
    controller = ControllerFFD()
    controller.run()