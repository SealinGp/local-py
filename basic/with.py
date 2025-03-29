import sqlite3

def greet_user(username):
    """显示简单的问候语"""
    print(f"Hello, {username}!")

# 文件操作的with语句示例
def file_example():
    # 写入文件
    with open('example.txt', 'w') as file:
        file.write('Hello, World!')
    
    # 读取文件
    with open('example.txt', 'r') as file:
        content = file.read()
        print(f"文件内容: {content}")

# 数据库连接的with语句示例
def database_example():    
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
        cursor.execute('INSERT INTO users (name) VALUES (?)', ('张三',))
        conn.commit()

# 使用with语句处理异常
def exception_example():
    try:
        with open('不存在的文件.txt', 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print("文件不存在，但资源已经被正确释放")

# 调用示例函数
if __name__ == "__main__":
    print("=== 文件操作示例 ===")
    file_example()
    
    print("\n=== 数据库操作示例 ===")
    database_example()
    
    print("\n=== 异常处理示例 ===")
    exception_example()