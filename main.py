from sqs_wrapper import send_json, return_all, create_queue
from dynamodb_wrapper import create_table, send_data, return_data

#prepare enviroment
create_table()
create_queue()

send_json({
    'first_number' : 14,
    'second_number' : 20
})
send_json({
    'first_number' : 15,
    'second_number' : 20
})


result = return_all()

for r in result:
    send_data(r)

res_dynamo = return_data()
for r in res_dynamo:
    print(r)

