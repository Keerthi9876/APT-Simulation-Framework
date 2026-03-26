import sys
from modules.reconnaissance import run_reconnaissance
from modules.initial_access import run_initial_access
from modules.c2_server import run_c2_communication
from modules.privilege_escalation import run_privilege_escalation
from modules.persistence import run_persistence
from modules.lateral_movement import run_lateral_movement
from modules.data_collection import run_data_collection
from modules.data_exfiltration import run_data_exfiltration
from logger_utils import log_event, generate_final_report

def display_menu():
    print("\n" + "☠️  "*5 + "APT SIMULATION FRAMEWORK" + " ☠️ "*5)
    print("1. Phase 1: Reconnaissance")
    print("2. Phase 2: Initial Access")
    print("3. Phase 3: Command & Control (C2)")
    print("4. Phase 4: Privilege Escalation")
    print("5. Phase 5: Persistence")
    print("6. Phase 6: Lateral Movement")
    print("7. Phase 7: Data Collection")
    print("8. Phase 8: Data Exfiltration")
    print("-" * 40)
    print("9. View Attack Timeline (On Screen)")
    print("10. Generate Final Report (.txt file)")
    print("0. Exit")
    print("=" * 45)

def main():
    while True:
        display_menu()
        choice = input("Select an option: ")

        if choice == '1': run_reconnaissance()
        elif choice == '2': run_initial_access()
        elif choice == '3': run_c2_communication()
        elif choice == '4': run_privilege_escalation()
        elif choice == '5': run_persistence()
        elif choice == '6': run_lateral_movement()
        elif choice == '7': run_data_collection()
        elif choice == '8': run_data_exfiltration()
        elif choice == '9':
            print("\n--- ATTACK TIMELINE ---")
            with open("logs/simulation.log", "r") as f: print(f.read())
        elif choice == '10':
            generate_final_report()
        elif choice == '0':
            sys.exit()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()