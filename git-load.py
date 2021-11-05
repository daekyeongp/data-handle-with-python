import os
import time
from datetime import datetime, timedelta
import io
import sys


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

path = "C:\\python\\velog\\velog-backup\\backup\\content\\"
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith(".md")]

print("file_list: {}".format(file_list_py))
# 현재 시간 기준 날짜
time2 = datetime.now()
count = 0  # 횟수 count
print((time2 - timedelta(days=153)).strftime('%a %b %d %H:%M:%S %Y'))
# exit(0)
for i in range(len(file_list_py)):
# for i in range(5):
    # 날짜 변수
    what_day = (time2 - timedelta(days=153-i)).strftime('%a %b %d %H:%M:%S %Y')
    count += 1
    # print(what_day)
    # 파일 로딩
    with open(path+file_list_py[i], 'r', encoding="utf-8") as f:
        md = open("C:\\github\\data-handle-with-python\\Pandas\\" + file_list_py[i], 'w', encoding='utf-8')
        text = f.read()
        md.write(f'{text}')
        f.close()
        md.close()
        # print(text)

    # 깃 프로세스 진행(깃 Add + commit -> 날짜 수정 -> 깃 푸시)
    os.system(f'git config --global auto.crlf true')
    os.system(f'git add .')
    os.system(f'git commit -m "{file_list_py[i]} commit"')
    os.system(f'git commit --amend --no-edit --date "{what_day} +0900T"')
    os.system(f'git push origin +master')

    print(f'{i + 1}회차 완료되었음')

print(count)