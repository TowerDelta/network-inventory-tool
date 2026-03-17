**main.py** (crea questo file):
```python
import csv
import json
from datetime import datetime

FILE = "network_inventory.csv"

def load_inventory():
    try:
        with open(FILE, "r") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        return []

def save_inventory(inventory):
    with open(FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["IP", "Hostname", "Tipo", "Stato", "Data"])
        writer.writeheader()
        writer.writerows(inventory)

def add_device():
    ip = input("IP: ")
    hostname = input("Hostname: ")
    tipo = input("Tipo (Switch/Router/PC/Server): ")
    stato = input("Stato (Online/Offline): ")
    inventory = load_inventory()
    inventory.append({"IP": ip, "Hostname": hostname, "Tipo": tipo, "Stato": stato, "Data": datetime.now().strftime("%d/%m/%Y")})
    save_inventory(inventory)
    print("✅ Dispositivo aggiunto!")

def search():
    term = input("Cerca IP o Hostname: ").lower()
    inventory = load_inventory()
    for device in inventory:
        if term in device["IP"].lower() or term in device["Hostname"].lower():
            print(device)

# Menu semplice
while True:
    print("\n=== Network Inventory Tool ===")
    print("1. Aggiungi dispositivo")
    print("2. Cerca dispositivo")
    print("3. Esci")
    choice = input("Scegli: ")
    if choice == "1": add_device()
    elif choice == "2": search()
    elif choice == "3": break
