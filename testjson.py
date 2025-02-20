import json

with open("sample-data.json", encoding="utf-8") as file:
    data = json.load(file)

print("Статус интерфейсов")
print("=" * 80)
print(f"{'DN':<50} {'Описание':<20} {'Скорость':<10} {'MTU':<5}")
print("-" * 80)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes["descr"] or "-"
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    print(f"{dn:<50} {descr:<20} {speed:<10} {mtu:<5}")
