
# 📚 ScholarFetch

**ScholarFetch** is a lightweight Python tool for researchers, students, and data enthusiasts to **automatically search Google Scholar** and **download available PDF versions** of academic papers.

> Save time. Skip the clicks. Fetch knowledge instantly.

---

## ✨ Features

- 🔍 **Custom Search** – Input any topic of interest and number of pages to crawl.
- 📥 **PDF Downloader** – Downloads direct-access academic PDFs when available.
- 🗂️ **Auto-folder Creation** – Organizes downloads by your search topic.
- 🛡️ **Content-Type Check** – Ensures only valid PDF files are downloaded.
- 🧼 **Safe Filenames** – Automatically sanitizes file names for your system.

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/google-scholar-downloader.git
cd google-scholar-downloader
```

### 2. Install the requirements

Make sure Python 3.6+ is installed. Then run:

```bash
pip install -r requirements.txt
```

### 3. Run the script

```bash
python scholar.py
```

You’ll be prompted to enter:

- A search topic (e.g. `deep learning`)
- Number of result pages to scan (each page = 10 results)

---

## 💡 Example

**Input:**
```
Enter your Topic: climate change
Enter the number of pages to search: 2
```

**Output:**
```
PAGE : 1
Understanding the climate system
https://example.edu/climate.pdf
Downloaded: climate change/Understanding the climate system.pdf
...
PAGE : 2
...
```

All PDFs will be saved inside a folder named `climate change`.

---

## 🧰 Tech Stack

- Python 3
- BeautifulSoup (for HTML parsing)
- Requests (for HTTP requests)
- Google Scholar search page (scraped)

---

## ⚠️ Disclaimer

> Google Scholar does not officially support scraping, and its structure may change at any time. This tool is for **educational and research purposes only**.  
> Use it responsibly and respect the [Google Terms of Service](https://policies.google.com/terms).

---

## 📄 License

MIT License — free for personal and commercial use with attribution.

---

## 🙋‍♂️ Contributions

Pull requests and suggestions are welcome! If Google Scholar changes its structure, feel free to submit a fix.

---

## ✉️ Contact

Created by **[Amirdoustdar]** — feel free to reach out via [MY GitHub Profile].
