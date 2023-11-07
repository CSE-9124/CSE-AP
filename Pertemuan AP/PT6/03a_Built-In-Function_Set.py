# 4. Built-In Function di Set
setExample = {'Java', 'Python', 1, 2}
# ~ Add         -> ".add()"
setExample.add('Kotlin')
print(setExample)

# ~ Pop         -> ".pop()"  (hanya mengambil dan menyimpan nilai int pertama/str pertama pada data set)
setExample.pop()
print(setExample)

# ~ Remove      -> ".remove()"
setExample.remove(1)
print(setExample)

# ~ Discard     -> ".discard()"  (utk menghapus nilai yg sama)
setExample.discard("Kotlin")
print(setExample)

setExample.discard("Tes")
print(setExample)


# 5. Frozen Set
duplicateSet = {1, 3, 2, 3, 2, 3, 4}
print(setExample)