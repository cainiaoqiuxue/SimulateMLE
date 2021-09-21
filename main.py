import os


def use(n, theta_0, thetas, is_show):
    dis = None
    if n == 1:
        from distribution import Poisson
        dis = Poisson(theta_0, thetas)
    elif n == 2:
        from distribution import Bernoulli
        dis = Bernoulli(theta_0, thetas)
    elif n == 3:
        from distribution import Fatiguelife
        dis = Fatiguelife(theta_0, thetas)
    elif n == 4:
        from distribution import Bradford
        dis = Bradford(theta_0, thetas)
    elif n == 5:
        from distribution import Dgamma
        dis = Dgamma(theta_0, thetas)
    elif n == 6:
        from distribution import Dweibull
        dis = Dweibull(theta_0, thetas)
    if is_show:
        dis.show_pdf()
    dis.main()


def main():
    os.system("cls")
    begin_content = '''
    --似然函数生成器--
    目前支持的概率分布：
    1.Poisson
    2.Bernoulli
    3.Fatiguelife
    4.Bradford
    5.Dgamma
    6.Dweibull
    '''
    print(begin_content)
    choice = input("输入概率分布前的序号:")
    theta_0 = input("输入给定的参数值(默认值0.3): ")
    theta = input("输入似然函数参数的取值范围(默认值[0.1,0.2,0.3,...,0.9]): ")
    is_show = input("是否展示概率密度函数？: ")
    choice = eval(choice)
    theta_0 = eval(theta_0) if theta_0 else 0.3
    theta = eval(theta) if theta else [0.1 * i for i in range(1, 10)]
    use(choice, theta_0, theta, is_show)


if __name__ == '__main__':
    main()
