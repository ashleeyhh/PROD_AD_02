from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput


class ToDoListApp(App):

    def build(self):
        self.tasks = []
        self.task_input = TextInput(hint_text='Enter task', multiline=False)
        add_button = Button(text='Add Task')
        add_button.bind(on_press=self.add_task)

        self.task_display = ScrollView()
        self.task_display_grid = BoxLayout(orientation='vertical', size_hint_y=None)
        self.task_display_grid.bind(minimum_height=self.task_display_grid.setter('height'))
        self.task_display.add_widget(self.task_display_grid)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.task_input)
        layout.add_widget(add_button)
        layout.add_widget(self.task_display)

        return layout

    def add_task(self, instance):
        task = self.task_input.text.strip()
        if task:
            self.tasks.append(task)
            self.task_input.text = ''
            self.update_display()

    def update_display(self):
        self.task_display_grid.clear_widgets()
        for task in self.tasks:
            task_box = BoxLayout(size_hint_y=None, height=40)
            task_label = TextInput(text=task, readonly=True, multiline=False, font_size=18)
            edit_button = Button(text='Edit', size_hint_x=None, width=80)
            edit_button.bind(on_press=lambda instance, task_label=task_label: self.edit_task(task_label))
            delete_button = Button(text='Delete', size_hint_x=None, width=80)
            delete_button.bind(on_press=lambda instance, task_label=task_label: self.delete_task(task_label))
            task_box.add_widget(task_label)
            task_box.add_widget(edit_button)
            task_box.add_widget(delete_button)
            self.task_display_grid.add_widget(task_box)

    def edit_task(self, task_label):
        old_task = task_label.text
        self.tasks.remove(old_task)
        new_task = task_label.text
        self.tasks.append(new_task)
        self.update_display()

    def delete_task(self, task_label):
        task = task_label.text
        self.tasks.remove(task)
        self.update_display()


if __name__ == '__main__':
    ToDoListApp().run()
