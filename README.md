Json api каталога книг 

Вся информация хранитсяв базе данных: 

Таблица books (id, title, published_year, author_id,genre, rating) 

Таблица authors (id, name) 

Api endpoints:
GET /books возвращает список книг
GET /authors возвращает список авторов
GET /books/top возвращает 10 книг с наивысшим rating 
GET /books/year? реализован поиск книг по годам в /books с помощью кнопки Filters в APIView
GET /authors/top возвращает 10 авторов опубликовавшихнаибольшее количество книг 
GET /genres возвращает список жанров и количествокниг в каждом жанре 
GET /find_by_authors? реализована в authros/ с помощью того же Filters по id автора в APIView

DELETE /books/{book_id} делает soft delete книгис id = book_id 
DELETE /authors/{author_id} soft delete авторов по их id
