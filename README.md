# Скрипт для обработки логов

## Запуск приложения

### Параметры
--file - файл с логами для обработки. Можно загрузить несколько файлов через пробел
--report - название файла, в который будут загружена статистика. По умолчанию `your_file.txt`
--date - выбор логов с конкретной датой. Можно задать диапазон записав две даты через пробел.

### Запуск скрипта
```bush
python main.py --file your_logs.log your_logs2.log --report my_report.txt
```
### Запуск c диапазоном дат
```bush
python main.py --file your_logs.log your_logs2.log --report my_report.txt --date 1337-05-24 1453-10-19
```
Пример работы скрипта
<img width="1255" height="224" alt="image" src="https://github.com/user-attachments/assets/8d41d4ac-36c5-4fde-b7b6-e5404e724060" />

Пример работы с фильтром по дате
<img width="1444" height="226" alt="image" src="https://github.com/user-attachments/assets/f99b00f9-b62d-4ce3-9e01-ad79fdeb8142" />

Пример работы с фильтром по диапазону дат
<img width="1540" height="227" alt="image" src="https://github.com/user-attachments/assets/c9fd4a9c-55e5-497f-9bf1-230b52e0f6ce" />

Покрытие тестами  
<img width="308" height="152" alt="изображение_2025-08-02_220704399" src="https://github.com/user-attachments/assets/50a90d72-4e20-40fb-a393-cb8029ddfeff" />
