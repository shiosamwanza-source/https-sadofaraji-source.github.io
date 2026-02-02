import os

# 1. Taja mahali folder lilipo (Nukta '.' inamaanisha folder hili hili la sasa)
folder_path = "." 

# 2. Pata orodha ya faili zote zilizomo
faili_zote = os.listdir(folder_path)

# 3. Anza kubadili majina moja baada ya jingine
namba = 1
for jina_la_zamani in faili_zote:
    # Tunabadili faili zinazoanza na 'IMG' tu
    if jina_la_zamani.startswith("IMG"):
        jina_jipya = f"picha_kitabu_{namba}.jpg"
        
        # Amri ya kubadili jina
        os.rename(jina_la_zamani, jina_jipya)
        
        print(f"Imefanikiwa: {jina_la_zamani} sasa ni {jina_jipya}")
        namba += 1
      
