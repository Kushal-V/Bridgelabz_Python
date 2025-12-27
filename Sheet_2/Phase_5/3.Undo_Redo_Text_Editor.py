#TextEditor class that uses a Stack (List) to store Command objects. Each Command has an execute() and undo() method

class TextEditor:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []
        self.text = ""
    
    def insert(self, text):
        self.undo_stack.append(text)
        self.redo_stack = []
        self.text += text
    
    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.undo_stack.pop())
            self.text = self.text[:-len(self.redo_stack[-1])]
    
    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.redo_stack.pop())
            self.text += self.undo_stack[-1]
    
    def get_text(self):
        return self.text

t1 = TextEditor()
t1.insert("Hello")
t1.insert("World")
t1.undo()
t1.redo()
print(t1.get_text())