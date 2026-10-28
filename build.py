"""Monta o index.html do site a partir do jogo e acrescenta o que faz ele virar app (PWA)."""
import sys
src=open(sys.argv[1]).read();old=open(sys.argv[2]).read()
head=old[:old.index('<title>')];i=src.index('</style>')+8
html=head+src[:i]+'\n</head>\n<body>\n'+src[i:]+'\n</body>\n</html>\n'
pwa=('<link rel="manifest" href="manifest.webmanifest">\n<link rel="apple-touch-icon" href="icons/icon-192.png">\n'
     '<script>if("serviceWorker" in navigator)addEventListener("load",()=>navigator.serviceWorker.register("sw.js").catch(()=>{}));</script>\n')
html=html.replace('<head>\n','<head>\n'+pwa,1)
# vídeo e imagem do menu viram arquivos separados (o site fica leve e o navegador guarda em cache)
import re,base64
for mime,ext,name in [('video/webm','webm','menu'),('video/mp4','mp4','menu'),('image/webp','webp','menu-poster')]:
    m=re.search(r'data:'+mime+r';base64,([A-Za-z0-9+/=]+)',html)
    if m:
        open(f'{name}.{ext}','wb').write(base64.b64decode(m.group(1)));html=html.replace(m.group(0),f'{name}.{ext}',1)
open('index.html','w').write(html)
