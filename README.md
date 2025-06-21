# 🔍 port_scanner

A fast and lightweight multi-threaded TCP port scanner in Python.

## 🚀 Features

- High-speed port scanning
- Adjustable thread count and timeout
- Customizable port range
- No external dependencies (uses only `socket`, `threading` and `time`)
- Performance timing

## 🧠 How It Works

Each thread scans ports in a staggered manner using `socket.connect_ex()`. Results are appended safely using threading locks.

## ⚠️ Disclaimer

This tool is provided **as-is** and is intended **solely for educational, testing, and learning purposes**. 

The user is **fully responsible** for how this software is used. The author **does not take any responsibility** for misuse, including any legal consequences that may arise from scanning systems without permission.

By using this software, you agree that you will use it ethically, legally, and with the proper authorization.

## 📦 Installation

You can install the package after uploading to PyPI or TestPyPI:

```bash
pip install port_scanner_rq
