from PIL import Image
import imagehash

hash0=imagehash.average_hash(Image.open("C:/Users/Administrator/Desktop/download3.jpg"))
hash1=imagehash.average_hash(Image.open("C:/Users/Administrator/Desktop/download4.jpg"))

#print(type(Image.open("C:/Users/Administrator/Desktop/download.jpg")))
print(hash0)
print(hash1)
print(hash0-hash1)

cutoff=5

if hash0-hash1 < cutoff:
    print("same images")
else:
    print("images are not same")
