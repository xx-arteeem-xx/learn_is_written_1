import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_welcome():
    print("╔══════════════════════════════════════════════╗")
    print("║           КРИПТОГРАФИЧЕСКИЕ ЗАДАЧИ           ║")
    print("║                                              ║")
    print("║  1. Шифр Вернама                             ║")
    print("║  2. Линейный конгруэнтный генератор          ║")
    print("║  3. Генерация чисел RC4                      ║")
    print("║  4. Формирование перестановки RC4            ║")
    print("║                                              ║")
    print("║  Введите 'q' для выхода                      ║")
    print("╚══════════════════════════════════════════════╝")

def vernam_encrypt(n1, n2, n3, k1, k2, k3):
    numbers = [n1, n2, n3]
    keys = [k1, k2, k3]
    results = []
    
    print("\n┌─────────────┬──────────┬──────────┬──────────┐")
    print("│   Число     │ Двоичное │   Ключ   │ Результат│")
    print("├─────────────┼──────────┼──────────┼──────────┤")
    
    for i, (num, key) in enumerate(zip(numbers, keys), 1):
        bin_num = format(num, '08b')
        bin_key = format(key, '08b')
        encrypted = num ^ key
        bin_encrypted = format(encrypted, '08b')
        
        print(f"│ n{i}={num:<9} │ {bin_num}  │ {bin_key}  │ {bin_encrypted} │")
        results.append(encrypted)
    
    print("└─────────────┴──────────┴──────────┴──────────┘")
    print(f"\nРезультат: {results}")

def linear_congruential_generator(a, b, c, x0, count):
    results = []
    x = x0
    
    print("\n┌──────┬────────────┐")
    print("│ Шаг  │   Значение │")
    print("├──────┼────────────┤")
    
    for i in range(count):
        results.append(x)
        print(f"│ {i+1:<4} │ {x:<10} │")
        x = (a * x + b) % c
    
    print("└──────┴────────────┘")
    return results

def rc4_generate(n, S_decimal, count=8):
    size = 2 ** n
    S = []
    
    for i in range(size):
        S.append((S_decimal >> (n * i)) & (size - 1))
    
    i = j = 0
    generated = []
    
    print("\n┌─────┬─────┬─────┬────────────────────┐")
    print("│  i  │  j  │  t  │    Перестановка S  │")
    print("├─────┼─────┼─────┼────────────────────┤")
    
    for step in range(count):
        i = (i + 1) % size
        j = (j + S[i]) % size
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % size
        generated.append(S[t])
        
        S_str = ' '.join(map(str, S))
        print(f"│ {i:<3} │ {j:<3} │ {t:<3} │ {S_str:<18} │")
    
    print("└─────┴─────┴─────┴────────────────────┘")
    return generated

def rc4_initialize(n, L, K):
    size = 2 ** n
    S = list(range(size))
    j = 0
    
    print("\n┌─────┬─────┬────────────────────┐")
    print("│  i  │  j  │    Перестановка S  │")
    print("├─────┼─────┼────────────────────┤")
    
    for i in range(size):
        j = (j + S[i] + K[i % L]) % size
        S[i], S[j] = S[j], S[i]
        
        S_str = ' '.join(map(str, S))
        print(f"│ {i:<3} │ {j:<3} │ {S_str:<18} │")
    
    print("└─────┴─────┴────────────────────┘")
    return S

def get_input(prompt, type_func=int):
    while True:
        try:
            return type_func(input(prompt))
        except ValueError:
            print("Ошибка! Введите корректное число.")

def main():
    while True:
        clear_screen()
        print_welcome()
        
        choice = input("\nВыберите задачу (1-4): ").strip()
        
        if choice == 'q':
            break
            
        if choice == '1':
            print("\n=== ЗАДАЧА 1: Шифр Вернама ===")
            n1 = get_input("n1 = ")
            n2 = get_input("n2 = ")
            n3 = get_input("n3 = ")
            k1 = get_input("k1 = ")
            k2 = get_input("k2 = ")
            k3 = get_input("k3 = ")
            vernam_encrypt(n1, n2, n3, k1, k2, k3)
            
        elif choice == '2':
            print("\n=== ЗАДАЧА 2: Линейный конгруэнтный генератор ===")
            a = get_input("a = ")
            b = get_input("b = ")
            c = get_input("c = ")
            x0 = get_input("x0 = ")
            count = get_input("Количество чисел = ")
            linear_congruential_generator(a, b, c, x0, count)
            
        elif choice == '3':
            print("\n=== ЗАДАЧА 3: Генерация чисел RC4 ===")
            n = get_input("n = ")
            S = get_input("S = ")
            rc4_generate(n, S)
            
        elif choice == '4':
            print("\n=== ЗАДАЧА 4: Формирование перестановки RC4 ===")
            n = get_input("n = ")
            L = get_input("L = ")
            K = []
            for i in range(L):
                K.append(get_input(f"K{i} = "))
            rc4_initialize(n, L, K)
            
        else:
            print("Неверный выбор!")
            
        input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()