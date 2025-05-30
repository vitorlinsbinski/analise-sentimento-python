import streamlit as st
from textblob import TextBlob
from deep_translator import GoogleTranslator

st.set_page_config(page_title='Análise de Sentimento', page_icon='💬', layout='centered')

st.markdown("<h1 style='color: #4B8BBE;'>💬 Análise de Sentimento de Textos</h1>", unsafe_allow_html=True)
st.markdown("<p>Insira um texto em qualquer idioma e veja a análise de sentimento!</p>", unsafe_allow_html=True)

with st.container():
    user_input = st.text_area('✍️ Digite o texto aqui', height=200)

if st.button('🔍 Analisar Sentimento'):
    if user_input.strip():
        try:
            translated_text = GoogleTranslator(source='auto', target='en').translate(user_input)
            
            blob = TextBlob(translated_text)
            sentiment = blob.sentiment

            st.markdown("### 📄 Texto traduzido:")
            st.info(translated_text)

            st.markdown("### 📊 Resultados da Análise:")
            col1, col2 = st.columns(2)
            col1.metric("Polaridade", f"{sentiment.polarity:.2f}")
            col2.metric("Subjetividade", f"{sentiment.subjectivity:.2f}")

            if sentiment.polarity > 0:
                st.success('Sentimento Positivo 😊')
            elif sentiment.polarity < 0:
                st.error('Sentimento Negativo 😞')
            else:
                st.info('Sentimento Neutro 😐')

        except Exception as e:
            st.error(f"❌ Ocorreu um erro durante a análise: {e}")
    else:
        st.warning('⚠️ Por favor, insira um texto para análise.')
