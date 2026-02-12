from dotenv import load_dotenv
import os

load_dotenv()


def main():
    openai_api_key = os.getenv("OPEN_AI_API_KEY")
    print(openai_api_key)
    print("Hello from langchain-course!")


if __name__ == "__main__":
    main()
