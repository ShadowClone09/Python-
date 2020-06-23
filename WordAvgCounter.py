fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    flen = line.rstrip()
    count = count + 1
    for line in flen:
        temp = flen.find('0')
        host = flen[temp :]     
        kill = float(host)
    total = total + kill
print(total)
print(count)
average = total / count
print(average)

