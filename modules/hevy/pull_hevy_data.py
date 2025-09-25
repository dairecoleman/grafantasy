# Script that pulls data from the HEVY website and saves it to grafantasy_data


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://hevy.com/login")
    page.fill("input[name='email']", "you@example.com")
    page.fill("input[name='password']", "your_password")
    page.click("button[type='submit']")
    page.wait_for_load_state("networkidle")

    with page.expect_download() as download_info:
        page.click("text=Export Data")
    download = download_info.value
    download.save_as("hevy_export.csv")
    browser.close()

