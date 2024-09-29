from utils.api_helper import APIHelper

def filter_fancode_users(users):
    lat_lag = []
    for user in users:
        if -40 <= float(user['address']['geo']['lat']) <= 5 and 5 <= float(user['address']['geo']['lng']) <= 100 :
            lat_lag.append(user)
    return lat_lag

def calculate_task_completion_percentage(user_id, todos):
    user_todos = []
    completed_todos = []
    for todo in todos:
         if todo['userId'] == user_id:
             user_todos.append(todo)
    for todo in user_todos:
        if todo['completed'] :
            completed_todos.append(todo)

    if user_todos:
        return (len(completed_todos) / len(user_todos)) * 100
    return 0

api_helper = APIHelper()
users =  api_helper.get_users()
todos =  api_helper.get_todos()

result = filter_fancode_users(users)
for user in result:
    completion_percentage = calculate_task_completion_percentage(user['id'],todos)
    if completion_percentage > 50:
        print(f"User {user['name']} has completed {completion_percentage:.2f}% of tasks.")
    else:
        print(f"User {user['name']} has NOT completed enough tasks: {completion_percentage:.2f}%.")





