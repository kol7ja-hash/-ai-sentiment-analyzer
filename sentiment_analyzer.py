"""
АНАЛИЗАТОР ТОНАЛЬНОСТИ ТЕКСТА
Готовый проект для портфолио

Использование:
    python sentiment_analyzer.py
"""

import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

from transformers import pipeline
import torch

print("=" * 60)
print("АНАЛИЗАТОР ТОНАЛЬНОСТИ ТЕКСТА")
print("=" * 60)

# Проверка GPU
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"\nИспользуется: {device}")

# Создаем анализатор
print("\n[INFO] Загрузка модели...")
classifier = pipeline("sentiment-analysis", device=0 if device == 'cuda' else -1)
print("[OK] Модель загружена!")

# Примеры текстов для анализа
texts = [
    "Я люблю программирование и AI!",
    "Это был ужасный день, всё пошло не так.",
    "Отличная работа! Всё получилось идеально.",
    "Нейронные сети - это будущее технологий.",
    "Сегодня плохая погода, не хочется выходить."
]

print("\n" + "=" * 60)
print("АНАЛИЗ ТЕКСТОВ")
print("=" * 60)

for i, text in enumerate(texts, 1):
    result = classifier(text)[0]
    label = result['label']
    score = result['score']
    
    # Переводим на русский
    if label == 'POSITIVE':
        label_ru = 'ПОЗИТИВНО'
        emoji = '😊'
    else:
        label_ru = 'НЕГАТИВНО'
        emoji = '😞'
    
    print(f"\n[{i}] {text}")
    print(f"    Результат: {label_ru} {emoji} (уверенность: {score:.2%})")

print("\n" + "=" * 60)
print("✅ АНАЛИЗ ЗАВЕРШЕН!")
print("=" * 60)

print("\n💡 ИДЕИ ДЛЯ УЛУЧШЕНИЯ:")
print("1. Добавьте веб-интерфейс (Streamlit/Gradio)")
print("2. Создайте API (FastAPI)")
print("3. Добавьте анализ файлов")
print("4. Интегрируйте в Telegram бота")

print("\n📝 ДЛЯ ПОРТФОЛИО:")
print("1. Загрузите на GitHub")
print("2. Добавьте README с описанием")
print("3. Создайте демо (Gradio)")
print("4. Укажите в профиле на Upwork/Fiverr")
