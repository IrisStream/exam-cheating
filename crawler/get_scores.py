import re
import subprocess

def remove_html_tags(text):
    clean = re.compile(r'<.*?>')
    return re.sub(clean, '', text)

def remove_n(text):
    clean = re.compile(r'\\n')
    return re.sub(clean, '', text)

def remove_t(text):
    clean = re.compile(r'\\t')
    return re.sub(clean, '', text)

def remove_leading_space(text):
    text = text.replace("   ","")
    return text.replace("  ", " ")

url = 'curl https://diemthi.vnexpress.net/diem-thi-nam-2018/detail/id/3522034/'

s = subprocess.check_output('curl https://diemthi.vnexpress.net/diem-thi-nam-2018/detail/id/3522034/', shell=True)

s = remove_html_tags(str(s))
s = s.strip()
s = remove_n(s)
s = remove_t(s)
s = remove_leading_space(s)
s = s.split(' ')
for ss in s:
    print(ss)