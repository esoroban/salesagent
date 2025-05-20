# Project Structure Reference: Soroban Sales Dialogue Generator

This document describes the directory and file layout of the AI-powered dialogue generation system for cold calls (Soroban mental arithmetic school).

---

## 📁 /src — Python Source Code

| File/Folder             | Description |
|-------------------------|-------------|
| `main.py`               | Entry point script that generates a single dialogue using OpenAI API |
| `generate_batch.py`     | Script to generate a batch of dialogues using configuration |
| `config.py`             | Central configuration file: paths, OpenAI API setup, defaults |

### /src/prompts — Prompt Templates
| File                    | Description |
|-------------------------|-------------|
| `templates.py`          | Loads and manages prompt templates from `prompt_templates.md` |
| `system_messages.py`    | System-level prompts (e.g., instructions for LLM agents) |

### /src/logic — Dialogue Generation Logic
| File                    | Description |
|-------------------------|-------------|
| `dialogue_generator.py` | Step-by-step dialogue generation logic |
| `step_logic.py`         | Workflow transitions and condition handling |
| `memory.py`             | State memory manager between dialogue steps |

### /src/functions — Tool Calls (Mocked)
| File                    | Description |
|-------------------------|-------------|
| `schema.py`             | Parses and exposes tool schemas from `functions_schema.json` |
| `fake_executor.py`      | Returns JSONs simulating function tool calls (e.g. `get_price`, `sign_for_promo`) |

### /src/utils — Helpers and Utilities
| File                    | Description |
|-------------------------|-------------|
| `file_io.py`            | Load/save JSONs and logs |
| `text_cleaner.py`       | Normalize or sanitize dialogue text |
| `random_utils.py`       | Random names, city selection, etc. |

---

## 📁 /data — Knowledge Base and Source Files

| File                          | Description |
|-------------------------------|-------------|
| `prompt_templates.md`         | Ukrainian prompt templates for greetings, price, closing, etc. |
| `workflow_logic.md`           | Call flow logic with steps and transitions |
| `agent_goals.md`              | What the AI sales agent should achieve |
| `objections_and_answers.md`   | Common objections and suggested replies |
| `client_profile_fields.md`    | List of data points to collect during the call |
| `fail_scenarios.md`           | What to do in failure or edge cases |
| `memory_format.md`            | Rules on what the AI must remember between turns |
| `functions_schema.json`       | Schema of all tools used in dialogue (as OpenAI functions) |
| `index.md`                    | Project overview and role of each file |

---

## 📁 /notebooks — Analysis

| File                | Description |
|---------------------|-------------|
| `analysis.ipynb`    | Jupyter notebook for testing, debugging, and reviewing generated dialogues |