from notion.client import NotionClient
from notion.block import ImageBlock
import datetime
import threading
import pyautogui
from key_code import MY_TOKEN, MY_PAGE_URL


# 로그인 (MY_TOKEN = 어플리케이션에서 노션의 세션 정보)
client = NotionClient(token_v2=MY_TOKEN)

# 현재 페이지 (MY_PAGE_URL = 노션 데이터베이스 페이지)
page = client.get_block(MY_PAGE_URL)
print("페이지 제목:", page.title)

# 시간 간격(초)
TIME_INTERVAL = 900

# 현재 페이지(테이블)에 자동으로 행 추가
def auto_add_table_row():
    # 현재 시각
    now = datetime.datetime.now()
    time_now = f"{now.month}_{now.day}_{now.hour}_{now.minute}_{now.second}"
    print(now)
    # 테이블에 새로운 행 생성, 제목 및 프로퍼티 할당
    add_table_row = page.collection.add_row()
    add_table_row.set_property("title", "나는 이 시각에 뭘 했을까?")
    add_table_row.set_property("Tags", ["자동생성"])
    # 현재 화면 스크린샷
    pyautogui.screenshot(
        f"C:/notion_auto_adder/screenshots/{time_now}.png"
    )  # 현재 스크린 저장
    screenshot = add_table_row.children.add_new(ImageBlock)  # 이미지 블록 생성
    screenshot.upload_file(
        f"C:/notion_auto_adder/screenshots/{time_now}.png"
    )  # 로컬에 저장된 스크린샷 업로드
    threading.Timer(TIME_INTERVAL, auto_add_table_row).start()  # 일정 시간 간격으로 반복 실행


auto_add_table_row()