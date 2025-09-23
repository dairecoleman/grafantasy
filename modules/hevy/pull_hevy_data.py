# Script that pulls data from the HEVY website and saves it to grafantasy_data
import requests
import pandas as pd

# Replace this with your Hevy export URL
url = "https://hevy.com/export/user_xxxxx.csv"

# Optional: if you need cookies/authentication, put them here
cookies = {
    # "session": "your_session_cookie"
}

# Download CSV
response = requests.get(url, cookies=cookies)
if response.status_code == 200:
    with open("hevy_data.csv", "wb") as f:
        f.write(response.content)
    print("✅ Hevy data saved as hevy_data.csv")
else:
    print(f"❌ Failed to fetch data. Status: {response.status_code}")

# Load into pandas if you want to manipulate it
#df = pd.read_csv("hevy_data.csv")
#print(df.head())
#playwright
#from playwright.sync_api import sync_playwright

#with sync_playwright() as p:
#    browser = p.chromium.launch(headless=True)
#    page = browser.new_page()
#    page.goto("https://hevy.com/login")
#    page.fill("input[name='email']", "you@example.com")
#    page.fill("input[name='password']", "your_password")
#    page.click("button[type='submit']")
#    page.wait_for_load_state("networkidle")

#    with page.expect_download() as download_info:
#        page.click("text=Export Data")
#    download = download_info.value
#    download.save_as("hevy_export.csv")
#    browser.close()

