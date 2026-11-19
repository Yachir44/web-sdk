from PIL import Image
d="apps/lines/static/assets/sprites/symbolsStatic/"
n=["H1","H2","H3","H4","H5","L1","L2","L3","L4","L5","S","W"]
sh=Image.new("RGBA",(2048,1536))
for i,k in enumerate(n): sh.paste(Image.open(d+k+".png").convert("RGBA").resize((512,512)),(divmod(i,4)[1]<<9,divmod(i,4)[0]<<9))
sh.save(d+"symbolsStatic.png")
sh.save(d+"symbolsStatic.webp",quality=90)
