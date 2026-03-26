import time
from logger_utils import log_event

def run_initial_access():
    log_event("Initial Access", "Simulating Phishing Email delivery...")
    time.sleep(1)
    
    log_event("Initial Access", "User 'Target_Employee' clicked on malicious link: 'http://legit-update.com/patch.exe'")
    time.sleep(1.5)
    
    log_event("Initial Access", "Payload 'patch.exe' downloaded and executed.")
    log_event("Initial Access", "Checking user privileges... Current User: 'StandardUser'")
    
    log_event("Initial Access", "Initial Access established successfully.")