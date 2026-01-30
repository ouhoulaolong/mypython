def factory():
    def product():
        print("我是工厂生产的产品")

    print("工厂生产了一个产品")
    return product  # 返回函数，不是调用函数


# 从工厂获取产品
my_product = factory()  # 输出: 工厂生产了一个产品

my_product()  # 输出: 我是工厂生产的产品