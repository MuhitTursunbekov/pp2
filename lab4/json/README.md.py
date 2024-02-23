import json

# Загрузка данных из JSON-файла
with open('sample-data.json', 'r') as file:
    data = json.load(file)

# Извлечение необходимой информации из JSON-данных
interface_data = data['imdata']

# Вывод заголовка
print("Статус интерфейса")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Описание", "Скорость", "MTU"))
print("-" * 80)

# Вывод деталей интерфейса
for interface in interface_data:
    dn = interface['topSystem']['attributes']['dn']
    description = interface['ethpmPhysIf']['attributes']['descr']
    speed = interface['ethpmPhysIf']['attributes']['speed']
    mtu = interface['ethpmPhysIf']['attributes']['mtu']

    # Вывод деталей интерфейса в желаемом формате
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))
