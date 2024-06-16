napok:list[str]=['hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek']

def maganhangzok_szamok(nap):
    darab=0 
    m='aáeéiíoóöőuúüű'
    for betu in nap:
        if betu in m:
            darab+=1
    return darab

legtobb=napok[1]
for nap in napok[1:]:
    if maganhangzok_szamok(nap)>maganhangzok_szamok(legtobb):
        legtobb=nap
print(f'A legtöbb magánhangzó a {legtobb}-ben van.')