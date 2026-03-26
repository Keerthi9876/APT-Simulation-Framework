import time
from logger_utils import log_event

def run_data_exfiltration():
    log_event("Data Exfiltration", "Opening encrypted tunnel to Attacker Server (HTTPS/Port 443)...")
    time.sleep(2)
    
    log_event("Data Exfiltration", "Uploading 'staged_data.zip' (Size: 45MB)...")
    # Simulate a progress bar
    for i in range(25, 101, 25):
        time.sleep(0.5)
        print(f"Uploading... {i}%")
    
    log_event("Data Exfiltration", "Upload complete. Connection closed.")
    log_event("Data Exfiltration", "APT OBJECTIVE COMPLETE. DATA EXFILTRATED.")