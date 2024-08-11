def find_job():
    from bs4 import BeautifulSoup
    import requests

    html_text =  requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=Python&txtKeywords=Python&txtLocation=").text
    soup = BeautifulSoup(html_text,"lxml")

    blocks = soup.find_all("li",class_="clearfix job-bx wht-shd-bx")
    companies = [block.h3.text.strip() for block in blocks]
    skills = [block.find("span",class_="srp-skills").text.strip().replace(" ","") for block in blocks]
    posts = [block.find("span",class_="sim-posted").text.strip().replace(" ","") for block in blocks]

    
    x = input("Skills that you don't possess").split(",")
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
        print(f'''
    Company Name: {companies[i]}
    Skill Requirement: {skills[i]}
    Posted: {posts[i]}
    ''')
        

if __name__ == "__main__":
    while True:
        find_job()

