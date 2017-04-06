#!/usr/bin/python3

def bold(string):
    return "**"+string+"**"
def italic(string):
    return "_"+string+"_"

print("This script will generate a writer's row from user")
print("input.\n")
print("Leave options blank if you don't know.\n")

# hockey team
team_name = input("Enter team:  ")
print("Enter ",team_name,"'s official site:  ", end='')   
team_site = input()

# beat writer
beat_writer = input("Beat writer:  ")
print("Most prolific writer for ",team_name,"? [Y/n]:  ", end='')
prolific = input()

# news site
news_name = input("Enter news site name:   ")
print("Link to ",news_name,"'s coverage of ",team_name,":  ", end='')
news_link = input()
print("Link to RSS feed on",news_name,":  ", end='')
news_rss = input()

# profiles
print("Link to ",beat_writer,"'s profile on ",news_name,":  ", end='')
writer_bio = input()
print(beat_writer,"'s twitter handle:  ", end='')
writer_twitter = input()
print(beat_writer,"'s email address:  ", end='')
writer_email = input()

# if fields are non empty, generate markdown style link handling

if prolific=="Y" or prolific=="y":
    beat_writer=bold(beat_writer)

if team_site != "":
    team_name = "["+team_name+"]("+team_site+")"

if writer_bio != "":
    beat_writer = "["+beat_writer+"]("+writer_bio+")"

if news_link != "":
    news_name = "["+news_name+"]("+news_link+")"

if writer_email != "":
    writer_email = "[ ![Email][envelope] ](mailto:"+writer_email+")" 

if writer_twitter != "":
    writer_twitter = "[ ![@"+writer_twitter+"][twitter] ](https://twitter.com/"+writer_twitter+")"

if news_rss != "":
    news_rss = "[ ![RSS][rss] ]("+news_rss+")"

print()
print(
        "|",
        team_name,
        "|",
        beat_writer,
        "|",
        news_name,
        "|",
        writer_twitter,
        news_rss,
        writer_email,
        "|"
)
