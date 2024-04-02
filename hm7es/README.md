# 7 ES

## Описание/Пошаговая инструкция выполнения домашнего задания:
> - Развернуть Instance ES – желательно в AWS
> - Создать в ES индекс, в нём должно быть обязательное поле text типа string
> - Создать для индекса pattern
> - Добавить в индекс как минимум 3 документа желательно со следующим содержанием:
    «моя мама мыла посуду а кот жевал сосиски»,
    «рама была отмыта и вылизана котом»,
    «мама мыла раму»
> - Написать запрос нечеткого поиска к этой коллекции документов ко ключу «мама ела сосиски»


## Создаем индекс, добавляем данные, осуществляем поиск
```sh
-- делаем индекс
PUT /otus_es
{
  "mappings": {
    "properties": {
      "title": { "type": "text" },
      "content": { "type": "text" }
    }
  }
}

{
  "acknowledged": true,
  "shards_acknowledged": true,
  "index": "otus_es"
}

-- создаем для индекса pattern

-- добавляем данные в индекс
POST /otus_es/_doc/
{
  "title": "Первая запись",
  "content": "моя мама мыла посуду а кот жевал сосиски"
}

{
  "_index": "otus_es",
  "_id": "49mStIwBV3-N4v5EJX2d",
  "_version": 1,
  "result": "created",
  "_shards": {
    "total": 2,
    "successful": 1,
    "failed": 0
  },
  "_seq_no": 0,
  "_primary_term": 1
}

POST /otus_es/_doc/
{
  "title": "Вторая запись",
  "content": "рама была отмыта и вылизана котом"
}

{
  "_index": "otus_es",
  "_id": "5NmTtIwBV3-N4v5EvX0y",
  "_version": 1,
  "result": "created",
  "_shards": {
    "total": 2,
    "successful": 1,
    "failed": 0
  },
  "_seq_no": 1,
  "_primary_term": 1
}

POST /otus_es/_doc/
{
  "title": "Третья запись",
  "content": "мама мыла раму"
}

{
  "_index": "otus_es",
  "_id": "5dmUtIwBV3-N4v5EFX2-",
  "_version": 1,
  "result": "created",
  "_shards": {
    "total": 2,
    "successful": 1,
    "failed": 0
  },
  "_seq_no": 2,
  "_primary_term": 1
}

-- поисковый запрос
GET /otus_es/_search
{
  "query": {
    "match": {
      "content": 
        "мама ела сосиски"
    }
  }
}

{
  "took": 1,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 2,
      "relation": "eq"
    },
    "max_score": 1.241674,
    "hits": [
      {
        "_index": "otus_es",
        "_id": "49mStIwBV3-N4v5EJX2d",
        "_score": 1.241674,
        "_source": {
          "title": "Первая запись",
          "content": "моя мама мыла посуду а кот жевал сосиски"
        }
      },
      {
        "_index": "otus_es",
        "_id": "5dmUtIwBV3-N4v5EFX2-",
        "_score": 0.5820575,
        "_source": {
          "title": "Третья запись",
          "content": "мама мыла раму"
        }
      }
    ]
  }

```