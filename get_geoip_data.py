from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

def get_geoip_data():
    result = {}
    url_string = "http://www.maxmind.com/app/locate_my_ip"
    res = urlopen(url_string)
    html = res.read()
    soup = BeautifulSoup(html)
    keys = soup.findAll(attrs={'class' : 'tblProduct1'})
    values = soup.findAll(attrs={'class' : 'output'})
    for i in range(0, len(keys)):
        result[keys[i].contents[0].strip()] = values[i].contents[0].strip()
    return result

def format_result():
    output = get_geoip_data()
    lat_lon = output['Latitude/Longitude'].split('/')
    ip = output['Your IP Address']
    print "%s, %s, %s" % (ip, lat_lon[0], lat_lon[1])
    
format_result()