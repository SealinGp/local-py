def greet_user(username):
    """显示简单的问候语"""
    print(f"Hello, {username}!")

def handle_unexpected_errors():
    """展示处理不可预见错误的方法"""
    
    # 1. 使用 Exception 捕获所有常见异常
    def catch_all_exceptions():
        try:
            # 一些可能产生未知错误的操作
            result = 1/0  # 除零错误
            unknown_function()  # 未定义函数
            "hello"[999]  # 索引错误
        except Exception as e:
            print(f"捕获到未知错误：{type(e).__name__}")
            print(f"错误信息：{str(e)}")
    
    # 2. 使用 BaseException 捕获所有异常（包括系统退出等）
    def catch_base_exceptions():
        try:
            # 一些可能产生系统级错误的操作
            import sys
            sys.exit(1)  # 系统退出
        except BaseException as e:
            print(f"捕获到基础异常：{type(e).__name__}")
            print(f"错误信息：{str(e)}")
    
    # 3. 使用通配符捕获所有异常（Python 3.11+）
    def catch_with_star():
        try:
            # 一些可能产生未知错误的操作
            x = 1/0
        except* Exception as e:
            print(f"捕获到异常组：{e}")
    
    # 4. 记录错误日志的示例
    def log_errors():
        import logging
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        
        try:
            # 一些可能产生未知错误的操作
            result = 1/0
        except Exception as e:
            logger.error(f"发生未知错误：{str(e)}", exc_info=True)
            # 可以在这里添加错误报告逻辑
            # 比如发送邮件通知、写入错误日志文件等
    
    print("=== 测试捕获所有异常 ===")
    catch_all_exceptions()
    
    print("\n=== 测试捕获基础异常 ===")
    catch_base_exceptions()
    
    print("\n=== 测试错误日志记录 ===")
    log_errors()

if __name__ == "__main__":
    handle_unexpected_errors()

