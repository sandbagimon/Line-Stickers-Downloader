
# coding: utf-8

# In[7]:


import os
import requests as r
from bs4 import BeautifulSoup as bs


# =============================================================================
# initilization,scripted by sandbagimon 2018-12/12
# =============================================================================

file_name = ''
end_flag = False
#emote_address =''# 'https://store.line.me/stickershop/product/1203269/en'
count=0
def set_address(emote_address):
    global soup
    global title_name
    site = r.get(emote_address)
    soup = bs(site.content,'lxml')
    title_name = str(soup.title)
    title_name=title_name.strip('<title>')
    title_name=title_name.strip('– LINE stickers | LINE STORE</title>')
    if not os.path.exists(title_name):
        os.makedirs(title_name)

    return 

def download_file(link,count):
    global file_name
    file_name = str(title_name) + (str(count))+('.png') 
    picture = r.get(link, stream=True)
    with open(str(title_name)+'/'+file_name,'wb') as f:
        for chunk in picture.iter_content(chunk_size=1024):           
            if chunk:
                f.write(chunk)
                f.flush()
                os.fsync(f.fileno())
    return
def core():
    global soup
    global count
    global end_flag
    end_flag = False
    for link in soup.find_all(attrs={"class": "mdCMN09Image"}):
        count = count+1
        a = link.get('style')
        a=a.strip('background-image:url(')
        a=a.strip(';compress=true);')
        download_file(a,count)
    count = 0
    end_flag = True
# =============================================================================
#     manage the output to gui script
# =============================================================================
def output_name():
    global file_name
    return file_name
def end_flag_out():
    global end_flag
    return end_flag
