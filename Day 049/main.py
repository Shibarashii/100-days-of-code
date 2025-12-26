from selenium import webdriver
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from textwrap import dedent
from datetime import datetime
from typing import Callable
import time as t

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

root = Path(__file__).parent

user_data_dir = root / "chrome_profile"
options.add_argument(f"--user-data-dir={user_data_dir}")

GYM_URL = "https://appbrewery.github.io/gym/"

driver = webdriver.Chrome(options=options)
driver.get(GYM_URL)

ACCOUNT_EMAIL = "helloworld@gmail.com"
ACCOUNT_PASSWORD = "printhelloworld123"

wait = WebDriverWait(driver, timeout=2)


def retry(func: Callable, retries=7, description=None, *args):
    for i in range(retries):
        print(f"Trying {func.__name__}. Attempt: {i + 1}")
        try:
            return func(*args)
        except Exception:
            if i == retries - 1:
                raise
            t.sleep(1)


def login():
    login_button = wait.until(ec.element_to_be_clickable(
        (By.ID, "login-button")))
    login_button.click()

    email_input = wait.until(
        ec.presence_of_element_located((By.NAME, "email")))
    email_input.clear()
    email_input.send_keys(ACCOUNT_EMAIL)

    password_input = wait.until(
        ec.presence_of_element_located((By.NAME, "password")))
    password_input.clear()
    password_input.send_keys(ACCOUNT_PASSWORD)

    submit_button = wait.until(
        ec.element_to_be_clickable((By.ID, "submit-button")))
    submit_button.click()

    wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))


counter = {
    "Booked": 0,
    "Waitlisted": 0,
    "Already Booked/Waitlisted": 0,
    "Processed": 0
}


def book_classes(days: list):
    global counter
    details = []

    for day in days:
        class_ = wait.until(
            ec.presence_of_element_located((By.CSS_SELECTOR, f"div[id^=day-group-{day}]")))

        date_text = class_.find_element(By.TAG_NAME, "h2").text

        cards = class_.find_elements(
            By.CSS_SELECTOR, "div[id^='class-card']")

        for card in cards:
            time = card.find_element(
                By.CSS_SELECTOR, "p[id^='class-time']").text

            if "6:00 PM" in time:
                class_name = card.find_element(By.TAG_NAME, "h3").text

                button = card.find_element(
                    By.CSS_SELECTOR, "button[id^='book-button-']")

                driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});", button)

                if button.text == "Book Class":
                    button.click()
                    print(f"✓ Booked: {class_name} on {date_text}")
                    counter["Booked"] += 1
                    details.append(
                        f"[New Booking] {class_name} on {date_text}")

                elif button.text == "Join Waitlist":
                    button.click()
                    print(
                        f"✓ Joined waitlist for: {class_name} on {date_text}")
                    counter["Waitlisted"] += 1
                    details.append(
                        f"[New Waitlist] {class_name} on {date_text}")

                elif button.text == "Waitlisted" or button.text == "Booked":
                    print(
                        f"✓ Already on waitlist: {class_name} on {date_text}")
                    counter["Already Booked/Waitlisted"] += 1

                counter["Processed"] += 1
            t.sleep(0.5)

    summary = dedent(f"""
    --- BOOKING SUMMARY ---
    Classes booked: {counter['Booked']}
    Waitlists joined: {counter['Waitlisted']}
    Already Booked/Waitlisted: {counter["Already Booked/Waitlisted"]}
    Total processes: {counter['Processed']}\n""")

    print(summary)
    if details:
        detailed_summary = (
            "--- DETAILED SUMMARY---\n" +
            "\n".join(details) + "\n"
        )
        print(detailed_summary)


def verify_bookings():
    global counter
    expected_bookings_count = sum(
        v for k, v in counter.items() if k != "Processed")

    mybookings_link = driver.find_element(By.ID, "my-bookings-link")
    mybookings_link.click()

    bookings_counter = 0
    print("--- VERIFYING ON MY BOOKINGS PAGE ---")

    bookings_cards = wait.until(ec.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "div[id^='booking-card']")))

    for card in bookings_cards:
        class_name = card.find_element(By.TAG_NAME, "h3").text
        print(f"Verified: {class_name}")
        bookings_counter += 1

    waitlist_cards = driver.find_elements(
        By.CSS_SELECTOR, "div[id^='waitlist-card']")

    for card in waitlist_cards:
        class_name = card.find_element(By.TAG_NAME, "h3").text
        print(f"Verified: {class_name}")
        bookings_counter += 1

    summary = (
        "\n--- VERITFICATION RESULTS ---\n" +
        f"Expected: {expected_bookings_count} bookings\n" +
        f"Found: {bookings_counter} bookings\n"
    )

    result = "✅ SUCCESS: All bookings verified!" if expected_bookings_count == bookings_counter else "❌ MISMATCH"

    print(summary)
    print(result)


def main():
    retry(login)

    date_h1_element = wait.until(ec.presence_of_element_located(
        (By.CSS_SELECTOR, "h1[class^='Schedule']"))).text

    date_in_site = date_h1_element.replace(
        "Class Schedule (Today: ", "").strip(")")

    date_in_site = datetime.strptime(date_in_site, "%m/%d/%Y")

    days_of_week = ("mon", "tue", "wed", "thu", "fri", "sat", "sun")
    day_today_in_site = date_in_site.weekday()
    day_tomorrow_in_site = day_today_in_site + 1

    days_to_book = ["tue", "thu"]

    for i, day in enumerate(days_to_book):
        if day == days_of_week[day_today_in_site]:
            days_to_book[i] = "today"
        if day == days_of_week[day_tomorrow_in_site]:
            days_to_book[i] = "tomorrow"

    retry(book_classes, 7, None, days_to_book)
    retry(verify_bookings)


if __name__ == "__main__":
    main()
