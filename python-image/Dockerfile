# 使用官方的 Python 基礎鏡像
FROM python:3.9-slim

# 設置工作目錄
WORKDIR /app

# 安裝 Git
RUN apt-get update && apt-get install -y git

# 複製 requirements.txt 文件並安裝依賴
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

# 複製應用程式的代碼到容器中
COPY . /app/

# 設置默認的啟動命令為 bash，以便於進入容器後手動運行命令
CMD ["bash"]
