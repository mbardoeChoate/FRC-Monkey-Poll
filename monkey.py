import random
import constants


class Monkey(object):

    def __init__(self, team):
        self.team=team

    def move(self):
        if random.random()<constants.LIKELIHOOD_OF_MOVE:
            match=self.team.get_random_match()
            new_team=match.get_team(self.team)
            self.team.monkeys.remove(self)
            self.team=new_team
            self.team.add_monkey(self)
