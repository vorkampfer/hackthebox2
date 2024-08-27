# HTB Busqueda
# OS: Linux
# Difficulty: Easy

### Synopsis:
Busqueda presents a website that gives links to various sites based on user input. Under the hood, it is using the Python Searchor command line tool, and I’ll find an unsafe eval vulnerability and exploit that to get code execution. On the host, the user can run sudo to run a Python script, but I can’t see the script. I’ll find a virtualhost with Gitea, and use that along with different creds to eventually find the source for the script, and identify how to run it to get arbitrary execution as root. ~0xdf
