# HTB Stocker
# OS: Linux
# Difficulty: Easy

### Synopsis:
Stocker starts out with a NoSQL injection allowing me to bypass login on the dev website. From there, I’ll exploit purchase order generation via a serverside cross site scripting in the PDF generation that allows me to read files from the host. I’ll get the application source and use a password it contains to get a shell on the box. The user can run some NodeJS scripts as root, but the sudo rule is misconfiguration that allows me to run arbirtray JavaScript, and get a shell as root. ~0xdf
