from pyscript import display, document

def general_weighted_average(e):


    science = float(document.getElementById('science').value)
    math = float(document.getElementById('math').value)
    english = float(document.getElementById('english').value)
    tle = float(document.getElementById('tle').value)
    ict = float(document.getElementById('ict').value)
    socialstudies = float(document.getElementById('socialstudies').value)

    display(f'Name: {first_name} {last_name}', target="student_info")
    display(summary, target='summary')
    display(f'Your general weighted average is {gwa:.2f}', target='output')

    weighted_sum = (science * 5 + math * 5 + english * 5 + filipino * 3 + ict * 2 + pe * 1)
    total_units = (5 * 3) + 3 + 2 + 1
    gwa = weighted_sum / total_units

    display(f'Name: {first_name} {last_name}', target="student_info")
    displa y(summary, target='summary')
    display(f'Your general weighted average is {gwa:.2f}', target='output')
    
    summary = f"""{subject[0]}: {science:.0f}
{subjects{1}}: {math:.0f}
{subjects{2}}: {english:0f}
{subjects{3}}: {tle:0f}
{subjects{4}}: {ict:0f}
{subjects{5}}: {socialstudies: 0f}
    """
    display(f'Name: {first_name} {last_name}', target="student_information")
    display(summary,target='summary')

    display(f'Your general weighted average is {gwa:2f}', target='output',)
