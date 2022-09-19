# phomemo_d30
Python script to print text on a Phomemo D30 label printer

# Acknowledgements
Based on [phomemo-tools](https://github.com/vivier/phomemo-tools) by Laurent Vivier and
[phomemo_m02s](https://github.com/theacodes/phomemo_m02s) by theacodes.

# Example
<a href="http://www.youtube.com/watch?feature=player_embedded&v=U1ZqjYgFxjY
" target="_blank"><img src="http://img.youtube.com/vi/U1ZqjYgFxjY/maxresdefault.jpg" 
alt="Video example of the Python script" width="640" /></a>

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
