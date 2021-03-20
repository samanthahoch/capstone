
code = {'AB': "A", '1B': "A", "2B": "B", "3B": "C", "4B": "D", "5B" : "E",
'6B':'F', '7B':'G', '8B':'H', '9B':'I', '10B' : "J",
'JB':'K', 'QB': "L", 'KB':"M",
'AR': "N", '1R': "N", "2R": "O", "3R": "P", "4R": "Q", "5R" : "R",
'6R':'S', '7R':'T', '8R':'U', '9R':'V', '10R' : "W",
'JR':'X', 'QR': "Y", 'KR':"Z"}


text = "KB 4R QB 9B 7R 3R QB 5B 2R QB 5B AB 5B 8R 5R 2R 3R AB 5B AB 8B AB 9R 5B 7B AB 9B AR 5B 4B 4B 9B 9R 9B AR 5B 6B AB 9R 2R 5R "

text = text.split(" ")

ans = ""
for i in text:
    a = code.get(i)
    if a is not None:
        ans = ans + code.get(i)
    else: 
        ans = ans + i 

print(ans)