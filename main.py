import sys
import t2commands as t2

runas_script = True  # Set to True if running not compiled

# Check if T2 is running as admin. If not, prompts the user with the option of re-running as admin
is_admin = t2.is_admin()
if not is_admin:
    while True:
        t2.cls()
        print("T2 doesn't have administrator privileges. Do you want to re-run the program with them? [Y/N]")
        prompt = input("> ")
        if prompt.upper() == "Y":
            t2.runas_admin(sys.executable)
            exit(0)
        elif prompt.upper() == "N":
            break

t2.rna(0)
input()