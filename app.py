from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

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

# Globalna instancja bota
chat_bot = SimpleAIChat()

@app.route('/')
def index():
    """Strona główna z interfejsem czatu"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """API endpoint do obsługi wiadomości"""
    data = request.get_json()
    
    if not data or 'message' not in data:
        return jsonify({'error': 'Brak wiadomości'}), 400
    
    user_message = data['message']
    bot_response = chat_bot.get_response(user_message)
    
    return jsonify({
        'user_message': user_message,
        'bot_response': bot_response
    })

@app.route('/api/chat', methods=['GET'])
def chat_info():
    """Informacje o API"""
    return jsonify({
        'name': 'AI Chat Example API',
        'version': '1.0',
        'endpoints': {
            'POST /api/chat': 'Wyślij wiadomość i otrzymaj odpowiedź',
            'GET /api/chat': 'Informacje o API'
        }
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
