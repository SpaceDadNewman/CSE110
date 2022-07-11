with open("hr_system.txt") as hr_file:
    for line in hr_file:
        clean_line = line.strip()
        line_list = clean_line.split(" ")
        name = line_list[0]
        id = line_list[1]
        job_title = line_list[2]
        salary = float(line_list[3])
        paycheck = salary / 24
        if job_title == 'Engineer':
            paycheck += 1000
        print(f'{name} (ID: {id}), {job_title} - ${"{:.2f}".format(paycheck)} ')