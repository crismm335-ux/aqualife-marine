"""Monta o index.html do site a partir do jogo e acrescenta o que faz ele virar app (PWA)."""
import sys
src=open(sys.argv[1]).read();old=open(sys.argv[2]).read()
head=old[:old.index('<title>')];i=src.index('</style>')+8
html=head+src[:i]+'\n</head>\n<body>\n'+src[i:]+'\n</body>\n</html>\n'
pwa=('<link rel="manifest" href="manifest.webmanifest">\n<link rel="apple-touch-icon" href="icons/icon-192.png">\n'
     '<script>if("serviceWorker" in navigator)addEventListener("load",()=>navigator.serviceWorker.register("sw.js").catch(()=>{}));</script>\n')
html=html.replace('<head>\n','<head>\n'+pwa,1)
open('index.html','w').write(html)
