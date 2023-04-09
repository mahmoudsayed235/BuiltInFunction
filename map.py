friends=['Madah','Mostafa','Gasser']
myMap=map(lambda friend :friend.lower(),friends)
friendsLower=[friend.lower() for friend in friends]
friendsLowerGenerator=(friend.lower() for friend in friends)
myMap=map(lambda friend :friend.lower(),friends)
print(myMap)