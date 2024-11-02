class ResponseInfo:
    def __init__(self):
        self.bestResponse = None
        self.highestWeight = 0
        self.bestTransition = None
        self.potentialResponses = []
        self.itemKey = None
