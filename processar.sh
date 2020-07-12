lista=$(ls ./fazer/x* | head -1)

# Usado para indicar qual elemento da lista está sendo processado

indice=1;
cat $lista | while read line 
do

echo '{"Type": "archive-retrieval","ArchiveId": "'$line'","Description": "'$lista' '$indice'"}' > request.json
aws glacier initiate-job --account-id - --vault-name 2020_abril_06  --job-parameters file://request.json
	((indice++))
done

mv $lista ./feitos
