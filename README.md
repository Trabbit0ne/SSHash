# SSHASH

![image](https://github.com/RAPS-LAUNCHER/SSHASH/assets/143559207/d6739c8d-0719-41dc-8143-56ce4a620bcc)



```
apt update && apt upgrade -y
```
```
cd && git clone https://github.com/RAPS-LAUNCHER/SSHASH.git
```

```
cd SSHASH && chmod +x *
```
Then 
```
./sshash
```
OR
```
bash sshash
```
## usage
Usage: sshash -u <user_file> -t <target> -p <port> -l <password_file>


Options:
 -u users_file
 -t target <ip or url>
 -p port
 -l password_list

Exemples:
 sshash -u usernames.txt -t https://exemple.com -p 22 -l passwords.txt
 sshash -u usernames.txt -t 192.168.123.32 -p 80 -l passwords.txt
 sshash -u users.txt -t https://exemple.com -l passwords.txt
