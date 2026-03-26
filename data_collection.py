import time
from logger_utils import log_event

def run_data_collection():
    log_event("Data Collection", "Searching for sensitive file types (.docx, .pdf, .xlsx)...")
    time.sleep(1)
    
    found_files = ["Financial_Report_2024.xlsx", "Customer_Passwords.txt", "Project_X_Blueprints.pdf"]
    for file in found_files:
        log_event("Data Collection", f"Found and staged: {file}")
    
    log_event("Data Collection", "Compressing files into 'staged_data.zip' and encrypting...")
    time.sleep(1.5)