#!/usr/bin/env python
# coding: utf-8

# **1. Write a python program to display all the header tags from ‘en.wikipedia.org/wiki/Main_Page’.**

# In[403]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
html=urlopen('https://en.wikipedia.org/wiki/Main_Page')
bs=BeautifulSoup(html,'html.parser')
header=bs.find_all(['h1','h2','h3','h4','h5','h6'])
print('List all the headers',*header,sep='\n\n')


# **2. Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. Name, IMDB rating, Year of
# release) and make data frame.**

# In[406]:


from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

movies = soup.select('td.titleColumn')
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]


imdb = []

for index in range(0,100):
    # Seperate movie into: 'place', 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    data = {"movie_title": movie_title,
            "year": year,
            "place": place,
            "rating": ratings[index]
           }
           
    imdb.append(data)

df=pd.DataFrame(imdb)
df=df[["movie_title","year","rating"]]
df


# **3. Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. Name, IMDB rating, Year
# of release) and make data frame.**

# In[407]:


from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

url = 'https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=461131e5-5af0-4e50-bee2-223fad1e00ca&pf_rd_r=4T9XJEYV23FG9WFPHB50&pf_rd_s=center-1&pf_rd_t=60601&pf_rd_i=india.toprated&ref_=fea_india_ss_toprated_india_tr_india250_hd'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

movies = soup.select('td.titleColumn')
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]


imdb = []

for index in range(0,100):
    
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    data = {"movie_title": movie_title,
            "year": year,
            "place": place,
            "rating": round(float(ratings[index]),2)
           }

    imdb.append(data)
#for item in imdb:
    #print(item['place'], '-', item['movie_title'], '('+item['year']+') -', 'rating:',round(float(item['rating'])))
df=pd.DataFrame(imdb)
df=df[["movie_title","year","rating"]]
df


# **4. Write a python program to scrap book name, author name, genre and book review of any 5 books from
# ‘www.bookpage.com’**
# 

# In[438]:


from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

url = 'https://bookpage.com/reviews'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')


books=soup.select("div.flex-article-content")
authors=soup.select("p.sans.bold")
genres=soup.select("p.genre-links.hidden-phone")
reviews=soup.select("p.excerpt")


bookpage=[]
for index in range(0,5):  
    book_string=books[index].get_text()
    book=(" ".join(book_string.split()).replace(",",""))
    author_string=authors[index].get_text()
    author=(" ".join(author_string.split()).replace(",",""))
    genre_string=genres[index].get_text()
    genre=(" ".join(genre_string.split()).replace(",",""))
    review_string=reviews[index].get_text()
    review=(" ".join(review_string.split()).replace(",",""))
    
    
    data = {"book": book,
            "author": author,
            "genre": genre,
            "review": review
           }

    bookpage.append(data)
    
df=pd.DataFrame(bookpage)
df=df[["book","author","genre","review"]]
df


# In[429]:


reviews


# # 5. Write a python program to scrape cricket rankings from ‘www.icc-cricket.com’. You have to scrape:
# 

# **i) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.**

# In[439]:


from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

url = 'https://www.icc-cricket.com/cricket-world-cup-super-league/standings'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')


odi=soup.select("td")


odi_report=[]
index =10
while index < len(odi):
        index = index +1
        team=odi[index].get_text()
        index = index +1
        match=odi[index].get_text()
        index = index +5
        point=odi[index].get_text()
        index = index +1
        rating=odi[index].get_text()
        index+=2
               
        report={"team":team,
               "match":match,
               "point":point,
               "rating":rating
               }
       
        odi_report.append(report)
        if index==110:
            break
        

   
df=pd.DataFrame(odi_report)
df=df[["team","match","point","rating"]]
df


# **ii) Top 10 ODI Batsmen in men along with the records of their team and rating.**

# In[440]:


from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

url = 'https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')


pos_string=soup.select("td.rankings-block__position")
pos_string=pos_string[0].get_text()
pos=("".join(pos_string.split()).replace(",",""))
name_string=soup.select("div.rankings-block__banner--name-large")
name_string=name_string[0].get_text()
name=("".join(name_string.split()).replace(",",""))
nation_string=soup.select("div.rankings-block__banner--nationality")
nation_string=nation_string[0].get_text()
nation2=("".join(nation_string.split()).replace(","," "))
rating_string=soup.select("div.rankings-block__banner--rating")
rating_string=rating_string[0].get_text()
rating=("".join(rating_string.split()).replace(",",""))

