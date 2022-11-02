import schedule
import requests
import time

def greeting():
    """Greeting function"""

    print('Task is complite')


def main():

    schedule.every(4).seconds.do(greeting)
    # schedule.every(5).minutes.do(greeting)
    # schedule.every().hour.do(greeting)
    # schedule.every().day.at('21:51').do(greeting)
    # schedule.every().thursday.do(greeting)
    # schedule.every().friday.at('23:45').do(greeting)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()