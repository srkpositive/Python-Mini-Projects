#import the necessary libraries
import time
#make sure you've installed the plyer module as it's not a built-in module
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Please take a break",
            message = "It's time to take some break, Go and have some coffee!",
            app_icon = "icon.ico",
            timeout = 10
        )
        time.sleep(60*60)
