import yaml

count=0
file_name = "sample.yml"
stream = open(file_name, "r")
dacs = yaml.load_all(stream,Loader=yaml.SafeLoader)
#print(data)
for doc in dacs:
    print(f"\n<<< Documer Number {count+1}>>>\n")
    for K,V in doc.items():
        if K.find("_Server") != -1:
            print(f"Key:{K} Value:{V}")
    count=count + 1
