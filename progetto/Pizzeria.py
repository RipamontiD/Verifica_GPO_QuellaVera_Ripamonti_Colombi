"""
Modulo per la gestione di una pizzeria.

Permette di gestire menu, ordini e stato delle consegne.
"""

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
    """
    Mostra il menu delle pizze disponibili.
    
    Stampa l'elenco completo delle pizze con ID, nome e prezzo.
    """
    print("\n" + "="*40)
    print("        🍕 MENU PIZZERIA 🍕")
    print("="*40)
    for pizza in menu:
        print(f"  {pizza['id']}. {pizza['nome']:<20} €{pizza['prezzo']:.2f}")
    print("="*40)


def nuovo_ordine():
    """
    Crea un nuovo ordine.
    
    Chiede il nome del cliente e permette di aggiungere pizze all'ordine.
    Calcola automaticamente il totale.
    """
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
    """
    Mostra tutti gli ordini.
    
    Visualizza numero, cliente, stato, pizze e totale di ogni ordine.
    """
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
    """
    Cambia lo stato di un ordine.
    
    Stati possibili: In attesa, In preparazione, Pronto, Consegnato.
    """
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
                
                if ordine["stato"] == "Consegnato":
                    stampa_scontrino(ordine)
            else:
                print("❌ Scelta non valida!")
        else:
            print("❌ Ordine non trovato!")
    except:
        print("❌ Input non valido!")


def aggiungi_pizza():
    """
    Aggiunge una nuova pizza al menu.
    
    Chiede nome e prezzo della nuova pizza.
    """
    print("\n--- AGGIUNGI PIZZA ---")
    nome = input("Nome pizza: ")
    
    try:
        prezzo = float(input("Prezzo (€): "))
        nuovo_id = max(p["id"] for p in menu) + 1
        menu.append({"id": nuovo_id, "nome": nome, "prezzo": prezzo})
        print(f"✅ Pizza '{nome}' aggiunta!")
    except:
        print("❌ Prezzo non valido!")
        


def stampa_scontrino(ordine):
    """
    Stampa lo scontrino di un ordine.
    
    Genera uno scontrino formattato con intestazione pizzeria,
    dettagli ordine, elenco pizze e totale.
    
    Args:
        ordine: Dizionario contenente numero, cliente, pizze e totale.
    """
    print("\n")
    print("╔════════════════════════════════════╗")
    print("║        🍕 PIZZERIA ITALIA 🍕       ║")
    print("║       Via Roma 123, Milano         ║")
    print("║         Tel: 02-1234567            ║")
    print("╠════════════════════════════════════╣")
    print(f"║  Ordine: #{ordine['numero']:<10}              ║")
    print(f"║  Cliente: {ordine['cliente']:<15}       ║")
    print("╠════════════════════════════════════╣")
    
    for p in ordine["pizze"]:
        print(f"║  {p['quantita']}x {p['nome']:<18} €{p['prezzo']:>6.2f} ║")
    
    print("╠════════════════════════════════════╣")
    print(f"║  TOTALE:                  €{ordine['totale']:>6.2f} ║")
    print("╠════════════════════════════════════╣")
    print("║         Grazie e arrivederci!      ║")
    print("╚════════════════════════════════════╝")
    print("\n")


# === PROGRAMMA PRINCIPALE ===
if __name__ == "__main__":
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