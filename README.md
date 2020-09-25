# dns-checker
A simple cli tool to check DNS record through multiple name servers

# How to

Insall dependencies
```bash
pip install -r requirements.txt
```

Run the tool 
```bash
python main.py -t A google.com
```

On success
```
All 24 nameservers responded!
```

On full/partial fail you will get list of failing nameservers
```
Response from the 71.122.219.170 is empty
Response from the 109.228.25.186 is empty
Response from the 212.98.75.35 is empty
```
