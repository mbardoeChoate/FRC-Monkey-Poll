import csv
from team import Team
from match import Match

class DataLoader(object):

    def __init__(self, file):
        self.file=file

    def get_teams(self):
        self.teams={}
        with open(self.file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                ateam1 = int(row['Ateam_1'])
                ateam2 = int(row['Ateam_2'])
                ateam3 = int(row['Ateam_3'])
                bteam1 = int(row['Bteam_1'])
                bteam2 = int(row['Bteam_2'])
                bteam3 = int(row['Bteam_3'])
                row_of_team=[ateam1, ateam2, ateam3, bteam1, bteam2, bteam3]
                for team in row_of_team:
                    if not team in self.teams.keys():
                        self.teams[team]=Team(team)
        csvfile.close()
        return self.teams

    def get_matches(self):
        self.matches=[]
        with open(self.file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ateam1 = self.teams[int(row['Ateam_1'])]
                ateam2 = self.teams[int(row['Ateam_2'])]
                ateam3 = self.teams[int(row['Ateam_3'])]
                bteam1 = self.teams[int(row['Bteam_1'])]
                bteam2 = self.teams[int(row['Bteam_2'])]
                bteam3 = self.teams[int(row['Bteam_3'])]
                ateam_score = int(row['Ateam_Score'])
                bteam_score = int(row['Bteam_Score'])
                row_of_team = [ateam1, ateam2, ateam3, bteam1, bteam2, bteam3]
                new_match=Match([ateam1, ateam2, ateam3], [bteam1, bteam2, bteam3], [ateam_score, bteam_score])
                for team in row_of_team:
                    team.add_match(new_match)
                self.matches.append(new_match)
        csvfile.close()
        return self.matches

    def get_opr(self):
        for team in list(self.teams.values()):
            team.calc_point_diff()


if __name__ == '__main__':
    data_loader=DataLoader("Data/AllEvents.csv")
    data_loader.get_teams()
    data_loader.get_matches()
    data_loader.get_opr()
    for team in data_loader.teams.values():
        print(team)
    print(len(data_loader.matches))
