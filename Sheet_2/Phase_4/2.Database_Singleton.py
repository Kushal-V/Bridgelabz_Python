class Database:
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance
    
    def connect(self):
        print("Database connected")

db1 = Database()
db2 = Database()

db1.connect()
db2.connect()

print(db1 == db2)