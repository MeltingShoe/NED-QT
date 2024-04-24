import subprocess
import time
import os
cwd = os.getcwd()

class session_info:
    def __init__(self):
        print(cwd)
        self.session_data = self._read_session()

    def _read_session(self):
        with open(cwd+'/.session_info', 'r') as f:
            data = f.readlines()
        return data
    
    def _write_session(self,data):
        with open(cwd+'/.session_info', 'w') as f:
            f.writelines(data)
        return true

    def _append_session(self,data):
        with open(cwd+'/.session_info', 'a') as f:
            f.writelines(data)
        return true

def main():
    sesh=session_info()
    data = sesh._read_session()
    for line in data:
        subprocess.run(['tmux','display-popup'])
        time.sleep(1)

main()
