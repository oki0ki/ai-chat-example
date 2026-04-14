# AI Chat Example

Prosty przykład czatu AI napisany w Pythonie. Projekt demonstruje podstawowe mechanizmy działania bota odpowiadającego na wiadomości użytkownika.

## Funkcje

- Prosta obsługa powitań
- Odpowiedzi na podstawowe pytania
- Losowanie odpowiedzi z puli
- Łatwa rozbudowa o nowe funkcje

## Wymagania

- Python 3.6+

## Instalacja

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/oki0ki/ai-chat-example.git
   cd ai-chat-example
   ```

2. Uruchom program:
   ```bash
   python main.py
   ```

## Przykład użycia

```
AI Chat Bot (wpisz 'wyjdź' aby zakończyć)
----------------------------------------
Ty: cześć
Bot: Witaj!
Ty: jak się masz?
Bot: Działam poprawnie!
Ty: wyjdź
Bot: Do widzenia!
```

## Rozwój

Aby dodać nowe odpowiedzi, edytuj słownik `self.responses` w klasie `SimpleAIChat`.

## Licencja

MIT