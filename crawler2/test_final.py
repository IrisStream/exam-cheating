from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import threading
import random

PATH = "./chromedriver"

def crawl(province_code):
    driver = webdriver.Chrome(PATH)
    driver.get("https://diemthi.vnexpress.net/diem-thi-nam-2018#area=2&college=0&q=score1")
    number_of_students = 100000
    file_name = f"{province_code}.csv"
    f = open(file_name, 'w')
    missing = 0
    for student_code in range(province_code * 1000001, number_of_students + province_code*1000000):
        search = driver.find_element_by_name("keyword")
        sbd = str(student_code).zfill(8)
        search.clear()
        search.send_keys(sbd)
        search.send_keys(Keys.RETURN)

        try:
            table_src = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "result"))
            )
            time.sleep(1 + random.random())
            table_soup = BeautifulSoup(table_src.get_attribute('innerHTML'), 'html.parser')
            scores_tag = table_soup.find_all('td', class_='width_sbd')
            if len(scores_tag) == 0:
                missing += 1
                continue
            if missing > 20:
                return
            missing = 0
            scores = [txt.get_text() for txt in scores_tag]
            line = ','.join(scores[3:])
            print(line)
            f.write(f"{line}\n")
        except:
            driver.quit()

if __name__ == "__main__":
    try:
        x = []
        for i in range(21, 40):
            x.append(threading.Thread(target=crawl, args=(i,)))
            x[-1].start()
    except:
        exit()
