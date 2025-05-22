import streamlit as st
from textblob import TextBlob
from deep_translator import GoogleTranslator

st.title('Análise de Sentimento de Textos')
st.write('Insira um texto em qualquer idioma para analisar o sentimento:')

user_input = st.text_area('Digite o texto aqui')

if user_input.strip():
    translated_text = GoogleTranslator(source='auto', target='en').translate(user_input)
else:
    translated_text = ''
    
if st.button('Analisar'):
    if translated_text:
        blob = TextBlob(translated_text)
        sentiment = blob.sentiment
        st.write(f'**Texto traduzido:** {translated_text}')
        st.write(f'**Polaridade:** {sentiment.polarity:.2f}')
        st.write(f'**Subjetividade:** {sentiment.subjectivity:.2f}')
        if sentiment.polarity > 0:
            st.success('Sentimento Positivo')
        elif sentiment.polarity < 0:
            st.error('Sentimento Negativo')
        else:
            st.info('Sentimento Neutro')
    else:
        st.warning('Por favor, insira um texto para análise.')
