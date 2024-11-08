import random
import time

class PythonTeacherBot:
    def __init__(self):
        self.level = None
        self.resources = {
            "beginner": "https://www.python.org/about/gettingstarted/",
            "intermediate": "https://docs.python.org/3/tutorial/",
            "advanced": "https://realpython.com/intermediate-python-project-ideas/"
        }
        self.topics = {
            "1": ["variables", "data types", "operators", "control flow"],
            "2": ["functions", "modules", "file handling", "error handling"],
            "3": ["object-oriented programming", "decorators", "generators", "web scraping"]
        }

    def start(self):
        print("Welcome to Pybot, your Python teacher!")
        self.choose_level()
        self.chat()

    def choose_level(self):
        while True:
            print("\nChoose your level:")
            print("1. Beginner (starting from very basics)")
            print("2. Intermediate (assuming you know the basics)")
            print("3. Advanced (practice questions)")
            self.level = input("Enter your level (1/2/3): ")
            if self.level in ["1", "2", "3"]:
                break
            else:
                print("Invalid input. Please enter 1, 2, or 3.")

    def chat(self):
        print(f"\nGreat! You've selected {'Beginner' if self.level == '1' else 'Intermediate' if self.level == '2' else 'Advanced'} level.")
        print("Type 'quit' to exit, 'resource' for learning materials, or 'topic' to change the topic.")
        
        while True:
            user_input = input("\nYou: ").lower().strip()
            if user_input == "quit":
                print("Bot: Thank you for learning Python! Goodbye!")
                break
            elif user_input == "resource":
                self.provide_resource()
            elif user_input == "topic":
                self.change_topic()
            else:
                response = self.generate_response(user_input)
                self.slow_print(f"Bot: {response}")

    def generate_response(self, user_input):
        if self.level == "1":
            return self.beginner_response(user_input)
        elif self.level == "2":
            return self.intermediate_response(user_input)
        else:
            return self.advanced_response(user_input)

    def beginner_response(self, user_input):
        responses = {
        "variables": "Variables are containers for storing data values. In Python, you create a variable by assigning a value to it. For example: x = 5",
        "data types": "Python has several built-in data types including integers, floating-point numbers, strings, and booleans. You can use the type() function to check the type of a variable.",
        "operators": "Python supports various operators for arithmetic (+, -, *, /), comparison (==, !=, >, <), and logical operations (and, or, not).",
        "control flow": "Control flow in Python includes if-else statements for decision making, and loops like for and while for repetitive tasks.",
        "print": "The print() function is used to output text to the console. For example: print('Hello, World!')",
        "input": "The input() function allows you to get user input from the console. For example: name = input('What is your name? ')",
        "lists": "Lists are ordered collections of items in Python. You can create a list using square brackets: my_list = [1, 2, 3, 4]",
        "dictionaries": "Dictionaries are key-value pairs in Python. You can create a dictionary using curly braces: my_dict = {'name': 'John', 'age': 30}",
        "thank you": "Your welcome! Is there anything else you'd like to know about Python?"
        }
        return responses.get(user_input.lower(), f"I don't have specific information about '{user_input}'. Can you try asking about variables, data types, operators, control flow, print, input, lists, or dictionaries?")

    def intermediate_response(self, user_input):
        responses = {
            "functions": "Functions in Python are defined using the 'def' keyword. They can take parameters and return values. Functions help in code reusability and organization.",
            "modules": "Modules are Python files containing functions and variables. You can use the 'import' statement to use code from other modules in your program.",
            "file handling": "Python provides functions like open(), read(), write() for file operations. Always remember to close files after use or use the 'with' statement.",
            "error handling": "Use try-except blocks to handle exceptions in Python. This helps your program continue running even when errors occur."
        }
        return responses.get(user_input, "That's a good intermediate topic. Can you specify what aspect you're interested in?")

    def advanced_response(self, user_input):
        responses = {
            "object-oriented programming": "Here's a challenge: Create a class hierarchy for a zoo management system. Include methods for feeding animals and calculating costs.",
            "decorators": "Try this: Write a decorator that logs the arguments and return value of any function it decorates.",
            "generators": "Practice problem: Implement a generator function that yields prime numbers indefinitely.",
            "web scraping": "Project idea: Build a web scraper that extracts headlines from a news website and saves them to a CSV file."
        }
        return responses.get(user_input, "That's an advanced topic. Here's a general practice question: Implement a custom data structure in Python and explain its time complexity.")

    def provide_resource(self):
        level_name = "beginner" if self.level == "1" else "intermediate" if self.level == "2" else "advanced"
        print(f"Bot: Here's a great resource for {level_name} level: {self.resources[level_name]}")

    def change_topic(self):
        print("Bot: Sure, let's change the topic. Here are some suggestions:")
        for topic in self.topics[self.level]:
            print(f"- {topic}")
        print("What would you like to discuss?")

    def slow_print(self, text, delay=0.03):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

if __name__ == "__main__":
    bot = PythonTeacherBot()
    bot.start()