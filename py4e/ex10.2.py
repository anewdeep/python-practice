'''Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.'''

fh = open("mbox-short.txt")
counts = dict()

for line in fh:
    if line.startswith("From "):
        lst = line.split()
        counts[lst[5][:2]] = counts.get(lst[5][:2], 0) + 1

sorted_keys = sorted(counts.keys())

for key in sorted_keys:
    print(key, counts[key])