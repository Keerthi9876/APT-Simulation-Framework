import time
from logger_utils import log_event

def run_c2_communication():
    log_event("C2 Channel", "Attempting to establish connection with Attacker IP: 192.168.5.101")
    time.sleep(2)
    
    # Simulate a "Heartbeat" (C2 servers check in periodically)
    log_event("C2 Channel", "Connection Established. Encryption: AES-256 enabled.")
    
    commands = ["whoami", "hostname", "net user"]
    for cmd in commands:
        time.sleep(1)
        log_event("C2 Channel", f"Received command from Attacker: '{cmd}'")
        log_event("C2 Channel", f"Sending results for '{cmd}' back to C2 server.")

    log_event("C2 Channel", "C2 Channel is now ACTIVE and waiting for instructions.")