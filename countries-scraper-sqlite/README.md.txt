*****  Countries Scraper & SQLite Database Project *******

This project is a simple example of Web Scraping and Database handling using Python.
It extracts information about the first 20 countries from the educational website ScrapeThisSite and stores the data in a SQLite database.

The main goal of this project is to practice:

Web data extraction (Scraping)
Data cleaning and transformation
Working with SQL databases
Basic data analysis

## 📌 Extracted Data

For each country, the following information is collected:

Country Name
Capital City
Population
Area

## 🗄️ Database Design

This project uses SQLite as the database system.

Database file:
countries.db
Table name:
countries
Table structure:
Column	Type	Description
id	INTEGER	Primary Key (Auto Increment)
country_name	TEXT	Name of the country
capital	TEXT	Capital city
population	INTEGER	Population
area	INTEGER	Area in square kilometers

## Features
- Web scraping using BeautifulSoup
- Data extraction from website
- Data type conversion
- Storing data in SQLite database
- Displaying first 5 records
- Calculating total population of 20 countries

## How to Run

Install dependencies:

pip install -r requirements.txt

Run the project:

python script.py


## Output
After running the program, you will see:
Success message
First 5 database records
Total population of 20 countries

## *****Notes****
This project is for educational purposes only.
Website structure may change over time.
Use VPN if connection issues occur.
----------------------------------------------------------------------------------
 Countries Scraper & SQLite Database Project

این پروژه یک نمونه ساده از
 **وب‌اسکرپینگ (Web Scraping)** 
و کار با پایگاه داده است.  
در این پروژه اطلاعات ۲۰ کشور اول از سایت آموزشی 
ScrapeThisSite
استخراج شده و در یک دیتابیس 
SQLite 
ذخیره می‌شود.


## هدف اصلی این پروژه تمرین مفاهیم زیر است:
- استخراج داده از صفحات وب
- پردازش و تبدیل داده‌ها (Data Cleaning)
- ذخیره‌سازی داده در پایگاه داده
- اجرای کوئری‌های ساده SQL


## داده‌های استخراج‌شده
برای هر کشور اطلاعات زیر دریافت می‌شود:
- نام کشور (Country Name)
- پایتخت (Capital)
- جمعیت (Population)
- مساحت (Area)


##  قابلیت‌های پروژه

- دریافت اطلاعات از وب‌سایت  
- استفاده از Web Scraping با BeautifulSoup  
- تبدیل داده‌ها به فرمت عددی (int)  
- ذخیره اطلاعات در SQLite  
- نمایش ۵ رکورد اول از دیتابیس  
- محاسبه مجموع جمعیت ۲۰ کشور  



## نحوه اجرا

ابتدا کتابخانه‌های مورد نیاز را نصب کنید:

```bash
pip install -r requirements.txt

سپس برنامه را اجرا کنید:

python script.py


## خروجی برنامه

پس از اجرای پروژه، موارد زیر در کنسول نمایش داده می‌شود:
پیام موفقیت‌آمیز بودن استخراج داده‌ها
نمایش ۵ کشور اول ذخیره‌شده در دیتابیس
مجموع جمعیت ۲۰ کشور


## نکات مهم
ساختار سایت ممکن است در آینده تغییر کند و روی 
scraping 
تأثیر بگذارد.
در صورت عدم اتصال، از 
VPN 
یا بررسی اینترنت استفاده کنید.