d={"pos":pos_string,
    "name":name_string,
    "nation":nation2,
    "rating":rating_string}
dfd=pd.DataFrame(d,index=[0])


pos_s1=soup.select("td.table-body__cell.table-body__cell--position.u-text-right")
name_s1=soup.select("td.table-body__cell.rankings-table__name.name")
nation_s1=soup.select("span.table-body__logo-text")
rating_s1=soup.select("td.table-body__cell.rating")

perf=[]

for i in range(0,9):    
    pos_string1=pos_s1[i].get_text()
    pos1=("".join(pos_string1.split()).replace(",",""))
    name_string1=name_s1[i].get_text()
    name1=("".join(name_string1.split()).replace("",""))
    nation=nation_s1[i].get_text()
    rating_string1=rating_s1[i].get_text()
    rating1=("".join(rating_string1.split()).replace(",",""))   

    data={"pos":pos1,
         "name":name1,
          "nation":nation,
         "rating":rating1
          }
    perf.append(data)


    
df=pd.DataFrame(perf)

join_df=pd.concat([dfd,df])

join_df=join_df[["pos","name","nation","rating"]]
join_df.reset_index(drop=True)         


# **iii) Top 10 ODI bowlers along with the records of their team and rating.**
# 

# In[441]:


from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

url = 'https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')


pos_string=soup.select("td.rankings-block__position")
pos_string=pos_string[0].get_text()
pos=("".join(pos_string.split()).replace(",",""))
name_string=soup.select("div.rankings-block__banner--name-large")
name_string=name_string[0].get_text()
name=("".join(name_string.split()).replace(",",""))
nation_string=soup.select("div.rankings-block__banner--nationality")
nation_string=nation_string[0].get_text()
nation2=("".join(nation_string.split()).replace(","," "))
rating_string=soup.select("div.rankings-block__banner--rating")
rating_string=rating_string[0].get_text()
rating=("".join(rating_string.split()).replace(",",""))

d={"pos":pos_string,
    "name":name_string,
    "nation":nation2,
    "rating":rating_string}
dfd=pd.DataFrame(d,index=[0])


pos_s1=soup.select("td.table-body__cell.table-body__cell--position.u-text-right")
name_s1=soup.select("td.table-body__cell.rankings-table__name.name")
nation_s1=soup.select("span.table-body__logo-text")
rating_s1=soup.select("td.table-body__cell.rating")

perf=[]

for i in range(0,9):    
    pos_string1=pos_s1[i].get_text()
    pos1=("".join(pos_string1.split()).replace(",",""))
    name_string1=name_s1[i].get_text()
    name1=("".join(name_string1.split()).replace("",""))
    nation=nation_s1[i].get_text()
    rating_string1=rating_s1[i].get_text()
    rating1=("".join(rating_string1.split()).replace(",",""))   

    data={"pos":pos1,
         "name":name1,
          "nation":nation,
         "rating":rating1
          }
    perf.append(data)


    
df=pd.DataFrame(perf)

join_df=pd.concat([dfd,df])

join_df=join_df[["pos","name","nation","rating"]]
join_df.reset_index(drop=True)   


# # 6. Write a python program to scrape cricket rankings from ‘www.icc-cricket.com’. You have to scrape:

# **i) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.**

# In[442]:


from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

url = 'https://www.icc-cricket.com/rankings/womens/team-rankings/odi'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')


pos_string=soup.select("td.rankings-block__banner--pos")
pos_string=pos_string[0].get_text()
pos=("".join(pos_string.split()).replace(",",""))
name_string=soup.select("span.u-hide-phablet")
name_string=name_string[0].get_text()
name=("".join(name_string.split()).replace(",",""))
match_string=soup.select("td.rankings-block__banner--matches")
match=match_string[0].get_text()
point_string=soup.select("td.rankings-block__banner--points")
point=point_string[0].get_text()
rating_string=soup.select("td.rankings-block__banner--rating.u-text-right")
rating=rating_string[0].get_text()
rating=("".join(rating.split()).replace(",",""))


