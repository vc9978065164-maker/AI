print("MEDICAL DIAGNOSIS EXPERT SYSTEM")

fever = input("Do you have fever? (yes/no): ").lower()
cough = input("Do you have cough? (yes/no): ").lower()
cold = input("Do you have cold? (yes/no): ").lower()
headache = input("Do you have headache? (yes/no): ").lower()

if fever == "yes" and cough == "yes" and cold == "yes":
    print("Possible condition: Flu")
elif fever == "yes" and headache == "yes":
    print("Possible condition: Viral Fever")
elif cough == "yes" and cold == "yes":
    print("Possible condition: Common Cold")
elif headache == "yes":
    print("Possible condition: Headache")
else:
    print("No matching condition found")

print("Please consult a qualified doctor for diagnosis.")
