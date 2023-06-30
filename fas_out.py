import pyautogui
import pyperclip
import os
from datetime import datetime

# CMD 창 환경 설정
os.system('mode con: cols=60 lines=23')
# os.system('color 0A')


# ===================== 한글입력지원 =========================

from pynput.keyboard import Controller, Key

# 한글 입력 함수
def type_kor(text):
    keyboard = Controller()

    # 한글 입력 모드로 변경
    keyboard.press(Key.ctrl)
    keyboard.press('`')
    keyboard.release('`')
    keyboard.release(Key.ctrl)

    # 한글 입력
    keyboard.type(text)

# 예시: "안녕하세요"를 한글로 입력
# type_kor("안녕하세요")

# ===================== 변동되는 데이터 =========================

location_1 = '영도'
location_2 = '본관'
location_3 = '5'
location_4 = '-'        

state1 = '지급'
state2 = '내부'
state3 = '개인용'
state4 = '-'

etc1 = '확인'
etc2 = '개인사용'

today = datetime.today().strftime('%Y-%m-%d')
print(today)

comment = '자산확인일자'

while True:
      # ===================== 시작 화면 설정 =========================
      os.system('cls')
      print('\n 1. 해상도 1920x1080에서만 동작합니다.\n\n 2. 왼쪽 모니터에 ERP를 전체화면으로 열고 시작하세요.\n')
      print(' 3. 현재 설정은 다음과 같습니다.\n\n'
            '\033[90m'
            '   위치정보 : '+location_1+', '+location_2+', '+location_3+', '+location_4+'\n\n'
            '   장비상태 : '+state1+', '+state2+', '+state3+', '+state4+'\n\n'
            '   점검정보 : '+etc1+', '+etc2+'\n\033[0m')
      print('\033[1;33m 긴급 중단 방법 : Ctrl + Alt + Del\033[0m')

      sn = input('\n S/N를 입력 하세요 : ')
      
      user = input('\n 사번을 입력 하세요 : ')
            
      # 좌표 저장 시작 (영도)
      click1 = 100,110  # [S/N]
      click2 = 100,245  # [검색결과]
      click3 = 835,307  # 사용자 버튼
      click4 = 1035,370  # 결과창을 더블클릭   
      click5 = 884,417  # [부서클릭] 
      click6 = 962,367  # [날짜]
      click7 = 923,506  # [Today]
      click8 = 1267,825 # [확인]
      click9 = 1697,52  # [저장버튼]

      # SN 검색 -> 부서입력 -> Today 클릭
      pyautogui.doubleClick(click1)   # SN 더블클릭
      pyautogui.hotkey('delete')      # 기존 입력 삭제

      pyautogui.write(sn)             # 입력받은 SN 입력
      pyautogui.hotkey('enter')       # Enter로 검색
      pyautogui.doubleClick(click2)   # 검색된 결과 1번 값 더블클릭

      pyautogui.click(click3)         # 사용자 버튼 클릭

      pyautogui.doubleClick(click4)   # 결과창을 클릭
      
      # 백스페이스 20번 누름 
      for _ in range(10):
            pyautogui.press('backspace')

      pyperclip.copy(user)            # 클립보드 복사
      pyautogui.hotkey('ctrl', 'v')   # 붙여넣기
      pyautogui.hotkey('enter')       # 검색
      pyautogui.doubleClick(click5)   # 검색결과 더블 클릭

      pyautogui.click(click6)         # 지급 일자의 날짜 클릭
      pyautogui.click(click7)         # Today 클릭

      pyautogui.hotkey('tab')
      type_kor(location_1)

      pyautogui.hotkey('tab')
      type_kor(location_2)

      pyautogui.hotkey('tab')
      type_kor(location_3)

      pyautogui.hotkey('tab')
      type_kor(location_4)

      pyautogui.hotkey('tab')  
      type_kor(state1)

      pyautogui.hotkey('tab')  
      type_kor(state2)

      pyautogui.hotkey('tab')   
      type_kor(state3)

      pyautogui.hotkey('tab')  
      type_kor(state4)

      pyautogui.hotkey('tab')   
      type_kor(etc1)

      pyautogui.hotkey('tab')   
      type_kor(etc2)

      pyautogui.hotkey('tab') 
      pyautogui.hotkey('tab')
      pyautogui.hotkey('tab')
      type_kor(today)

      pyautogui.hotkey('tab')
      type_kor(comment)

      pyautogui.click(click8)
      pyautogui.click(click9)
      pyautogui.hotkey('enter')
      pyautogui.hotkey('enter')
      pyautogui.hotkey('alt', 'tab')





