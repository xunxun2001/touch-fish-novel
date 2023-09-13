import re
import random
import time

LOG_LEVELS = ["INFO", "DEBUG", "WARN", "ERROR"]

def fake_log():
    log_level = random.choice(LOG_LEVELS)
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    messages = [
        "Starting process...",
        "Fetching data from server...",
        "Service initialized.",
        "Connection established.",
        "Loading configuration...",
        "Authentication successful."
    ]
    message = random.choice(messages)
    print(f"[{timestamp}] [{log_level}] {message}")

def show_content_with_log(chapter, page=0):
    # Display a fake log before the content
    fake_log()
    time.sleep(random.uniform(0.2, 0.6))  # Random delay

    show_content(chapter, page)

    # Display a fake log after the content
    time.sleep(random.uniform(0.2, 0.6))  # Random delay
    fake_log()

'''
import keyboard

def get_user_input():
    print("\n按 'n' 翻到下一页, 'p' 翻到上一页, 'l' 显示章节列表或直接输入章节编号并按 'Enter'：")
    while True:
        if keyboard.is_pressed('n'):
            return 'next'
        elif keyboard.is_pressed('p'):
            return 'prev'
        elif keyboard.is_pressed('l'):
            return 'list'
        elif keyboard.is_pressed('\n'):
            return input()  # 读取用户输入的章节编号

'''


def parse_chapters(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    chapter_pattern = r'第([0-9零一二两三四五六七八九十百千万亿]+)章\s+[^\n]+' #更普遍地匹配任意空格（包括全角和半角）

    chapter_titles = [match.group() for match in re.finditer(chapter_pattern, content)]

    # 切分章节内容
    chapter_positions = [match.start() for match in re.finditer(chapter_pattern, content)]
    chapter_positions.append(len(content))
    chapters_content = [content[chapter_positions[i]:chapter_positions[i + 1]] for i in
                        range(len(chapter_positions) - 1)]

    return list(zip(chapter_titles, chapters_content))


def show_chapters(chapters):
    for idx, (title, _) in enumerate(chapters):
        print(f"{idx + 1}. {title}")



def show_content(chapter, page=0):
    _, content_section = chapter
    pages = [content_section[i:i + 500] for i in range(0, len(content_section), 500)]

    if page >= len(pages):
        print("已经是最后一页了。")
        return page

    if page < 0:
        print("已经是第一页了。")
        return 0

    print(pages[page])
    return page


def get_user_input():
    return input("\n请选择章节编号或使用'next'/'prev'翻页: ")


def main():
    filename = "万相之王.txt"
    chapters = parse_chapters(filename)
    current_chapter = 0
    current_page = 0

    while True:
        user_input = get_user_input()

        if user_input == 'next':
            current_page += 1
            current_page = show_content_with_log(chapters[current_chapter], current_page)
        elif user_input == 'prev':
            current_page -= 1
            current_page = show_content_with_log(chapters[current_chapter], current_page)
        elif user_input == 'list' or user_input == 'chapters':
            show_chapters(chapters)
        elif user_input.isdigit():
            selected_chapter = int(user_input) - 1
            if 0 <= selected_chapter < len(chapters):
                current_chapter = selected_chapter
                current_page = 0
                show_content_with_log(chapters[current_chapter], current_page)
            else:
                print("无效的章节编号，请重试。")
        else:
            print("无效的输入，请重试。")



def get_user_input():
    return input("\n输入章节编号、'next'/'prev'翻页或 'list' 显示章节列表: ")


if __name__ == "__main__":
    main()
