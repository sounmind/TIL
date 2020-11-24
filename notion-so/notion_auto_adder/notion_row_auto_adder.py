from notion.client import NotionClient
from notion.block import ImageBlock
from desktopmagic.screengrab_win32 import getScreenAsImage
import datetime
import threading
from key_code import MY_TOKEN, MY_PAGE_URL
import random

CLIENT = NotionClient(token_v2=MY_TOKEN)  # 로그인 정보 (MY_TOKEN = 어플리케이션에서 노션의 세션 정보)
NOTION_PAGE = CLIENT.get_block(
    MY_PAGE_URL
)  # 현재 페이지 정보 (MY_PAGE_URL = 노션 데이터베이스 페이지 주소)
print("페이지 제목:", NOTION_PAGE.title)
MAX_TIME_INTERVAL = 15
MIN_TIME_INTERVAL = 1


def get_time_now():
    now = datetime.datetime.now()
    return f"{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}_{now.second}"


def save_screenshot_local(path):
    getScreenAsImage().save(path, format="png")


def upload_screenshot_notion(parent_page, path):
    screenshot_block = parent_page.children.add_new(ImageBlock)  # 이미지 블록 생성
    screenshot_block.upload_file(path)  # 로컬에 저장된 스크린샷 업로드


def add_table_row():  # 테이블에 새로운 행 생성, 제목 및 프로퍼티 할당
    new_table_row = NOTION_PAGE.collection.add_row()
    new_table_row.set_property("title", "나는 이 시각에 뭘 했을까?")
    new_table_row.set_property("Tags", ["자동생성"])
    return new_table_row


def get_random_time():
    random_time = random.randrange(MIN_TIME_INTERVAL, MAX_TIME_INTERVAL)
    print("Time interval is", random_time)
    return random_time


def init():
    NOW = get_time_now()
    PATH = f"C:/notion_auto_adder/screenshots/{NOW}.png"
    new_row = add_table_row()
    save_screenshot_local(PATH)
    upload_screenshot_notion(new_row, PATH)
    print("Captured at", NOW)
    threading.Timer(get_random_time(), init).start()  # 일정 시간마다 반복


init()
