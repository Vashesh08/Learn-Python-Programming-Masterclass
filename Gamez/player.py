class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self._score += delta * 1000
            self._level = level
        else:
            print("Level cant be less than 1")

    #
    # def _set_score(self):
    #     if self.level > 0:
    #         if self.level*1000 == self._score:
    #             return self._score
    #         elif self.level*1000 > self._score:
    #             self._score += 1000
    #         else:
    #             self._score -= self.level * 1000
    #         return self._score
    #     else:
    #         print("Level must be greater than zero")
    #         self.level = 0
    #         return 0
    #
    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)
    # score = property(_set_score)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)
