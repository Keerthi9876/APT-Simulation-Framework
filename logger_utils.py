import datetime
import os

LOG_FILE = "logs/simulation.log"

def log_event(phase, message):
    """
    This function records an event with a timestamp.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{phase}] {message}\n"
    
    # Ensure the logs directory exists
    if not os.path.exists('logs'):
        os.makedirs('logs')
        
    # Append the log to the file
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)
    
    # Also print it to the screen
    print(f"DEBUG: {log_entry.strip()}")

def generate_final_report():
    """
    Reads the log and creates a formal report in the reports/ folder.
    """
    if not os.path.exists('reports'):
        os.makedirs('reports')
        
    report_name = f"reports/APT_Report_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.txt"
    
    try:
        with open(LOG_FILE, "r") as log_f:
            content = log_f.read()
            
        with open(report_name, "w") as rep_f:
            rep_f.write("="*60 + "\n")
            rep_f.write("          APT SIMULATION FINAL INCIDENT REPORT\n")
            rep_f.write("="*60 + "\n\n")
            rep_f.write(f"Report Generated On: {datetime.datetime.now()}\n")
            rep_f.write("-" * 60 + "\n")
            rep_f.write(content)
            rep_f.write("\n" + "="*60 + "\n")
            rep_f.write("END OF REPORT\n")
            
        print(f"\n[+] Success! Formal report generated at: {report_name}")
    except FileNotFoundError:
        print("[!] Error: No log file found to generate a report from.")
    except Exception as e:
        print(f"Error generating report: {e}")