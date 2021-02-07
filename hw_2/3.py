import yaml

data = {
    '1':[1, 2, 3],
    '2': 2,
    '3': {
        '1€': '1',
        '2€': '2',
        '3€': '3'
    }
}

file = 'file.yaml'

with open(file, 'w', encoding='utf-8') as f:
    yaml.dump(data, f, default_flow_style=True, allow_unicode=True)

with open(file, encoding='utf-8') as fn:
    result = fn.read()
    print(result)
