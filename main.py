import argparse
import json
from datetime import datetime
import os

from tabulate import tabulate


def open_log(log_files):
    """Читает файлы с логами и объединяет в один массив строк"""
    whole_logs = []
    for log_file in log_files:
        with open(log_file, 'r', encoding='utf-8') as file:
            logs = file.readlines()
        whole_logs += logs
    return whole_logs


def check_log_file(log_files):
    """Проверка возможности открытия файла с логами"""
    if not log_files:
        print("Please enter the name of the file(s)")
        return False

    for file in log_files:
        if not os.path.exists(file):
            print(f"File {file} does not exist")
            return False
        if os.path.isdir(file):
            print(f"Error: {file} is a directory. Please specify files only")
            return False
    return True


def save_statistic(log_stat, name):
    """Сохранение полученной статистики"""
    with open(name, 'w', encoding='utf-8') as file:
        for line in log_stat:
            file.write(str(line) + "\n")


def check_date(date):
    """Проверка корректности введённой даты"""
    if date is None or not date:
        return True

    if len(date) > 2:
        print("Too many arguments for --date, 1 or 2 are acceptable")
        return False

    for i, x in enumerate(date):
        try:
            if len(x.split('-')[0]) != 4:   # Если год по знакам меньше 4, то добавить в начало недостающие 0
                x = (4 -len(x.split('-')[0]))*'0' + x
                date[i] = x

            datetime.strptime(x, "%Y-%m-%d")
        except Exception as e:
            print(e)
            return False

    if len(date) == 2:
        if datetime.strptime(date[1], "%Y-%m-%d") < datetime.strptime(date[0], "%Y-%m-%d"):
            print(f"The second --date argument '{date[1]}' cannot be lower than the first '{date[0]}'")
            return False

    return True

def get_stat(logs, date):
    """Расчёт статистики логов"""
    dct = {}

    for log in logs:

        line = json.loads(log)
        timestamp = line['@timestamp']
        url = line['url']
        response_time = line['response_time']

        if date:
            if len(date) == 1 and date[0] == timestamp[:10]:
                dct[url] = dct.get(url, []) + [response_time]
            if len(date) == 2:
                log_date = datetime.strptime(timestamp[:10], "%Y-%m-%d")
                start_date = datetime.strptime(date[0], "%Y-%m-%d")
                end_date = datetime.strptime(date[1], "%Y-%m-%d")
                if start_date <= log_date <= end_date:
                    dct.setdefault(url, []).append(response_time)
        else:
            dct[url] = dct.get(url, []) + [response_time]

    stats = [
        {
            "handler": url,
            "total": len(times),
            "avg_response_time": round(sum(times) / len(times), 3)
        }
        for url, times in dct.items()
    ]

    stats = sorted(stats, key=lambda x: list(x.values())[2], reverse=True) # Сортировка по 'avg_response_time'
    stats = sorted(stats, key=lambda x: list(x.values())[1], reverse=True) # Сортировка по 'total'

    return stats

def main():
    parser = argparse.ArgumentParser(description='get log statistics')
    parser.add_argument('--file', nargs='*', type=str, help='input log files')
    parser.add_argument('--report', type=str, default='your_file.txt', help='report name')
    parser.add_argument('--date', nargs='*', type=str, help='search by specific date in format YYYY-MM-DD')
    args = parser.parse_args()

    if not check_log_file(args.file):
        return 0

    if not check_date(args.date):
        return 0

    logs = open_log(args.file)
    stats = get_stat(logs, args.date)

    save_statistic(stats, args.report)
    
    print(tabulate(stats, headers='keys', showindex="always"))

if __name__ == '__main__':
    main()