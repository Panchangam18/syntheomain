import os
import random
import google.generativeai as genai
from dotenv import load_dotenv
from google.generativeai.types.generation_types import StopCandidateException

load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

print("Gemini: Hello! I'm Gemini, your AI song creation assistant. Let's create a wonderful song together!")

safety_instruction = "Please ensure that the content you generate is safe, appropriate, and free from explicit or harmful language."

# Genre selection loop
genre_instruction = "If the user wants a specific genre, assign this to the variable genre in the code by responding with 'Genre: [chosen genre]'."
genre = ""
while True:
    genre_question = input("You (genre): ")
    genre_response = chat.send_message(safety_instruction + " " + genre_instruction + " " + genre_question)
    print('\n')
    print(f"Bot (genre): {genre_response.text}")
    print('\n')
    if "Genre:" in genre_response.text:
        genre = genre_response.text.split("Genre:")[-1].strip()
        break

# print(f"Selected genre: {genre}")

# Lyrics generation loop
lyrics_instruction = "Generate two verses of lyrics for a song in the " + genre + " genre based on the user's input. Respond with 'Lyrics: [generated lyrics]'. " + safety_instruction
lyrics = ""
while True:
    lyrics_question = input("You (lyrics): ")
    try:
        lyrics_response = chat.send_message(safety_instruction + " " + lyrics_instruction + " " + lyrics_question)
        print('\n')
        print(f"Bot (lyrics): {lyrics_response.text}")
        print('\n')
        if "Lyrics:" in lyrics_response.text:
            lyrics = lyrics_response.text.split("Lyrics:")[-1].strip()
            break
    except StopCandidateException as e:
        print("Gemini: I apologize, but the generated lyrics contained content that triggered a safety rating.")
        print("Please provide different input or rephrase your request.")
        continue

# print(f"Generated lyrics:\n{lyrics}")

# Title generation loop
title_instruction = "Suggest a title for the song based on the generated lyrics and the " + genre + " genre. Respond with 'Title: [suggested title]'. " + safety_instruction
title = ""
while True:
    title_question = input("You (title): ")
    try:
        title_response = chat.send_message(safety_instruction + " " + title_instruction + " " + title_question)
        print('\n')
        print(f"Bot (title): {title_response.text}")
        print('\n')
        if "Title:" in title_response.text:
            title = title_response.text.split("Title:")[-1].strip()
            break
    except StopCandidateException as e:
        print("Gemini: I apologize, but the generated title contained content that triggered a safety rating.")
        print("Please provide different input or rephrase your request.")
        continue

print(f"Great we have all the information for your song. Click next!")