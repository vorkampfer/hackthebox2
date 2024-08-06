# HTB MonitorsTwo
# OS: Linux
# Difficulty: Easy -> Actually Medium to Hard

# NOTE: The Docker escape on this box was fun.

### Synopsis:
MonitorsTwo starts with a Cacti website (just like Monitors). There’s a command injection vuln that has a bunch of POCs that don’t work as of the time of MonitorsTwo’s release. I’ll show why, and exploit it manually to get a shell in a container. I’ll pivot to the database container and crack a hash to get a foothold on the box. For root, I’ll exploit a couple of Docker CVEs that allow for creating a SetUID binary inside the container that I can then run as root on the host. ~0xdf
