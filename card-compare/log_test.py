log_file_path = 'app.log'

with open(log_file_path, 'r') as file:
    log_content = file.read()

# 打印 .log 檔案的內容
print(log_content)
