import json
from bottle import route, run, HTTPError, request

import album

# Для тестирования функции просмотра альбомов после запуска скрипта введите в адресной строке браузера:
# http://localhost:8080/albums/Pink Floyd
# http://localhost:8080/albums/Queen
@route("/albums/<artist>")
def view_albums(artist):
    """ Возвращает список альбомов исполнителя, имя которого передано с помощью GET-запроса"""
    albums_list = album.find(artist)
    if not albums_list:
        message = "Альбомов исполнителя {} не найдено".format(artist)
        return HTTPError(400, message)
    else:
        album_names = [album.album for album in albums_list]
        result = "<h3>У исполнителя <b>{}</b> найдено <b>{}</b> альбомов</h3>".format(artist, len(albums_list))
        result += "<p>"+"; <br>".join(album_names)+"</p>"
        return result


# Для тестирования функции добавления альбома в БД после запуска скрипта введие в командой строке (при наличии httpie):
# http -f POST http://localhost:8080/albums year="2010" artist="New Artist" genre="Rock" album="Super"
# http -f POST http://localhost:8080/albums year="2021" artist="Sun and Moon" genre="Pop" album="Queen"
# http -f POST http://localhost:8080/albums year="1990год" artist="Green Weeks" genre="Rock" album="Red"
@route("/albums", method="POST")
def add_album():
    """ Добавляет исполнителя и его альбом с годом выпуска и жанром в БД с помощью POST-запроса"""
    albums_data = {
        "artist": request.forms.get("artist"),
        "genre": request.forms.get("genre"),
        "album": request.forms.get("album"),
    }
    try:
        albums_data['year'] = int(request.forms.get("year"))
        if albums_data['year'] < 1900 or albums_data['year'] > 2021: 
            raise ValueError()
    except ValueError:
        return HTTPError(400, "Некорректные параметры года")
    else:
        if albums_data["artist"] or albums_data["genre"] or albums_data["album"]:
            return HTTPError(400, "Поля не должны быть пустыми")
        if album.album_in_base(albums_data["album"]):
            message = "Альбом {} уже существует в базе".format(albums_data["album"])
            result = HTTPError(409, message)
            return result
        else:
            new_album = album.request(albums_data)
            return "Данные об альбоме {} успешно сохранены".format(new_album.album)

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)
