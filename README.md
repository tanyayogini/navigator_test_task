# navigator_test_task
Кушнарева Татьяна

Тестовое задание Python

Реализовать сервис, который принимает и отвечает на HTTP запросы.

# Функционал:

* В случае успешной обработки сервис должен отвечать статусом 200, в случае любой ошибки — статус 400.
* Сохранение всех объектов в базе данных.
* Запросы:

  GET /city/ — получение всех городов из базы;

  GET /city/street/ — получение всех улиц города;(city_id — идентификатор города)
  
  POST /shop/ — создание магазина; Данный метод получает json c объектом магазина, в ответ возвращает id созданной записи.

  GET /shop/?street=&city=&open=0/1 — получение списка магазинов; Метод принимает параметры для фильтрации. Параметры не обязательны. В случае отсутствия
параметров выводятся все магазины, если хоть один параметр есть, то по нему выполняется фильтрация.

  Важно!: в объекте каждого магазина выводится название города и улицы, а не id записей.

  Параметр open: 0 - закрыт, 1 - открыт. Данный статус определяется исходя из параметров «Время открытия», «Время закрытия» и текущего времени сервера.

* Объекты:

* Магазин:
  - Название
  - Город
  - Улица
  - Дом
  - Время открытия
  - Время закрытия
* Город:
  - Название
* Улица:
  - Название
  - Город
    
!! Замечание: поле id у объектов не указаны, но подразумевается что они есть.
!! Важно: Выстроить связи между таблицами в базе данных.

# Запуск
* клонировать репозиторий
* заполнить файл .env (см. env.example)
* ввести команду `docker-compose up`
* доступные эндпойнты:
  - http://127.0.0.1:8000/city/
  - http://127.0.0.1:8000/city/<city_id>/street/
  - http://127.0.0.1:8000/shop/
* для создания возможности отслеживать режим работы магазинов в разных городах относительно времени сервера, к модели города добавлено поле с часовым поясом

# Тесты
* установить зависимость `pip install -r requirements.txt'
* ввести команду `pytest`
