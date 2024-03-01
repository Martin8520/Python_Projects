friends = {"Bob", "Ralf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)
if len(local_friends) == 1:
    print(f"{local_friends} lives here")
elif len(local_friends) > 1:
    print(f"{local_friends} live here")
else:
    print(f"{friends} live abroad")

friends2 = local_friends.union(abroad)
print(friends2)

art = {"Bob", "Jen", "Ralf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
print(f"{both} study art and science.")
