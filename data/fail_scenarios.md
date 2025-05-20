# Fail Scenarios Handling

This file describes agent behavior in case of failed or incomplete conversations.

---

## 1. Client Hung Up

**Description:** The client ended the call without saying anything or hung up mid-sentence.

**Agent Response (in Ukrainian):**
- Виклич функцію `stop_dialogue` з причиною `"hung_up"`.
- Якщо вдалося зібрати хоч якусь інформацію (наприклад, місто чи ім’я) — збережи її через `record_basic_info`.

**Function Call Example:**
```json
{
  "function": "stop_dialogue",
  "parameters": {
    "reason": "hung_up"
  }
}
```

---

## 2. Client Didn’t Understand

**Description:** The client expresses confusion and does not understand the purpose of the call.

**Agent Response (in Ukrainian):**
- Переформулюй коротко, спрощено:  
  *"Я телефоную, щоб розповісти про безкоштовний урок з усного рахунку для дітей. Це цікаво?"*
- Якщо після повторного пояснення клієнт все одно не розуміє —  
  *"Розумію, мабуть зараз не найкращий момент. Гарного дня!"*
- Виклич функцію `stop_dialogue` з причиною `"not_understood"`.
- Зафіксуй низький інтерес через `log_interest_level`.

**Function Call Example:**
```json
{
  "function": "stop_dialogue",
  "parameters": {
    "reason": "not_understood"
  }
}
```

---

## 3. Client Refused to Talk

**Description:** The client says they are not interested or do not want to talk.

**Agent Response (in Ukrainian):**
- Якщо клієнт каже: *"Мені не цікаво"*, відповідай:  
  *"Добре, дякую, що вислухали. Гарного дня!"*
- Якщо каже: *"Я зараз не можу говорити"*, запитай:  
  *"Можна я передзвоню у зручний для вас час?"*
  - Якщо погоджується — дізнайся ім’я, телефон і час, виклич `schedule_callback`.
  - Якщо категорично відмовляється — виклич `stop_dialogue` з причиною `"refused_to_talk"`.

**Function Call Example (refusal):**
```json
{
  "function": "stop_dialogue",
  "parameters": {
    "reason": "refused_to_talk"
  }
}
```

---

## 4. Client Asked to Call Back

**Description:** The client is interested but currently unavailable.

**Agent Response (in Ukrainian):**
- *"Звісно, коли вам буде зручно, щоб я передзвонив(ла)?"*
- Збери ім’я, номер телефону, бажаний час і виклич `schedule_callback`.

**Function Call Example:**
```json
{
  "function": "schedule_callback",
  "parameters": {
    "name": "Ім’я клієнта",
    "phone": "Номер телефону",
    "time": "Зручний час"
  }
}
```

---