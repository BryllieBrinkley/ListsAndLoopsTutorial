songs = ["ROCKSTAR", "Do It", "For The Night"]

#print(songs[1])
#print(songs[0:2])

songs[2] = "Mob Ties"
#print(songs)

# adds an element to the end of the list
songs.append("Tuesday")

# adds a list to end of a list
songs.extend(["Lust for Life"])
songs.insert(0, "No Guidance")
#print(songs)

del songs[0]
#print(songs)

# for song in songs:
  #  print(song)

# for i in range(len(songs)):
    #print(songs[i])


animals = ["Giraffe", "Gorilla", "Penguin"]

animals.append("Panda")

print(animals)
print(animals[2])

#del animals[0]
#print(animals)

for i in range(len(animals)):
  print(animals[i])
