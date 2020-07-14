
cat lista_archiveID | while read line
do
	echo "aws glacier delete-archive --account-id - --vault-name 2020_abril_06 --archive-id $line"
done


