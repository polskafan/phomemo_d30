# phomemo_d30
Python script to print text on a Phomemo D30 label printer

# Attribution
Based on previous phomemo-tools(https://github.com/vivier/phomemo-tools) by Laurent Vivier and
phomemo_m02s(https://github.com/theacodes/phomemo_m02s) by theacodes.

# Checkout and install
```bash
git clone https://github.com/polskafan/phomemo_d30.git
cd phomemo_d30
python3 -m venv venv
venv/bin/pip install -r requirements.txt
```

# Usage
Connect to printer with rfcomm
```bash
sudo rfcomm connect 1 XX:XX:XX:XX:XX:XX
```

Basic usage
```bash
venv/bin/python print_text.py "Hello World!"
```

Print on "fruit" labels
```bash
venv/bin/python print_text.py --fruit "This is a fruit label."
```

Change font
```bash
venv/bin/python print_text.py --font Arial.ttf "Hello World!"
```

Multiline Labels
```bash
venv/bin/python print_text.py "First line\nSecond line"
```
