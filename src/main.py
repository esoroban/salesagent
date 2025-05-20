# src/main.py

from src.logic.dialogue_generator import DialogueGenerator

def run_single_dialogue():
    print("=== СИМУЛЯЦІЯ ДІАЛОГУ ===")
    dg = DialogueGenerator()

    while True:
        user_input = input("\n👤 Клієнт: ")
        if user_input.lower() in ("вихід", "exit", "quit"):
            print("🛑 Діалог завершено.")
            break

        dg.add_user_input(user_input)
        reply = dg.generate_reply()

        if hasattr(reply, "function_call") and reply.function_call:
            print(f"\n🤖 Виклик функції: {reply.function_call}")
        else:
            print(f"\n🤖 Агент: {reply.content}")

if __name__ == "__main__":
    run_single_dialogue()