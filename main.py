from bs4 import BeautifulSoup
import requests
import time 

def find_job():
    html_text =  requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=Python&txtKeywords=Python&txtLocation=").text
    soup = BeautifulSoup(html_text,"lxml")

    blocks = soup.find_all("li",class_="clearfix job-bx wht-shd-bx")
    companies = [block.h3.text.strip() for block in blocks]
    skills = [block.find("span",class_="srp-skills").text.strip().replace(" ","").replace(",","_") for block in blocks]
    posts = [block.find("span",class_="sim-posted").text.strip().replace(" ","") for block in blocks]
    more_infos =[block.h2.a["href"] for block in blocks] 

    
    x = input("Skills that you don't possess \n").split(",")

    str1 ="Posted,Company Name,Skill Requirement,More Info\n"

    for i in range(len(companies)):
        error = 1
        if (posts[i] == "Postedfewdaysago"):
            for a in x:
                if a in skills[i]:
                    error = 0
                    break
        else:
            continue
        if error == 0:
            continue
        #Writing Outputs into text files
        print(f'''
Company Name: {companies[i]}
Skill Requirement: {skills[i]}
Posted: {posts[i]}
More Info: {more_infos[i]}
    ''')
       
        str1 = str1 + (f"{posts[i]},{companies[i]},{skills[i]},{more_infos[i]} \n")
        
    with open(f"output.csv","w") as f:
        f.write(str1)
        
if __name__ == "__main__":
    while True:
        find_job()
        time_wait = 10
        print(f"Waiting time: {time_wait} Minutes")
        time.sleep(time_wait*60)

