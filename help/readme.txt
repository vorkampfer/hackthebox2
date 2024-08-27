# HTB Help
# OS: Linux
# Difficulty: Easy

### Synopsis:
Help was an easy box with some neat challenges. As far as I can tell, most people took the unintended route which allowed for skipping the initial section. I’ll either enumerate a GraphQL API to get credentials for a HelpDeskZ instance. I’ll use those creds to exploit an authenticated SQLi vulnerability and dump the database. In the database, I’ll find creds which work to ssh into the box. Alternatively, I can use an unauthenticated upload bypass in HelpDeskZ to upload a webshell and get a shell from there. For root, it’s kernel exploits. ~0xdf
