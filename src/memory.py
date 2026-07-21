class ChatMemory:
    def __init__(self, max_messages=10):
        self.max_messages = max_messages
        self.history = []

    def add_user_message(self, message):
        self.history.append(("Usuario", message))
        self._trim()

    def add_ai_message(self, message):
        self.history.append(("Asistente", message))
        self._trim()

    def get_history(self):
        return "\n".join(
            f"{role}: {message}"
            for role, message in self.history
        )

    def clear(self):
        self.history = []

    def _trim(self):
        if len(self.history) > self.max_messages:
            self.history = self.history[-self.max_messages:]