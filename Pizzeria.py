# === DATI ===
menu = [
    {"id": 1, "nome": "Margherita", "prezzo": 6.00},
    {"id": 2, "nome": "Marinara", "prezzo": 5.00},
    {"id": 3, "nome": "Diavola", "prezzo": 8.00},
    {"id": 4, "nome": "Quattro Formaggi", "prezzo": 9.00},
    {"id": 5, "nome": "Capricciosa", "prezzo": 9.50},
    {"id": 6, "nome": "Prosciutto e Funghi", "prezzo": 8.50},
]

ordini = []
numero_ordine = 1


# === FUNZIONI ===
def mostra_menu():
    print("\n" + "="*40)
    print("        🍕 MENU PIZZERIA 🍕")
    print("="*40)
    for pizza in menu:
        print(f"  {pizza['id']}. {pizza['nome']:<20} €{pizza['prezzo']:.2f}")
    print("="*40)


def nuovo_ordine():
    global numero_ordine
    
    print("\n--- NUOVO ORDINE ---")
    nome_cliente = input("Nome cliente: ")
    
    ordine = {
        "numero": numero_ordine,
        "cliente": nome_cliente,
        "pizze": [],
        "totale": 0,
        "stato": "In attesa"
    }
    
    while True:
        mostra_menu()
        scelta = input("\nID pizza (0 per terminare): ")
        
        if scelta == "0":
            break
            
        try:
            id_pizza = int(scelta)
            pizza = next((p for p in menu if p["id"] == id_pizza), None)
            
            if pizza:
                quantita = int(input("Quantità: "))
                ordine["pizze"].append({
                    "nome": pizza["nome"],
                    "quantita": quantita,
                    "prezzo": pizza["prezzo"] * quantita
                })
                ordine["totale"] += pizza["prezzo"] * quantita
                print(f"✅ Aggiunto: {quantita}x {pizza['nome']}")
            else:
                print("❌ Pizza non trovata!")
        except:
            print("❌ Input non valido!")
    
    if ordine["pizze"]:
        ordini.append(ordine)
        numero_ordine += 1
        print(f"\n✅ Ordine #{ordine['numero']} confermato!")
        print(f"   Totale: €{ordine['totale']:.2f}")
    else:
        print("❌ Ordine annullato.")


def lista_ordini():
    if not ordini:
        print("\n📋 Nessun ordine.")
        return
    
    print("\n" + "="*50)
    print("              📋 LISTA ORDINI")
    print("="*50)
    
    for o in ordini:
        print(f"\n🔸 Ordine #{o['numero']} - {o['cliente']} [{o['stato']}]")
        for p in o["pizze"]:
            print(f"   {p['quantita']}x {p['nome']}")
        print(f"   💰 Totale: €{o['totale']:.2f}")


def cambia_stato():
    if not ordini:
        print("\n📋 Nessun ordine.")
        return
    
    lista_ordini()
    
    try:
        num = int(input("\nNumero ordine: "))
        ordine = next((o for o in ordini if o["numero"] == num), None)
        
        if ordine:
            print("\n1. In attesa")
            print("2. In preparazione")
            print("3. Pronto")
            print("4. Consegnato")
            
            stati = ["In attesa", "In preparazione", "Pronto", "Consegnato"]
            scelta = int(input("Nuovo stato: ")) - 1
            
            if 0 <= scelta < 4:
                ordine["stato"] = stati[scelta]
                print(f"✅ Stato aggiornato: {ordine['stato']}")
            else:
                print("❌ Scelta non valida!")
        else:
            print("❌ Ordine non trovato!")
    except:
        print("❌ Input non valido!")


def aggiungi_pizza():
    print("\n--- AGGIUNGI PIZZA ---")
    nome = input("Nome pizza: ")
    
    try:
        prezzo = float(input("Prezzo (€): "))
        nuovo_id = max(p["id"] for p in menu) + 1
        menu.append({"id": nuovo_id, "nome": nome, "prezzo": prezzo})
        print(f"✅ Pizza '{nome}' aggiunta!")
    except:
        print("❌ Prezzo non valido!")
        

def elimina_ordine():
    if not ordini:
        print("\n📋 Nessun ordine.")
        return
    
    lista_ordini()
    
    try:
        num = int(input("\nNumero ordine da eliminare: "))
        ordine = next((o for o in ordini if o["numero"] == num), None)
        
        if ordine:
            conferma = input(f"Eliminare ordine #{num}? (s/n): ")
            if conferma.lower() == "s":
                ordini.remove(ordine)
                print(f"✅ Ordine #{num} eliminato!")
            else:
                print("❌ Operazione annullata.")
        else:
            print("❌ Ordine non trovato!")
    except:
        print("❌ Input non valido!")


# === PROGRAMMA PRINCIPALE ===
print("""
╔═══════════════════════════════════════╗
║   🍕 GESTIONE PIZZERIA 🍕            ║
╚═══════════════════════════════════════╝
""")

while True:
    print("\n--- MENU ---")
    print("1. Visualizza Menu")
    print("2. Nuovo Ordine")
    print("3. Lista Ordini")
    print("4. Cambia Stato Ordine")
    print("5. Aggiungi Pizza")
    print("6. Elimina Ordine")
    print("0. Esci")
    
    scelta = input("\nScelta: ")
    
    if scelta == "1":
        mostra_menu()
    elif scelta == "2":
        nuovo_ordine()
    elif scelta == "3":
        lista_ordini()
    elif scelta == "4":
        cambia_stato()
    elif scelta == "5":
        aggiungi_pizza()
    elif scelta == "6":
        elimina_ordine()
    elif scelta == "0":
        print("\n👋 Arrivederci!")
        break
    else:
        print("❌ Scelta non valida!")