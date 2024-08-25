from src import scrapper
import os
from dotenv import load_dotenv

load_dotenv()
url = os.getenv('job_url')
linkedin_username = os.getenv('linkedin_username')
linkedin_password = os.getenv('linkedin_password')

clean_jd = scrapper.scrapper_main(url,linkedin_username,linkedin_password)
