import os
import time
import tkinter as tk
import subprocess
from colorama import init, Fore
import webbrowser
from http.server import HTTPServer, BaseHTTPRequestHandler

total = 10

html_code = """ <!DOCTYPE html> <html> <head> <style> body { display: flex; flex-wrap: wrap; align-content: flex-start; /* gap: 1%; */ background-color: #f2f2f2; font-family: Arial, sans-serif; padding: 30px; min-height: 100%; max-height: 100%; overflow: auto; } .server { position: relative; width: 30%; margin-right: 10px; margin-bottom: 10px; padding: 10px; background-color: #fff; border: 1px solid #ccc; border-radius: 4px; transition: background-color 0.3s, color 0.3s; display: flex; flex-direction: column; justify-content: flex-start; } .server:hover { color: #fff; background-color: #527bff; } .server h3 { margin-left: 70px; } .server p { margin: 0; /* ลบระยะขอบของย่อหน้าใน <p> */ line-height: 1.2; /* ปรับระยะห่างระหว่างบรรทัดใน <p> */ font-size: 14px; /* ปรับขนาดตัวอักษรใน <p> */ margin-bottom: 10px; margin-left: auto; } .server button { background-color: #4CAF50; color: white; padding: 8px 16px; border: none; border-radius: 4px; cursor: pointer; transition: background-color 0.3s; } .server button:hover { background-color: #45a049; } .server .actions { display: flex; justify-content: space-between; } .server .actions { display: flex; justify-content: space-between; margin-top: auto; /* เพิ่มคุณสมบัติ margin-top เป็น auto */ } .server img { position: absolute; /* จัดตำแหน่งโลโก้ให้อยู่ในตำแหน่งที่ต้องการ */ top: 10px; /* ปรับตำแหน่งแนวตั้ง (ห่างจากด้านบน) ตามที่ต้องการ */ left: 10px; /* ปรับตำแหน่งแนวนอน (ห่างจากด้านซ้าย) ตามที่ต้องการ */ width: 50px; /* ปรับขนาดความกว้างของโลโก้ตามที่ต้องการ */ height: 50px; /* ปรับขนาดความสูงของโลโก้ตามที่ต้องการ */ border-radius: 50%; /* ปรับรูปร่างของโลโก้เป็นวงกลม (หากต้องการ) */ background-color: #ffffff; /* ปรับสีพื้นหลังของโลโก้ตามที่ต้องการ */ /* border: 1px solid #cccccc; ปรับเส้นขอบของโลโก้ตามที่ต้องการ */ } </style> </head> <body> <div class="server"> <img src="https://cdn.discordapp.com/attachments/732556321169342517/1120711051378425877/291497399_467034158567390_2664618870935676894_n.jpg" alt="Server Logo"> <h3>What Server 1</h3> <p>IP: cfx.re/join/v48r4q</p> <div class="actions"> <button onclick="connect('fivem://connect/cfx.re/join/v48r4q')">Connect</button> <button onclick="copyIP('cfx.re/join/v48r4q')">Copy IP</button> </div> </div> <div class="server"> <img src="https://cdn.discordapp.com/attachments/732556321169342517/1120711051378425877/291497399_467034158567390_2664618870935676894_n.jpg" alt="Server Logo"> <h3>What Server 2</h3> <p>IP: cfx.re/join/yq7ypj</p> <div class="actions"> <button onclick="connect('fivem://connect/cfx.re/join/yq7ypj')">Connect</button> <button onclick="copyIP('cfx.re/join/yq7ypj')">Copy IP</button> </div> </div> <div class="server"> <img src="https://cdn.discordapp.com/attachments/732556321169342517/1120711051378425877/291497399_467034158567390_2664618870935676894_n.jpg" alt="Server Logo"> <h3>What Server 3 (BANNED PLAYERS)</h3> <p>IP: 147.50.229.146:30122</p> <div class="actions"> <button onclick="connect('fivem://connect/147.50.229.146:30122')">Connect</button> <button onclick="copyIP('147.50.229.146:30122')">Copy IP</button> </div> </div> <div class="server"> <img src="https://cdn.discordapp.com/attachments/732556321169342517/1120711051378425877/291497399_467034158567390_2664618870935676894_n.jpg" alt="Server Logo"> <h3>What Server 4</h3> <p>IP: 147.50.229.152:30122</p> <div class="actions"> <button onclick="connect('fivem://connect/147.50.229.152:30122')">Connect</button> <button onclick="copyIP('147.50.229.152:30122')">Copy IP</button> </div> </div> <div class="server"> <img src="https://cdn.discordapp.com/attachments/732556321169342517/1120711051378425877/291497399_467034158567390_2664618870935676894_n.jpg" alt="Server Logo"> <h3>What Server 5</h3> <p>IP: 147.50.229.124/30124</p> <div class="actions"> <button onclick="connect('fivem://connect/147.50.229.124/30124')">Connect</button> <button onclick="copyIP('cfx.re/147.50.229.124/30124')">Copy IP</button> </div> </div> <!-- <div class="server"> <img src="https://media.discordapp.net/attachments/1082883921353642036/1082884116376211507/Ci-Whatcity_Multiverse_BlakcStorkw.png?width=701&height=701" alt="Server Logo"> <h3>What MULTIVERSE</h3> <p>IP: cfx.re/join/orp8rj</p> <div class="actions"> <button onclick="connect('fivem://connect/cfx.re/join/orp8rj')">Connect</button> <button onclick="copyIP('cfx.re/join/orp8rj')">Copy IP</button> </div> </div> <div class="server"> <img src="https://cdn.discordapp.com/attachments/732556321169342517/1120711051378425877/291497399_467034158567390_2664618870935676894_n.jpg" alt="Server Logo"> <h3>What CITY</h3> <p>IP: cfx.re/join/4x4lj5</p> <div class="actions"> <button onclick="connect('fivem://connect/cfx.re/join/4x4lj5')">Connect</button> <button onclick="copyIP('cfx.re/join/4x4lj5')">Copy IP</button> </div> </div> --> <script> function connect(url) { window.location.href = url; } function copyIP(ip) { navigator.clipboard.writeText(ip); alert('ที่อยู่ IP ' + ip + ' ถูกคัดลอกไปยังคลิปบอร์ดแล้ว'); } </script> </body> </html> """

