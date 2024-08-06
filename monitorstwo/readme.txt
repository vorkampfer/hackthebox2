# HTB MonitorsTwo
# OS: Linux
# Difficulty: Easy -> Actually Medium to Hard

# NOTE: The 2 python exploits are the same just executed in a different way to understand how the exploit works. The exploitDB version of the python script has the line of code that I take and modify to gain a shell with Burpsuite. Gaining the initial shell is easy. The Docker escape on this box was fun.

### Synopsis:
MonitorsTwo starts with a Cacti website (just like Monitors). There’s a command injection vuln that has a bunch of POCs that don’t work as of the time of MonitorsTwo’s release. I’ll show why, and exploit it manually to get a shell in a container. I’ll pivot to the database container and crack a hash to get a foothold on the box. For root, I’ll exploit a couple of Docker CVEs that allow for creating a SetUID binary inside the container that I can then run as root on the host. ~0xdf
