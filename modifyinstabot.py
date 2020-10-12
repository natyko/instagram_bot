from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd
from dotenv import load_dotenv
import os

chromedriver_path = '/Users/nataliakozitcyna/Downloads/coding/chromedriver' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)

webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher') #instagram
sleep(3)

load_dotenv()

password_ok = os.getenv("password_ok", default="OOPS")
user = os.getenv("user", default="OOPS")


username = webdriver.find_element_by_name('username')
# username.send_keys('photo_by_tasha')  # your user_name
username.send_keys(user)  # your user_name
password = webdriver.find_element_by_name('password')
password.send_keys(password_ok)  # your password

button_login = webdriver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button > div')

button_login.click()
sleep(3)

login_not_now = webdriver.find_element_by_css_selector('section > main > div > div > div > div > button.sqdOP.yWX7d.y3zKF')
login_not_now.click()
sleep(4)

# notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm') # first working model
notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications


hashtag_list = ['miamifashionblogger', 'miamimodel', 'miamimodels', 'miamiblogger']

prev_user_list = [] # - if its's the first time you run it, use this line and comment below
# prev_user_list = pd.read_csv('20200522-134915_users_followed_list.csv', delimiter=',').iloc[:,1:2] #useful to build a user log
# prev_user_list = list(prev_user_list['0'])
new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0

for hashtag in hashtag_list:
    tag += 1
    webdriver.get('https://www.instagram.com/explore/tags/' + hashtag_list[tag] + '/')
    sleep(5)
    first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')

    first_thumbnail.click()
    sleep(randint(1,2))
    try:
        for x in range(1,200):
            username = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text
            # /html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button
            # /html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a #1

            if username not in prev_user_list:
                # If we already follow, do not unfollow
                if webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':
                    webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                    
                    new_followed.append(username)
                    followed += 1

                    # Liking the picture
                    button_like = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span')

                    button_like.click()
                    likes += 1
                    sleep(randint(18,25))

                    # Comments and tracker
                    comm_prob = randint(1,10)
                    print('{}_{}: {}'.format(hashtag, x, comm_prob))
                    # if comm_prob > 7:
                    comments += 1

                    # webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[2]/button').click()
                    # //*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[2]/button/div/svg
                    # #react-root > section > main > div > div.ltEKP > article > div.eo2As > section.ltpMr.Slqrh > span._15y0l > button > div > svg
                    # document.querySelector("#react-root > section > main > div > div.ltEKP > article > div.eo2As > section.ltpMr.Slqrh > span._15y0l > button > div > svg")
                    comment_box = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div[1]/form/textarea')
                    # //*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea
                    # //*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div[1]/form/textarea
                    # #react-root > section > main > div > div.ltEKP > article > div.eo2As > section.sH9wk._JgwE > div > form > textarea


                    if comm_prob == 1:
                        comment_box.send_keys('Great work!')
                        sleep(1)
                    elif comm_prob == 2:
                        comment_box.send_keys('really good!')
                        sleep(1)
                    elif comm_prob == 3:
                        comment_box.send_keys("that's amazing")
                        sleep(1)
                    elif comm_prob == 4:
                        comment_box.send_keys('love it')
                        sleep(1)
                    elif comm_prob == 5:
                        comment_box.send_keys('nice capture')
                        sleep(1)
                    elif comm_prob == 6:
                        comment_box.send_keys('Amazing work :)')
                        sleep(1)
                    elif comm_prob == 7:
                        comment_box.send_keys('great job')
                        sleep(1)
                    elif comm_prob == 8:
                        comment_box.send_keys('Nice shot!!')
                        sleep(1)
                    elif comm_prob == 9:
                        comment_box.send_keys('Nice gallery!!')
                        sleep(1)
                    elif comm_prob == 10:
                        comment_box.send_keys('This is so cool!')
                        sleep(1)
                        # Enter to post comment
                    comment_box.send_keys(Keys.ENTER)
                    sleep(randint(22,29))
                # Next picture
                webdriver.find_element_by_link_text('Next').click()
                sleep(randint(25,30))
            else:
                webdriver.find_element_by_link_text('Next').click()
                sleep(randint(20,27))
     # Some hashtag stops refreshing photos ( it might happen sometimes), it continues to the nest
    except:
        continue


for n in range (0, len(new_followed)):
    prev_user_list.append(new_followed[n])


updated_user_df = pd.DataFrame(prev_user_list)
updated_user_df.to_csv('{}_users_followed_list.csv'.format(strftime("%Y%m%d-%H%M%S")))
print('Liked {} photos.'.format(likes))
print('Commented {} photos.'.format(comments))
print('Followed {} new people.'.format(followed))
