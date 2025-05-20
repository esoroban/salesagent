# 📁 Project Index: Soroban AI Sales Agent Dataset

## 1. Agent Goals
**File:** `agent_goals.md`  
**Purpose:**  
Defines the high-level goals of the AI sales agent during cold calls:
- Check if the respondent is available to talk
- Collect their name
- Determine if they have children aged 5–11
- Present the Soroban methodology
- Handle objections
- Offer and schedule a promo lesson
- End or defer the conversation

---

## 2. Workflow Logic
**File:** `workflow_logic.md`  
**Purpose:**  
Step-by-step logic for agent actions and decisions.  
Includes:
- Format clarification (online/offline)
- City confirmation
- Transitions based on user responses
- Links to function calls

---

## 3. Function Call Schema
**File:** `functions_schema.json`  
**Purpose:**  
JSON structure defining callable functions.  
Functions include:
- `get_price`
- `sign_for_promo`
- `schedule_callback`
- `stop_dialogue`
- `record_basic_info`
- `record_child_name`
- `record_objection`
- `log_interest_level`

---

## 4. Prompt Templates
**File:** `prompt_templates.md`  
**Purpose:**  
Templates (in Ukrainian) used by the agent for:
- Greetings
- Questions and interest discovery
- Promo offer
- Ending conversation  
Aligned with `workflow_logic.md` and supports function invocations from `functions_schema.json`.

---

## 5. Client Profile Fields
**File:** `client_profile_fields.md`  
**Purpose:**  
List of user information fields the agent should collect:  
name, city, lesson format, child's age, etc.

---

## 6. Objections and Answers
**File:** `objections_and_answers.md`  
**Purpose:**  
Reference list of common objections (in Ukrainian) and agent replies.  
Supports `record_objection` function usage.

---

## 7. Memory Format
**File:** `memory_format.md`  
**Purpose:**  
Describes what data the agent remembers and transfers between dialogue steps:  
name, city, interest, format, child’s name, etc.  
Written in English for internal logic use.

---

## 8. Fail Scenarios
**File:** `fail_scenarios.md`  
**Purpose:**  
Guide for handling failed or incomplete calls (in Ukrainian):
- User hangs up
- Misunderstanding
- Refuses to talk
- Requests a callback

---

This index provides a complete reference for maintaining consistency across prompt generation, memory usage, and function call logic for the Soroban sales agent.
