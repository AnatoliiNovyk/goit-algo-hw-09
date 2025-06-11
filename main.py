import timeit

def find_coins_greedy(amount):
    """
    Реалізує жадібний алгоритм для видачі решти.
    
    Args:
        amount (int): Сума, яку потрібно видати.
        
    Returns:
        dict: Словник з номіналами монет та їх кількістю.
    """
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount <= 0:
            break
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
            
    return result

def find_min_coins(amount):
    """
    Реалізує алгоритм динамічного програмування для видачі решти.
    
    Args:
        amount (int): Сума, яку потрібно видати.
        
    Returns:
        dict: Словник з номіналами монет та їх кількістю для найефективнішого способу.
    """
    coins = [1, 2, 5, 10, 25, 50]
    # min_coins[i] буде зберігати мінімальну кількість монет для суми i
    min_coins = [float('inf')] * (amount + 1)
    # coin_used[i] буде зберігати останню монету, використану для досягнення суми i
    coin_used = [0] * (amount + 1)
    
    min_coins[0] = 0
    
    for s in range(1, amount + 1):
        for coin in coins:
            if s >= coin:
                if min_coins[s - coin] + 1 < min_coins[s]:
                    min_coins[s] = min_coins[s - coin] + 1
                    coin_used[s] = coin

    # Якщо для заданої суми неможливо знайти розв'язок
    if min_coins[amount] == float('inf'):
        return {}
        
    # Відновлення набору монет
    result = {}
    current_amount = amount
    while current_amount > 0:
        last_coin = coin_used[current_amount]
        result[last_coin] = result.get(last_coin, 0) + 1
        current_amount -= last_coin
        
    return result

# Тестування на прикладі з опису
amount_1 = 113
print(f"Жадібний алгоритм для суми {amount_1}: {find_coins_greedy(amount_1)}")
print(f"Динамічне програмування для суми {amount_1}: {find_min_coins(amount_1)}")
print("-" * 30)

# Тестування на великій сумі
amount_2 = 123456

# Вимірювання часу виконання
time_greedy = timeit.timeit(lambda: find_coins_greedy(amount_2), number=100)
time_dp = timeit.timeit(lambda: find_min_coins(amount_2), number=10)

print(f"Результат жадібного алгоритму для {amount_2}: {find_coins_greedy(amount_2)}")
print(f"Результат ДП для {amount_2}: {find_min_coins(amount_2)}")
print("-" * 30)
print(f"Час виконання find_coins_greedy для суми {amount_2} (100 викликів): {time_greedy:.6f} секунд")
print(f"Час виконання find_min_coins для суми {amount_2} (10 викликів): {time_dp:.6f} секунд")
