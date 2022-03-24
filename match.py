import random
from math import exp
import constants


class Match(object):

    def __init__(self, A_teams, B_teams, score):
        self.A_teams=A_teams # a list of A teams
        self.B_teams=B_teams # a list of B teams
        self.score=score # the score with A teams first and B teams second

    def get_team(self, team):

        if team in self.A_teams:
            teams=self.B_teams
        else:
            teams=self.A_teams

        # Choose the team to go with
        my_weights = []

        for team in teams:
            my_weights.append(exp(constants.SCALE_POINT_DIFF * team.point_diff))
        choice=random.choices([0,1,2], weights=my_weights)[0]
        return teams[choice]