def progress_bar(total):
    for i in range(1, total + 1):
        percent = (i * 100) // total
        completed = i * 20 // total  # 20 is the width of the progress bar
        progressbar = '█' * completed + '-' * (20 - completed)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\n\n\n\n\n\n\n\n")
        print(f"\033[1mProgress: [{progressbar}]".center(120))
        print(f"\033[1m{percent}%".center(120))
        print("\n")
        time.sleep(1)

def clean_temp_files():
    os.system('del /s /f /q c:\\windows\\temp\\*.*')
    os.system('rd /s /q c:\\windows\\temp')
    os.system('md c:\\windows\\temp')
    os.system('del /s /f /q C:\\WINDOWS\\Prefetch')
    os.system('del /s /f /q %temp%\\*.*')
    os.system('rd /s /q %temp%')
    os.system('md %temp%')
    os.system('deltree /y c:\\windows\\tempor~1')
    os.system('deltree /y c:\\windows\\temp')
    os.system('deltree /y c:\\windows\\tmp')
    os.system('deltree /y c:\\windows\\ff*.tmp')
    os.system('deltree /y c:\\windows\\history')
    os.system('deltree /y c:\\windows\\cookies')
    os.system('deltree /y c:\\windows\\recent')
    os.system('deltree /y c:\\windows\\spool\\printers')
    os.system('del c:\\WIN386.SWP')
    os.system('echo Running Windows Cleaner (cleanmgr.exe)')
    os.system('start "" /wait "C:\\Windows\\System32\\cleanmgr.exe" /sagerun:50')
    os.system('cls')

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_code.encode())

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print('Server running at http://localhost:8000/')
    httpd.serve_forever()

def open_webpage_in_browser():
    url = 'http://localhost:8000/'
    webbrowser.open(url)

def main():
    init()
    os.system('chcp 65001 >nul 2>&1')
    os.system('mode 120,30')
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('title UNKNOW.FIVEM')

    print("\n\n\n\n\n\n\n\n\n")
    print(Fore.RED + "             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓       ".center(120))
    print(Fore.CYAN + "                       Welcome To BOOSTFIVEM".center(100))
    print(Fore.RED + "             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛       ".center(120))
    print("\n")
    print(Fore.RED + "             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓       ".center(120))
    print(Fore.CYAN + "                       Press ENTER to continue".center(100))
    print(Fore.RED + "             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛       ".center(120))
    print("\n")
    input()

    progress_bar(total)
    clean_temp_files()

    os.system('chcp 65001 >nul 2>&1')
    os.system('mode 120,30')
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('title UNKNOW.FIVEM')

    print("\n\n\n\n\n\n\n\n\n")
    print(Fore.GREEN +"         #     # #     # #    # #     # ####### #     #      ".center(120))
    print(Fore.GREEN +"         #     # ##    # #   #  ##    # #     # #  #  #      ".center(120))
    print(Fore.GREEN +"         #     # # #   # #  #   # #   # #     # #  #  #      ".center(120))
    print(Fore.GREEN +"         #     # #  #  # ###    #  #  # #     # #  #  #      ".center(120))
    print(Fore.GREEN +"         #     # #   # # #  #   #   # # #     # #  #  #      ".center(120))
    print(Fore.GREEN +"         #     # #    ## #   #  #    ## #     # #  #  #      ".center(120))
    print(Fore.GREEN +"         #######  #     # #    # #    # #######  ## ##       ".center(120))
    print("\n")
    open_webpage_in_browser()
    run_server()
    input()

if __name__ == "__main__":
    main()
