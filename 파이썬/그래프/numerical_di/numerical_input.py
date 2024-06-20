import numpy as np
import matplotlib.pyplot as plt

def plot_polynomial_function(coefficients):
    # x값 범위 설정
    x = np.linspace(-10, 10, 400)
    
    # 다항함수 계산
    y = np.polyval(coefficients, x)
    
    # 그래프 그리기
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=np.poly1d(coefficients))
    plt.title('Polynomial Function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    # 다항함수의 계수 입력 받기
    coefficients_str = input('다항함수의 계수를 입력하세요 (최고차항부터 입력): ')
    coefficients = [float(c) for c in coefficients_str.split()]

    # 그래프 그리기
    plot_polynomial_function(coefficients)

if __name__ == "__main__":
    main()
