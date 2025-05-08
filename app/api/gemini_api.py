import google.generativeai as genai
from dotenv import load_dotenv
import base64
import os
import json  # Importing json module for returning JSON

base_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(base_dir, 'api_key.env')

# Load the .env file
env_loaded = load_dotenv(dotenv_path)
print(f"✅ .env file loaded: {env_loaded}")

api_key = os.getenv('GEMINI_API_KEY')

# Configure Gemini client
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

def parse_examples_from_response(response_text):
    examples = {}
    for line in response_text.strip().split('\n'):
        if ':' in line:
            category, example = line.split(':', 1)
            examples[category.strip()] = example.strip()
    return examples

def generate_euler_examples(euler_circuit):
    categories = [
        "Transportation", "Package Delivery", "Tourism", "Household Chores",
        "Work Tasks", "School Schedule", "Shopping", "Social Visits", "Sports", "Nature"
    ]

    prompt = f"""
        You are a creative assistant that helps explain Euler circuits through real-life stories.

        Given the Euler circuit: {euler_circuit}

        Make SURE that you will create an example for each categories.
        Generate exactly 10 meaningful real-world examples that follow the path of this Euler circuit, one for each of the following categories:
        {', '.join(categories)}.
        
        Don't put any starting remarks or something, just get to the point
        Each example must:
        - Clearly reflect the structure of the Euler circuit (i.e., visiting every edge once and returning to the starting point).
        - Be written in a storytelling tone (use a character or a relatable situation).
        - Use natural language and context to make the scenario easy to visualize.
        - Begin with the category in this format: Category: Story

        Only include categories that fit the circuit logically. Skip those that don't fit meaningfully.
        Make sure each example includes the specific path in parentheses at the end.
        

        

            References:
            ✨ Transportation: Every Saturday morning, Alex drives a loop to handle errands: he starts from home (A), stops at the grocery store (B) for food, picks up medicine at the pharmacy (C), drops off a parcel at the post office (D), makes a quick bank visit (F), fuels up at the gas station (E), and finally returns home (A).

            ✨ Package Delivery: A delivery driver begins their day at the depot (A). They drop packages at House 1 (B), 2 (C), 3 (D), 5 (F), and 4 (E) in that order—looping efficiently back to the depot (A) just in time for lunch.
        """

    try:
        response = model.generate_content(prompt)
        examples = parse_examples_from_response(response.text)
        return json.dumps(examples, indent=4)  # Return the examples as a nicely formatted JSON string
    except Exception as e:
        return json.dumps({"error": str(e)})  # Return error as JSON

# if __name__ == '__main__':
#     try:
#         examples = generate_euler_examples("A->B->C->D->F->E->G->H->A")
#         print(examples)  # This will print the JSON formatted examples
#     except Exception as e:
#         print(f"❌ Unexpected Error: {e}")


