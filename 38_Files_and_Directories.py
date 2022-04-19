from pathlib import Path

#absolute Path
#C:\Program Files\User...

#Relativce Path

path = Path("ecomerce")
print(path.exists())
#path.mkdir("emails") # add directory
#path.rmdir("emails") # remove

path = Path()
for file in path.glob('*.py'):
    print(file)