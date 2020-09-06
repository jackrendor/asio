# asio
All Shell In One. Generate Reverse Shells and/or generate single code that runs all the payloads.

# Usage
### To get a list of all the payloads
```bash
python3 asio.py --host 127.0.0.1 --port 8080
```

### To generate the all in one
```bash
python3 asio.py --host 127.0.0.1 --port 8080 --all
```

# Add new payloads
If you want to add new payloads, simply add them inside the file `personal_shells.txt` with the following sintaxt:
```
<Payload Name> | <Payload Code>
```
Without using `<` or `>` ofcourse. :)

If you think it should be in the default, just make a pull request or contact me on [Telegram](t.me/jackrendor)
