from colorama import Fore, Style
import os
import time
os.system('cls' if os.name == 'nt' else 'clear')

logo = """
 ██████╗  ██╗  ██╗ ███╗   ███╗ ██╗   ██╗ ██╗    ██╗ ███████╗ ██████╗ 
██╔═══██╗ ██║  ██║ ████╗ ████║ ╚██╗ ██╔╝ ██║    ██║ ██╔════╝ ██╔══██╗
██║   ██║ ███████║ ██╔████╔██║  ╚████╔╝  ██║ █╗ ██║ █████╗   ██████╔╝
██║   ██║ ██╔══██║ ██║╚██╔╝██║   ╚██╔╝   ██║███╗██║ ██╔══╝   ██╔══██╗
╚██████╔╝ ██║  ██║ ██║ ╚═╝ ██║    ██║    ╚███╔███╔╝ ███████╗ ██████╔╝
 ╚═════╝  ╚═╝  ╚═╝ ╚═╝     ╚═╝    ╚═╝     ╚══╝╚══╝  ╚══════╝ ╚═════╝
                        Mentalistler
---------------------------------------------------------------------------
"""
print(Fore.GREEN + logo + Fore.RESET)
def resultprint(data,_type="i"):
    data = data + "                                           "
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    now = Fore.CYAN + f"[{current_time}] "
    if(_type == "i"):
        print(now + Fore.GREEN + data + Fore.RESET +'\033[F')
        print("\n")
    elif(_type == "w"):
        print(now + Fore.YELLOW + data + Fore.RESET +'\033[F')
    elif(_type == "f"):
        print(now + Fore.RED + data + Fore.RESET +'\033[F')

def colorprint(data, _type="i"):
    #i= info
    #w= warning
    #f =  fail
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    now = Fore.CYAN + f"[{current_time}] "
    if(_type == "i"):
        print(now + Fore.GREEN + data + Fore.RESET)
    elif(_type == "w"):
        print(now + Fore.YELLOW + data + Fore.RESET)
    elif(_type == "f"):
        print(now + Fore.RED + data + Fore.RESET)
