from src.utils.helper import format_name

class User:
    def __init__(self, name, age):
        self.name = format_name(name)
        self.age = age
    
    def get_info(self):
        return f"用户：{self.name}，年龄：{self.age}" 