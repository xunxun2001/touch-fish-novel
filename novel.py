import re
import random
import time
#import keyboard
import signal


class NovelReader:
    LOG_LEVELS = ["INFO", "DEBUG", "WARN", "ERROR"]
    MAX_LINES_PER_PAGE = 50 #  设定每页的最大行数

    def __init__(self, filename):
        self.filename = filename  # 存储提供的文件名，以便后续使用
        self.chapters = self.parse_chapters(filename)  # 解析文件，获取章节内容列表
        self.current_chapter = 0  # 初始化当前章节的索引为0，表示从第一章开始
        self.current_page = 0  # 初始化当前页的索引为0，表示从每一章的第一页开始
        signal.signal(signal.SIGINT, self.handler)  # 设置信号处理器，以便在程序接收到中断信号时，执行特定的处理函数

    def handler(self, signum, frame):
        """
        处理接收到的信号，用于程序的优雅退出。

        当程序接收到一个中断信号（例如，用户按下 Ctrl+C）时，此方法会被调用。
        它首先调用 exit_logs() 方法，输出关闭程序的日志，然后通知用户程序正在优雅地退出。
        最后，它确保程序完全退出。

        :param signum:接收到的信号的标识符
        :param frame:当前栈帧对象
        """
        self.exit_logs()
        print("\nUser terminated. Exiting gracefully...")
        exit(0)

    def exit_logs(self):
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

    def fake_log(self):
        log_level = random.choice(self.LOG_LEVELS)
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

    def get_total_pages(self, chapter):
        '''
        :param chapter: 要计算页数的章节内容字符串
        :return: 该章节的总页数
        '''
        return -(-len(chapter.split('\n')) // self.MAX_LINES_PER_PAGE) # 向上取整计算总页数

    def show_content_with_log(chapter, page=0):
        '''
        显示指定章节的内容，并在内容中插入伪装日志。

        此函数会首先计算章节的总页数，然后显示当前的页码和总页数。
        接着，它会将章节内容分成多行，并在其中随机插入伪装日志，以模拟真实的日志输出场景。
        在章节内容的开始和结束部分，还会显示多条伪装日志，增加真实感。

        :param page:要显示的页码，默认为0
        :return:返回当前页码，供后续操作使用
        '''
        total_pages = chapter.get_total_pages(chapter[1])
        # Display the page number and total pages
        print(f"\n---  Page {page + 1}/{total_pages}  ---\n")

        # 将章节内容分为行
        lines = chapter[1].split('\n')
        num_lines = len(lines)

        # 确定在哪些行后插入伪装日志
        log_positions = random.sample(range(1, num_lines), 9)  # 随机选3个位置插入日志，可根据需要调整
        log_positions.sort()

        # Display multiple fake logs at the beginning
        for _ in range(random.randint(5, 15)):
            chapter.fake_log()
            time.sleep(random.uniform(0.1, 0.3))

        # 打印小说内容，并在特定位置插入日志
        for i, line in enumerate(lines):
            print(line)
            if i in log_positions:
                chapter.fake_log()
                time.sleep(random.uniform(0.2, 0.6))

        # Display multiple fake logs at the end
        for _ in range(random.randint(5, 15)):
            time.sleep(random.uniform(0.1, 0.3))
            chapter.fake_log()

        # 返回页码，如果需要的话
        return page



    def parse_chapters(filename):
        '''
        解析给定文件中的章节，并返回章节标题与其对应的内容。

        此函数首先打开指定的文件，并读取其全部内容。然后，使用正则表达式匹配章节标题。
        每一个匹配到的章节标题后面的文本内容都被视为该章节的内容，直到下一个章节标题出现为止。

        :param: chapters：一个包含章节标题和内容的元组
        :param: filename: 要解析的文本文件的路径
        :return:返回一个列表，其中每个元素是一个元组，元组的第一个元素是章节标题，第二个元素是该章节的内容。
        '''
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

    def get_user_input(self):
        return input("\n输入章节编号、'next'/'prev'翻页、'list' 显示章节列表或 'q' 退出: ")

    def run(self):
        while True:
            user_input = self.get_user_input()

            if user_input == 'next':
                self.current_page += 1
                self.current_page = self.show_content_with_log(
                    self.chapters[self.current_chapter], self.current_page)
            elif user_input == 'prev':
                self.current_page -= 1
                self.current_page = self.show_content_with_log(
                    self.chapters[self.current_chapter], self.current_page)
            elif user_input == 'list':
                self.show_chapters()
            elif user_input.isdigit():
                selected_chapter = int(user_input) - 1
                if 0 <= selected_chapter < len(self.chapters):
                    self.current_chapter = selected_chapter
                    self.current_page = 0
                    self.show_content_with_log(
                        self.chapters[self.current_chapter], self.current_page)
                else:
                    print("无效的章节编号，请重试。")
            elif user_input == 'q':
                self.exit_logs()
                break
            else:
                print("无效的输入，请重试。")


if __name__ == "__main__":
    reader = NovelReader("./test/万相之王.txt")
    reader.run()
