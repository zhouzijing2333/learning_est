import numpy as np #纳入矩阵计算器
import matplotlib.pyplot as plt #加入绘制图像包

def perform_linear_regression(show_plot=True):
    # 设置数据集
    x = np.linspace(0, 10, 50)
    y = 2 * x + 1 + np.random.randn(50) * 2  # 加入噪声
    plt.scatter(x, y)
    # plt.xlabel("x")
    # plt.ylabel("y")
    # plt.show()

    # 采用小二乘法
    A = np.vstack([x, np.ones(len(x))]).T
    # print(A)
    k, b = np.linalg.lstsq(A, y, rcond=None)[0]
    if show_plot:
        plt.scatter(x, y)
        # plt.xlabel("x")
        # plt.ylabel("y")
        # plt.show()
        print(f"k为{k:.2f},b为{b:.2f}")
        plt.plot(x, k * x + b, 'r', label=f"line:y={k:.2f}x+{b:.2f}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title('Least squares regression')
        plt.legend()
        plt.grid()
        plt.show()
    return k,b
k_val, b_val = perform_linear_regression()

