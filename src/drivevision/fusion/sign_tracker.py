from collections import Counter,deque

class SignVote:
    def __init__(self,window=7):self.labels=deque(maxlen=window)
    def update(self,label):
        self.labels.append(label)
        return Counter(self.labels).most_common(1)[0][0]
