import time
from logger_utils import log_event

def run_lateral_movement():
    log_event("Lateral Movement", "Scanning internal network (Subnet: 192.168.1.0/24)...")
    time.sleep(1.5)
    
    targets = ["192.168.1.5 (File-Server)", "192.168.1.10 (Database-Admin)"]
    log_event("Lateral Movement", f"Internal targets identified: {targets}")
    
    log_event("Lateral Movement", "Attempting 'Pass-the-Hash' attack on 192.168.1.10...")
    time.sleep(2)
    
    log_event("Lateral Movement", "Successfully logged into Database-Admin via SMB.")
    log_event("Lateral Movement", "Spreading payload to secondary target...")