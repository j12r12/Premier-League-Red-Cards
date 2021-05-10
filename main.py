from function_file import *    
    
if __name__ == "__main__":
    
    # Create dataframe
    
    df2 = pd.read_csv("../input/english-premier-league-data-for-10-seasons/epldat10seasons/epl-allseasons-matchstats.csv")
    
    
    # Create dataframe to summarise cards given by season and create "TotalReds" column
    
    season_cards = df2.groupby("Season")["HomeRedCards", "AwayRedCards"].sum()
    season_cards["TotalReds"] = season_cards["HomeRedCards"] + season_cards["AwayRedCards"]
    season_cards = season_cards.rename(columns={"HomeRedCards":"HomeReds", "AwayRedCards":"AwayReds"})
    
    
    # Create line graphs for HomeReds, AwayReds and TotalReds, including linear regression lines
    
    line_graph(season_cards["HomeReds"], "HomeReds", "Home Team Red Cards", style="seaborn-poster")
    line_graph(season_cards["AwayReds"], "AwayReds", "Away Team Red Cards", style="seaborn-poster")
    line_graph(season_cards["TotalReds"], "TotalReds", "Total Team Red Cards", style="seaborn-poster")
    
    
    # Create variables to use to calculate z-values
    
    data = season_cards["TotalReds"]
    s1415 = np.max(data) # Taking the highest red card tally value, which is for season 2014/15
    s1718 = np.min(data) # Taking the lowest red card tally value, which is for season 2017/18
    mean = np.mean(data) # Taking the mean value for the 10 years of red card data
    std = np.std(data) # Taking the standard deviation of this data
    
    
    # Plot normal curves and show z-values
    
    normal_curve(True, z1718, "Season 2017/18 Data")
    normal_curve(True, z1415, "Season 2014/15 Data")
    
    
    # Calculate p-values
    p_value1415 = norm.sf(abs(z1415))
    p_value1718 = norm.sf(abs(z1718))

    
