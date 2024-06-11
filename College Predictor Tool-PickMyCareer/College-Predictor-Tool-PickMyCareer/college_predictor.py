category_list = [
    ['Computer Science', 'Computer Science (SS)'],
    ['Information Technology', 'Information Technology (SS)', 'Information Science & Technology'],
    ['Computer Science Business System', 'Computer Science Business System (SS)'],
    ['Computer Science (AIML)', 'Computer Science (AIML) (SS)'],
    ['Artificial Intelligence & Data Science', 'Artificial Intelligence & Data Science (SS)'],
    ['Civil Engineering', 'Civil Engineering (SS)'],
    ['Electronics &Communication', 'Electronics &Communication (SS)'],
    ['Electrical & Electronics', 'Electrical & Electronics (SS)', 'Electrical & Electronics (Sandwich) (SS)'],
    ['Mechanical (Tamil Medium)'],
    ['Civil Engineering (Tamil Medium)'],
    ['Industrial'],
    ['Manufacturing'],
    ['M. Tech Computer Science (5Y)'],
    ['Mechanical', 'Mechanical (SS)', 'Mechanical (Sandwich) (SS)'],
    ['Mechatronics', 'Mechatronics (SS)'],
    ['Robotics And Automation', 'Robotics And Automation (SS)'],
    ['Metallurgical', 'Metallurgical (SS)'],
    ['Production', 'Production (SS)', 'Production (Sandwich) (SS)'],
    ['Food Technology', 'Food Technology (SS)'],
    ['Bio Technology', 'Bio Technology (SS)', 'Industrial Bio Technology', 'Industrial Bio Technology (SS)']
]

def category(course):
    for category in category_list:
        if course in category:
            return category
    return [course]

def list_of_colleges(mark, course, community, data):
    course_final = category(course)
    filtered_data = data[data['Branch Name'].isin(course_final) & (data[community] <= (mark + 5))]
    result = filtered_data[['College Code', 'College Name','Branch Code', 'Branch Name' , community]]
    result = result.sort_values(by=community, ascending=False)
    return result