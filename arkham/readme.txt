# HTB ARKHAM
# Windows
# Difficulty: Medium 

### Note: Should be rated insane IMO, but well worth it. This was a well made box.

### Synopsis:
In my opinion, Arkham was the most difficult Medium level box on HTB, as it could have easily been Hard and wouldn’t have been out of place at Insane. But it is still a great box. I’ll start with an encrypted LUKZ disk image, which I have to crack. On it I’ll find the config for a Java Server Faces (JSF) site, which provides the keys that allow me to perform a deserialization attack on the ViewState, providing an initial shell. I’ll find an email file with the password for a user in the administrators group. Once I have that shell, I’ll have to bypass UAC to grab root.txt. ~0xdf
### Skill-set

1. SMB Enumeration
2. Data Exfiltration using SMBCLIENT and SMBMAP
3. LUKS Decryption of LUKS .img file
4. Deserialization on ViewState
5. Coding des_viewstate_decoder.py (3 iterations).
6. Password Hunting
7. Certutil.exe encoding for exfiltration of data
8. PSCredential to batman for use of -ScriptBlock
9. Bypass UAC aka Applocker [Privilege Escalation]
