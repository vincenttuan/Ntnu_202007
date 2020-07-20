class Score:
    def __init__(self, key, value) -> None:
        self.scores = {}  # {} -> dict
        Score.__setitem__(self, key, value)

    def __setitem__(self, key, value):
        self.scores[key] = value

    def __len__(self):
        return len(self.scores)

if __name__ == '__main__' :
    s = Score('英文', 80)
    s['國文'] = 60
    s['數學'] = 70
    print(s.scores)
    print(len(s))
