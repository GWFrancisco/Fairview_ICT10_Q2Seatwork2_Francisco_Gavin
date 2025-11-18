from pyscript import document, display

def general_weighted_average(e):

    # Clear previous output
    document.getElementById("student_info").innerText = ""
    document.getElementById("summary").innerText = ""
    document.getElementById("output").innerText = ""

    # Get student name
    first_name = document.getElementById('first_name').value
    last_name = document.getElementById('last_name').value

    # Get grades
    science = float(document.getElementById('science').value)
    math = float(document.getElementById('math').value)
    english = float(document.getElementById('english').value)
    filipino = float(document.getElementById('filipino').value)
    ict = float(document.getElementById('ict').value)
    pe = float(document.getElementById('pe').value)

    # Compute weights
    weighted_sum = (
        science * 5 +
        math * 5 +
        english * 5 +
        filipino * 3 +
        ict * 2 +
        pe * 1
    )

    total_units = (5 * 3) + 3 + 2 + 1   # 21 units total
    gwa = weighted_sum / total_units

    # Display student name
    display(f"Name: {first_name} {last_name}", target="student_info")

    # Summary of grades
    summary = f"""
    Science: {science:.0f}
    Math: {math:.0f}
    English: {english:.0f}
    Filipino: {filipino:.0f}
    ICT: {ict:.0f}
    PE: {pe:.0f}
    """
    display(summary, target="summary")

    # Display GWA
    display(f"Your General Weighted Average is: {gwa:.2f}", target="output")


