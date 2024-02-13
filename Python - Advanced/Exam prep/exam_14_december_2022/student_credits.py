def students_credits(*args):

    total_credits = 0
    courses = {}
    credits_needed = 240

    for item in args:
        course_name,credits_max,max_points,got_points = item.split('-')
        percentage_of_points = int(got_points) / int(max_points)
        points_gotten = int(credits_max) * percentage_of_points

        courses[course_name] = points_gotten
        total_credits += points_gotten

    result = ''

    if total_credits >= credits_needed:
        result += f"Diyan gets a diploma with {total_credits:.1f} credits.\n"
    else:
        result += f'Diyan needs {int(credits_needed) - total_credits:.1f} credits more for a diploma.\n'

    sorted_dic = sorted(courses.items(), key=lambda x: (-x[1]))

    for course,points in sorted_dic:
        result += f'{course} - {points:.1f}\n'

    return result



print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
