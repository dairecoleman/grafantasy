# Script that pulls data from the HEVY website and saves it to grafantasy_data
import os
import subprocess
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv("/home/daire/grafantasy/.env")
email = os.environ.get("HEVY_EMAIL")
password = os.environ.get("HEVY_PASSWORD")

if not email or not password:
    raise ValueError("HEVY_EMAIL or HEVY_PASSWORD not set in .env")

filepath="/home/daire/grafantasy/modules/playwright/hevy_export.csv"

# function that launchs chromium session and returns browser and browser page
def launch_browser_page(p):
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    return browser, page

# function that logs into the hevy site with credentials
def login(page):
    page.goto("https://hevy.com/login")
    page.fill("input[label='Email or username']", email)
    page.fill("input[type='password']", password)
    page.click("button[type='submit']")
    page.wait_for_load_state("networkidle")

# function that navigates to export data page and downloads workout data
def export_data(page):
    page.goto("https://hevy.com/settings?export")
    with page.expect_download() as download_info:
        page.get_by_role("button", name="Export Workout Data").click()
        download = download_info.value
        download.save_as(filepath)
        print("Saved CSV:", download.path())

with sync_playwright() as p:
    browser, page = launch_browser_page(p)
    login(page)
    export_data(page)
    input("Press Enter to close the browser...")
    browser.close()

# need to check it works
