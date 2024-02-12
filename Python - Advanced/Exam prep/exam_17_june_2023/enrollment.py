def gather_credits(credits_needed,*args):
    credits_count = 0
    courses = []
    result = ''

    for course,credits in args:
        if credits_count >= credits_needed:
            break
        if course in courses:
            continue
        credits_count += credits
        courses.append(course)

    if credits_count >= credits_needed:
        result += f'Enrollment finished! Maximum credits: {credits_count}.\n'
    else:
        return f'You need to enroll in more courses! You have to gather {credits_needed - credits_count} credits more.'
    courses = sorted(courses)
    result += f'Courses: {", ".join(courses)}'
    return result

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))


