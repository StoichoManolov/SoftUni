software_version = [int(x) for x in input().split('.')]


def new_version():

    if software_version[2] == 9:
        software_version[2] = 0
        software_version[1] += 1
        if software_version[1] == 10:
            software_version[1] = 0
            software_version[0] += 1
    else:
        software_version[2] += 1

    return software_version


print(*new_version(), sep='.')

