# HTB Traceback
# OS: Linux
# Difficulty: Easy

### Synopsis:
Traceback starts with finding a webshell that’s already one the server with some enumeration and a bit of open source research. From there, I’ll pivot to the next user with sudo that allows me to run Luvit, a Lua interpreter. To get root, I’ll notice that I can write to the message of the day directory. These scripts are run by root whenever a user logs in. I actually found this by seeing the cron that cleans up scripts dropped in this directory, but I’ll also show how to find it with some basic enumeration as well. In Beyond Root, I’ll take a quick look at the cron that’s cleaning up every thiry seconds. ~0xdf
