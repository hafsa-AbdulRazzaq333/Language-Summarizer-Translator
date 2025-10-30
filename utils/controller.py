from groq import Groq

from dotenv import load_dotenv
import os
load_dotenv()  # Isse .env file ki values environment mein load ho jayengi

api_key = os.getenv("GROQ_API_KEY")

def summarize_and_translate(sentence, target_language):
    client = Groq(api_key=api_key)

    # Step 1️⃣ — Summarize
    summarize_prompt = f"Summarize the following text in a concise and clear way:\n\n{sentence}"
    summary_response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": summarize_prompt}
        ],
        temperature=1,
        max_tokens=512,
        top_p=1,
        stream=False,
        stop=None,
    )

    summary = summary_response.choices[0].message.content.strip()

    # Step 2️⃣ — Translate
    translate_prompt = f"Translate the following text into {target_language}:\n\n{summary}"
    translation_response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": translate_prompt}
        ],
        temperature=1,
        max_tokens=512,
        top_p=1,
        stream=False,
        stop=None,
    )

    translation = translation_response.choices[0].message.content.strip()

    return summary, translation
