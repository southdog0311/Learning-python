import tracemalloc
import time
import psutil
import cProfile
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(name)s:%(lineno)d - %(message)s')
logger = logging.getLogger()

def compare_cards(card1, card2):
    valid_cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    
    if card1 not in valid_cards or card2 not in valid_cards:
        raise ValueError("Invalid card value")
    
    value1 = valid_cards[card1]
    value2 = valid_cards[card2]
    
    if value1 > value2:
        logger.info(f"{card1} is greater than {card2}")
        return card1
    elif value2 > value1:
        logger.info(f"{card2} is greater than {card1}")
        return card2
    else:
        logger.info(f"{card1} and {card2} are equal")
        return "Equal"

def main():
    start_time = time.time()
    cpu_start_time = time.process_time()
    
    # 獲取當前進程
    process = psutil.Process()
    
    # 獲取初始 CPU 和記憶體使用情況
    cpu_start = process.cpu_percent(interval=None)
    memory_start = process.memory_info().rss
    
    # 開始追蹤記憶體分配
    tracemalloc.start()
    
    # 執行你的程式碼
    result = compare_cards('K', 'Q')
    print(result)
    
    # 獲取最終 CPU 和記憶體使用情況
    cpu_end = process.cpu_percent(interval=None)
    memory_end = process.memory_info().rss
    
    end_time = time.time()
    cpu_end_time = time.process_time()
    
    # 獲取記憶體分配統計
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    # Log performance data
    logger.info(f"Execution time: {end_time - start_time} seconds")
    logger.info(f"CPU usage: {cpu_end - cpu_start}%")
    logger.info(f"Memory usage: {memory_end - memory_start} bytes")
    logger.info(f"Current memory usage: {current / 10**6} MB; Peak memory usage: {peak / 10**6} MB")
    logger.info(f"CPU time: {cpu_end_time - cpu_start_time} seconds")
    
    print(f"執行時間: {end_time - start_time} 秒")
    print(f"CPU 使用率: {cpu_end - cpu_start}%")
    print(f"記憶體使用量: {memory_end - memory_start} bytes")
    print(f"當前記憶體使用量: {current / 10**6} MB; 峰值記憶體使用量: {peak / 10**6} MB")
    print(f"CPU 時間: {cpu_end_time - cpu_start_time} 秒")

if __name__ == "__main__":
    cProfile.run('main()')
