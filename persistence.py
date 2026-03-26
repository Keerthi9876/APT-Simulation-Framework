import time
from logger_utils import log_event

def run_persistence():
    log_event("Persistence", "Installing persistence mechanisms...")
    time.sleep(1)
    
    # Simulate adding a registry key (Common in Windows APTs)
    log_event("Persistence", "Action: Created Registry Key 'HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\SecurityHealthUpdater'")
    log_event("Persistence", "Action: Pointing registry key to malicious payload 'patch.exe'")
    
    time.sleep(1.5)
    
    log_event("Persistence", "Persistence established. Attacker will regain access after system reboot.")