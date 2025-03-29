from src.models.user import User
from src.utils.helper import calculate_sum

def main():
    # 创建用户实例
    user = User("zhang san", 25)
    print(user.get_info())
    
    # 使用工具函数
    result = calculate_sum(10, 20)
    print(f"计算结果：{result}")

if __name__ == "__main__":
    main() 