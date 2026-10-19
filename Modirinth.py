import requests
url = "https://api.modrinth.com/v2/project/"
Table = {}

def get(id):
    if requests.get(url+id).status_code == 200 :

        result = requests.get(url+id).text
        result = result[result.index("[")+1 :result.index("]")].split('","')
        result[0] = result[0].replace('"',"")
        result[-1] = result[-1].replace('"',"")
        Table[id] = result[::-1]
        print()
        print("Listed mods:")
        for key, value in Table.items():
            print(f"{key}: {value}")
        #print(Table[id])
    else:
        print("The requested item(s) were not found or no authorization to access the requested item(s)")

def worker(x):
    for key, value in Table.items():
        if key != next(iter(Table)):
            if x in value:
                continue
            else:
                return False
        else:
            continue
    return True

def check():
    compatible = []
    versions = next(iter(Table.values()), None)
    for version in versions:
        if worker(version):
            compatible.append(version)
    if len(compatible) == 0:
        return False
    else:
        return compatible

while True:
    method = input("add/remove/check?").lower()
    if method == "add":
        get(id = input("ID/slug?"))
    elif method == "remove":
        del Table[input("ID/slug?")]
        print()
        print("Listed mods:")
        print(Table)
    elif method == "check":
        print(check())




