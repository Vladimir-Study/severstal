# Данный репозиторий является тестовым заданием

Цель задания создать 2 потока:  
1. Первый из которых обработывает набор фотографий расположенных по пути: ***./src/images***, получает их размер в байтах и складывает в очередь **Redis**.
2. Получает данные из очереди **Redis** и записывае в базу данных два поля, ***вермя записи*** и ***размер файл в байтах***  

Код таблицы:

```
CREATE TABLE images (Id SERIAL PRIMARY KEY, time_write TIMESTAMP DEFAULT CURRENT_TIMESTAMP, size_images INTEGER NOT NULL);
```