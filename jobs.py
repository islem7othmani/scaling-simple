from flask import Flask, jsonify, request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from flask_cors import CORS
import time  # You were missing this import for time.sleep()

app = Flask(__name__)
CORS(app)

def scrape_jobs(location):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get(f"https://www.simplyhired.com/search?q=web+designer")

    time.sleep(3)  # Wait for the page to load

    src = driver.page_source
    soup = BeautifulSoup(src, "lxml")

    jobs_data = []  # Initialize list to store jobs

    # Scrape job listings
    jobs = soup.find_all("ul", {'id': 'job-list'})
    for job in jobs:
        list_items = job.find_all("li")
        for job_item in list_items:
            job_details = {}

            job_title_div = job_item.find("div")
            if job_title_div:
                job_title_h2 = job_title_div.find("h2")
                if job_title_h2:
                    job_title_a = job_title_h2.find("a")
                    if job_title_a:
                        job_title = job_title_a.text.strip()
                        job_details["title"] = job_title

                job_place_p1 = job_title_div.find("p", {'class': 'chakra-text css-1sawo7p'})
                if job_place_p1:
                    job_place = job_place_p1.text.strip()
                    job_details["place"] = job_place

                job_description = job_title_div.find("p", {'class': 'chakra-text css-jhqp7z'})
                if job_description:
                    job_desc = job_description.text.strip()
                    job_details["description"] = job_desc

                salary = job_title_div.find("div", {'class': 'css-2imjyh'})
                if salary:
                    job_salary = salary.text.strip()
                    job_details["salary"] = job_salary
                    time_p = salary.find("p", {'class': 'chakra-text css-5yilgw'})
                    if time_p:
                        time_str = time_p.text.strip()
                        job_details["time"] = time_str

                if job_details:  # Add job details only if data is collected
                    jobs_data.append(job_details)

    driver.quit()
    return jobs_data

@app.route('/scrapeJobs', methods=['GET'])
def scrape():
    location = request.args.get('location', 'default_location')  # Default location if not provided
    try:
        jobs = scrape_jobs(location)
        if jobs:
            return jsonify({"status": "success", "jobs": jobs}), 200
        else:
            return jsonify({"status": "success", "message": "No jobs found"}), 404
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    # Change the port to 5001 (or any other available port)
    app.run(debug=True, port=5001)
