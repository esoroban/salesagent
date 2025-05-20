# memory_format.md

## 🧠 Memory Format for Sales AI Agent

This document defines the memory structure used by the AI agent throughout a dialogue. The memory helps the agent:

- Personalize responses using client data
- Track dialogue progress
- Trigger correct function calls
- Avoid repeating questions
- Handle objections and interest levels appropriately

---

## 1. 📌 Core Memory Fields

| Field               | Description |
|---------------------|-------------|
| `parent_name`       | Name of the parent (e.g., Олена). |
| `child_name`        | Name of the child (e.g., Марк). Stored even if no promo signup happens. |
| `city`              | City of the client (e.g., Львів). Required for price and scheduling. |
| `format`            | "онлайн" or "офлайн". Affects price and available promo options. |
| `phone`             | Client’s phone number, captured for callbacks. |
| `callback_time`     | Preferred time to call back, e.g., `"завтра о 15:00"`. |
| `last_user_message` | Latest user message (used for intent analysis or memory update). |
| `objections`        | List of objections (e.g., `"Дорого"`, `"Немає часу"`). Logged with `record_objection`. |
| `interest_level`    | Estimated interest level: `"high"`, `"medium"`, or `"low"`. |
| `price_requested`   | Boolean flag if `get_price` was triggered. |
| `promo_offered`     | Was the promotional lesson offered. |
| `promo_signed_up`   | Was the user successfully signed up via `sign_for_promo`. |
| `dialogue_stopped`  | Was the dialogue ended using `stop_dialogue`. |

---

## 2. 🧩 Memory Update Triggers

Memory is updated at specific steps:

- **After user message**:
  - `last_user_message` is always updated.
  - If it contains an objection → `record_objection` is called.

- **After successful function calls**:
  - `sign_for_promo` → updates `parent_name`, `child_name`, `city`, `format`, `promo_signed_up = true`.
  - `get_price` → sets `price_requested = true`.
  - `record_basic_info` → sets `parent_name`, `city`, `format` if provided.
  - `schedule_callback` → sets `phone` and `callback_time`.
  - `log_interest_level` → sets `interest_level`.

- **When stopping the dialogue**:
  - `stop_dialogue` → sets `dialogue_stopped = true`.

---

## 3. 🔄 Memory Between Steps

Memory is preserved across all steps of a single session and passed between:

- Prompt templates
- Dialogue generation logic
- Function call planning
- Post-function response creation

It behaves like a JSON object injected into every step.

### Example memory object:

```json
{
  "parent_name": "Олена",
  "child_name": "Марк",
  "city": "Львів",
  "format": "офлайн",
  "phone": "+380501234567",
  "callback_time": "завтра о 15:00",
  "last_user_message": "Давайте ви мені передзвоните завтра",
  "objections": ["Дорого", "Занадто зайняті"],
  "interest_level": "medium",
  "price_requested": true,
  "promo_offered": true,
  "promo_signed_up": false,
  "dialogue_stopped": false
}
```

---

## 4. 📥 Implementation Notes

- Memory should be used as source of truth—don't ask again what is already known.
- When calling functions, always take values from memory (`city`, `format`, etc.).
- If session restarts, memory can be recovered from dialogue history or CRM.
