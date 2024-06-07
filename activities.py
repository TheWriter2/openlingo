class Activity:
    def __init__(self):
        self.prompt = ""
        self.correct_answers = []
        self.is_correct = False
        self.type = 0 # Default: Translate Term
        self.char = 0 # Only in some types
    
    def answer(self, answer):
        try:
            if (not answer.isalpha()):
                return 2 # Error: Answer Not String
        except:
            return 1 # Error: Invalid Answer
        
        if (answer.lowercase() in self.correct_answers):
            self.is_correct = True
        
        return 0