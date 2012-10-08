
import urllib
from BeautifulSoup import BeautifulSoup

def incident_log(month, day, year):
    month, day, year = int(month), int(day), int(year)

    incidents = []
    f = urllib.urlopen('http://police.umich.edu/?s=crime_log&d=%d/%d/%d' %
                       (year, month, day))
    soup = BeautifulSoup(f)
    
    for tag in soup('td', width='150'):
        d = {}
        # jump to parent tr
        tag = tag.parent
        # in the same tr
        l = tag('td')
        d['date'] = str(l[0].string)
        d['type'] = str(l[1].next.next.string)
        d['case'] = str(l[2].string)
        # next tr
        sep = ' &nbsp; '
        s = str(tag.nextSibling('font')[0].string)
        if sep in s:
            d['building'], d['address'] = tag.nextSibling('font')[0].string.split(sep)
        else:
            d['building'] = ''
            d['address'] = s
        
        # next tr
        d['description'] = str(tag.nextSibling.nextSibling('td')[0].string)
        # next tr
        try:
            d['action'] = str(tag.nextSibling.nextSibling.nextSibling('td')[0]('i')[0].next.next.string)
        except IndexError:
            d['action'] = ''

        incidents.append(d)

    return incidents

if __name__ == '__main__':
    print incident_log('08', '24', '2011')
    
