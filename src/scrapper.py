import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import regex as re

load_dotenv()
url = os.getenv('job_url')
linkedin_username = os.getenv('linkedin_username')
linkedin_password = os.getenv('linkedin_password')

def scrapper_main(url,linkedin_username,linkedin_password):
     # Path to your ChromeDriver (ensure it's downloaded and accessible)
     # webdriver_path = "/path/to/chromedriver"  # Replace with the actual path to chromedriver

     # Path to Brave browser executable
     brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"  # Replace with the actual path to Brave executable

     # Set up Chrome options to use Brave
     chrome_options = Options()
     chrome_options.binary_location = brave_path

     # Create a new instance of the Chrome driver with Brave's executable
     service = Service()

     driver = webdriver.Chrome(service=service, options=chrome_options)


     # Step 1: Log in to LinkedIn
     driver.get("https://www.linkedin.com/login")
     time.sleep(2)  # Allow the page to load

     # Enter your LinkedIn credentials
     username = driver.find_element("id", "username")
     username.send_keys(linkedin_username)  # Replace with your LinkedIn email

     password = driver.find_element("id", "password")
     password.send_keys(linkedin_password)  # Replace with your LinkedIn password

     # Click the login button
     login_button = driver.find_element("xpath", "//button[@type='submit']")
     login_button.click()
     time.sleep(5)  # Wait for the login process to complete

     # Step 2: Navigate to the specific job listing
     print(url)
     driver.get(url)
     time.sleep(5)  # Wait for the job page to load

     html_content = driver.page_source
     with open("content/job_page.html", "w", encoding="utf-8") as file:
          file.write(html_content)

     print("HTML content saved to 'job_page.html'.")

     soup = BeautifulSoup(html_content, 'html.parser')
     job_content = soup.find(class_ = 'jobs-description__content jobs-description-content')
     clean_jd = re.sub('<.*?>', '', str(job_content))

     with open("content/clean_jd.html", "w", encoding="utf-8") as file:
          file.write(clean_jd)

     return clean_jd
     
