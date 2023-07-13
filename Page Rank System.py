p=[]
with open("pages.txt","r") as f:
    data=f.readlines()
d={}
for line in data:
    parts = line.split(": ")
    key = parts[0].split(",")
    url = key[0]
    weightage = key[1]
    urls = parts[1].strip().split()
    print(urls)
    url_list = set()
    for i in urls:
        if i.startswith("URL"):
            url_list.add(i.rstrip(".").rstrip(","))
    d[url] = {"weightage": weightage, "urls": list(url_list)}
u = list(d.keys())
weightages = [d[url]['weightage'] for url in u]
related_urls = [d[url]['urls'] for url in u]
for i in range(len(u)):
    w=u[i]
    t=0
    for j in range(len(related_urls)):
        if w in related_urls[j]:
            t=t+float(weightages[j])/len(related_urls[j])
    p.append(round(t,2))
result = []
for i in range(len(u)):
    result.append((u[i],p[i]))
for i in range(len(result)):
    for j in range(len(result) - 1):
        if result[j][1] < result[j+1][1]:
            result[j], result[j+1] = result[j+1], result[j]
print(result)
