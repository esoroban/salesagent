from src.logic.dialogue_generator import generate_dialogue

def main():
    dialogue = generate_dialogue()

    print("📞 Згенерований діалог:")
    for step in dialogue:
        print(step)

if __name__ == "__main__":
    main()