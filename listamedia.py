#Oihana Arambarri
#lista bat egin eta listako elementuak batuta media egin
list=[1,2,3,4,5,6]
def l_media(list):
    sum = 0
    for i in (list):
        sum = sum + i
    return sum / len(list)
print("media=",l_media(list))
