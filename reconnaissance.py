import time
import socket
import platform
from logger_utils import log_event

def run_reconnaissance():
    log_event("Reconnaissance", "Starting target system information collection...")
    
    # 1. Collect System Info (Simulated)
    sys_info = f"OS: {platform.system()} {platform.release()}"
    log_event("Reconnaissance", f"Identified Target OS: {sys_info}")
    time.sleep(1) # Adding delay to make it look realistic
    
    # 2. Simulate Port Scanning
    ports_to_scan = [21, 22, 80, 443, 3389]
    log_event("Reconnaissance", f"Scanning common ports: {ports_to_scan}")
    
    for port in ports_to_scan:
        time.sleep(0.5)
        # We simulate finding port 80 and 443 open
        if port in [80, 443]:
            log_event("Reconnaissance", f"Port {port} is OPEN (Service: HTTP/HTTPS)")
        else:
            log_event("Reconnaissance", f"Port {port} is CLOSED")

    log_event("Reconnaissance", "Phase 1 completed successfully.")