from requests_html import HTMLSession
import time
import random

session = HTMLSession()

f = open("output.txt", "a")

for area_code in range(5, 66):
    area_code_text = str(area_code)
    area_code_text = area_code_text.zfill(2)
    for student_id in range(2458,20000):
        time.sleep(random.random())
        student_id_text = str(student_id)
        student_id_text = student_id_text.zfill(5)
        url = f"https://diemthi.vnexpress.net/diem-thi-nam-2018#area=2&college=0&q={area_code_text}0{student_id_text}"
        r = session.get(url)
        print(f"{area_code_text}0{student_id_text}")
        f.write(f"{area_code_text}0{student_id_text}\n")
        r.html.render()
        rs = r.html.find("#result table a", first = False)

        for i in rs:
            student_url = 'https://diemthi.vnexpress.net' + i.attrs['href']
            print(student_url)
            f.write(f"{student_url}\n")

f.close()