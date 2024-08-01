# HTB Headless
### OS: Linux
### Difficulty: Easy

### NOTE: This was a fun box. It went over some basic csrf, command injection skills that are good to know.

### Synopsis:
Headless is a nice introduction to cross site scripting, command injection, and understanding Linux and Bash. I’ll start with a simple website with a contact form. When I put any HTML tags into the message, there’s an alert saying that my request headers have been forwarded for analysis. I’ll embed a XSS payload into request headers and steal a cookie from the admin. As an admin user, I get access to the dashboard, where a simple form has command injection. To escalate, I’ll abuse a system check script that tries to run another script with a relative path. In Beyond Root, I’ll look at understanding and attacking the cookie used by the site, and some odd status codes I noticed during the solution. ~0xdf

### Skill-set:
1. CSRF stealing admin cookie
2. Abusing SSH to gain ssh shell via command injection.
3. Abusing poor coding practices to assign stickybit to /bin/bash

