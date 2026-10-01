# 📖 Fetch-Novel-Online

A mini Python project that fetches novel chapters from an online source and saves them as `.txt` files for offline reading.

This project was created as a practice exercise for learning **Python web scraping**, HTTP requests, HTML parsing, and file handling.

## ✨ Features

* Fetch novel chapters from a URL
* Parse chapter titles and content from HTML
* Automatically navigate through multiple chapters
* Save each chapter as a `.txt` file
* Use UTF-8 encoding to support Chinese and other Unicode characters

## 🛠️ Technologies

* **Python 3**
* `requests` — Send HTTP requests
* `lxml` — Parse and extract content from HTML

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Sherlock-YH/Fetch-Novel-Online.git
cd Fetch-Novel-Online
```

Install the required dependencies:

```bash
pip install requests lxml
```

## 🚀 Usage

Run the Python script:

```bash
python main.py
```

The script fetches the novel chapters from the configured URL and saves them as text files.

For example:

```text
Chapter 1.txt
Chapter 2.txt
Chapter 3.txt
...
```

## 📂 Example Project Structure

```text
Fetch-Novel-Online/
├── main.py
├── README.md
└── chapters/
    ├── 1.txt
    ├── 2.txt
    └── ...
```

## 📚 What I Learned

This project was mainly built to practise:

* Making HTTP requests with Python
* Working with `requests`
* Parsing HTML using XPath and `lxml`
* Extracting text from web pages
* Handling URLs with `urljoin`
* Writing text files with Python
* Handling UTF-8 encoded content
* Automating repetitive web requests

## ⚠️ Disclaimer

This project is intended for **educational and personal use** to practise Python programming and web scraping.

Please respect the website's terms of service, copyright, robots.txt, and applicable laws when using this project. Only download content that you have permission to access and save.

## 📄 License

This project is licensed under the MIT License.
