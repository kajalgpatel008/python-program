def check_blood_donation_eligibility(age,weight,hemoglobin):
    if age>=18:
        if weight>=50:
            if hemoglobin>=12.5:
                print("Eligible to donate blood")
            else:
                print("Not eligible.Hemoglobin is too low.")

        else:
            print("Not eligible :Weight is below 50 kg.")
    else:
        print("Not eligible : Age is below 18 years.")

age=int(input("Enter Age :"))
weight=int(input("Enter weight :"))
hemoglobin=int(input("Enter Hemoglobin :"))
eligibility_message=check_blood_donation_eligibility(age,weight,hemoglobin)
