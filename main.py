import os
import zipfile
import yagmail
from common.file_path import FilePath
os.sys.path.append(r"D:\Program Files\JetBrains\PycharmProjects\AotoUIProjects")

if __name__ == '__main__':

    file_report = FilePath().get_report()

    os.system("pytest -q --alluredir=test_result --clean-alluredir")
    os.system("allure generate test_result -o test_result/report_html -c")
    os.system("allure open test_result/report_html -p 65535")

    text = '''@echo off 
if "%1" == "h" goto begin 
mshta vbscript:createobject("wscript.shell").run("%~nx0 h",0)(window.close)&&exit 
:begin
cd ..
allure open report_html'''

    if not os.path.exists(file_report):
        os.makedirs(file_report)
    xxoo = file_report+'\\allure'+'.bat'
    file = open(xxoo, 'w')
    file.write(text)
    file.close()
