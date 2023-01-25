import random
import string
import nameslist

email_providers = ["yahoo", "gmail","hotmail", "outlook"]
tlds = [".com",".co.uk", ".net", ".au",".org"]

for i in range (1000):
    random_numbers = random.randint(1,2)
    random_server_sel = "@"+random.choice(email_providers)+random.choice(tlds)
    randnames = random.choice(nameslist.Names)
    random_2lettercomb = ''.join(random.choice(string.ascii_letters) for i in range (2))
    print(randnames+random_2lettercomb+str(random_numbers)+random_server_sel)

#don't forget to create another file (nameslist)
Names = [
"Theodore"

]
