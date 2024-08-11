def find_job():
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
