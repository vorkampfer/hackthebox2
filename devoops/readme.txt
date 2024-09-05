# HTB DevOops
# OS: Linux
# Difficulty: Medium

### NOTE: I agree with 0xdf this box was a-lot of fun. Very well made box.

### Synopsis:
DevOops was a really fun box that did a great job of providing interesting challenges that weren’t too difficult to solve. I’ll show how to gain access using XXE to leak the users SSH key, and then how I get root by discovering the root SSH key in an old git commit. In Beyond Root, I’ll show an alternative path to user shell exploiting a python pickle deserialization bug. ~0xdf

### Skill-set:
1. XXE External Entity Injection
2. Abusing git to reveal root ssh key
