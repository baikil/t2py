import ctypes
import os
import sys


def is_admin():
    '''
    Checks if the program has admin rights
    :return: True if the user is an admin, False otherwise
    '''
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def runas_admin(program: str):
    '''
    Runs the program as an admin
    :param program: File path of the program to run
    '''
    ctypes.windll.shell32.ShellExecuteW(None, "runas", program, " ".join(sys.argv), None, 1)


def cls():
    '''
    Clears the terminal
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def rna(adapter: int = 0, name: str = ""):
    '''
    Restart Network Adapter *NEEDS ADMIN
    :param adapter: Select which adapter to restart (0=Wi-Fi, 1=Ethernet, 2=Other)
    :param name: Name of the network adapter you want to restart (adapter=2)
    :raises ValueError: If `adapter` is not between 0 and 2
    '''
    if not 0 <= adapter <= 2:
        raise ValueError("adapter must be between 0 and 2")
    else:
        adapter_list = ["Wi-Fi", "Ethernet", name]
        os.system('powershell -command "(Restart-NetAdapter -Name "' + adapter_list[adapter] + '")"')


def ripdns():
    '''
    Reset IP and DNS *NEEDS ADMIN
    Release and renew IP address and flush DNS
    '''
    os.system("ipconfig /release")
    os.system("ipconfig /renew")
    os.system("arp -d *")
    os.system("nbtstat -R")
    os.system("nbtstat -RR")
    os.system("ipconfig /flushdns")
    os.system("ipconfig /registerdns")
