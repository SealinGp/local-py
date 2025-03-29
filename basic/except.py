def main():
    """主函数"""
    print("这是主函数")

def error_handling_examples():
    """展示不同的错误处理方式"""
    
    # 1. try-except-else-finally 示例
    def file_operation():
        try:
            file = open('test.txt', 'r')
            content = file.read()
        except FileNotFoundError:
            print("文件不存在")
        except PermissionError:
            print("没有权限访问文件")
        else:
            print("文件读取成功")
            print(content)
        finally:
            print("清理工作：关闭文件")
            file.close()
    
    # 2. try-finally 示例
    def resource_cleanup():
        resource = "打开的资源"
        try:
            print(f"使用{resource}")
            # 可能发生错误的操作
        finally:
            print(f"清理{resource}")
    
    # 3. raise 示例
    def validate_age(age):
        if not isinstance(age, int):
            raise TypeError("年龄必须是整数")
        if age < 0:
            raise ValueError("年龄不能为负数")
        if age > 150:
            raise ValueError("年龄超出合理范围")
        return age
    
    # 4. assert 示例
    def calculate_average(numbers):
        assert len(numbers) > 0, "列表不能为空"
        assert all(isinstance(x, (int, float)) for x in numbers), "所有元素必须是数字"
        return sum(numbers) / len(numbers)
    
    # 测试这些函数
    print("=== 测试文件操作 ===")
    file_operation()
    
    print("\n=== 测试资源清理 ===")
    resource_cleanup()
    
    print("\n=== 测试年龄验证 ===")
    try:
        validate_age("20")  # 会抛出TypeError
    except TypeError as e:
        print(f"错误：{e}")
    
    print("\n=== 测试断言 ===")
    try:
        calculate_average([])  # 会触发断言错误
    except AssertionError as e:
        print(f"断言错误：{e}")

# 只有直接运行这个文件时才会执行
if __name__ == "__main__":
    print("这个文件被直接运行了")
    error_handling_examples()
