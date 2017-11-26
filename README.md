# ScrapyCrawler

Create a virtual Env  in conda 
```conda create -n scrapy python=3.6 anaconda```

Install following packages in the environment using 
```pip install or conda install```
```Scrappy,pyquery,ipython```

Activate conda env
```Activate scrapy```

First check the URL via scrappy shell
```Scrapy shell ```

```scrapy shell http://www.rsscarch.com/project/peters-township-library/```

check the response in the shell first - This step is to check the response is hitting our python env , some cases firewall or some Javascript sites might now work well with scrapy.

```In [4]: response.url
Out[4]: 'http://www.rsscarch.com/project/peters-township-library/'

In [5]: response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "post-title", " " ))] | //p').extract()
Out[5]:
['<h2 class="post-title">Peters Township Library</h2>',
 '<p><strong>Client: </strong>Peters Township<br>\n<strong>Location: </strong>McMurray Township, Pennsylvania<br>\n<strong>Size: </strong>23,000 SF</p>',
 '<p><span id="more-178"></span></p>',```
 
 
 Once the response is checked, Create a scrapy project. Unlike other libraries The scrapy provides the skeleton structure for easy spider development
 ```scrapy startproject rsscrachcrawler```
 
 once project is created follow the spider code in the repo - rsscrach.py
 
 To Run the crawler:
 
 ```scrapy crawl spiders ``` - From the Anaconda prompt  //Name of the spider in this crawler is spiders
 
For scrapy related help - Follow the Scrapy official documentation 
[a link]https://doc.scrapy.org/en/latest/index.html#
 