d={"pos":pos,
     "name":name,
    "match":match,
   "point":point,
   "rating":rating
  }
df1=pd.DataFrame(d,index=[0])



pos_s1=soup.select("td.table-body__cell.table-body__cell--position.u-text-right")
name_s1=soup.select("td.table-body__cell.rankings-table__team")
match_s1=soup.select("td.table-body__cell.u-center-text")
point_s1=soup.select("td,table-body__cell.u-center-text")
rating_s1=soup.select("td.table-body__cell.u-text-right.rating")
match_string1=None
point_string1=None
report=[]
for i in range(0,18):
    
        
    if i%2==0:
        match_string1=match_s1[i].get_text()         
        
    else:
        point_string1=match_s1[i].get_text()   
        
      
    if match_string1 is not None  and point_string1 is not None: 
        data={"match":match_string1,"point":point_string1}            
        report.append(data)
        match_string1=None
        point_string1=None

 

for i in range(0,9): 
    pos_string1=pos_s1[i].get_text()
    pos1=("".join(pos_string1.split()).replace(",",""))
    name_string1=name_s1[i].get_text()
    name1=("".join(name_string1.split()).replace(",",""))
    rating_string1=rating_s1[i].get_text()
    rating1=("".join(rating_string1.split()).replace(",",""))
    
    data = report[i]
    
    data.update({"pos":pos1,
          "name":name1,
          "rating":rating1
          })
    
    report[i]=data
    

    
df=pd.DataFrame(report)
df

join_df=pd.concat([df1,df])

join_df=join_df[["pos","name","match","point","rating"]].reset_index(drop=True)
join_df


# **ii) Top 10 women’s ODI players along with the records of their team and rating.**

# In[443]:


from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

url = 'https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')


pos_string=soup.select("td.rankings-block__position")
pos_string=pos_string[0].get_text()
pos=("".join(pos_string.split()).replace(",",""))
name_string=soup.select("div.rankings-block__banner--name-large")
name_string=name_string[0].get_text()
name=("".join(name_string.split()).replace(",",""))
nation_string=soup.select("div.rankings-block__banner--nationality")
nation_string=nation_string[0].get_text()
nation2=("".join(nation_string.split()).replace(","," "))
rating_string=soup.select("div.rankings-block__banner--rating")
rating_string=rating_string[0].get_text()
rating=("".join(rating_string.split()).replace(",",""))

d={"pos":pos_string,
    "name":name_string,
    "nation":nation2,
    "rating":rating_string}
dfd=pd.DataFrame(d,index=[0])



name_s1=soup.select("td.table-body__cell.rankings-table__name.name")
nation_s1=soup.select("td.table-body__cell.nationality-logo.rankings-table__team")
rating_s1=soup.select("td.table-body__cell.rating")

pos_s1=[b.get_text().split("\n")[1] for b in soup.select("td.table-body__cell.table-body__cell--position.u-text-right")]

pos=[]
i=0
t=len(str(len(pos_s1)))
for ele in pos_s1:
    if i<10:
        b=pos_s1[i][-t::]
    i+=1
    if i ==10:
        break
    data={"pos":b}
    pos.append(data)
pos=pd.DataFrame(pos)




perf=[]

for i in range(0,9):    
    #pos_string1=pos_s1[i].get_text()
    #print(pos_s1[i])
    #pos1=("".join(pos_string1.split()).replace(",",""))
    name_string1=name_s1[i].get_text()
    name1=("".join(name_string1.split()).replace("",""))
    nation=nation_s1[i].get_text()
    nation=("".join(nation.split()).replace(",",""))
    rating_string1=rating_s1[i].get_text()
    rating1=("".join(rating_string1.split()).replace(",",""))   
    
    
    data1={"name":name1,
          "nation":nation,
         "rating":rating1
          }
    perf.append(data1)
    


    
df=pd.DataFrame(perf)
df
df["pos"]=pos
df

join_df=pd.concat([dfd,df])
join_df.reset_index(drop=True,inplace=True)
join_df


# **iii) Top 10 women’s ODI all-rounder along with the records of their team and rating.**

# In[444]:


from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

url = 'https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')


