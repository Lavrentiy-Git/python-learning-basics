def is_even(n):
    return n % 2 == 0 # четное ли число?

def greet(name, age):
    print("Привет, ", name, "! ", "Тебе ", age, " лет.", sep = "")

def sum_list(nums):
    S = 0
    for i in nums:
        S += i
    return S

# Тесты (запустятся, ТОЛЬКО если файл запустить как скрипт)
if __name__ == "__main__":
    print(is_even(4))          # True
    print(is_even(7))          # False
    greet("Lavrentiy", 20)
    print(sum_list([1, 2, 3, 4]))  # 10
