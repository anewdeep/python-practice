'''Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.'''

fh = open("mbox-short.txt")
counts = dict()
prolific_committer = ""
no_of_emails = None

for line in fh:
    if line.startswith("From "):
        words = line.split()
        counts[words[1]] = counts.get(words[1], 0) + 1

for email, count in counts.items():
    if no_of_emails is None or no_of_emails < count:
        prolific_committer = email
        no_of_emails = count

print(prolific_committer, counts[prolific_committer])