pos_string=soup.select("td.rankings-block__position")
pos_string=pos_string[0].get_text()
pos=("".join(pos_string.split()).replace(",",""))
name_string=soup.select("div.rankings-block__banner--name-large")
name_string=name_string[0].get_text()
name=("".join(name_string.split()).replace(",",""))
nation_string=soup.select("div.rankings-block__banner--nationality")
nation_string=nation_string[0].get_text()
nation2=("".join(nation_string.split()).replace(","," "))
rating_string=soup.select("div.rankings-block__banner--rating")
rating_string=rating_string[0].get_text()
rating=("".join(rating_string.split()).replace(",",""))

d={"pos":pos_string,
    "name":name_string,
    "nation":nation2,
    "rating":rating_string}
dfd=pd.DataFrame(d,index=[0])


#pos_s1=soup.select("td.table-body__cell.table-body__cell--position.u-text-right")
name_s1=soup.select("td.table-body__cell.rankings-table__name.name")
nation_s1=soup.select("td.table-body__cell.nationality-logo.rankings-table__team")
rating_s1=soup.select("td.table-body__cell.rating")

pos_s1=[b.get_text().split("\n")[1] for b in soup.select("td.table-body__cell.table-body__cell--position.u-text-right")]

pos=[]
i=0
t=len(str(len(pos_s1)))
for ele in pos_s1:
    if i<10:
        b=pos_s1[i][-t::]
    i+=1
    if i ==10:
        break
    data={"pos":b}
    pos.append(data)
pos=pd.DataFrame(pos)

perf=[]

for i in range(0,9):    
    #pos_string1=pos_s1[i].get_text()
    #pos1=("".join(pos_string1.split()).replace(",",""))
    name_string1=name_s1[i].get_text()
    name1=("".join(name_string1.split()).replace("",""))
    nation=nation_s1[i].get_text()
    nation=("".join(nation.split()).replace(",",""))
    rating_string1=rating_s1[i].get_text()
    rating1=("".join(rating_string1.split()).replace(",",""))   

    data={"pos":pos1,
         "name":name1,
          "nation":nation,
         "rating":rating1
          }
    perf.append(data)


    
df=pd.DataFrame(perf)
df["pos"]=pos

join_df=pd.concat([dfd,df])

join_df=join_df[["pos","name","nation","rating"]]
join_df.reset_index(drop=True)   


# **7. Write a python program to scrape details of all the mobile phones under Rs. 20,000 listed on Amazon.in. The 
# scraped data should include Product Name, Price, Image URL and Average Rating.**

# In[51]:


from bs4 import BeautifulSoup
import pandas as pd
import requests


url ='https://www.amazon.in/s?i=electronics&bbn=1389401031&rh=n%3A976419031%2Cn%3A1389401031%2Cn%3A1389432031%2Cp_36%3A10000-2000000&dc&qid=1623684869&rnid=1389401031&ref=sr_nr_n_3'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
mobile_string=soup.select("span.a-size-base-plus.a-color-base.a-text-normal")
price_string=soup.select("span.a-offscreen")
rating_string=soup.select("span.a-icon-alt")
image = [b.attrs.get('src') for b in soup.select("img.s-image")]
perf=[]

for i in range(0,len(mobile_string)):    
    mobile_string1=mobile_string[i].get_text()
    price_string1=price_string[i].get_text()
    rating_string1=rating_string[i].get_text()
    
    data={"name":mobile_string1,
         "price":price_string1,
         "rating":rating_string1,
         "image":image
         }
    
    perf.append(data)
    
df=pd.DataFrame(perf)
df


# In[40]:


response## some time code doesn't run due to 503 error service not available.


# **8. Write a python program to extract information about the local weather from the National Weather Service 
# website of USA, https://www.weather.gov/ for the city, San Francisco. You need to extract data about 7 day 
# extended forecast display for the city. The data should include period, short description, temperature and 
# description.**

# In[10]:


from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

url = "https://forecast.weather.gov/MapClick.php?textField1=37.77&textField2=-122.42#.YMjqY6gzYdU"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

period_title=soup.select("div.col-sm-2.forecast-label")
description=soup.select("div.col-sm-10.forecast-text")

j=0
destring=[]
for i in range(0,len(description)):
    desc=description[j].get_text()
    j+=1
    destring.append(desc)
    

