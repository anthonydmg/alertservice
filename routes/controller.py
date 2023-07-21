import subprocess
from dotenv import load_dotenv
import os
import re

load_dotenv()

PYTHON_INTERPRETER = os.getenv("PYTHON_INTERPRETER")
FIRE_DETECTION_SYSTEM_SCRIPT = os.getenv("FIRE_DETECTION_SYSTEM_SCRIPT")
ALTIMETER_INITIALIZE_SCRIPT = os.getenv("ALTIMETER_INITIALIZE_SCRIPT")

class ControllerFFD():
    def __init__(self):
        self.current_process = None
        self.script = FIRE_DETECTION_SYSTEM_SCRIPT
        self.script_altimeter = ALTIMETER_INITIALIZE_SCRIPT
    
    def is_running(self):
        return self.current_process and self.current_process.returncode is None

    def run(self):
        while self.is_running():
            self.stop()
        
        self.current_process = subprocess.Popen([PYTHON_INTERPRETER, self.script, "-s", "True"])
        print("current_process: ", self.current_process)    
    
    def run_initialize_altimeter(self):
        process_init_alt = subprocess.run([PYTHON_INTERPRETER, self.script_altimeter, "--init", "True"], capture_output = True, text= True)
        output_process = str(process_init_alt.stdout)
        print("Init Altimeter: ", output_process)
        confirmation_text = "El punto de referencia se inicializo correctamente"
        if confirmation_text in output_process:
            matches = re.findall("Altura: -?\d\.\d+", output_process)
            altura = float(matches[0].replace("Altura: ", ""))
            print("altura:", altura)
            return altura
        else:
            print("Algo salio mal")
            return None
    def stop(self):
        if self.is_running():
            self.current_process.send_signal(subprocess.signal.SIGINT)
            self.current_process = None


if __name__  == "__main__":
    controller = ControllerFFD()
    controller.run_initialize_altimeter()
    #controller.run()