Json api каталога книг. 
Вся информация хранитсяв базе данных:* 
Таблица books (id, title, published_year, author_id,genre, rating)* 
Таблица authors (id, name)Api endpoints:* 
GET /books возвращает список книг* 
GET /authors возвращает список авторов* 
GET /books/top возвращает 10 книг с наивысшим rating* 
GET /books/year?from=<year_from>&to=<year_to> возвращаеткниги опубликованныемежду year_from и year_to* 
GET /authors/top возвращает 10 авторов опубликовавшихнаибольшее количество книг* 
GET /genres возвращает список жанров и количествокниг в каждом жанре* 
GET /find_by_authors?q=<authors_names> возвращаеткниги авторов, имена которыхбыли переданы в параметре authors_names. 
Книги в ответедолжны быть сгруппированыпо автору* 

DELETE /books/{book_id} делает soft delete книгис id = book_id. 
Запись из базы данныхне удаляется, но все остальные API методы должны думать,что этой записи больше нет.* 
DELETE /authors/{author_id} soft delete авторовпо аналогии с книгами
