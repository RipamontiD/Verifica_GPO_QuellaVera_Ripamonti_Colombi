import unittest
from progetto.Pizzeria import menu, ordini, numero_ordine


class TestMenu(unittest.TestCase):
    """Test per il menu della pizzeria."""
    
    def test_menu_non_vuoto(self):
        """Verifica che il menu contenga pizze."""
        self.assertGreater(len(menu), 0)
    
    def test_menu_ha_margherita(self):
        """Verifica che la Margherita sia nel menu."""
        nomi = [p["nome"] for p in menu]
        self.assertIn("Margherita", nomi)
    
    def test_menu_ha_marinara(self):
        """Verifica che la Marinara sia nel menu."""
        nomi = [p["nome"] for p in menu]
        self.assertIn("Marinara", nomi)
    
    def test_prezzi_positivi(self):
        """Verifica che tutti i prezzi siano positivi."""
        for pizza in menu:
            self.assertGreater(pizza["prezzo"], 0)
    
    def test_id_univoci(self):
        """Verifica che gli ID delle pizze siano univoci."""
        ids = [p["id"] for p in menu]
        self.assertEqual(len(ids), len(set(ids)))
    
    def test_struttura_pizza(self):
        """Verifica che ogni pizza abbia id, nome e prezzo."""
        for pizza in menu:
            self.assertIn("id", pizza)
            self.assertIn("nome", pizza)
            self.assertIn("prezzo", pizza)


class TestOrdini(unittest.TestCase):
    """Test per la gestione ordini."""
    
    def setUp(self):
        """Pulisce gli ordini prima di ogni test."""
        ordini.clear()
    
    def test_ordini_inizialmente_vuoti(self):
        """Verifica che la lista ordini parta vuota."""
        self.assertEqual(len(ordini), 0)
    
    def test_aggiunta_ordine(self):
        """Verifica che si possa aggiungere un ordine."""
        ordine = {
            "numero": 1,
            "cliente": "Mario",
            "pizze": [{"nome": "Margherita", "quantita": 2, "prezzo": 12.00}],
            "totale": 12.00,
            "stato": "In attesa"
        }
        ordini.append(ordine)
        self.assertEqual(len(ordini), 1)
    
    def test_struttura_ordine(self):
        """Verifica la struttura di un ordine."""
        ordine = {
            "numero": 1,
            "cliente": "Luigi",
            "pizze": [],
            "totale": 0,
            "stato": "In attesa"
        }
        ordini.append(ordine)
        
        self.assertIn("numero", ordini[0])
        self.assertIn("cliente", ordini[0])
        self.assertIn("pizze", ordini[0])
        self.assertIn("totale", ordini[0])
        self.assertIn("stato", ordini[0])
    
    def test_stati_validi(self):
        """Verifica che gli stati siano validi."""
        stati_validi = ["In attesa", "In preparazione", "Pronto", "Consegnato"]
        ordine = {
            "numero": 1,
            "cliente": "Test",
            "pizze": [],
            "totale": 0,
            "stato": "In attesa"
        }
        self.assertIn(ordine["stato"], stati_validi)
    
    def test_elimina_ordine(self):
        """Verifica che si possa eliminare un ordine."""
        ordine = {
            "numero": 1,
            "cliente": "Mario",
            "pizze": [],
            "totale": 0,
            "stato": "In attesa"
        }
        ordini.append(ordine)
        ordini.remove(ordine)
        self.assertEqual(len(ordini), 0)


class TestCalcoli(unittest.TestCase):
    """Test per i calcoli dei prezzi."""
    
    def test_calcolo_totale(self):
        """Verifica il calcolo del totale ordine."""
        margherita = next(p for p in menu if p["nome"] == "Margherita")
        quantita = 3
        totale = margherita["prezzo"] * quantita
        self.assertEqual(totale, 18.00)
    
    def test_prezzo_margherita(self):
        """Verifica il prezzo della Margherita."""
        margherita = next(p for p in menu if p["nome"] == "Margherita")
        self.assertEqual(margherita["prezzo"], 6.00)
    
    def test_prezzo_diavola(self):
        """Verifica il prezzo della Diavola."""
        diavola = next(p for p in menu if p["nome"] == "Diavola")
        self.assertEqual(diavola["prezzo"], 8.00)


if __name__ == "__main__":
    unittest.main()