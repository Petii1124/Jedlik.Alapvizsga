szoveg='Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima aliquam neque, quo excepturi totam sit ratione aliquid earum soluta magnam, natus debitis fugit eligendi architecto voluptates eum dolore nemo eaque! Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequatur beatae eos odio cum omnis natus sit porro molestiae officiis ex exercitationem eius repudiandae quos magni obcaecati, numquam pariatur! Aspernatur, quis.'

irasjelek='.,:-?!;'
for irasj in irasjelek:  #irasjeleket eltuntetjuk
    szoveg=szoveg.replace(irasj,'')

szoveg=szoveg.lower()
szavak=szoveg.split(' ') 
#print(szavak)

stat={}
for szo in szavak:
    if szo in stat.keys():
        stat[szo]+=1
    else:
        stat[szo]=1
#print(stat)

for a,b in stat.items():
    if b>2:
        print(f'{a} - {b} db')

# legtobb_value=-1
# legtobb_key=""
# for key,value in stat.items():
#     if value>legtobb_value:
#         legtobb_value=value
#         legtobb_key=key
# print(f'Legtöbbször a "{legtobb_key}" szó fordul elő {legtobb_value} alkalommal')
        
legtobb_value=max(stat.values())
print(f'Legtöbbször {legtobb_value} alkalommal) előforduló szavak:')
for key, value in stat.items():
    if value==legtobb_value:
        print(f'\t {key}')