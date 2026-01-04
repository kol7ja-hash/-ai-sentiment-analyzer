# 🤖 Анализатор тональности текста

Профессиональный AI-анализатор тональности текста с веб-интерфейсом, созданный с помощью PyTorch и Transformers.

## ✨ Возможности

- 📊 Анализ тональности текста (позитивный/негативный)
- 🎯 Высокая точность (97%+)
- 🚀 Работа на GPU (CUDA)
- 🌐 Красивый веб-интерфейс (Gradio)
- ⚡ Быстрая обработка

## 🛠️ Технологии

- **Python 3.13**
- **PyTorch 2.7.1+cu118** (с поддержкой CUDA)
- **Transformers** (Hugging Face)
- **Gradio** (веб-интерфейс)
- **NVIDIA CUDA 11.8**

## 📋 Требования

- Python 3.10+
- CUDA Toolkit 11.8+ (для GPU)
- NVIDIA GPU (опционально, но рекомендуется)

## 🚀 Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/kol7ja-hash/ai-sentiment-analyzer.git
cd ai-sentiment-analyzer
```

2. Установите зависимости:
```bash
pip install -r requirements_simple.txt
```

## 💻 Использование

### Командная строка:
```bash
python sentiment_analyzer.py
```

### Веб-интерфейс:
```bash
python sentiment_web.py
```

Откройте браузер по адресу: http://127.0.0.1:7860

## 🌐 Демо

Попробуйте онлайн: https://huggingface.co/spaces/Nik26ru/sentiment-analyzer

## 🎯 Примеры использования

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
result = classifier("Я люблю программирование!")
print(result)
# [{'label': 'POSITIVE', 'score': 0.9767}]
```

## 📝 Лицензия

MIT License

## 🔗 Ссылки

- [PyTorch](https://pytorch.org/)
- [Hugging Face](https://huggingface.co/)
- [Gradio](https://gradio.app/)

---

**Создано с ❤️ для портфолио**

