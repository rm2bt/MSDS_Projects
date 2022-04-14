#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 16:45:58 2020

@author: rehanmerchant
"""

import pandas as pd

#importing data in Pandas DF
batting = pd.read_csv('/Users/rehanmerchant/Desktop/Grad School/CS 5010/Project/Batting.csv')
salaries = pd.read_csv('/Users/rehanmerchant/Desktop/Grad School/CS 5010/Project/Salaries.csv')
teams = pd.read_csv('/Users/rehanmerchant/Desktop/Grad School/CS 5010/Project/Teams.csv')
teamsFranchise = pd.read_csv('/Users/rehanmerchant/Desktop/Grad School/CS 5010/Project/TeamsFranchises.csv')


#removing batting stats before 1985 since we dont have salary data for before 1985
indexBatting = batting[batting['yearID']<1985].index
batting.drop(indexBatting,inplace=True)


#which team has the most chamiponships out of the active teams today
#only WS winners
indexteams = teams[teams['WSWin']!='Y'].index
teams.drop(indexteams,inplace=True)

#only active teams
indexFranchise = teamsFranchise[teamsFranchise['active']!='Y'].index
teamsFranchise.drop(indexFranchise,inplace=True)

i = teamsFranchise.franchID.isin(teams.franchID)
print(i)
WSwinningteams = teamsFranchise[i]
WSwinningteams=WSwinningteams.drop('NAassoc',1)
WSwinningteams=WSwinningteams.drop('active',1)
WSwinningteams= WSwinningteams.set_index('franchID')
print(WSwinningteams)



numWSwins =teams.groupby('franchID').size()
print(numWSwins)

WSWinsAndTeams = WSwinningteams.assign(WSWins = numWSwins)
print(WSWinsAndTeams)

WSWinsAndTeams.plot.bar()


#Which team won the world championship each year and how much salary they spent compared to the average?
#WS winning teams 1985 to 2015
print(teams)
teams1985_2015 = teams
teams1985_2015index = teams1985_2015[teams1985_2015['yearID']<1985].index
teams1985_2015.drop(teams1985_2015index, inplace = True)
print(teams1985_2015)
print(salaries)
# legue avg salaries by year
groupSalaries_avg = salaries.groupby('yearID').mean()
print(groupSalaries_avg)
#grouping salaries by year and team
grouped_multiple = salaries.groupby(['yearID', 'teamID']).agg({'salary':['mean']})
grouped_multiple.columns = grouped_multiple.columns.droplevel(-1)
print(grouped_multiple)




avg_salary_WSWinning_teams =pd.merge(teams1985_2015, grouped_multiple, on =['yearID', 'teamID'])
#avg_salary_WSWinning_teams.rename(columns={'WS_Winning_team_salary': 'salary' })
#print(avg_salary_WSWinning_teams.columns)


avg_salary_WSWinning_teams_avg_league_salary = pd.merge(avg_salary_WSWinning_teams,groupSalaries_avg, on=['yearID'])
print(avg_salary_WSWinning_teams_avg_league_salary)
#graph should be salary from avg_salary_WSWinning_teams and groupSalaries_avg with x-axis being years

avg_salary_WSWinning_teams_avg_league_salary_plot = avg_salary_WSWinning_teams_avg_league_salary.plot(x="yearID", y=["salary_x", "salary_y"], kind="bar")
avg_salary_WSWinning_teams_avg_league_salary_plot.legend(["WS winning team average salary", "average league salary"])
#salary x = WS winning team #salary y = league average


