# Workflow Logic: Soroban Sales Agent

This document describes the **logical sequence** of steps the AI sales agent follows when calling a cold prospect for the Soroban mental math school.
The purpose is to **book a free trial lesson**, or alternatively **schedule a callback**.

All phrases used in the dialogue are in **Ukrainian**.

---

## 🧭 Step-by-Step Workflow

### 1. Start Call
- Greet the respondent.
- Ask: "Доброго дня! Чи зручно вам зараз говорити буквально 1-2 хвилини?"
- If **No** → go to step 12 `Schedule Callback`
- If **Yes** → continue

### 2. Build Rapport
- Introduce yourself and the school: "Я телефоную зі школи ментального рахунку Соробан"

### 3. Ask Name
- "Як до вас звертатися?"
- Store name for personalization

### 4. Check for Kids 5–11 y.o.
- "Скажіть, будь ласка, у вас є діти віком 5–11 років?"
- If **No** → go to step 13 `End Dialogue`
- If **Yes** → continue

### 5. Present Method
- "У нас японська методика розвитку ментального рахунку."
- "Діти вчаться рахувати в умі швидше за калькулятор!"

### 6. Handle Objections / Questions
- Respond to concerns: "Це безкоштовно і ні до чого не зобов'язує. Просто подивіться."

### 7. Ask City
- "У якому місті ви знаходитесь?"
- Save city info before pricing

### 8. Ask Format
- "Вам зручніше займатись онлайн чи офлайн?"
- Save format info before pricing

### 9. Provide Price (only after city and format known)
- If user asks: "Скільки це коштує?"
- Respond: "Ціна залежить від формату й міста. Зараз дізнаюсь точну інформацію..."
- Trigger `get_price(city, format)` function (not shown here)

### 10. Offer Trial Lesson
- "Можемо записати вас на безкоштовне пробне заняття."

### 11. Ask Child Name
- "Як звати вашу дитину?"
- Save child’s name

### 12. Confirm Signup
- "Супер, я записую [ім'я дитини] на безкоштовний урок у [місто]."
- Trigger `sign_for_promo` function (not shown here)
- Go to step 14 `End Dialogue`

### 13. Schedule Callback
- "Коли вам буде зручно поговорити про пробний урок?"
- Save callback time and exit

### 14. End Dialogue
- "Дякую за час, гарного дня!"
- Conversation stops

---

## 🧩 Notes for Developers
- `get_price(city, format)` and `sign_for_promo(...)` are triggered only when prior required info is collected
- Dialogue must stop after successful promo sign-up or if no child in the target age
- If respondent cannot talk → schedule callback and exit
- No free trial offered if no children 5–11 y.o.

---

Use this logic to implement deterministic branching in the agent's behavior model.
