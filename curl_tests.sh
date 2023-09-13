curl --request POST \
     --url http://10.1.0.4:8000/query \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --data '{
     "query": "How did Julius Caesar die?"
     }'
	 
curl --request POST \
     --url http://10.1.0.4:8000/query \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --data '{
     "query": "How julius died?"
     }'
	 
curl --request POST \
     --url http://10.1.0.4:8000/query \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --data '{
     "query": "What was the cause of Julius death?"
     }'

