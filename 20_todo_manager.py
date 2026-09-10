class TodoManager:
    def __init__(self):
        self.todos = []
        self.next_id = 1

    def add(self, task):
        todo = {'id': self.next_id, 'task': task, 'done': False}
        self.todos.append(todo)
        self.next_id += 1
        return todo

    def complete(self, todo_id):
        for t in self.todos:
            if t['id'] == todo_id:
                t['done'] = True
                return True
        return False

    def remove(self, todo_id):
        self.todos = [t for t in self.todos if t['id'] != todo_id]

    def list_all(self):
        return self.todos

if __name__ == '__main__':
    tm = TodoManager()
    tm.add('Write code')
    tm.add('Review PR')
    tm.complete(1)
    for t in tm.list_all():
        status = '✓' if t['done'] else '✗'
        print(f"{status} [{t['id']}] {t['task']}")
