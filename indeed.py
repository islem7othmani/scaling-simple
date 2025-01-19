from flask import Flask, jsonify, request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes by default
def scrape_jobs(location):
    # Set up the Chrome WebDriver service
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Open the Indeed website
    driver.get(f"https://fr.indeed.com/jobs?q=software+engineer&l={location}")

    # Wait for the page to load, ensuring the job listings are present
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "css-1faftfv"))
        )
    except Exception as e:
        driver.quit()
        raise Exception("Timed out waiting for the page to load.")

    # Get the page source after ensuring content is loaded
    src = driver.page_source

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(src, "lxml")

    # Find the job list container
    jobs_data = []
    jobsIndeed = soup.find_all("ul", {'class': 'css-1faftfv eu4oa1w0'})

    if jobsIndeed:
        for job in jobsIndeed:
            list_items = job.find_all("li", class_='css-1ac2h1w eu4oa1w0')
            for job_item in list_items:
                job_details = {}

                # Job Title
                job_title_div = job_item.find("h2", class_='jobTitle css-1psdjh5 eu4oa1w0')
                if job_title_div:
                    job_details["job_title"] = job_title_div.text.strip()

                # Company Name
                job_company = job_item.find("span", class_='css-1h7lukg eu4oa1w0')
                if job_company:
                    job_details["company"] = job_company.text.strip()

                # Job Location
                job_location = job_item.find("div", class_='css-1restlb eu4oa1w0')
                if job_location:
                    job_details["location"] = job_location.text.strip()

                if job_details:
                    jobs_data.append(job_details)

    # Close the WebDriver after scraping
    driver.quit()

    return jobs_data

@app.route('/scrape', methods=['GET'])
def scrape():
    location = request.args.get('location', 'France')  # Default location is France if none is provided
    try:
        jobs = scrape_jobs(location)
        if jobs:
            return jsonify({"status": "success", "jobs": jobs}), 200
        else:
            return jsonify({"status": "success", "message": "No jobs found"}), 404
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
