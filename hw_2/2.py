import json


def write_order_to_json(item, quantity, price, buyer, date):
    result = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date
    }

    file = 'files/orders.json'

    with open(file, encoding='utf-8') as f:
        orders = json.load(f)
        if orders['orders']:
            order_list = orders['orders']
            order_list.append(result)
            orders['orders'] = order_list
            with open(file, 'w', encoding='utf-8') as fn:
                json.dump(orders, fn, indent=4)
        else:
            orders['orders'] = [result]
            with open(file, 'w', encoding='utf-8') as fn:
                json.dump(orders, fn, indent=4)


i = 0
while i <= 5:
    write_order_to_json('product' + str(i), i, 100 + i, 'buyer' + str(i), '06.09.2020')
    i += 1
