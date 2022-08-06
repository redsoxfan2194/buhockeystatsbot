from burecordbook import *

if __name__ == '__main__':
  dfGames=generateRecordBook()
  dfGamesWomens=generateWomensRecordBook()
  dfJersey,dfJerseyMens,dfJerseyWomens=generateJerseys()
  dfSkate,dfSkateMens,dfSkateWomens=generateSkaters()
  dfGoalie,dfGoalieMens,dfGoalieWomens=generateGoalies()
  dfLead,dfLeadWomens=generateSeasonLeaders()
  dfBeanpot,dfBeanpotWomens=generateBeanpotHistory()
  dfSeasSkate,dfSeasSkateMens,dfSeasSkateWomens=generateSeasonSkaters()
  dfSeasGoalie,dfSeasGoalieMens,dfSeasGoalieWomens=generateSeasonGoalies()
  dfBeanpotAwards,dfBeanpotAwardsWomens=generateBeanpotAwards()
  dfBean={'results':dfBeanpot,'awards':dfBeanpotAwards}

  query=input("Query: ")
  while(query!='' and query != 'quit' and query != 'q'): 
    origQuery=query
    query,gender=determineGender(query)
    query=query.lstrip(' ')
    if(gender=='Womens'):
        query=cleanupQuery(query,'bean')
        dfBean={'results':dfBeanpotWomens,'awards':dfBeanpotAwardsWomens}
        result=getBeanpotStats(dfBean,query)
    else:
        query=cleanupQuery(query,'bean')
        dfBean={'results':dfBeanpot,'awards':dfBeanpotAwards}
        result=getBeanpotStats(dfBean,query)
    if(result==''):
        if(determineQueryType(query)!='player'):
            if(gender=='Womens'):
                result=getResults(dfGamesWomens,query)  
            else:
                result=getResults(dfGames,query)  
        else:
            playerDfs={}
            playerDfs['jerseys']=dfJersey
            playerDfs['seasonleaders']=dfLead
            playerDfs['careerSkaters']=dfSkate
            playerDfs['careerGoalies']=dfGoalie
            playerDfs['seasonSkaters']=dfSeasSkate
            playerDfs['seasonGoalies']=dfSeasGoalie
            if(gender=='Womens'):
                playerDfs['jerseys']=dfJerseyWomens
                playerDfs['seasonleaders']=dfLeadWomens
                playerDfs['careerSkaters']=dfSkateWomens
                playerDfs['careerGoalies']=dfGoalieWomens
                playerDfs['seasonSkaters']=dfSeasSkateWomens
                playerDfs['seasonGoalies']=dfSeasGoalieWomens
            if(gender=='Mens'):
                playerDfs['seasonSkaters']=dfSeasSkateMens
                playerDfs['seasonGoalies']=dfSeasGoalieMens
                playerDfs['jerseys']=dfJerseyMens
            result=getPlayerStats(playerDfs,query)
    print(origQuery.upper(),result,sep='\n')
    print()
    query=input("Query (Enter quit to exit): ")
