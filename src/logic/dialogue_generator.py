# src/logic/dialogue_generator.py

from src.utils.openai_client import call_openai_chat

class DialogueGenerator:
    def __init__(self, system_prompt=None):
        self.system_prompt = system_prompt or "Ти ввічливий агент школи усного рахунку Соробан."
        self.messages = [{"role": "system", "content": self.system_prompt}]

    def add_user_input(self, user_input):
        self.messages.append({"role": "user", "content": user_input})

    def generate_reply(self, functions=None):
        response = call_openai_chat(self.messages, functions=functions)
        reply = response.choices[0].message
        self.messages.append(reply)
        return reply