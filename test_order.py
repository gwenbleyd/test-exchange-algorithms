import unittest
from main import create_and_get_orders


class TestOrders(unittest.TestCase):

    def test_input_type(self):
        data = "some string"
        with self.assertRaises(TypeError):
            create_and_get_orders(data)

    def test_input_value_volume(self):
        data1 = {
            "volume": -10000.0,
            "number": 5,
            "amountDif": 50.0,
            "side": "SELL",
            "priceMin": 200.0,
            "priceMax": 300.0
        }
        data2 = {
            "volume": "some string",
            "number": 5,
            "amountDif": 50.0,
            "side": "SELL",
            "priceMin": 200.0,
            "priceMax": 300.0
        }
        with self.assertRaises(ValueError):
            create_and_get_orders(data1)
        with self.assertRaises(ValueError):
            create_and_get_orders(data2)

    def test_input_side(self):
        data1 = {
            "volume": 10000.0,
            "number": 5,
            "amountDif": 50.0,
            "side": "Fdfs",
            "priceMin": 200.0,
            "priceMax": 300.0
        }
        data2 = {
            "volume": 10000.0,
            "number": 5,
            "amountDif": 50.0,
            "side": "12424",
            "priceMin": 200.0,
            "priceMax": 300.0
        }
        data3 = {
            "volume": 10000.0,
            "number": 5,
            "amountDif": 50.0,
            "side": 512,
            "priceMin": 200.0,
            "priceMax": 300.0
        }
        with self.assertRaises(ValueError):
            create_and_get_orders(data1)
        with self.assertRaises(ValueError):
            create_and_get_orders(data2)
        with self.assertRaises(ValueError):
            create_and_get_orders(data3)


if __name__ == "__main__":
    unittest.main()