df=[]

for ele in destring:  
    splitstr=ele.split(",",1)
    short=splitstr[0]
    rest=splitstr[-1]
    #print(short)
    #print(rest)
    
    data={"ShortDescription":short,
         "TemperatureDesc":rest}
    df.append(data)
    
df=pd.DataFrame(df)
df1=[]    
for i in range(0,len(description)):
    period=period_title[i].get_text()
    df1.append(period)
  
df1=pd.DataFrame(df1)
df1.columns=["Period"] 
join=pd.concat([df1,df],axis=1) 
join


# **9. Write a python program to scrape fresher job listings from ‘https://internshala.com/’. It should include job title, 
# company name, CTC, and apply date.**

# In[130]:


from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

url = 'https://internshala.com/fresher-jobs'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

job_title=soup.select("div.heading_4_5.profile")
company_name=soup.select("div.heading_6.company_name")
ctc=soup.select("div.item_body")


ctc_report=[]
index=0
while index < len(ctc):
        index = index +1
        salary=ctc[index].get_text()
        salary=("".join(salary.split()).replace(",",""))
        
        index = index +1
        joindate=ctc[index].get_text()
        joindate=("".join(joindate.split()).replace(",",""))
        index = index +1
       
        report={"salary":salary,
               "joindate":joindate,
               }
       
        ctc_report.append(report)
        
perf=[]

for i in range(0,len(job_title)):    
    job=job_title[i].get_text()
    job_title1=("".join(job.split()).replace(",",""))
 
    company_name1=company_name[i].get_text()
    company_name1=("".join(company_name1.split()).replace(",",""))
    
    data=ctc_report[i]
    
    data.update({"jobtitle":job_title1,
         "ComapnyName":company_name1,
         })
    perf.append(data)
   
df=pd.DataFrame(perf)
df 


# **10. Write a python program to scrape house details from mentioned url. It should include house title, location, 
# area, emi and price
# https://www.nobroker.in/property/sale/bangalore/Electronic%20City?type=BHK4&searchParam=W3sibGF0IjoxMi44N
# DUyMTQ1LCJsb24iOjc3LjY2MDE2OTUsInBsYWNlSWQiOiJDaElKdy1GUWQ0cHNyanNSSGZkYXpnXzhYRW8
# iLCJwbGFjZU5hbWUiOiJFbGVjdHJvbmljIENpdHkifV0=&propertyAge=0&radius=2.0**

# In[451]:


from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

url ="https://www.nobroker.in/property/sale/bangalore/Swathantra%20Nagar?searchParam=W3sibGF0IjoxMy4wMDkxOTkxLCJsb24iOjc3LjcxMTkyMDcsInBsYWNlSWQiOiJDaElKVTlsVk1iQVJyanNSaFVFcHQ0eWQ3eTgiLCJwbGFjZU5hbWUiOiJNYXJ0aGFsbGkgYnVzIHN0b3AifV0=&radius=2.0" 
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')



house_title=soup.select("h2.heading-6.font-semi-bold.nb__1AShY")
#house=house_title[0].get_text()
loc_title=soup.select("div.nb__2CMjv")
#location=loc_title[0].get_text()
area_title=soup.select("div.nb__3oNyC")
#area=area_title[0].get_text()
emi_pm=soup.select("div.font-semi-bold.heading-6")
price_string=soup.select("div.font-semi-bold.heading-6")

emi=[]
pri=[]
index=0
indice=0
for i in range(0,len(house_title)):
    index=index+1
    indice=indice+2
    em=emi_pm[index].get_text()
    price=emi_pm[indice].get_text()
    index+=2
    indice+=1
    
    
   
    emi.append(em)
    pri.append(price)
data={"emi":emi,
     "price":pri}
df=pd.DataFrame(data)
df
               
report=[]

for i in range(0,len(house_title)):
               housename=house_title[i].get_text()
               location=loc_title[i].get_text()
               area=area_title[i].get_text()
               
               data={"housename":housename,
                    "location":location,
                    "area":area}
               report.append(data)

report
df1=pd.DataFrame(report)
df1
df
#print(df1)

join_report=pd.concat([df1,df],axis=1)
join_report


# In[ ]:




