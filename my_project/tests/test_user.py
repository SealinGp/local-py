import sys
import os

# 添加src目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.models.user import User

def test_user():
    user = User("li si", 30)
    assert user.name == "Li Si"
    assert user.age == 30
    print("测试通过！")

if __name__ == "__main__":
    test_user() 