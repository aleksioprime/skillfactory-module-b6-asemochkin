# skillfactory-module-b6-asemochkin
Домашнее задание "Веб-сервер на Python"

В рамках задачи реализован основной модуль albums_server.py, который создаёт локальный веб-сервер, и вспомагательный модуль album.py, в который вынесены классы и функции для работы с базой данных albums.sqlite3

Для тестирования функции вывода на экран сообщения с количеством альбомов исполнителя artist и списком названий этих альбомов можно запустить файл albums_server.py через интерпретатор python и ввести в адресную строку браузера такие команды, как например:

http://localhost:8080/albums/Pink Floyd
http://localhost:8080/albums/Queen
http://localhost:8080/albums/The Rolling Stones

Для тестирования функции сохранения переданых пользователем данных об альбоме в формате веб-формы в базу данных можно при запущенном скрипте albums_server.py ввести в командную строку (при условии, что в окружении установлена утилита httpie) такие команды, как:

http -f POST http://localhost:8080/albums year="2010" artist="New Artist" genre="Rock" album="Super" (команда добавит запись в базу данных)
http -f POST http://localhost:8080/albums year="2021" artist="Sun and Moon" genre="Pop" album="Queen" (команда вызовет ошибку 409, так как такой альбом уже существует)
http -f POST http://localhost:8080/albums year="1990год" artist="Green Weeks" genre="Rock" album="Red" (команда вызовет исключение 400 - "Некорректные параметры года")
