import requests
import os

targetSite = 'https://old.reddit.com/r/netsec/'


def findAll(target, sub):
        loop=0
        while True:
                loop = target.find(sub, loop)
                if loop == -1:
                        return
                yield loop
                loop += len(sub)


def findPart(target, startSymbol, endSymbol):
        start = target.find(startSymbol)+len(startSymbol)
        end = target[start:].find(endSymbol) + start + len(endSymbol) - 1
        return(target[start:end])


def main():
        loop = 0
        found = []
        tags = []
        while len(found) < 13:
                if loop > 10:
                        print('Error finding webpage')
                        return
                r = requests.get(targetSite, headers = {'User-agent': 'newsRequestBot'})
                found = list(findAll(r.text,'<a class=\"title may-blank'))
                loop += 1


        for tag in found[:13]:
                tagEnd = tag + r.text[tag:].find("</a>") + 4
                tags.append(r.text[tag:tagEnd])


        for i in range(len(tags)):
                link = findPart(tags[i], "href=\"", "\"")
                if not link.startswith("https://alb"):
                        print(findPart(tags[i], ">", "<"))
                        print("\t" + link)


main()
input()
