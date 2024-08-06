
# HTB PC
# OS: Linux
# Difficulty: Easy

### Synopsis:
PC starts with only SSH and TCP port 50051 open. I’ll poke at 50051 until I can figure out that it’s GRPC, and then use grpcurl to enumerate the service. I’ll find an SQL injection in the SQLite database and get some creds that I can use over SSH. To escalate, I’ll find an instance of pyLoad running as root and exploit a 2023 CVE to get execution. In Beyond Root, a video exploring the Python GRPC application to see how it works.~0xdf

### Skill-set:
1. Enumerating mysterious port 50051
2. Using grpcurl to interact with gRPC
3. Using grpcurl to dump sqlite3 hashes
4. Blind command injection using pyload exploit
