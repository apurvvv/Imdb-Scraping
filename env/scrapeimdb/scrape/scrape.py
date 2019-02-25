import requests
from lxml import html


class Scrapster():

    def scrappy(self, url):
        site = requests.get(url)
        page = html.fromstring(site.content)
        name = page.xpath('// div[@class="title_wrapper"]/h1/text()')
        name = name[0]
        star = page.xpath('//*[@id="title-overview-widget"]/div[1]/div[2]/div/div[1]/div[1]/div[1]/ strong/span/text()')
        star = star[0]
        img = page.xpath('//*/img/@src')[2]
        desc = page.xpath('//div[@id="titleStoryLine"]')[0]
        description = desc.xpath('.//p/span/text()')[0]
        char = page.xpath('//*[@id="titleCast"]/*')
        ch = char[2]
        a = ch.xpath('//tr')
        count = 1
        content = {}
        try:
            while count < len(a)-2:
                castx = ch.xpath('//tr')[count]
                children = castx.getchildren()
                cast = children[1].xpath('./a/text()')[0].strip()
                character = children[3].xpath('./a/text()')
                if len(character) > 1:
                    character = (' / ').join(character)
                else:
                    character = ('').join(character)
                if not character:
                    character = children[3].xpath('./text()')[0].strip()
                content[cast] = character
                count += 1
        except:
            while count < len(a)-4:
                castx = ch.xpath('//tr')[count]
                children = castx.getchildren()
                cast = children[1].xpath('./a/text()')[0].strip()
                character = children[3].xpath('./a/text()')
                if len(character) > 1:
                    character = ('/').join(character)
                else:
                    character = ('').join(character)
                if not character:
                    character = children[3].xpath('./text()')[0].strip()
                content[cast] = character
                count += 1
        return name, star, description, img, content
