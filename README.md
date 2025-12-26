## Web Scraping and Data Visualization Project

📌 Project Overview

This project focuses on automated data extraction from public web pages using Python-based web scraping techniques. The system collects relevant information from websites, processes it into a structured dataset, and visualizes the extracted data through an interactive user interface dashboard.

The project demonstrates practical implementation of web scraping, data handling, and visualization techniques commonly used in real-world data analysis applications.

# 🎯 Objectives

To automatically extract structured data from public websites

To understand and handle HTML structure for accurate data collection

To create custom datasets tailored for analysis purposes

To visualize scraped data using an interactive UI dashboard

# 🛠️ Technologies & Tools Used

Python – Core programming language

BeautifulSoup – HTML parsing and data extraction

Requests – Sending HTTP requests to web pages

Pandas – Data processing and dataset creation

Streamlit – Interactive UI dashboard for data visualization

# ⚙️ System Workflow

Send HTTP requests to the target public website

Parse the HTML content using BeautifulSoup

Extract relevant data elements from the web page

Store the extracted data in CSV format

Load the dataset into Streamlit

Display and analyze the data using a web-based dashboard

# 📂 Project Features

Automated web data collection

Structured CSV dataset generation

Interactive and user-friendly dashboard

Modular and scalable project architecture

# 📊 Output

CSV Dataset containing scraped web data

Interactive UI Dashboard for data visualization and analysis

# 🔗 GitHub Repository

The complete source code for this project is available on GitHub:

# 👉 GitHub Profile:

https://github.com/Priyanshu-1608-dubey

# 📝 Conclusion

This project successfully demonstrates the use of web scraping techniques to collect data from public websites and transform it into meaningful datasets. The addition of an interactive dashboard enhances data accessibility and usability, making the system suitable for academic and practical applications.

## How to Run the Project (Step-by-Step)

Follow the steps below to successfully run the web scraping project and view the UI dashboard.

🔹 Step 1: Clone or Download the Project

Download the project folder or clone it from GitHub.

git clone https://github.com/Priyanshu-1608-dubey

Or manually extract the project folder to your system.

🔹 Step 2: Open Project Directory

Open Command Prompt / PowerShell and navigate to the project folder:

cd web_scraping_project

🔹 Step 3: Install Required Python Libraries

Make sure Python is installed. Then install the required dependencies:

pip install requests beautifulsoup4 pandas streamlit

# ⚠️ If multiple Python versions are installed, use:

py -m pip install requests beautifulsoup4 pandas streamlit

🔹 Step 4: Run the Web Scraping Script

Execute the scraping script to extract data and generate the dataset:

py scraper/scrape_quotes.py

# ✅ This will create a CSV file inside the data/ folder.

🔹 Step 5: Run the Streamlit UI Dashboard

Start the interactive dashboard using the following command:

py -m streamlit run dashboard/app.py

🔹 Step 6: View Output in Browser
