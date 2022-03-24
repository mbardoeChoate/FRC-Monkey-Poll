import random

import constants


class Team(object):

    def __init__(self, team_number):
        self.team_number=team_number
        self.matches=[]
        self.monkeys=[]
        self.match_weights=[]
        self.point_diff=0
    def add_match(self,match):
        self.matches.append(match)

    def calc_point_diff(self):
        for match in self.matches:
            if (match.score[0]>match.score[1] and self in match.A_teams) or (match.score[0]<match.score[1] and self in match.B_teams):
                self.match_weights.append(constants.WIN_WEIGHT)
            else:
                self.match_weights.append(constants.LOSS_WEIGHT)
            if self in match.A_teams:
                self.point_diff+= match.score[0] - match.score[1]
            else:
                self.point_diff += match.score[1] - match.score[0]
        self.point_diff/=float(len(self.matches))
    def get_random_match(self):
        return random.choices(self.matches, weights=self.match_weights)[0]


    def add_monkey(self, monkey):
        self.monkeys.append(monkey)

    def num_monkeys(self):
        return len(self.monkeys)

    def __eq__(self, other):
        return self.team_number==other.team_number

    def __str__(self):
        ans= str(self.team_number) +"\t" + str(self.point_diff) + "\t" + str(self.num_monkeys())
        return ans