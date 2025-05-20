# src/config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Default OpenAI model configuration
MODEL_NAME = "gpt-4o"
TEMPERATURE = 0.7
MAX_TOKENS = 1000

# Prompt and schema paths (optional, for future use)
PROMPT_TEMPLATE_PATH = "data/prompt_templates.md"
FUNCTION_SCHEMA_PATH = "data/functions_schema.json"