# 🌐 **Web Scraping Tool** 

Welcome to the **Web Scraping Tool** repository! This tool is still in its **early stages** of development and primarily focuses on scraping **event data** from various websites. Built with **Selenium**, it automates the extraction process, saving time and effort. While the current focus is on event-related sites like **Luma**, the tool is designed to be scalable and adaptable to a wider range of use cases.

With the **rise of Large Language Models (LLMs)**, the need for large-scale, high-quality datasets for fine-tuning has never been greater. Web scraping offers an efficient and scalable solution to gather the data required for this purpose. This project serves as a foundation for scraping event-related data, which can be utilized for training LLMs and powering data-driven applications across various domains.

---

## 🛠 **Features**
- 🔄 **Modular Codebase**: A flexible and reusable design for easy extension to new data sources.
- ⚙️ **Selenium Integration**: Automates browser actions to extract event data effortlessly.
- 💾 **CSV Output**: Stores the scraped data in a structured CSV format for easy processing and analysis.
- 🎟 **Event Website Focus**: Includes scrapers for platforms like **Luma** and **Eventbrite**.
- 🌍 **Location-Based Scraping**: Enables filtering event data by location (e.g., Austin, New York).

---

## 📂 **File Structure**

```
├── main.py              # Main entry for scraping events
├── helperfunctions.py   # Utility functions for data handling & processing
├── helper_selenium.py   # Functions for Selenium-based scraping
├── constants.py         # Stores constants such as class names and IDs for scraping
├── LumaEvents.py        # Scraper for events on Luma
├── EventBriteEvents.py  # Scraper for events on Eventbrite
└── data/                # Stores scraped data and URLs
```

---

## ⚡ **How to Use**

### 1. **Install Dependencies**

The project relies on **Selenium** for automation. To install dependencies, run:

```bash
pip install -r requirements.txt
```

### 2. **Run the Scraper**

To start scraping, simply execute the **main.py** script:

```bash
python main.py
```

By default, the scraper will pull data from **Eventbrite**. You can modify it to scrape data from **Luma** or other websites by uncommenting the respective function call.

### 3. **Add New Scrapers**

You can extend the scraper to collect data from other websites. Just define the scraping logic for the new platform, and the tool will manage the rest.

---

## 📄 **File Details**

- **`helperfunctions.py`**: Contains key functions like `concatURL`, `ReadFile`, and `CreateCSV` for managing URLs and files.
- **`helper_selenium.py`**: Handles browser interaction with functions like `GetHTML` and `ChromeHeadless`.
- **`constants.py`**: Defines essential constants for scraping, including class names and element IDs.
- **`LumaEvents.py`**: Scraper for extracting event data from **Luma**.
- **`EventBriteEvents.py`**: Scraper for gathering event data from **Eventbrite**.

---

## 🤝 **Contributing**

This project is in its early stages, and contributions are welcome! Whether you're looking to improve its modularity, add new features, or introduce support for more websites, feel free to **fork the repo** and submit a **pull request**.

---

## 📄 **License**

This project is licensed under the **MIT License**.