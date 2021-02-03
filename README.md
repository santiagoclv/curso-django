# [Django for Everybody Specialization](https://www.coursera.org/specializations/django)

```
docker build -t django-playground .

```

```
docker run -it --rm --name ai django-playground

```

```

docker image rm django-playground

```


## create django project 
```
django-admin startproject [site-name]
```

## run server on development mode 
```
python manage.py runserver [ip|0]:[PORT|8000]
```

## add app to the project
```
python manage.py startapp polls
```

## make migrations files from modules
```
python manage.py makemigrations
```

## deploy migrations
```
python manage.py migrate
```

## Run scripts
```
python manage.py runscript cats_load
```