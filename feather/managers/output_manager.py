class OutputManager:
    def __init__(self):
        self.history = []

    def print(self, text):
        self.history[-1]["outputs"].append(text)
        print("\n", text)
    
    def save_input(self, text):
        self.history.append({
            "input": text,
            "outputs": []})
