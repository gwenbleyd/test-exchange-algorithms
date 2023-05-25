import binance.client
from secret_key import api_secret, api_key
import random

# Создаем клиент для подключения к бирже
client = binance.client.Client(api_key, api_secret)


# Функция для создания и получения ордеров
def create_and_get_orders(data):
    # Проверяем, что входные данные являются словарем
    if not isinstance(data, dict):
        raise TypeError("Input data must be a dictionary")

    # Извлекаем данные из входного словаря
    volume = data["volume"]
    number = data["number"]
    amountDif = data["amountDif"]
    side = data["side"]
    priceMin = data["priceMin"]
    priceMax = data["priceMax"]

    # Проверяем, что все данные являются числами и больше нуля
    if not (isinstance(volume, (int, float)) and volume > 0):
        raise ValueError("Volume must be a positive number")
    if not (isinstance(number, int) and number > 0):
        raise ValueError("Number must be a positive integer")
    if not (isinstance(amountDif, (int, float)) and amountDif > 0):
        raise ValueError("AmountDif must be a positive number")
    if not (isinstance(priceMin, (int, float)) and priceMin > 0):
        raise ValueError("PriceMin must be a positive number")
    if not (isinstance(priceMax, (int, float)) and priceMax > 0):
        raise ValueError("PriceMax must be a positive number")

    # Проверяем, что сторона торговли является строкой и равна SELL или BUY
    if not (isinstance(side, str) and side in ["SELL", "BUY"]):
        raise ValueError("Side must be a string and equal to SELL or BUY")

    # Проверяем, что нижний диапазон цены меньше верхнего диапазона цены
    if not (priceMin < priceMax):
        raise ValueError("PriceMin must be less than PriceMax")

    # Создаем пустой список для хранения ордеров
    orders = []

    # Вычисляем средний объем одного ордера
    average_volume = volume / number

    # Создаем переменную для хранения общего объема получившихся ордеров
    total_volume = 0

    # Цикл по количеству ордеров
    for i in range(number):
        try:
            order_volume = round(average_volume + round(random.uniform(-amountDif, amountDif), 1), 1)
            order_price = round(random.uniform(priceMin, priceMax), 1)
            total_volume += order_volume
            if i == number:
                order_volume += round(volume - total_volume, 2)
            order = client.create_order(symbol="BTCUSDT", side=side, type="LIMIT", timeInForce="GTC",
                                        quantity=round(order_volume / order_price, 1), price=order_price)
            orders.append(order)
        except Exception as e:
            # Если произошла какая-то ошибка при создании ордера, то выводим ее на экран и пропускаем этот ордер
            print(f"Failed to create order {i + 1}: {e}")
            continue

    # Возвращаем список ордеров
    return orders


if __name__ == "__main__":
    data = {
        "volume": 10000.0,
        "number": 5,
        "amountDif": 50.0,
        "side": "SELL",
        "priceMin": 200.0,
        "priceMax": 300.0
    }
    orders = create_and_get_orders(data)
    for order in orders:
        print(order)