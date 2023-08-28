import random
quotes = {
    'Inspirational': [
        {"Quotation": "Never regret being a good person,even to the wrong people. Y/our behaviour says everything about you and their behaviour says enough about them", "author": "Krishna"},
        {"Quotation": "If you focus on hurt, you will contimue to suffer. If you focus on the lesson,you will continue to grow.", "author": "Eleanor Roosevelt"},
        {"Quotation": "Sometimes the world seems against you/The journey may leave a scar/But sars can heal and reveal/just where you are.", "author": "Gramma Tala,Moana"},
        {"Quotation": "Embrace uncertainity. Some of the most beautiful chapters in our lives won't have a title until much later.", "author": "Bob Goff"},
        {"Quotation": "Be the moon and inspire people even when you're far from full", "author": "K.tolnoe"}
    ],
    'SUCCESS': [
        {"Quotation": "Success is no Accident.It is hardwork, perseverance, learning, studying, sacrifice and most of all.", "author": "Pele"},
        {"Quotation": "Today is your opportunity to build the tomorrow you want.", "author": "Ken Poirot"},
        {"Quotation": "Don't Let anybody work harder than you do", "author": "Serena williams"},
        {"Quotation": "If you can dream it,you can do it", "author": "Walt disney"},
        {"Quotation": "The only place where success comes before work is in the dictionary.", "author": "Vidal Sassoon"}
    ],
    'HAPPY':[
        {"Quotation":"and here you are living despite it all.","author":"Rupi Kaur"},
        {"Quotation":"Happiness means loving yourself and being less concerned with the approval of others.","author":"Owen Campbell"},
        {"Quotation":"Nothing that wear matters more than a smile.","author":"Dusk Words"},
        {"Quotation":"One pure moment holds the power to create infinite love.","author":"Welland-Crosby"},
        {"Quotation":"A happy soul is the best shield for a cruel world","author":"Atticus"}
    ],
    'LIFE': [
        {"Quotation": "Make Happiness a Priority and be gentle with Yourself in the process", "author": "Brownnie Ware"},
        {"Quotation": "Do not let the behaviour of others destroy your inner peace. ", "author": "Dalai Lama"},
        {"Quotation": "Life is all about balance.you don't always need to getting stuff done.Sometimes it's perfectly okay,and absolutely necessary to shut down.", "author": "Lori Deschene"},
        {"Quotation": "Life itself is a Privilege. But to live life to the fullest-well that is a choice.", "author": "Andy andrwes"},
        {"Quotation": "Life is either a daring adventure or nothing at all.", "author": "Helen Keller"}
    ],
    'LOVE': [
        {"Quotation": "Do not let the behaviour of Others destroy your inner peace", "author": "Dalai Lama"},
        {"Quotation": "Love is composed of a single soul inhabiting two bodies.", "author": "Aristotle"},
        {"Quotation":"A successful marriage requires falling in love many times, always with the same person.", "author": "Mignon McLaughlin"},
        {"Quotation": "The best thing to hold onto in life is each other.", "author": "Audrey Hepburn"},
        {"Quotation": "Life is short.Time is fast.No replay,No rewind.so enjoy every moment as it comes", "author": "Thakur"}
    ],
    'FRIENDSHIP': [
        {"Quotation": "Memories with the right people will always remain priceless", "author": "Kylen"},
        {"Quotation": "True friends are like bright sunflowers that never fade away,even over distance and time.", "author": "Marrie williams Johnstone"},
        {"Quotation": "A friend is one that knows you as you are,understands where you have been,accepts what you have been,and still,gently allows you to grow.", "author": "William Shakesspeare"},
        {"Quotation": "Good friends are like stars you don't always see them but you know they are there.", "author": "Heather stillufsen"},
        {"Quotation": "We need at least one friend who understands what we do not say", "author": "Sun wolf"}
    ],
    'WISDOM': [
        {"Quotation": "Don't compare yourself with anyone in this world.if you do so,you are insulting yourself.", "author": "Bill Gates"},
        {"Quotation": "Kindness is a language which the deaf can hear and the blind can see.", "author": "Mark Twain"},
        {"Quotation": "Don't belittle your worth, Just because someone couldn't see it.", "author": "Spoorthi"},
        {"Quotation": "Knowledge speaks, but wisdom listens", "author": "Jimi Hendrix"},
        {"Quotation": "Knowing others is wisdom,knowing yourself is enlightenment.", "author": "Lao Tzu"}
    ]
}

def get_user_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.strip():
            return user_input.strip()
        print("Invalid input. Please try again.")

def generate_quote():
    Name = get_user_input("Enter your name: ")
    name=Name.upper()
    print()

    print("Select the category of your choice for the Quote: ")
    categories = list(quotes.keys())
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category.capitalize()}")

    while True:
        category_choice = get_user_input("Enter the category number: ")
        if category_choice.isdigit() and 1 <= int(category_choice) <= len(categories):
            category = categories[int(category_choice) - 1]
            break
        print("OOPS.. Error have been Occured Retry Once again by Providing valid Choice.")

    random_quote = random.choice(quotes[category])
    quote = random_quote["Quotation"]
    author = random_quote["author"]

    formatted_quote = f"{name}, {quote} - {author}"
    print(f"\n Hello {formatted_quote}")

generate_quote()