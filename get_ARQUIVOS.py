import json 

# aws glacier list-jobs --account-id - --vault-name 2020_abril_06	 > testar

with open('testar') as f:
    data = json.load(f)

# Primeira passada
fonte={}

for item in data["JobList"]:
	print  "aws glacier get-job-output --account-id - --vault-name 2020_abril_06	 --job-id  %s %s.mp4"  % (item["JobId"], item["JobId"])
