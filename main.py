import random

class SimpleAIChat:
    """Prosta klasa symulująca czat AI"""
    
    def __init__(self):
        self.responses = {
            "cześć": ["Cześć!", "Witaj!", "Hej!"],
            "jak się masz": ["Działam poprawnie!", "Wszystko w porządku!", "Gotowy do pracy!"],
            "co robisz": ["Uczę się!", "Przetwarzam dane!", "Czekam na Twoje pytania!"],
            "kim jesteś": ["Jestem prostym botem AI.", "Jestem symulacją czatu.", "Jestem Twoim asystentem."],
        }
    
    def get_response(self, user_input):
        """Generuje odpowiedź na podstawie inputu użytkownika"""
        user_input = user_input.lower().strip()
        
        # Sprawdź dopasowania
        for key, responses in self.responses.items():
            if key in user_input:
                return random.choice(responses)
        
        # Domyślne odpowiedzi
        default_responses = [
            "Nie rozumiem, ale się uczę!",
            "Ciekawe pytanie! Niestety nie mam na nie odpowiedzi.",
            "Możesz powtórzyć inaczej?",
            "Przepraszam, nie znam jeszcze tej funkcji."
        ]
        return random.choice(default_responses)

def main():
    chat = SimpleAIChat()
    print("AI Chat Bot (wpisz 'wyjdź' aby zakończyć)")
    print("-" * 40)
    
    while True:
        user_input = input("Ty: ")
        
        if user_input.lower() in ['wyjdź', 'exit', 'quit']:
            print("Bot: Do widzenia!")
            break
        
        response = chat.get_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()