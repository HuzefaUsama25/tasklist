import os
import datetime
import time


def get_tasklist():
    shit = "\nImage Name                     PID Session Name        Session#    Mem Usage\n========================= ======== ================ =========== ============\n"

    raw_tasklist = os.popen("tasklist").read().replace(shit, "").split("\n")
    tasklist = list()

    for raw_task in raw_tasklist:
        start = raw_task.find("\n") + len("\n")
        end = raw_task.find(" "*2)
        task = raw_task[start:end]
        if task not in tasklist:
            tasklist.append(task)
        if "" in tasklist:
            tasklist.remove("")
    return sorted(tasklist)


def get_current_time():
    e = datetime.datetime.now()
    current_time = e.strftime("%a, %b %d, %Y -- %I:%M:%S %p")
    return current_time


def log_to_file(tasklist, current_time):
    filename = f"{datetime.datetime.now().strftime('%d %b, %Y')}.txt"
    with open(filename, "a+") as log_file:
        tasklist_string = ",\n".join(tasklist)
        equals = "="*25
        log_file.write(
            f'''{equals}\n{current_time}\n\n{tasklist_string}\n\n\n\n''')


def main():
    tasklist = get_tasklist()
    print(tasklist)
    time.sleep(5)
    while True:
        current_time = get_current_time()
        new_tasklist = get_tasklist()
        new_tasks = [item for item in new_tasklist if item not in tasklist]
        log_to_file(new_tasklist, current_time)
        print(f"{current_time}\n{new_tasks}\n")
        tasklist = new_tasklist
        time.sleep(10)


main()
