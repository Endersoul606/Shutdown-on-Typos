import keyboard, time, os, subprocess

def load_dictionary(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dictionary file ‘{file_path}’ not found.")
    with open(file_path, "r", encoding="utf-8") as f:
        return set(word.strip().lower() for word in f if word.strip())

def on_typo(word):
    print(f"[TYPO DETECTED] '{word}' is not in dictionary!")
    subprocess.run(['shutdown', '-s', '-f', '-t', '0'])

def main():
    dictionary = load_dictionary("words.txt")
    current_word = ""

    print("Program Started")

    while True:
        try:
            event = keyboard.read_event()

            if event.event_type != keyboard.KEY_DOWN:
                continue

            if event.name in ("space", "enter", "tab"):
                if current_word:
                    if current_word.lower() not in dictionary:
                        on_typo(current_word)
                current_word = ""
                continue

            if event.name == "backspace":
                if current_word:
                    current_word = current_word[:-1]
                continue

            if isinstance(event.name, str) and len(event.name) == 1 and event.name.isalpha():
                current_word += event.name.lower()
                continue

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(0.5)

if __name__ == "__main__":
    main()