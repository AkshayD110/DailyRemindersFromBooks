"""
linux commands used for data massaging --

#sed -i '/(*)/d' MyClippings-Kindle.txt
#sed -i '/Your Bookmark/d' MyClippings-Kindle.txt
#sed -i '/Your Note/d' MyClippings-Kindle.txt
#sed -i '/Your Highlight/d' MyClippings-Kindle.txt
"""
import random
import config
from sendingmail import SendingMail


def main():
    select_highlights()


def select_highlights():
    with open(r'KindleHighlights', encoding="utf8") as f:
        lines = f.readlines()
    highlights_set = list(set(lines))
    highlights_of_the_day = random.sample(highlights_set, k=config.number_of_highlights_per_day)
    highlights_to_mail = ''
    for highlights in highlights_of_the_day:
        highlights_to_mail += highlights
        highlights_to_mail += '\n'
    print(highlights_to_mail)
    sendingmail_object = SendingMail(highlights_to_mail)
    #sendingmail_object.sendmail()


if __name__ == '__main__':
    main()

