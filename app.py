import streamlit as st

import pathlib
import textwrap
import requests
import google.generativeai as genai
import json
import os



# VIDEO_URL = "https://example.com/not-youtube.mp4"
# st.video(VIDEO_URL)

def getSongUrl(title):
    url = "https://mothersuno-api.vercel.app/api/get?id"
    response = requests.get(url)
    response.json()
    for i in range(len(response.json())):
        if (response.json()[i]['title'] == title):
            return response.json()[i]['audio_url']

def generate_audio(lyrics, genre, title):
    url = "https://mothersuno-api.vercel.app/api/custom_generate"
    payload = {"prompt": lyrics, "tags" : genre, "title" : str(title), "make_instrumental": False, "wait_audio": False}
    response = requests.post(url,json=payload)
    return response.text

# print(str(title))
# print(lyrics)
# print(genre)



st.set_page_config(page_title="Syntheo", page_icon=":robot:")
st.header("Syntheo")

if "generated" not in st.session_state:
  st.session_state["generated"] = []

if "past" not in st.session_state:
  st.session_state["past"] = []

if "messages" not in st.session_state:
  st.session_state["messages"] = []

init_alr = False

def init_model(user_input):
    # os.environ["API_KEY"] = "AIzaSyAgqODyVqcqlsDC1Gzuy8TkpiWnQZVGovw"
    # genai.configure(api_key=os.environ.get("API_KEY"))
    # model = genai.GenerativeModel('gemini-pro')
    
    # userInput = user_input #"Give me an afrofunk beat along with a cool melody and catchy drums, along with an opera style"
    # prompt = userInput + ". Output ONLY the specific music genre that the user would like that fits their requirements, with no excess words. NO APOSTROPHES. Add more than one genre to best fit the user's prompt. Desired Output: <all_lowercase_comma_separated_genres>"
    # response = model.generate_content(prompt)
    # genre = response.text
    
    # userInput = "Genre: " + genre + ". Generate lyrics that would best fit into the required genre. Generate around 2 minutes worth of lyrics. Separate verses using [Verse #] and NO APOSTROPHES AT ALL. Desired Format: <seperate_each_verse_no_asteriks_or_apostrophes>"
    # response = model.generate_content(userInput)
    # lyrics = response.text
    
    # lyricInput = "Lyrics: " + lyrics[:25] + ". Based upon the following lyrics, please generate a title for this song. Desired Format: <title_case_without_genre>"
    # response = model.generate_content(lyricInput)
    # title = response.text

    # userInput = "Lyrics: " + lyrics + ". Split the following lyrics into ONLY 10 slices with each slice enhanced to describe a music video. You may slightlly alter the lyrics to best cater to this requirment. Each section is separated by a |. Use only 10 |'s. Delete ALL \n characters and Verse seperators as well. Desired Output: <|_separated>"
    # response = model.generate_content(userInput)
    # sepTen = response.text
    # whollySplit = sepTen.split("|")


    #generate_audio(lyrics, genre, title)
    
    #make API request
    #audiourl = getSongUrl(title)

    title = 'Realm of Whispers'
    genre = 'afrofunk, opera'

    lyrics = "[Verse 1]\nIn the realm where rhythms soar\nWhere funky beats ignite the core\nLike a cosmic dance, our spirits unite\nAs ancestral drums carry us through the night\n[Verse 2]\nAfrofunk's siren, a call so divine\nA symphony of souls, a musical shrine\nFrom Yoruba chants to Congolese grooves\nWe traverse the realms of mystical moves\n[Verse 3]\nVoices erupt in operatic splendor\nA timeless tapestry, a transcendent render\nEchoes of Verdi meet Fela's bold fire\nOpera's grandeur melds with funk's primal desire\n[Verse 4]\nIn this fusion of worlds, a cosmic delight\nWhere melodies soar to an ethereal height\nWe become vessels of musical ecstasy\nAfrofunk and opera, a symphony of majesty"
    

    audiourl = "https://cdn1.suno.ai/c94802b4-5624-48ee-8e85-44837ae69e4a.mp4"
    
    #call webscraping script
    #get_mp3("Samba Kickoff")

    return title, genre, lyrics, audiourl 

#st_callback = StreamlitCallbackHandler(st.container())



if prompt := st.chat_input():
    st.chat_message("user").write(prompt)
    with st.chat_message("assistant"):
        #st_callback = StreamlitCallbackHandler(st.container())

        if init_alr == False:
            init_alr = True
            
            title, genre, lyrics, audiourl  = init_model(prompt)
            #Call query generator with text_input
            #query = prompty(date_input, prompt)
            #result = qa({"query": query})
    
            st.write('Based on the interesting description you have provided, we will generate a ' + genre + ' music experience for you:')
            st.write('Title: ' + title)
            st.write('Lyrics: ' + lyrics)
            st.write('You can find the final generated mp4 file here: ' + audiourl)
            st.stop()
