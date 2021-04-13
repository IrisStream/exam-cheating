import re
import pandas as pd
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
    # text = text.replace("   ","")
    return text.replace("  ", " ")

def is_float(x):
    try:
        float(x)
        return True
    except:
        return False

def get_student(url):
    s = subprocess.check_output(f"curl {url}", shell=True)
    s = remove_html_tags(str(s))
    s = s.strip()
    s = remove_n(s)
    s = remove_t(s)
    s = remove_leading_space(s)
    return s.split(' ')

fin = open('output.txt','rt')
lines = fin.readlines()
fin.close()

fout = open('out', 'w')
df = pd.DataFrame(columns=['SBD', 'Toan', 'Ngu van', 'Ngoai ngu', 'Vat ly', 'Hoa hoc', 'Sinh hoc', 'Lich su', 'Dia ly', 'GDCD'])
i = 0
for line in lines:
    line = line.strip()
    if len(line) < 10:
        continue
    s = get_student(line)
    s.append('To\\xc3\\xa1n:')
    s.append('')
    s.append('v\\xc4\\x83n:')
    s.append('')
    s.append('ng\\xe1\\xbb\\xaf:')
    s.append('')
    s.append('V\\xe1\\xba\\xadt')
    s.append('')
    s.append('')
    s.append('H\\xc3\\xb3a')
    s.append('')
    s.append('')
    s.append('Sinh')
    s.append('')
    s.append('')
    s.append('L\\xe1\\xbb\\x8bch')
    s.append('')
    s.append('')
    s.append('\\xc4\\x90\\xe1\\xbb\\x8ba')
    s.append('')
    s.append('')
    s.append('d\\xc3\\xa2n:')
    s.append('')
    s.append('danh:')
    s.append('')

    for p in s:
        fout.write(f"{p}\n")
    df.loc[i] = [s[s.index('danh:')+1][:8], s[s.index('To\\xc3\\xa1n:') + 1], s[s.index('v\\xc4\\x83n:') + 1], s[s.index('ng\\xe1\\xbb\\xaf:') + 1], s[s.index('V\\xe1\\xba\\xadt') + 2], s[s.index('H\\xc3\\xb3a') + 2], s[s.index('Sinh') + 2], s[s.index('L\\xe1\\xbb\\x8bch') + 2], s[s.index('\\xc4\\x90\\xe1\\xbb\\x8ba') + 2], s[s.index('d\\xc3\\xa2n:') + 1]]
    i += 1

df.set_index('SBD')
fout.close()

df.to_csv('data.csv')
