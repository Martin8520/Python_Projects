from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.listview import ListItemButton
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
import csv
from datetime import datetime


class Task:
    def __init__(self, task="", hours=None, price=None, start_date="", end_date=""):
        self.task = task
        self.hours = hours
        self.price = price
        self.start_date = start_date
        self.end_date = end_date


class TaskManager(BoxLayout):
    tasks = ListProperty([])
    total_price = 0
    selected_index = None

    def __init__(self, **kwargs):
        super(TaskManager, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.task_listview = TaskListView()
        self.task_listview.bind(on_selection_change=self.on_task_selection_change)
        self.add_widget(self.task_listview)
        self.task_editor = TaskEditor()
        self.task_editor.bind(on_save=self.save_task)
        self.add_widget(self.task_editor)

    def on_task_selection_change(self, instance, value):
        if value:
            self.selected_index = value[0]

    def save_task(self, task):
        if self.selected_index is not None:
            self.tasks[self.selected_index] = task
        else:
            self.tasks.append(task)
        self.task_listview.refresh_list()
        self.calculate_total()

    def calculate_total(self):
        self.total_price = sum(
            (task.hours * task.price) if (task.hours is not None and task.price is not None) else 0 for task in
            self.tasks)
        self.task_editor.total_price_label.text = f"Обща цена: {self.total_price} лв."


class TaskListView(BoxLayout):
    tasks = ListProperty([])
    selected_task = ObjectProperty(None)
    on_selection_change = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(TaskListView, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.listview = ListView()
        self.listview.bind(selection_change=self.on_selection_change)
        self.add_widget(self.listview)
        self.refresh_list()

    def refresh_list(self):
        self.tasks = [{'text': f"Задача: {task.task}, Часове: {task.hours}, Цена на час в лева: {task.price} лв., "
                               f"Дата на започване: {task.start_date}, Дата на завършване: {task.end_date}",
                       'background_color': '#a6ffb4' if task.end_date else '#ff6666'} for task in
                      App.get_running_app().root.tasks]
        self.listview.list_data = self.tasks


class TaskEditor(BoxLayout):
    task_name = ObjectProperty(None)
    task_hours = ObjectProperty(None)
    task_price = ObjectProperty(None)
    total_price_label = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(TaskEditor, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.task_name = TextInput(hint_text='Задача')
        self.add_widget(self.task_name)
        self.task_hours = TextInput(hint_text='Часове')
        self.add_widget(self.task_hours)
        self.task_price = TextInput(hint_text='Цена на час в BGN')
        self.add_widget(self.task_price)
        self.save_button = Button(text='Запази')
        self.save_button.bind(on_release=self.save_task)
        self.add_widget(self.save_button)

    def save_task(self, instance):
        task = Task(
            task=self.task_name.text,
            hours=float(self.task_hours.text) if self.task_hours.text else None,
            price=float(self.task_price.text) if self.task_price.text else None,
            start_date=datetime.now().strftime("%Y-%m-%d %H:%M"),
            end_date=""
        )
        self.task_name.text = ''
        self.task_hours.text = ''
        self.task_price.text = ''
        self.total_price_label.text = ''
        self.parent.save_task(task)


class ListView(ListItemButton):
    pass


class TaskApp(App):
    def build(self):
        return TaskManager()


if __name__ == '__main__':
    TaskApp().run()
