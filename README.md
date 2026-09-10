# Dummy_code

Test Python code repository for AI force — a collection of dummy Python scripts and utilities used for testing, experimentation, and demonstration purposes.

## 📖 Overview

This repository contains a variety of small, self-contained Python scripts covering common programming concepts, algorithms, data structures, and utility functions. Each file is independent and can be run on its own.

## 📁 Repository Contents

### 🔧 Core Files

| File | Description |
|------|-------------|
| `dummy.py` | Basic dummy script with greet and add functions |
| `list_use_case.py` | Fetches published use cases from the AIforce API |

### 🐍 Utility & Example Scripts

| # | File | Description |
|---|------|-------------|
| 01 | `01_calculator.py` | Basic arithmetic operations (add, subtract, multiply, divide) |
| 02 | `02_fibonacci.py` | Fibonacci sequence generator |
| 03 | `03_prime_checker.py` | Prime number checker |
| 04 | `04_palindrome.py` | Palindrome string checker |
| 05 | `05_factorial.py` | Recursive factorial calculator |
| 06 | `06_file_reader.py` | File reading utilities |
| 07 | `07_json_utils.py` | JSON load/save helpers |
| 08 | `08_sorting.py` | Bubble sort & Quick sort implementations |
| 09 | `09_password_generator.py` | Random password generator |
| 10 | `10_word_counter.py` | Word frequency counter |
| 11 | `11_temperature_converter.py` | Celsius/Fahrenheit/Kelvin conversions |
| 12 | `12_url_shortener.py` | Simple URL shortener class |
| 13 | `13_binary_search.py` | Binary search algorithm |
| 14 | `14_email_validator.py` | Regex-based email validator |
| 15 | `15_stack.py` | Stack data structure implementation |
| 16 | `16_queue.py` | Queue data structure implementation |
| 17 | `17_matrix_operations.py` | Matrix add / transpose / multiply operations |
| 18 | `18_date_utils.py` | Date arithmetic helpers |
| 19 | `19_http_client.py` | Simple HTTP client wrapper |
| 20 | `20_todo_manager.py` | Todo list manager class |
| 21 | `21_linked_list.py` | Singly linked list implementation |
| 22 | `22_caesar_cipher.py` | Caesar cipher encryption/decryption |
| 23 | `23_dice_roller.py` | Random dice roller with notation parser (e.g. `2d6`) |
| 24 | `24_csv_parser.py` | CSV read/write/filter utilities |
| 25 | `25_weather_fetcher.py` | Fetches weather data from OpenWeatherMap API |

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- `requests` library (for `list_use_case.py`, `19_http_client.py`, and `25_weather_fetcher.py`)

### Installation
```bash
git clone https://github.com/altassiantest/Dummy_code.git
cd Dummy_code
pip install requests
```

### Running a Script
Each script can be executed directly:
```bash
python 01_calculator.py
python 02_fibonacci.py
# ... and so on
```

## 🔐 Environment Variables

Some scripts require environment variables:

| Variable | Used By | Description |
|----------|---------|-------------|
| `AIFORCE_BASE_URL` | `list_use_case.py` | Base URL of the AIforce API |
| `TOOL_API_KEY` or `USECASE_AUTH_TOKEN` | `list_use_case.py` | Bearer token for authentication |
| `OPENWEATHER_API_KEY` | `25_weather_fetcher.py` | API key from OpenWeatherMap |

## 📝 Purpose

This repository is intended for:
- 🧪 Testing AI-powered code analysis tools
- 📚 Providing simple, readable Python examples
- 🎯 Demonstrating common algorithms and data structures
- 🔬 Experimentation and prototyping

## 📄 License

This is a test/dummy repository for internal use.
