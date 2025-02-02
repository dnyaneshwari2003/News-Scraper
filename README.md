# Yahoo News Scraper & Web Display

This project is a web application built using **Flask** that scrapes news headlines from Yahoo and displays them on a webpage.

## 🚀 Features
- Scrapes the latest news headlines from Yahoo.
- Displays the headlines on a simple Flask-powered webpage.
- Stores the headlines in a CSV file.

---

## 📌 Prerequisites
Before running the project, ensure you have the following installed:

- **Python 3.7+**
- **pip** (Python package manager)

### Install Dependencies
Run the following command to install required Python libraries:

```
pip install flask beautifulsoup4 requests
```

---

## 🛠️ Project Structure
```
scrapper/
├── app.py          # Main Flask application
├── templates/
│   ├── index.html  # HTML template for displaying headlines

```

---

## 🔧 How to Run the Project

### 1️⃣ Start the Flask App
```
python app.py
```

### 2️⃣ Open in Browser
Once the server starts, visit:
```
http://127.0.0.1:5000/
```
This will display the latest Yahoo news headlines.

---

## 🔄 How It Works
1. **Scraping Data**: The script fetches Yahoo's homepage and extracts news headlines using BeautifulSoup.
2. **Saving to CSV**: The extracted headlines are saved into `news_data.csv`.
3. **Displaying on Webpage**: The headlines are passed to an HTML template and displayed dynamically.

---

## 📝 Customization
- **Modify `app.py`** to scrape a different website by changing `url = 'http://yahoo.com'`.
- **Update `index.html`** for a better UI design.

---

## 🛠️ Troubleshooting
**Issue:** `jinja2.exceptions.TemplateNotFound: index.html`  
🔹 Ensure `index.html` is inside the `templates/` folder.

**Issue:** UnicodeEncodeError when writing to CSV  
🔹 Modify `open()` function in `app.py`:
```
with open("news_data.csv", 'w', encoding="utf-8", newline="") as output_file:
```

---

## 🤝 Contributing
Feel free to fork this project and improve it! If you find any issues, create a pull request or open an issue.

---
