from database import create_database, add_task, list_tasks, delete_task, complete_task, completed, notcompleted


def main_menu():
    print("=== Task Manager ===")
    print("1. Dodaj zadanie")
    print("2. Wyświetl zadania")
    print("3. Usuń zadanie")
    print("4. Oznacz zadanie jako wykonane")
    print("5. Wyświetl zadania niewykonane")
    print("6. Wyświetl zadania wykonane")
    print("7. Wyjdź")


def main():
    create_database()

    while True:
        main_menu()
        choice = input("Wybierz opcję: ")

        if choice == "1":
            name = input("Nazwa zadania: ")
            while not name.strip():
                print("Nazwa zadania nie może być pusta!")
                name = input("Nazwa zadania: ")
            description = input("Opis zadania: ")
            priority = input("Priorytet (niski/średni/wysoki): ").lower()
            while priority not in ['niski,średni,wysoki']:
                print("Zły priorytet!")
                priority = input("Priorytet (niski/średni/wysoki)")
            due_date = input("Termin (YYYY-MM-DD): ")
            add_task(name, description, priority, due_date)
            print("Dodano zadanie!")

        elif choice == "2":
            tasks = list_tasks()
            print("\n=== Lista zadań ===")
            for task in tasks:
                status = "tak" if task[4] else "nie"
                print(f"[{task[0]}] {task[1]} - Priorytet: {task[2]} - Termin: {task[3]} - Wykonane: {status}")
            print()

        elif choice == "3":
            task_id = int(input("Podaj ID zadania do usunięcia: "))
            delete_task(task_id)
            print("Usunięto zadanie!")

        elif choice == "4":
            task_id = int(input("Podaj ID zadania do oznaczenia jako wykonane: "))
            complete_task(task_id)
            print("Zadanie oznaczone jako wykonane!")

        elif choice == "5":
            tasks = completed()
            print("\n=== Lista wykonanych zadań ===")
            for task in tasks:
                status = "tak" #if task[4] else "nie"
                print(f"[{task[0]}] {task[1]} - Priorytet: {task[2]} - Termin: {task[3]} - Wykonane: {status}")
            print()

        elif choice == "6":
            tasks = notcompleted()
            print ("\n=== Lista niewykonanych zadań ===")
            for task in tasks:
                status = "nie" #if task[4] else "nie"
                print (f"[{task[0]}] {task[1]} - Priorytet: {task[2]} - Termin: {task[3]} - Wykonane: {status}")
            print()

        elif choice == "7":
            print("Do zobaczenia!")
            break


        else:
            print("Nieprawidłowa opcja, spróbuj ponownie.")


if __name__ == "__main__":
    main()
