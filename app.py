import streamlit as st
import numpy as np
from llm import generate_response


# streamlit run app.py

# Конфиг страницы
st.set_page_config(
    page_title='Генерация отчёта по КНИР',
    page_icon="🧙‍♂️",
    initial_sidebar_state="expanded",
)
st.title('Генерация отчёта по КНИР📝')

# Ввод текста
txt_input = st.text_area('Введите запрос:', '',
                         height=275, key='example_text')

col1, col2, col3 = st.columns(3)
with col2:
    button_submit = st.button("Сгенерировать отчёт📄")

if button_submit:  # при нажатии кнопки на генерацию
    container = st.container()
    header = container.empty()
    header.write("Генерация ответа...")
    placeholders = []
    for i in range(1):
        placeholder = container.empty()
        placeholders.append(placeholder)

    placeholders[0].status("Генерация...")

    # =============== Генерация ответа ===============
    response = generate_response(txt_input)

    # =============== Отображение ответа ===============
    placeholders[0].info(response)

    header.write("Генерация завершена!")
