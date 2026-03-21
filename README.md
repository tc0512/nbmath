# nbmath

一个实用的数学工具包，支持方程求解、几何计算、统计分析等功能。

## 安装
```bash
pip install https://github.com/tc0512/nbmath/releases/download/v0.1.7/nbmath-0.1.7-py3-none-any.whl
```

## 快速开始
```python
from nbmath.equation import solve
from nbmath.const import pi
from nbmath.optimize import newton

#解方程
print(solve(1, -3, 2)) #[(2+0j), (1+0j)]

#调用常数
print(pi()) #3.141592653589793

#最小值
TOL = 1e-6
MAX_ITER = 100
print(newton(lambda x: x**2+6*x+9, 1.5, TOL, MAX_ITER)) #x接近-3,y接近0(有浮点误差)
```

## 模块介绍
### 常数模块`nbmath.const`
- `pi` `tau` `e` - 数学常数
- `G` `g` `k` `NA` - 物理常数
### 方程模块`nbmath.solve`
- 一元一次/二次/三次/四次方程求解
- 牛顿迭代法解高次方程
- 不等式
- 统一接口`solve`
### 几何模块`nbmath.geometry`
- 点`Point`
- 线段`Line`
- 圆`Circle`
- 多边形`Polygon`
### 统计模块`nbmath.stats`
- `mean`平均数 `percentile`百分位数
- `mode`众数 `var`方差 `std`标准差
### 工具模块`nbmath.utils`
- `gcd`最大公约数 `lcm`最小公倍数
- `floor`向下取整 `trunc`截断取整
- `fac`阶乘 `diff`多项式求导
- `np.linspace`纯python实现
- `polyval`多项式代入求值
- `timer`计时器
### 优化算法模块`nbmath.optimize`
- `brute`咆哮算法
- `golden_section`黄金分割法
- `newton`牛顿法
- `gradient_descent`梯度下降
- `simulated_annealing`模拟退火

## 示例代码
```python
from nbmath.equation import solve
from nbmath.stats import mode
from nbmath.optimize import simulated_annealing

#求解x^4-10x^2+9=0
roots = solve(1, 0, -10, 0, 9)
print(roots) #接近±1,±3，浮点误差可能存在，请以实际使用为准
print(solve(2, 3, ">")) #x>-1.5

data = [1, 1, 2, 3, 4]
print(mode(data)) #[1]

#求y=x^4-5x^2+4的最小值
def F(x):return x**4-5*x**2+4
TEMP = 100
COOLING = 0.95
STEPS = 1000
TOL = 1e-6
print(simulated_annealing(F, -5, 5, TEMP, COOLING, STEPS, TOL)) #{'x': -1.581998612252256, 'fun': -2.249992603725974}
```

## 许可证
MIT
