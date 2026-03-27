import time
from logger_utils import log_event

def simulate_sqli_scan(target_url):
    log_event("Vulnerability Scan", f"Testing SQL Injection on {target_url}...")
    # Attacker sends a single quote '
    payload = "'" 
    time.sleep(1)
    
    # Simulating a database error response
    mock_response = "SQL Syntax Error near '''"
    
    if "SQL" in mock_response:
        log_event("ALERT", "SQL Injection Vulnerability CONFIRMED!")
        return True
    return False

def simulate_xss_scan(target_url):
    log_event("Vulnerability Scan", f"Testing XSS on {target_url}...")
    # Attacker sends a script tag
    payload = "<script>alert('XSS')</script>"
    time.sleep(1)
    
    # Simulating the script being reflected in the page
    mock_page = f"Search results for: {payload}"
    
    if "<script>" in mock_page:
        log_event("ALERT", "Cross-Site Scripting (XSS) Vulnerability CONFIRMED!")
        return True
    return False