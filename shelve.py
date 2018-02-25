Python 3.5.1+ (default, Mar 30 2016, 22:46:26) 
[GCC 5.3.1 20160330] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import shelve
>>> shelfFile = shelve.open('mydata')
>>> cats = ['zophie','pooka','simon']
>>> shelfFile['cats'] = cats
>>> shelfFile.close()
>>> 
