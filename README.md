# SSHASH

![image](https://i.ibb.co/XFkBgJh/Video-Guru-20231213-174553412.gif)


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
Usage: 

Usage: sshash -u USERLIST -i IP_OR_URL [-p PORT] -l PASSWORDLIST

Options:
  -u USERLIST         Path to the user list file.
  -i IP_OR_URL        IP address or URL of the target.
  -p PORT             SSH port (default is 22 if not specified).
  -l PASSWORDLIST     Path to the password list file.


Exemple: 

```
sshash -u users.txt -i https://example.com -p 2222 -l passwords.txt
```
