import re

class RuleBot:
    def __init__(self):
        # Dictionary mapping regex patterns to predefined responses
        self.rules = {
            r'\b(hi|hello|hey|greetings)\b': "Hello there! How can I help you today?",
            r'\b(how are you|how do you do)\b': "I'm just a rule-based bot, but I'm operating at 100% capacity! How are you?",
            r'\b(name|who are you)\b': "I am a simple rule-based chatbot built for Task 1.",
            r'\b(internship|codsoft|task)\b': "It sounds like you are working on your portfolio! Keep up the great work.",
            r'\b(java|python|code)\b': "I love talking about code. Though I'm written in Python right now, Java is fantastic for robust systems.",
            r'\b(help|support|assist)\b': "I can answer basic greetings and questions. Try asking about my name or your code!",
            r'\b(bye|exit|quit)\b': "Goodbye! Have a highly productive day.",
        }
        # Fallback response if no patterns match
        self.default_response = "I'm sorry, my rules don't cover that yet. Could you try rephrasing?"

    def generate_response(self, user_input):
        """Scans input against regex patterns and returns the matched response."""
        user_input = user_input.lower()
        
        for pattern, response in self.rules.items():
            if re.search(pattern, user_input):
                return response
                
        return self.default_response

    def chat(self):
        """Starts the interactive terminal chat loop."""
        print("--- Rule-Based Chatbot Initialized ---")
        print("Type 'quit' or 'exit' to end the conversation.\n")
        
        while True:
            user_input = input("You: ")
            
            # Prevent empty inputs from crashing the loop
            if not user_input.strip():
                continue
                
            response = self.generate_response(user_input)
            print(f"Bot: {response}\n")
            
            # Break the loop if the user wants to leave
            if re.search(r'\b(bye|exit|quit)\b', user_input.lower()):
                break

if __name__ == "__main__":
    bot = RuleBot()
    bot.chat()
