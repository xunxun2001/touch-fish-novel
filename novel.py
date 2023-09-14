import re
import random
import time
#import keyboard

LOG_LEVELS = ["INFO", "DEBUG", "WARN", "ERROR"]
def exit_logs():
    messages = [
        "Commencing detailed shutdown sequence...",
        "Running pre-shutdown diagnostics...",
        "Backing up current session's configurations and settings...",
        "Releasing all active database connections. Closing database 'MainDB'...",
        "Releasing secondary database connections from 'AnalyticsDB'...",
        "Sending safe shutdown signals to all external APIs...",
        "Flushing any pending logs to persistent storage. Ensuring no data loss...",
        "Terminating and joining active threads. Total threads active: 37...",
        "Sending stop signals to all microservices. Waiting for graceful terminations...",
        "Closing all open file handles associated with modules 'DataProc', 'NetCore'...",
        "Shutting down background workers. Workers active: 8...",
        "Clearing cache and buffers from memory region '0x4F0000' to '0xAF12FF'...",
        "Releasing network resources. Disconnecting from IP '192.168.0.102'...",
        "Closing active socket connections. Sockets open: 23...",
        "Sending termination signals to all connected clients. Clients active: 3...",
        "Running garbage collection and ensuring optimal memory deallocation...",
        "Ensuring all file I/O operations are complete. Waiting for confirmations...",
        "Disconnecting from external services: 'AuthService', 'FileStoreAPI'...",
        "Finalizing the shutdown sequence. Storing states and user data...",
        "Creating a compressed archive of this session's logs...",
        "Sending shutdown reports to monitoring services 'MonitX', 'GuardStat'...",
        "Stopping all scheduled tasks. Deactivating cron job 'auto_backup.sh'...",
        "Running final audit and security checks...",
        "Cleaning up and removing all temporary directories from '/tmp/', '/app/cache/'...",
        "Unbinding from all network ports and releasing IP reservations...",
        "Releasing all OS-level resources. Sending shutdown signal to system...",
        "Notifying all dependent services and parent systems. Awaiting acknowledgments...",
        "Final checks: memory integrity check, disk space check, network report...",
        "Program ready to terminate. Initiating countdown...",
        "Shutdown in 5 seconds...",
        "Shutdown in 4 seconds...",
        "Shutdown in 3 seconds...",
        "Shutdown in 2 seconds...",
        "Shutdown in 1 second...",
        "Program has been successfully terminated. Goodbye!"
    ]

    for message in messages:
        log_level = "INFO"
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print(f"[{timestamp}] [{log_level}] {message}")
        time.sleep(random.uniform(0.1, 0.3))


def fake_log():
    log_level = random.choice(LOG_LEVELS)
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    messages = [
        "Initializing secure connection to the server at address 192.168.0.102:5000...",
        "Fetching data from remote endpoint: /api/v2/fetch with headers {'User-Agent': 'CLI-Tool/1.0'}...",
        "Received 200 OK from server after 142ms. Processing payload and mapping to internal structures...",
        "Starting background task with ID #283728, expected to run for approximately 180 seconds...",
        "Service successfully initialized. Listening on port 8080 with available threads: 8...",
        "Successfully established connection with remote IP: 192.168.0.105 on port 3762. Encrypting using TLSv1.3...",
        "Reading configuration data from /etc/config.json and merging with environment variables...",
        "Authentication handshake successful. Generated token: 8f7328f7-a6ad-48d0-b271-5d475283a1b2, expires in 3600s...",
        "Database connection established using driver pgsql. Querying table: users with SELECT * LIMIT 100...",
        "Task with ID #283728 completed successfully after 162.5 seconds. Cleaning up resources and archiving logs...",
        "Received signal: SIGTERM from process PID 872. Preparing to shut down gracefully after finalizing 3 pending tasks...",
        "Writing audit logs to /var/log/audit.log. Total entries written: 3842. Backup to S3 bucket initiated..."
    ]
    message = random.choice(messages)
    print(f"[{timestamp}] [{log_level}] {message}")

def show_content_with_log(chapter, page=0):
    total_pages = get_total_pages(chapter[1])

    # Display the page number and total pages
    print(f"\n---  Page {page + 1}/{total_pages}  ---\n")

    # 将章节内容分为行
    lines = chapter[1].split('\n')
    num_lines = len(lines)

    # 确定在哪些行后插入伪装日志
    log_positions = random.sample(range(1, num_lines), 3)  # 随机选3个位置插入日志，可根据需要调整
    log_positions.sort()

    # Display multiple fake logs at the beginning
    for _ in range(random.randint(5, 15)):
        fake_log()
        time.sleep(random.uniform(0.1, 0.3))

    # 打印小说内容，并在特定位置插入日志
    for i, line in enumerate(lines):
        print(line)
        if i in log_positions:
            fake_log()
            time.sleep(random.uniform(0.2, 0.6))

    # Display multiple fake logs at the end
    for _ in range(random.randint(5, 15)):
        time.sleep(random.uniform(0.1, 0.3))
        fake_log()

    # 返回页码，如果需要的话
    return page




# def get_user_input():
#     print("\n按 'n' 翻到下一页, 'p' 翻到上一页, 'l' 显示章节列表或直接输入章节编号并按 'Enter'：")
#     while True:
#         if keyboard.is_pressed('n'):
#             return 'next'
#         elif keyboard.is_pressed('p'):
#             return 'prev'
#         elif keyboard.is_pressed('l'):
#             return 'list'
#         elif keyboard.is_pressed('\n'):
#             return input()  # 读取用户输入的章节编号



MAX_LINES_PER_PAGE = 50  # 设定每页的最大行数

def get_total_pages(chapter):
    # 根据章节内容和每页的最大行数来计算总页数
    return -(-len(chapter.split('\n')) // MAX_LINES_PER_PAGE)  # 向上取整计算总页数

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



def main():
    filename = "./test/万相之王.txt"
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
        elif user_input == 'q':
            exit_logs()
            break
        else:
            print("无效的输入，请重试。")




def get_user_input():
    return input("\n输入章节编号、'next'/'prev'翻页、'list' 显示章节列表或 'q' 退出: ")



if __name__ == "__main__":
    main()
