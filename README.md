# Soroban Sales Agent (AI Dialogue Generator)

AI-агент для генерації природних та переконливих діалогів під час холодних дзвінків батькам потенційних учнів школи усного рахунку **Соробан**.

---

## 🚀 Мета проекту

Цей агент виконує ролі:
- Вітання клієнта та перевірка, чи зручно говорити
- Збір імені клієнта, наявності дитини віком 5–11 років
- Коротка презентація методики Соробан
- Обробка типових заперечень
- Пропозиція пробного уроку
- Генерація JSON-функцій для запису, перенесення дзвінка, зупинки діалогу тощо

---

## 🧱 Структура проекту

```
soroban-sales-agent/
│
├── src/                    # Основна логіка генерації
│   ├── prompts/            # Шаблони промптів
│   ├── logic/              # Побудова діалогу, обробка пам'яті
│   ├── functions/          # JSON-функції (моки)
│   ├── utils/              # Допоміжні скрипти (OpenAI API, текст)
│   └── config.py           # API ключі, модель, параметри
│
├── data/                   # Вхідні файли: шаблони, логіка, функції
├── notebooks/              # Тестові/аналітичні ноутбуки
├── main.py                 # Точка входу для генерації діалогу
├── requirements.txt        # Залежності
├── .env                    # 🔒 API-ключ OpenAI (НЕ комітити)
└── .gitignore              # Ігнорує venv, .env тощо
```

---

## ⚙️ Установка

```bash
git clone https://github.com/esoroban/salesagent.git
cd soroban-sales-agent

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

Створи `.env` файл:

```env
OPENAI_API_KEY=sk-ваш_ключ
```

---

## ▶️ Запуск

```bash
PYTHONPATH=. python src/main.py
```

---

## 📚 Джерела даних

Файли в `data/` містять:
- `prompt_templates.md` — тексти агенту
- `workflow_logic.md` — логіка кроків
- `functions_schema.json` — JSON-функції
- `objections_and_answers.md` — типові заперечення

---

## ✅ Функції, які підтримуються

- `get_price(city, format)`
- `sign_for_promo(parent_name, child_name, city, format)`
- `schedule_callback(name, phone, time)`
- `stop_dialogue(reason)`
- `record_objection(text)`
- `log_interest_level(level)`

---

## 🧠 Памʼять між кроками

Агент запамʼятовує імʼя батьків, місто, формат навчання, імʼя дитини, рівень інтересу, заперечення та виклики функцій.

---

## 🛠️ Плани розвитку

- Підключення реального API OpenAI
- Підтримка багатьох діалогів одночасно
- Фільтрація діалогів за сценаріями (успішний, відмова, відкладений)

---

## 👤 Автор

Проект створено Iurii Novoselov як частина автоматизації продажів франшизи Соробан.