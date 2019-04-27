""" google_scholar"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time

class google_scholar():
    """ parses personal google scholar """
    def __init__(self,url):
        driver = webdriver.Safari()
        driver.get(url)
        while True:
            button = driver.find_element_by_id('gsc_bpf_more')
            if not button.get_attribute('disabled'):
                button.click()
            # a better solution must exist
                time.sleep(1)
            else:
               break
        source =driver.page_source
        driver.close()
        soup = BeautifulSoup(source)
        self._titles      = [ papa.text for papa in soup.find_all('a',class_='gsc_a_at')]    
        self._detail_url  = [ papa.attrs['data-href'] for papa in soup.find_all('a',class_='gsc_a_at')]
        self._paper_cites = [ papa.text for papa in soup.find_all('a',class_='gsc_a_ac gs_ibl') ]
        self._years       = [ papa.text for papa in soup.find_all('span',class_='gsc_a_h gsc_a_hc gs_ibl')] 
        self._cites       = dict(zip([ papa.text      for papa in soup.find_all('span',class_='gsc_g_t')],
                                     [ int(papa.text) for papa in soup.find_all('span',class_='gsc_g_al')]))
        return

    def get_cite_chart(self):
        val = '\n\
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js">\n\
</script>\n\
<script type="text/javascript" src="http://code.highcharts.com/highcharts.js">\n\
</script>\n\
<script type="text/javascript" src="http://code.highcharts.com/modules/exporting.js">\n\
</script>\n\
\n\
<div id="container" style="min-width: 310px; height: 400px; margin: 0 auto">\n\
</div>\n\
\n\
<script type="module">\n\
    import Highcharts from "https://code.highcharts.com/es-modules/masters/highcharts.src.js";\n\
    Highcharts.chart("container", {{\n\
            chart: {{\n\
                type: "column" \n\
            }}, \n\
            credits : {{ enabled : false }},\n\
            title: {{\n\
                text: "Recent citations",\n\
            }},\n\
            xAxis: {{\n\
                categories: {}\n\
            }},\n\
            yAxis: {{\n\
                title: {{\n\
                    text: "number of cites"\n\
                }}\n\
            }},\n\
            legend: {{\n\
                layout: "vertical",\n\
                align: "right",\n\
                verticalAlign: "middle",\n\
                borderWidth: 0\n\
            }},\n\
            series: [{{ \n\
                name : "Citations", \n\
                data : {} \n\
            }}]\n\
        }});\n\
</script>'.format(list(self._cites.keys()),list(self._cites.values()))
        print(val)


a = google_scholar(r'https://scholar.google.com/citations?user=KNorg_UAAAAJ&hl=en')
a.get_cite_chart()
