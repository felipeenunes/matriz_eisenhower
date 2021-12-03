class NotFoundError(Exception):
    def __init__(self, message):
        self.message = message
        self.code = 404

class OutOfRangeError(Exception):
    def __init__(self, importance, urgency):
        self.message = {
            "error": {
                "valid_options": {
                    "importance": [1, 2],
                    "urgency": [1, 2]
                },
                "received_options": {
                    "importance": importance,
                    "urgency": urgency
                }
            }
        }
        self.code = 404

    