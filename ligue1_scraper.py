from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep, time
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

# set up empty dataframe in a list for storage. errors is set up to handle any matches that dont scrape.
dataframe = []
errors = []



season_end = 69288

for id in range(69238, season_end):

    base_url = f'https://www.ligue1.com/match?matchId={id}'

    option = Options()
    driver = webdriver.Chrome("###########################,
                              options=option)
    driver.get(base_url)


    # click the cookie pop up
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div/div/div[3]/button[2]/span"))).click()

    # navigate to the stats - general tab.
    element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Stats']")))
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()

    # scraping the general stats page.

    try:
        sleep(1)

        date = driver.find_element("xpath",
                                   '/html/body/main/div[1]/div/div/div[2]/div[1]/p[1]').text

        Round = driver.find_element("xpath",
                                    '/html/body/main/div[1]/div/div/div[2]/div[1]/h2').text

        home_team = driver.find_element("xpath",
                                        '/html/body/main/div[1]/div/div/div[2]/div[2]/div[1]/a/h2').text

        away_team = driver.find_element("xpath",
                                        '/html/body/main/div[1]/div/div/div[2]/div[2]/div[3]/a/h2').text

        home_possesion = driver.find_element("xpath",
                                             '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[1]/div/table/tbody/tr[2]/td[1]').text

        away_possesion = driver.find_element("xpath",
                                             '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[1]/div/table/tbody/tr[2]/td[3]').text

        home_duel_success_rate = driver.find_element("xpath",
                                                     '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[1]/div/table/tbody/tr[4]/td[1]').text

        away_duel_success_rate = driver.find_element("xpath",
                                                     '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[1]/div/table/tbody/tr[4]/td[3]').text

        home_aerial_success_rate = driver.find_element("xpath",
                                                       '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[1]/div/table/tbody/tr[6]/td[1]').text

        away_aerial_success_rate = driver.find_element("xpath",
                                                       '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[1]/div/table/tbody/tr[6]/td[3]').text

        home_interceptions = driver.find_element("xpath",
                                                 '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[1]/div/table/tbody/tr[8]/td[1]').text

        away_interceptions = driver.find_element("xpath",
                                                 '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[1]/div/table/tbody/tr[8]/td[3]').text

        home_offsides = driver.find_element("xpath",
                                            '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[1]/div/table/tbody/tr[10]/td[1]').text

        away_offsides = driver.find_element("xpath",
                                            '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[1]/div/table/tbody/tr[10]/td[3]').text

        home_corners = driver.find_element("xpath",
                                           '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[1]/div/table/tbody/tr[12]/td[1]').text

        away_corners = driver.find_element("xpath",
                                           '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[1]/div/table/tbody/tr[12]/td[3]').text

        sleep(1)
        # move to distribution tab.

        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Distribution']")))
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()

        home_passes = driver.find_element("xpath",
                                          '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[2]/div/table/tbody/tr[2]/td[1]').text

        away_passes = driver.find_element("xpath",
                                          '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[2]/div/table/tbody/tr[2]/td[3]').text

        home_long_passes = driver.find_element("xpath",
                                               '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[2]/div/table/tbody/tr[4]/td[1]').text

        away_long_passes = driver.find_element("xpath",
                                               '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[2]/div/table/tbody/tr[4]/td[3]').text

        home_pass_acc = driver.find_element("xpath",
                                            '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[2]/div/table/tbody/tr[6]/td[1]').text

        away_pass_acc = driver.find_element("xpath",
                                            '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[2]/div/table/tbody/tr[6]/td[3]').text

        home_pass_acc_opp_half = driver.find_element("xpath",
                                                     '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[2]/div/table/tbody/tr[8]/td[1]').text

        away_pass_acc_opp_half = driver.find_element("xpath",
                                                     '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[2]/div/table/tbody/tr[8]/td[3]').text

        home_crossing = driver.find_element("xpath",
                                            '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[2]/div/table/tbody/tr[10]/td[1]').text

        away_crossing = driver.find_element("xpath",
                                            '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[2]/div/table/tbody/tr[10]/td[3]').text

        home_crossing_acc = driver.find_element("xpath",
                                                '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[2]/div/table/tbody/tr[12]/td[1]').text

        away_crossing_acc = driver.find_element("xpath",
                                                '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[2]/div/table/tbody/tr[12]/td[3]').text

        sleep(1)
        # move to attack tab.

        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Attack']")))
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()

        home_goals = driver.find_element("xpath",
                                         '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[3]/div/table/tbody/tr[2]/td[1]').text

        away_goals = driver.find_element("xpath",
                                         '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[3]/div/table/tbody/tr[2]/td[3]').text

        home_shots = driver.find_element("xpath",
                                         '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[3]/div/table/tbody/tr[4]/td[1]').text

        away_shots = driver.find_element("xpath",
                                         '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[3]/div/table/tbody/tr[4]/td[3]').text

        home_shots_on_target = driver.find_element("xpath",
                                                   '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[3]/div/table/tbody/tr[6]/td[1]').text

        away_shots_on_target = driver.find_element("xpath",
                                                   '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[3]/div/table/tbody/tr[6]/td[3]').text

        home_blocked_shots = driver.find_element("xpath",
                                                 '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[3]/div/table/tbody/tr[8]/td[1]').text

        away_blocked_shots = driver.find_element("xpath",
                                                 '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[3]/div/table/tbody/tr[8]/td[3]').text

        home_shots_os_box = driver.find_element("xpath",
                                                '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[3]/div/table/tbody/tr[10]/td[1]').text

        away_shots_os_box = driver.find_element("xpath",
                                                '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[3]/div/table/tbody/tr[10]/td[3]').text

        home_shots_is_box = driver.find_element("xpath",
                                                '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[3]/div/table/tbody/tr[12]/td[1]').text

        away_shots_is_box = driver.find_element("xpath",
                                                '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[3]/div/table/tbody/tr[12]/td[3]').text

        home_shooting_acc = driver.find_element("xpath",
                                                '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[3]/div/table/tbody/tr[14]/td[1]').text

        away_shooting_acc = driver.find_element("xpath",
                                                '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[3]/div/table/tbody/tr[14]/td[3]').text

        sleep(1)

        # move to defence tab.

        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Defence']")))
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()

        home_tackles = driver.find_element("xpath",
                                           '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[4]/div/table/tbody/tr[2]/td[1]').text

        away_tackles = driver.find_element("xpath",
                                           '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[4]/div/table/tbody/tr[2]/td[3]').text

        home_tackles_success_rate = driver.find_element("xpath",
                                                        '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[4]/div/table/tbody/tr[4]/td[1]').text

        away_tackles_success_rate = driver.find_element("xpath",
                                                        '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[4]/div/table/tbody/tr[4]/td[3]').text

        home_clearances = driver.find_element("xpath",
                                              '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[4]/div/table/tbody/tr[6]/td[1]').text

        away_clearances = driver.find_element("xpath",
                                              '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[4]/div/table/tbody/tr[6]/td[3]').text

        sleep(1)

        # move to discipline tab.

        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Discipline']")))
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()

        home_fouls = driver.find_element("xpath",
                                         '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[5]/div/table/tbody/tr[2]/td[1]').text

        away_fouls = driver.find_element("xpath",
                                         '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[5]/div/table/tbody/tr[2]/td[3]').text

        home_yellows = driver.find_element("xpath",
                                           '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[5]/div/table/tbody/tr[4]/td[1]').text

        away_yellows = driver.find_element("xpath",
                                           '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[5]/div/table/tbody/tr[4]/td[3]').text

        home_reds = driver.find_element("xpath",
                                        '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[5]/div/table/tbody/tr[6]/td[1]').text

        away_reds = driver.find_element("xpath",
                                        '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/ul/li[5]/div/table/tbody/tr[6]/td[3]').text

        sleep(1)

        # move to lineups tab to get referee.

        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Line-ups']")))
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()

        referee = driver.find_element("xpath",
                                      '/html/body/main/div[2]/div/div/div[2]/div[4]/div/div/div[3]/div/div/div[2]/ul/li[1]/span[2]').text

        scraped_data = [date, Round, home_team, away_team, home_possesion, away_possesion, home_duel_success_rate,
                        away_duel_success_rate, home_aerial_success_rate, away_aerial_success_rate,
                        home_interceptions, away_interceptions, home_offsides, away_offsides, home_corners,
                        away_corners, home_passes, away_passes, home_long_passes, away_long_passes, home_pass_acc,
                        away_pass_acc, home_pass_acc_opp_half, away_pass_acc_opp_half, home_crossing, away_crossing,
                        home_crossing_acc, away_crossing_acc, home_goals, away_goals,
                        home_shots, away_shots, home_shots_on_target, away_shots_on_target, home_blocked_shots,
                        away_blocked_shots, home_shots_os_box, away_shots_os_box, home_shots_is_box,
                        away_shots_is_box, home_shooting_acc, away_shooting_acc, home_tackles, away_tackles,
                        home_tackles_success_rate, away_tackles_success_rate, home_clearances, away_clearances,
                        home_fouls, away_fouls, home_yellows, away_yellows, home_reds, away_reds, referee]

        dataframe.append(scraped_data)
        print("Scraped the match:", id, 'Successfully')

    except:
        driver.quit()
        errors.append(id)
        continue

    driver.quit()

