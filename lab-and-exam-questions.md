### Zagadnienia praktyczne z przedmiotu "Integracja systemów informatycznych"

#### I. Git
1. Utwórz nową gałąź (np. `nowa`) z bieżącej (najczęściej będzie to `main`), stwórz w nowej gałęzi nowy plik i zmerguj nową gałąź do bieżącej.
2. Pokaż jak działa `pull request` na jednym ze swoich repozytoriów.
3. Omów różnicę między `git fetch` a `git pull` na przykładzie swojego repozytorium.
4. Pokaż działanie `git stash`.
5. Pokaż działanie `git rebase` i omów róznicę w stosunku do `git merge`.

#### II. Bazy danych
1. Za pomocą skryptu w wybranym języku dodaj kolejny rekord do wskazanej bazy danych.
2. Dla wybranej bazy danych pokaż działanie co najmniej tzech różnych typów JOIN'a.
3. Zaloguj się do bazy danych PostgreSQL w kontenerze Dockerowym i wykonaj operację `SELECT` dla dowolnej tabeli.
4. Wskaż różnice między SQLite a PostgreSQL.
5. Przygotuj zapytania zawierające polecenia `WHERE`, `LIKE`, `COUNT`, `GROUP BY`, `HAVING` i bądz gotowy do ich uruchomienia i modyfikacji.

#### III. Aplikacja wg wzorca projektowego MVC (Model-View-Controller)
1. Czym jest ORM, omów na przykładzie własnego projektu? 
2. Czym jest wzorzec MVC, wskaż w kodzie aplikacji poszczególne elementy tego wzorca i określ ich role.
3. Dodaj nowy URL w aplikacji i spraw, aby po uruchomieniu go w przeglądarce pojawiło się Twoje imię i nazwisko.
4. Dodaj nowy URL w aplikacji i spraw, aby po uruchomieniu go w przeglądarce pojawił się formularz, który pozwala dodać dwie liczby.
5. Dodaj nowe pole w wybranym modelu i przeprowadź proces migracji.

#### IV. Docker
1. Utwórz plik z obrazem `Dockerfile`, w którym z hosta do kontenera kopiowany będzie folder `code` (zawiera jeden skrypt w języku Python) i zbuduj go:  
    - uruchom ww. skrypt wewnątrz kontenera.
2. Skopiuj wybrany plik tekstowy z hosta (swojego komputera) do kontenera Dockerowego.
3. Skopiuj wybrany plik tekstowy z kontenera Dockerowego do hosta (swojego komputera).
4. Pokaż użycie komend `ENTRYPOINT` i `CMD`.
5. Pokaż użycie komend `ADD` i `COPY` i `WORKDIR`.
6. Pokaż działanie `docker compose`.
7. Omów na podstawie swojej aplikacji komendy `docker inspect` i `docker logs`.
8. Czym sa sieci w Dockerze?

#### V. Programowanie
1. Przygotuj klasę `Kalkulator` z czterema wybranymi działaniami matematycznymi (jako metody) i bądź gotowy do utworenia obiektów i modyfikacji tejże klasy.
