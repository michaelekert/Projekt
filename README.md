# Blogens elegancki 🅱️

Prosty szkielet blog'a napisany w framework'u Django

![blog](./images/blog.png)
![blog-kolejny](./images/blog1.png)

Aplikacja została napisana w 
- Python 3.9.5
- Django 3.2.4

## Instalacja i uruchamianie

Po sklonowaniu aplikacji z repozytorium użyj menadżera pakietów [pip](https://pip.pypa.io/en/stable/) do zainatalowania zależności aplikacji.

```bash
pip install -r requirements.txt
``` 

Nastepnie należy uruchomić środowisko wirtualne:  


### Linux & OS X

```bash
source venv/bin/activate
```
### Windows

```bash
venv\Scripts\activate
```

Kiedy mamy uruchomione środowisko uruchamiamy aplikacje poleceniem:

```bash
python manage.py runserver
```
W przeglądarce wpisujemy 

```bash
http://127.0.0.1:8000/
```

Po wprowadzeniu powinna ukazać się blog


## Użycie

Aby móc korzytać trzeba się zalogować na konto uzytkownika

* Nazwa użytkownika: Jan
* Hasło: ptakilatająkluczem

