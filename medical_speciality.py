# lex_auth_012693816757551104165

def max_visited_speciality(patient_medical_speciality_list, medical_speciality):
    speciality_count = {}

    # Count the number of patients for each speciality
    for patient in patient_medical_speciality_list:
        speciality = patient
        if speciality in speciality_count:
            speciality_count[speciality] += 1
        else:
            speciality_count[speciality] = 1

    # Find the speciality with the maximum count
    max_speciality = max(speciality_count, key=speciality_count.get)
    speciality_name = medical_speciality.get(max_speciality)

    return speciality_name


# provide different values in the list and test your program
patient_medical_speciality_list = [
    101, 'O', 102, 'E', 302, 'P', 305, 'P', 401, 'E', 656, 'O', 987, 'E']


medical_speciality = {"P": "Pediatrics", "O": "Orthopedics", "E": "ENT"}
speciality = max_visited_speciality(
    patient_medical_speciality_list, medical_speciality)
print(speciality)