columns = ['Date', 'Round', 'HomeTeam', 'AwayTeam', 'Possession_Home', 'Possession_Away', 'Home_duels_success_rate',
           'Away_duels_success_rate', 'Home_aerials_success_rate', 'Away_aerials_success_rate', 'Home_interceptions',
           'Away_interceptions', 'Home_offsides', 'Away_offsides', 'Home_corners', 'Away_corners', 'Home_passes',
           'Away_passes',
           'Home_long_passes', 'Away_long_passes', 'Home_passing_acc', 'Away_passing_acc', 'Home_passing_acc_opp_half',
           'Away_passing_acc_opp_half', 'Home_crosses', 'Away_crosses',
           'Home_crossing_acc', 'Away_crossing_acc', 'HomeGoals', 'AwayGoals', 'HomeShots', 'AwayShots', 'HomeSOT',
           'AwaySOT', 'Home_blocked_shots', 'Away_blocked_shots', 'Home_Shots_OB', 'Away_Shots_OB', 'Home_Shots_IB',
           'Away_shots_IB', 'Home_shooting_acc', 'Away_shooting_acc', 'HomeTackles', 'AwayTackles',
           'Home_Tackle_success_rate', 'Away_Tackle_success_rate',
           'HomeClearances', 'AwayClearances', 'HomeFouls', 'AwayFouls', 'HomeYellows', 'AwayYellows', 'HomeReds',
           'AwayReds', 'Referee']

