from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

##### Definitions ######
browser = webdriver.Chrome(executable_path='/users/clayozuna/Downloads/chromedriver')
# goes to the website requested
command = ""
##### Functions ######
def fullscreen():
    actions.double_click(player)
    actions.pause(2)
    actions.perform()
def playpause():
    actions.send_keys(Keys.SPACE)
    actions.perform()
def exitfullscreen():
    actions.double_click(player)
    actions.perform()
def nextvideo():
    #Go to next video
    nextvideo = browser.find_element_by_xpath("//span[@class='prev-next'][@style='float:right;']")
    # Double Click video
    nextvideo.click()
def previousvideo():
    #Go to previous video
    previousvideo = browser.find_element_by_xpath("//span[@class='prev-next'][@style='float:left;']")
    # Double Click video
    previousvideo.click()
def slidepercentage():
    sliderpercentage = browser.find_element_by_xpath("//div[@class='vjs-time-tooltip']").text ## Should get text in theory
    print(sliderpercentage)
def commands():
        print("Here are the different commands:")
        print("1 - enter fullscreen")
        print("2 - play or pause video")
        print("3 - go to the next video")
        print("4 - exit fullscreen")
        print("5 - go to the previous video")
        print("exit - exit the video")
        print("command - Show the commands")
        print("shutdown - Close the browser\n")
def switchcase(num):
    if num == '1':
        fullscreen()
    if num == '2':
        playpause()
    if num == '3':
        nextvideo()
    if num == '4':
        exitfullscreen()
    if num == '5':
        previousvideo()
    if num == 'exit':
        # Exit the script
        exit
    if num == 'command':
        commands()
    if num == 'shutdown':
        # Close browser
        browser.close()

def automatic():
    while True:
        fullscreen()
        time.sleep(3)
        playpause()
        time.sleep(1300)
        exitfullscreen()
        time.sleep(1)
        nextvideo()
        time.sleep(5)


#### INTRO #######
print("Welcome to the laz3 video controller. \n")
episode_number = input("Enter the HunterxHunter(2011) episode you would like to watch: ")
print("")

if episode_number == 'nvm':
    browser.close()
    print("Shutting down your browser\n")
else:
    browser.get("https://www.thewatchcartoononline.tv/hunter-x-hunter-2011-episode-"+episode_number+"-english-dubbed")
    print("Headed to your episode\n")

##### While Loop #####
while command != "shutdown" or episode_number != 'nvm':
    actions = ActionChains(browser)
    player = browser.find_element_by_class_name('pcat-jwplayer')

    actions.move_to_element(player)
    print("Enter 'command' if you would like to see the list of commands\n")
    # automatic()
    command = input("What would you like to do?: ")
    print("")

    switchcase(command)

##### NEXT STEPS#####

### Make system automatic by reading the value on the video slider
