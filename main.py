**main.py** (crea questo file):
```python
import csv
from datetime import datetime

FILE = "network_inventory.csv"

def load_inventory():
    try:
        with open(FILE, "r") as f:
            return list(csv.DictReader(f)) or []
    except FileNotFoundError:
        return []

def save_inventory(inventory):
    with open(FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["IP", "Hostname", "Tipo", "Stato", "Data"])
        writer.writeheader()
        writer.writerows(inventory)

def add_device():
    ip = input("IP: ").strip()
    hostname = input("Hostname: ").strip()
    tipo = input("Tipo (Switch/Router/PC/Server): ").strip()
    stato = input("Stato (Online/Offline): ").strip()
    if not all([ip, hostname, tipo, stato]):
        print("❌ Tutti i campi sono obbligatori!")
        return
    inventory = load_inventory()
    inventory.append({"IP": ip, "Hostname": hostname, "Tipo": tipo, "Stato": stato, "Data": datetime.now().strftime("%d/%m/%Y")})
    save_inventory(inventory)
    print("✅ Dispositivo aggiunto!")

def search():
    term = input("Cerca IP o Hostname: ").strip().lower()
    if not term:
        print("❌ Inserisci un termine di ricerca!")
        return
    inventory = load_inventory()
    results = [device for device in inventory if term in device["IP"].lower() or term in device["Hostname"].lower()]
    if results:
        for device in results:
            print(device)
    else:
        print("❌ Nessun dispositivo trovato!")

def list_all():
    inventory = load_inventory()
    if not inventory:
        print("❌ Nessun dispositivo in inventario!")
        return
    for device in inventory:
        print(device)

while True:
    print("\n=== Network Inventory Tool ===")
    print("1. Aggiungi dispositivo")
    print("2. Cerca dispositivo")
    print("3. Visualizza tutti")
    print("4. Esci")
    choice = input("Scegli: ").strip()
    if choice == "1": add_device()
    elif choice == "2": search()
    elif choice == "3": list_all()
    elif choice == "4": break
    else:
        print("❌ Scelta non valida!")