final_df = pd.DataFrame(dataframe)
final_df.columns = columns

# cleaning

# strip ROUND from round

final_df['Round'] = final_df['Round'].str.strip('ROUND')

# extract time from date

final_df['Time'] = [i.split("-")[1] for i in final_df['Date']]

# turn date column into datetime.

final_df['Date'] = pd.to_datetime(final_df['Date'])
final_df['Date'] = final_df['Date'].dt.date

# fix capitalisation of string columns

final_df['HomeTeam'] = final_df['HomeTeam'].str.title()
final_df['AwayTeam'] = final_df['AwayTeam'].str.title()
final_df['Referee'] = final_df['Referee'].str.title()

# remove % sign

final_df = final_df.replace('\%', '', regex=True)


# check for erroneous values and input 0, if shots for example is 0 it will return a error.

columns_to_convert = ['Round','Possession_Home', 'Possession_Away','Home_duels_success_rate', 'Away_duels_success_rate','Home_aerials_success_rate',
                      'Away_aerials_success_rate', 'Home_interceptions', 'Away_interceptions','Home_offsides', 'Away_offsides', 'Home_corners', 'Away_corners',
                      'Home_passes', 'Away_passes','Home_long_passes', 'Away_long_passes', 'Home_passing_acc', 'Away_passing_acc', 'Home_passing_acc_opp_half',
                      'Away_passing_acc_opp_half', 'Home_crosses', 'Away_crosses', 'Home_crossing_acc', 'Away_crossing_acc', 'HomeGoals',
                      'AwayGoals', 'HomeShots', 'AwayShots', 'HomeSOT', 'AwaySOT', 'Home_blocked_shots', 'Away_blocked_shots',
                      'Home_Shots_OB', 'Away_Shots_OB', 'Home_Shots_IB', 'Away_shots_IB', 'Home_shooting_acc', 'Away_shooting_acc',
                      'HomeTackles', 'AwayTackles', 'Home_Tackle_success_rate', 'Away_Tackle_success_rate', 'HomeClearances',
                      'AwayClearances', 'HomeFouls', 'AwayFouls', 'HomeYellows', 'AwayYellows', 'HomeReds', 'AwayReds']

for col in columns_to_convert:
    final_df[col] = final_df[col].replace("-", np.nan)
    final_df[col] = final_df[col].astype(float)
    final_df[col] = final_df[col].fillna(0)


# turn columns into float.

