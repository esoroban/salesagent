# src/utils/openai_client.py

from openai import OpenAI
from src.config import MODEL_NAME, TEMPERATURE, MAX_TOKENS

# Создаём клиента (API-ключ берётся из переменной окружения OPENAI_API_KEY)
client = OpenAI()

def call_openai_chat(messages, functions=None, function_call="auto"):
    """
    Вызов OpenAI Chat API с поддержкой function calling (совместимо с SDK >= 1.0).

    Args:
        messages (list): [{'role': 'user'/'system'/'assistant', 'content': str}]
        functions (list): JSON-схема функций (опционально)
        function_call (str|dict): 'auto', 'none' или {"name": "название_функції"}

    Returns:
        object: Объект ответа от OpenAI (response.choices[0].message)
    """
    params = {
        "model": MODEL_NAME,
        "messages": messages,
        "temperature": TEMPERATURE,
        "max_tokens": MAX_TOKENS,
    }

    # Добавляем только если указаны функции
    if functions:
        params["functions"] = functions
        params["function_call"] = function_call

    response = client.chat.completions.create(**params)
    return response