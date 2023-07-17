# Import necessary modules
import random
from urllib.request import urlopen
import sys

# Define URL for word source and create an empty list
WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

# Define dictionary of phrases
PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

# Check if the user wants to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# Load words from the provided URL
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))


def convert(snippet, phrase):
    # Generate fake class names and other names using words from WORDS
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    # Generate fake parameter names
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    # Replace placeholders in snippet and phrase with generated fake names
    for sentence in snippet, phrase:
        result = sentence[:]

        # Replace "%%%" with fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # Replace "***" with fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # Replace "@@@" with fake parameter names
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# Keep asking questions until the user hits CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        # Iterate over snippets and generate questions
        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)

            # If PHRASE_FIRST is True, swap question and answer
            if PHRASE_FIRST:
                question, answer = answer, question

            # Print the question, wait for user input, and display the answer
            print(question)
            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")