final_df[['Round', 'Possession_Home', 'Possession_Away', 'Home_duels_success_rate', 'Away_duels_success_rate',
          'Home_aerials_success_rate', 'Away_aerials_success_rate', 'Home_interceptions', 'Away_interceptions',
          'Home_offsides', 'Away_offsides', 'Home_corners', 'Away_corners', 'Home_passes', 'Away_passes',
          'Home_long_passes', 'Away_long_passes', 'Home_passing_acc', 'Away_passing_acc', 'Home_passing_acc_opp_half',
          'Away_passing_acc_opp_half', 'Home_crosses', 'Away_crosses',
          'Home_crossing_acc', 'Away_crossing_acc', 'HomeGoals', 'AwayGoals', 'HomeShots', 'AwayShots', 'HomeSOT',
          'AwaySOT', 'Home_blocked_shots', 'Away_blocked_shots', 'Home_Shots_OB', 'Away_Shots_OB', 'Home_Shots_IB',
          'Away_shots_IB', 'Home_shooting_acc', 'Away_shooting_acc', 'HomeTackles', 'AwayTackles',
          'Home_Tackle_success_rate', 'Away_Tackle_success_rate',
          'HomeClearances', 'AwayClearances', 'HomeFouls', 'AwayFouls', 'HomeYellows', 'AwayYellows', 'HomeReds',
          'AwayReds']] = final_df[
    ['Round', 'Possession_Home', 'Possession_Away', 'Home_duels_success_rate', 'Away_duels_success_rate',
     'Home_aerials_success_rate', 'Away_aerials_success_rate', 'Home_interceptions', 'Away_interceptions',
     'Home_offsides', 'Away_offsides', 'Home_corners', 'Away_corners', 'Home_passes', 'Away_passes', 'Home_long_passes',
     'Away_long_passes', 'Home_passing_acc', 'Away_passing_acc', 'Home_passing_acc_opp_half',
     'Away_passing_acc_opp_half', 'Home_crosses', 'Away_crosses', 'Home_crossing_acc', 'Away_crossing_acc', 'HomeGoals',
     'AwayGoals', 'HomeShots', 'AwayShots', 'HomeSOT', 'AwaySOT', 'Home_blocked_shots', 'Away_blocked_shots',
     'Home_Shots_OB', 'Away_Shots_OB', 'Home_Shots_IB', 'Away_shots_IB', 'Home_shooting_acc', 'Away_shooting_acc',
     'HomeTackles', 'AwayTackles', 'Home_Tackle_success_rate', 'Away_Tackle_success_rate', 'HomeClearances',
     'AwayClearances', 'HomeFouls', 'AwayFouls', 'HomeYellows', 'AwayYellows', 'HomeReds', 'AwayReds']].astype(float)

# reformat % columns by dividing by 100.


final_df[['Possession_Home', 'Possession_Away', 'Home_duels_success_rate', 'Away_duels_success_rate',
          'Home_aerials_success_rate', 'Away_aerials_success_rate', 'Home_passing_acc', 'Away_passing_acc',
          'Home_passing_acc_opp_half', 'Away_passing_acc_opp_half', 'Home_crossing_acc', 'Away_crossing_acc',
          'Home_shooting_acc', 'Away_shooting_acc', 'Home_Tackle_success_rate', 'Away_Tackle_success_rate']] = final_df[
    ['Possession_Home', 'Possession_Away', 'Home_duels_success_rate', 'Away_duels_success_rate',
     'Home_aerials_success_rate', 'Away_aerials_success_rate', 'Home_passing_acc', 'Away_passing_acc',
     'Home_passing_acc_opp_half', 'Away_passing_acc_opp_half', 'Home_crossing_acc', 'Away_crossing_acc',
     'Home_shooting_acc', 'Away_shooting_acc', 'Home_Tackle_success_rate', 'Away_Tackle_success_rate']].div(100).round(
    2)

# apply dictionary to remap names.


teams_dict = {"Rc Lens": "Lens",
              "Angers Sco": "Angers",
              "Fc Nantes": "Nantes",
              "Losc": "Lille",
              "Ol": "Lyon",
              "Ogc Nice": "Nice",
              "Om": "Marseille",
              "As Monaco": "Monaco",
              "Ac Ajaccio": "Ajaccio",
              "Aj Auxerre": "Auxerre",
              "Toulouse Fc": "Toulouse",
              "Fc Lorient": "Lorient"}

for key, value in final_df['HomeTeam'].iteritems():
    final_df['HomeTeam'] = final_df['HomeTeam'].apply(lambda x: teams_dict.get(x, x))

for key, value in final_df['AwayTeam'].iteritems():
    final_df['AwayTeam'] = final_df['AwayTeam'].apply(lambda x: teams_dict.get(x, x))

final_df

errors = pd.DataFrame(errors)

errors.to_csv('errors.csv')

final_df.to_csv('ligue1_2122.csv', index=False)

