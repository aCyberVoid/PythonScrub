import random

def magic_8_ball():
    answers = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    
    # Prompt for user question
    question = input("Ask a question: ")
    
    # Randomly select an answer
    answer = random.choice(answers)
    
    print("Magic 8-Ball says:", answer)

# Run the magic 8-ball simulation
magic_8_ball()
