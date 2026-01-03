"""
ВЕБ-ИНТЕРФЕЙС ДЛЯ АНАЛИЗАТОРА ТОНАЛЬНОСТИ
Создано с помощью Gradio

Использование:
    python sentiment_web.py
"""

import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

import gradio as gr
from transformers import pipeline
import torch

# Проверка GPU
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"Используется: {device}")

# Загрузка модели
print("Загрузка модели...")
classifier = pipeline("sentiment-analysis", device=0 if device == 'cuda' else -1)
print("Модель загружена!")

def analyze_text(text):
    """Анализирует тональность текста"""
    if not text.strip():
        return "Пожалуйста, введите текст для анализа"
    
    result = classifier(text)[0]
    label = result['label']
    score = result['score']
    
    if label == 'POSITIVE':
        label_ru = 'ПОЗИТИВНО 😊'
        color = "#28a745"
    else:
        label_ru = 'НЕГАТИВНО 😞'
        color = "#dc3545"
    
    return f"**Результат:** {label_ru}\n\n**Уверенность:** {score:.2%}"

# Создание интерфейса
interface = gr.Interface(
    fn=analyze_text,
    inputs=gr.Textbox(
        label="Введите текст для анализа",
        placeholder="Например: Я люблю программирование!",
        lines=5
    ),
    outputs=gr.Markdown(
        label="Результат анализа"
    ),
    title="🤖 Анализатор тональности текста",
    description="Введите текст, и AI определит, позитивный он или негативный",
    examples=[
        ["Я люблю программирование и AI!"],
        ["Это был ужасный день, всё пошло не так."],
        ["Отличная работа! Всё получилось идеально."],
        ["Нейронные сети - это будущее технологий."]
    ],
    theme=gr.themes.Soft()
)

# Запуск
if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("ЗАПУСК ВЕБ-ИНТЕРФЕЙСА")
    print("=" * 60)
    print("\nОткроется браузер с веб-интерфейсом")
    print("Если браузер не открылся, перейдите по адресу:")
    print("http://localhost:7860")
    print("\nДля остановки нажмите Ctrl+C")
    print("=" * 60 + "\n")
    
    interface.launch(share=False, server_name="127.0.0.1")
