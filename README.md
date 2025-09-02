# 🐍 Dictionary Based on Python  

A simple **Python-based dictionary application** that allows users to search for word definitions from a JSON dataset. It also provides **suggestions for misspelled words** using the `difflib` module.  

---

## 📑 Table of Contents  

1. [Features](#-features)  
2. [Project Structure](#-project-structure)  
3. [Installation](#-installation)  
4. [Usage](#-usage)  
5. [Contributing](#-contributing)  
6. [Contact](#-contact)  

---

## ✨ Features  

- 📖 Search for word definitions from `data.json`.  
- 🔎 Suggests the closest matching word if a spelling mistake is detected.  
- 📜 Retrieve a list of all words in the dictionary.  
- 🖥️ Simple command-line interface.  

---

## 📂 Project Structure  

```

📦 dictionary-python
┣ 📜 data.json        # Contains dictionary word definitions
┣ 📜 dictionary.py    # Main Python script for running the dictionary

````

---

## ⚙️ Installation  

### Prerequisites  
- Python 3.6+  

### Steps  
1. Clone this repository:  
   ```bash
   https://github.com/JAM3S11/dictionary-data_python.git

2. Navigate into the project folder:

   ```bash
   cd dictionary-data-python
   ```
3. Run the script:

   ```bash
   python dictionary.py
   ```

---

## 🚀 Usage

When you run the program, you’ll be prompted to enter a word:

```bash
Enter a word: computer
```

Example outputs:

* If the word exists:

  ```bash
  ['An electronic device for storing and processing data.']
  ```

* If the word is misspelled:

  ```bash
  Did you mean compute instead of computr? Please try again.
  ```

* If the word does not exist:

  ```bash
  The word xyzabc does not exist in the dictionary. Please try again.
  ```

You can also list all words by modifying the script to call:

```python
print(getAllWords())
```

---

## 🤝 Contributing

We welcome contributions!

* Fork the repo
* Create a feature branch
* Commit your changes
* Submit a pull request

---

## 📬 Contact

* **Author**: JAM3S11
* **GitHub Issues**: [Open an Issue](https://github.com/your-username/dictionary-python/issues)

---
