import json
f="apps/lines/static/assets/sprites/symbolsStatic/symbolsStatic.json"
j=json.load(open(f))
o=["h1.webp","h2.webp","h3.webp","h4.webp","h5.webp","l1.webp","l2.webp","l3.webp","l4.webp","l5.webp","s.png","w.png"]
for i,k in enumerate(o): j["frames"][k]["frame"]["x"]=divmod(i,4)[1]<<9; j["frames"][k]["frame"]["y"]=divmod(i,4)[0]<<9
json.dump(j,open(f,"w"))
