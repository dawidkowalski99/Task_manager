from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
import database

class TaskManagerApp(App):
    def build(self):
        self.task_list = []  # Do wyświetlania zadań
        self.root = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # Nagłówek
        header = Label(text="Task Manager", font_size=32, size_hint=(1, 0.1))
        self.root.add_widget(header)

        # Pole na listę zadań
        self.task_scroll = ScrollView(size_hint=(1, 0.6))
        self.task_container = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.task_container.bind(minimum_height=self.task_container.setter("height"))
        self.task_scroll.add_widget(self.task_container)
        self.root.add_widget(self.task_scroll)

        # Formularz dodawania zadań
        form_layout = BoxLayout(orientation="vertical", size_hint=(1, 0.3))

        self.task_name_input = TextInput(hint_text="Nazwa zadania", size_hint=(1, None), height=40)
        form_layout.add_widget(self.task_name_input)

        self.task_desc_input = TextInput(hint_text="Opis zadania", size_hint=(1, None), height=40)
        form_layout.add_widget(self.task_desc_input)

        self.task_deadline_input = TextInput(hint_text="Termin (YYYY-MM-DD)", size_hint=(1, None), height=40)
        form_layout.add_widget(self.task_deadline_input)

        # Przycisk dodawania zadania
        add_task_button = Button(text="Dodaj zadanie", size_hint=(1, None), height=50)
        add_task_button.bind(on_press=self.add_task)
        form_layout.add_widget(add_task_button)

        self.root.add_widget(form_layout)

        # Wczytaj istniejące zadania
        self.refresh_tasks()
        return self.root

    def add_task(self, instance):
        name = self.task_name_input.text.strip()
        desc = self.task_desc_input.text.strip()
        deadline = self.task_deadline_input.text.strip()

        if not name:
            return  # Nazwa zadania jest wymagana

        try:
            database.add_task(name, desc, "Średni", deadline)  # Domyślny priorytet: Średni
            self.task_name_input.text = ""
            self.task_desc_input.text = ""
            self.task_deadline_input.text = ""
            self.refresh_tasks()
        except Exception as e:
            print(f"Nie udało się dodać zadania: {str(e)}")

    def refresh_tasks(self):
        self.task_container.clear_widgets()
        self.task_list = database.list_tasks()

        for task in self.task_list:
            id, name, priority, due_date, completed = task
            task_layout = BoxLayout(orientation="horizontal", size_hint=(1, None), height=50)
            task_label = Label(text=f"{name} - {due_date}", size_hint=(0.8, 1))
            task_delete_button = Button(text="Usuń", size_hint=(0.2, 1))
            task_delete_button.bind(on_press=lambda instance, t_id=id: self.delete_task(t_id))

            task_layout.add_widget(task_label)
            task_layout.add_widget(task_delete_button)
            self.task_container.add_widget(task_layout)

    def delete_task(self, task_id):
        try:
            database.delete_task(task_id)
            self.refresh_tasks()
        except Exception as e:
            print(f"Nie udało się usunąć zadania: {str(e)}")

# Uruchomienie aplikacji
if __name__ == "__main__":
    TaskManagerApp().run()
