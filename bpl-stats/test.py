from __init__ import topScorers
from __init__ import pointsTable
from __init__ import next3Fixtures
import argparse
def topScorersCall():
    L = topScorers()
    M = L.top_scorers_goals()
    desired_dots = 55
    print "Scorerers" + "Goals".rjust(50,' ')
    for i in range(len(M[0])):
        print (M[0][i].ljust(desired_dots,' ') + M[1][i])
def fixturesCall():
    L = next3Fixtures() 
    M = L.fixtures()
    desired_dots = 20
    for x in M:
        print (str(x[0]).ljust(20,' ') + str(x[1]).ljust(20,' ') + str(x[2]))
        
def pointsTableCall():
    L = pointsTable()
    M = L.table()
    desired_dots = 22
    print "Team Names".ljust(desired_dots-1,' ') + "Points".ljust(desired_dots,' ') + "Played".ljust(desired_dots,' ') + "Won"
    for x in range(len(M[0])):
        print (M[0][x].ljust(desired_dots,' ') + M[1][x].ljust(desired_dots,' ') + M[2][x].ljust(desired_dots,' ') + M[3][x])        

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--top_scorers_goals',help = "For Top Scorerers  and Goals",action = 'store_true')
    parser.add_argument('-nf3', '--next3fixtures'    ,help = "For the Next 3 Fixtures"     ,action = 'store_true')
    parser.add_argument('-pt' , '--pointstable'      ,help = "For all teams matches points",action = 'store_true')

    args = vars(parser.parse_args())
    i = 4
    while i:
        try:
            if args['top_scorers_goals']:
                topScorersCall()
            elif args['next3fixtures']:
                fixturesCall()
            elif args['pointstable']:
                pointsTableCall()
            break
        except:
            print "Not able to Connect to Internet.Trying Again Attempts " + str(5-i)
        i = i -1
    if i == 0:
        print "Unable to Connect Network"

if __name__ == '__main__':
    Main()
