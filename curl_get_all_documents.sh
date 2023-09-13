curl --request POST \
     --url http://10.1.0.4:8000/documents/get_by_filters \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --data '{"filters": {}}' | more
