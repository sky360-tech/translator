from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

if __name__ == "__main__":
    print("Welcome to the Language Translator!")
    while True:
        source_text = input("Enter the text you want to translate (or 'q' to quit): ")
        if source_text.lower() == 'q':
            break
        target_language = input("Enter the language code you want to translate to (e.g., 'fr' for French, 'es' for Spanish): ")
        translated_text = translate_text(source_text, target_language)
        print(f"Translated Text: {translated_text}\n")