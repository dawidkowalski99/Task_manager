import sqlite3

# Funkcja do tworzenia bazy danych i tabeli
def create_database():
    connection = sqlite3.connect('tasks.db')  # Łączy się lub tworzy bazę danych
    cursor = connection.cursor()
    # Tworzy tabelę tasks, jeśli jeszcze nie istnieje
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT,
            priority TEXT,
            due_date TEXT,
            completed BOOLEAN DEFAULT 0
        )
    ''')
    connection.commit()
    connection.close()

# Funkcja do dodawania nowego zadania do tabeli
def add_task(name, description, priority, due_date):
    connection = sqlite3.connect('tasks.db')  # Łączy się z bazą danych
    cursor = connection.cursor()
    # Dodaje nowe zadanie do tabeli
    cursor.execute('''
        INSERT INTO tasks (name, description, priority, due_date)
        VALUES (?, ?, ?, ?)
    ''', (name, description, priority, due_date))
    connection.commit()
    connection.close()

# Funkcja do pobierania wszystkich zadań z tabeli
def list_tasks():
    connection = sqlite3.connect('tasks.db')  # Łączy się z bazą danych
    cursor = connection.cursor()
    # Pobiera wszystkie zadania z tabeli
    cursor.execute('SELECT id, name, priority, due_date, completed FROM tasks')
    tasks = cursor.fetchall()  # Pobiera wszystkie rekordy
    connection.close()
    return tasks

# Funkcja do usuwania zadania na podstawie ID
def delete_task(task_id):
    connection = sqlite3.connect('tasks.db')  # Łączy się z bazą danych
    cursor = connection.cursor()
    # Usuwa zadanie z tabeli
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    connection.commit()
    connection.close()

# Funkcja do oznaczania zadania jako wykonanego na podstawie ID
def complete_task(task_id):
    connection = sqlite3.connect('tasks.db')  # Łączy się z bazą danych
    cursor = connection.cursor()
    # Aktualizuje status zadania na wykonane
    cursor.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
    connection.commit()
    connection.close()

# Funkcja do sprawdzania wykonanych zadań
def completed():
    connection = sqlite3.connect('tasks.db')  # Łączy się z bazą danych
    cursor = connection.cursor()
    # Pobiera wszystkie zadania z tabeli
    cursor.execute('SELECT id, name, priority, due_date, completed FROM tasks where completed = 1')
    tasks = cursor.fetchall()  # Pobiera wszystkie rekordy
    connection.close()
    return tasks

# Funkcja do sprawdzania niewykonanych zadań
def notcompleted():
    connection = sqlite3.connect('tasks.db')  # Łączy się z bazą danych
    cursor = connection.cursor()
    # Pobiera wszystkie zadania z tabeli
    cursor.execute('SELECT id, name, priority, due_date, completed FROM tasks where completed = 0')
    tasks = cursor.fetchall()  # Pobiera wszystkie rekordy
    connection.close()
    return tasks