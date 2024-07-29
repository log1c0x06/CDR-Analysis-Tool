
# CDR Analysis Tool

This tool is designed to load and analyze Call Detail Records (CDR) from various file formats including CSV, TXT, XML, and JSON.

## Features

- Load CDR data from CSV, TXT, XML, and JSON files.
- Analyze and display data including call start time, end time, duration, caller number, receiver number, call type, country, tower ID, ISP name, cost, and call status.
- Save analysis results to a text file.

## Usage

### For Termux

**Update the packages:**
```sh
pkg up -y
```

**Install some dependencies:**
```sh
pkg install git wget python3 -y
```

**Clone the repository:**
```sh
git clone https://github.com/log1c0x06/CDR-Analysis-Tool.git
```

**Go to the CDR-Analysis-Tool directory:**
```sh
cd CDR-Analysis-Tool
```

**Run the script:**
```sh
python cdr_analysis_tool.py
```

### For Debian-based GNU/Linux distributions

**Update the packages:**
```sh
sudo apt update
```

**Install some dependencies:**
```sh
sudo apt install git wget python3 -y
```

**Clone the repository:**
```sh
git clone https://github.com/log1c0x06/CDR-Analysis-Tool.git
```

**Go to the CDR-Analysis-Tool directory:**
```sh
cd CDR-Analysis-Tool
```

**Run the script:**
```sh
python3 cdr_analysis_tool.py
```

### For Windows

**Install Python from [python.org](https://www.python.org/downloads/)**

**Clone the repository using Git Bash or download the ZIP:**
```sh
git clone https://github.com/log1c0x06/CDR-Analysis-Tool.git
```
Or download and extract the ZIP file from GitHub.

**Navigate to the CDR-Analysis-Tool directory:**
```sh
cd CDR-Analysis-Tool
```

**Run the script:**
```sh
python cdr_analysis_tool.py
```

## License

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Acknowledgements

This tool was developed by `log1c0x06`.
