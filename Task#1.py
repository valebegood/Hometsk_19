
import numpy as np
#a 
zeros_array = np.zeros((4, 3))
ones_array = np.ones((4, 3))
numbers_array = np.arange(12).reshape(4, 3)

print("Массив из нулей:")
print(zeros_array)
print("\nМассив из единиц:")
print(ones_array)
print("\nМассив чисел от 0 до 11:")
print(numbers_array)



#b 
x_values = np.arange(1, 101, 1)
y_values = 2 * x_values ** 2 + 5

print("Табулирование функции F(x) = 2x^2 + 5:")
for x, y in zip(x_values, y_values):
    print(f"F({x}) = {y}")

#c 
x_values = np.arange(-10, 11, 1)
y_values = np.exp(-x_values)

print("Табулирование функции F(x) = e^(-x):")
for x, y in zip(x_values, y_values):
    print(f"F({x}) = {y}")    


