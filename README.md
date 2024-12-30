Task Manager to aplikacja do zarządzania zadaniami, stworzona w języku Python. Projekt umożliwia użytkownikowi:
Dodawanie nowych zadań.
Usuwanie istniejących zadań.
Zarządzanie terminami i priorytetami.
Przechowywanie danych w bazie SQLite.

Aplikacja została zaprojektowana w dwóch wersjach:
<li>Wersja tekstowa (CLI - Command Line Interface): Lekka wersja działająca w terminalu.
<li>Wersja GUI (z interfejsem graficznym): Atrakcyjna wizualnie wersja zbudowana w frameworku Kivy.

Wersja tekstowa aplikacji to prosty program działający w terminalu. Użytkownik może wprowadzać polecenia za pomocą klawiatury, które umożliwiają zarządzanie zadaniami. Dane są przechowywane w lokalnej bazie danych SQLite.

<b>Funkcje</b>

<li>Dodawanie zadania: Użytkownik wprowadza nazwę, opis, priorytet i termin zadania.
<li>Wyświetlanie listy zadań: Program wypisuje listę wszystkich zadań z bazy danych.
<li>Usuwanie zadania: Użytkownik może usunąć zadanie, podając jego identyfikator.
  
<b>Technologie</b>

<li>Python: Główny język programowania.
<li>SQLite: Lokalna baza danych do przechowywania informacji o zadaniach.
  
Wersja z interfejsem graficznym została stworzona przy użyciu frameworku Kivy. Oferuje użytkownikowi bardziej przyjazny i intuicyjny sposób zarządzania zadaniami dzięki wizualnemu układowi elementów.

<b>Funkcje</b>

<li>Dodawanie zadania: Formularz z polami do wpisania nazwy, opisu i terminu.
<li>Wyświetlanie listy zadań: Lista zadań z możliwością przewijania.
<li>Usuwanie zadania: Przycisk "Usuń" obok każdego zadania.
  
<b>Technologie</b>
  
<li>Python: Główny język programowania.
<li>SQLite: Lokalna baza danych.
<li>Kivy: Framework do tworzenia interfejsów graficznych.

<b>Pliki projektu</b>

Wersja tekstowa:

task_manager.py – główny plik programu w wersji terminalowej.

database.py – moduł zarządzający połączeniem z bazą danych.

Wersja GUI:

task_manager_kivy.py – główny plik programu z interfejsem graficznym.

database.py – moduł zarządzający połączeniem z bazą danych.

task_manager_kivy.exe - plik programu możliwy do uruchomienia poprzez dwuklik.

