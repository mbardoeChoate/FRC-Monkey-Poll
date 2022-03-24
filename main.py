from dataloader import DataLoader
from monkey import Monkey
import random

class Main(object):

    def __init__(self, file="Data/AllEvents.csv", num_monkeys=3000, num_iterations=10000):
        self.dataloader=DataLoader(file)
        self.num_iterations=num_iterations
        # Get a dictionary of teams
        self.teams=self.dataloader.get_teams()
        # Get a list of matches
        self.matches=self.dataloader.get_matches()
        self.dataloader.get_opr()
        # make and distribute monkeys
        self.monkeys=[]
        teams=list(self.teams.values())
        for i in range(num_monkeys):
            my_team=random.choices(teams)[0]
            new_monkey = Monkey(my_team)
            my_team.add_monkey(new_monkey)
            self.monkeys.append(new_monkey)

    def move_monkeys(self):
        for i in range(self.num_iterations):
            if i%1000==0:
                print(i)
            for monkey in self.monkeys:
                monkey.move()

    def report(self):
        all_teams=list(self.teams.values())
        sorted_teams=sorted(all_teams, key = lambda team:  team.num_monkeys())
        for team in sorted_teams:
            print(str(team))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main=Main(num_monkeys=4000, num_iterations=20000)
    main.move_monkeys()
    main.report()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
