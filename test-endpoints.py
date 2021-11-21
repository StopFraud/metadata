import yaml

with open("endpoints.yml", "r") as stream:
    try:
       y=yaml.safe_load(stream)
       l=(len(y))
       for i in range(0,l):
           print(y[i]["service"]["name"])

    except yaml.YAMLError as exc:
        print(exc)
