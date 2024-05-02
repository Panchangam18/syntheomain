import os
import random
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google.generativeai.types.generation_types import StopCandidateException

load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.json['message']
    request_type = request.json.get('requestType', '')
    response, genre, lyrics, title = generate_response(message, request_type)
    return jsonify({'response': response, 'genre': genre, 'lyrics': lyrics, 'title': title})

def generate_response(message, request_type):
    safety_instruction = "Please ensure that the content you generate is safe, appropriate, and free from explicit or harmful language."
    genre_instruction = "If the user wants a specific genre, assign this to the variable genre in the code by responding with 'Genre: [chosen genre]'."
    genre = ""
    lyrics_instruction = "Generate two verses of lyrics for a song in the " + genre + " genre based on the user's input. Respond with 'Lyrics: [generated lyrics]'. " + safety_instruction
    lyrics = ""
    title_instruction = "Suggest a title for the song based on the generated lyrics and the " + genre + " genre. Respond with 'Title: [suggested title]'. " + safety_instruction
    title = ""
    try:
        if request_type == 'genre':
            chat_response = chat.send_message(genre_instruction + safety_instruction + " " + message)
            response = chat_response.text
            if "Genre:" in response:
                genre = response.split("Genre:")[-1].strip()
                response = f"Selected genre: {genre}"
            else:
                response = "I'm sorry, I couldn't identify the genre from your input. Please try again."
        elif request_type == 'lyrics':
            chat_response = chat.send_message(lyrics_instruction + safety_instruction + " " + message)
            response = chat_response.text
            if "Lyrics:" in response:
                lyrics = response.split("Lyrics:")[-1].strip()
                response = f"Generated lyrics:\n{lyrics}"
            else:
                response = "I'm sorry, I couldn't generate lyrics based on your input. Please try again."
        elif request_type == 'title':
            chat_response = chat.send_message(title_instruction + safety_instruction + " " + message)
            response = chat_response.text
            if "Title:" in response:
                title = response.split("Title:")[-1].strip()
                response = f"Suggested title: {title}"
            else:
                response = "I'm sorry, I couldn't suggest a title based on your input. Please try again."
        else:
            chat_response = chat.send_message(safety_instruction + " " + message)
            response = chat_response.text
    except StopCandidateException as e:
        response = "I apologize, but the generated content contained inappropriate or explicit language. Please try again with different input."
    return response, genre, lyrics, title

if __name__ == '__main__':
    app.run(debug=True)