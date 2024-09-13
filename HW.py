def ask_symptom(patient, symptom_name):
    """Ask the user if the patient has a specific symptom."""
    response = input(f"Does {patient} have a {symptom_name} (y/n)? ").strip().lower()
    return response == 'y'

def diagnose(patient):
    """Diagnose the disease based on the patient's symptoms."""
    if (symptom(patient, "fever") and 
        symptom(patient, "cough") and
        symptom(patient, "conjunctivitis") and
        symptom(patient, "runny nose") and
        symptom(patient, "rash")):
        return "measles"
    
    elif (symptom(patient, "fever") and 
          symptom(patient, "headache") and
          symptom(patient, "runny nose") and
          symptom(patient, "rash")):
        return "german_measles"
    
    elif (symptom(patient, "fever") and 
          symptom(patient, "headache") and
          symptom(patient, "body ache") and
          symptom(patient, "conjunctivitis") and
          symptom(patient, "chills") and
          symptom(patient, "sore throat") and
          symptom(patient, "cough") and
          symptom(patient, "runny nose")):
        return "flu"
    
    elif (symptom(patient, "headache") and 
          symptom(patient, "sneezing") and
          symptom(patient, "sore throat") and
          symptom(patient, "chills") and
          symptom(patient, "runny nose")):
        return "common_cold"
    
    elif (symptom(patient, "fever") and 
          symptom(patient, "swollen glands")):
        return "mumps"
    
    elif (symptom(patient, "fever") and 
          symptom(patient, "rash") and
          symptom(patient, "body ache") and
          symptom(patient, "chills")):
        return "chicken_pox"
    
    elif (symptom(patient, "cough") and 
          symptom(patient, "sneezing") and
          symptom(patient, "runny nose")):
        return "whooping_cough"
    
    else:
        return None

def symptom(patient, symptom_name):
    """Check if the patient has a specific symptom."""
    return ask_symptom(patient, symptom_name)

def main():
    """Main function to interact with the user and diagnose the disease."""
    patient = input("What is the patient’s name? ").strip()
    disease = diagnose(patient)
    
    if disease:
        print(f"{patient} probably has {disease}.")
    else:
        print("Sorry, I don’t seem to be able to diagnose the disease.")

if __name__ == "__main__":
    main()