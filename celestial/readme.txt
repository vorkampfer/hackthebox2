# HTB Celestial
# OS: Linux
# Difficulty: Medium

### Synopsis:
Celestial is a fairly easy box that gives us a chance to play with deserialization vulnerabilities in Node.js. Weather it’s in struts, or python’s pickle, or in Node.js, deserialization of user input is almost always a bad idea, and here’s we’ll show why. To escalate, we’ll take advantage of a cron running the user’s code as root. ~0xdf

### Skill-set:
1. NodeJS Deserialization Attack [RCE]
2. IIFE Serialization/Deserialization Attack - Explained
3. Node Reverse Shell
4. Abusing Cron Job
