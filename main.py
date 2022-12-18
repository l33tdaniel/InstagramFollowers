import instaloader
def main():
    remove_file = open("remove.txt", "w")
    followers_file = open("followers.txt", "w")
    followees_file = open("followees.txt", "w")
    
    username = input("What is the username of the account you'll be logging into? ")
    password = input("What is the password for the account you'll be logging into? ")
    loader = instaloader.Instaloader()
    loader.login(username, password)

    accountToSearchFor = input("What is the name of the account you're searching for?")
    profile = instaloader.Profile.from_username(loader.context,accountToSearchFor)

    followers = profile.get_followers()
    followees = profile.get_followees()

    list_to_remove = list(set(followees) - set(followers))
    for x in list_to_remove:
        print(x.username)
    for x in followers:
        followers_file.write(f"{x.username}\n")
    for x in followees:
        followees_file.write(f"{x.username}\n")
    for x in list_to_remove:
        remove_file.write(f"{x.username}\n")
main()