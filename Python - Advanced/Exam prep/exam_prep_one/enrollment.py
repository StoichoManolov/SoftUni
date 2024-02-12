def gather_credits(credits_needed,*args):

    total_credits = 0
    courses = {}

    for name, price in args:
        if total_credits >= credits_needed:
            break
        if name not in courses:
            courses[name] = price
            total_credits += price

    if total_credits >= credits_needed:
        return f'Enrollment finished! Maximum credits: {total_credits}.\nCourses: {", ".join(sorted(courses.keys()))}'
    else:
        return f"You need to enroll in more courses! You have to gather {credits_needed - total_credits} credits more."

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
