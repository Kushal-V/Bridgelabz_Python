#Model File and Folder classes. A Folder can contain Files or other Folders. Implement a get_size() method that recursively calculates total size.

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

class Folder:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def get_size(self):
        total_size = 0
        for child in self.children:
            total_size += child.get_size()
        return total_size

file1 = File("a.txt", 100)
file2 = File("b.txt", 200)

subfolder = Folder("sub")
subfolder.add_child(file2)

root = Folder("root")
root.add_child(file1)
root.add_child(subfolder)

print(root.get_size())
