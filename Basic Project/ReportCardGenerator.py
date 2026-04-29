#Report Card Generator
def main() :
    print("Check your Result!")

    English= int(input("Enter your English score :"))
    Mathematics= int(input("Enter your Mathematics score :"))
    GeneralKnowledge= int(input("Enter your General Knowledeg score :"))

    sum = English + Mathematics + GeneralKnowledge
    percentage = float(sum / 3)
    def marks_obtained(score):
        if score >= 90 :
            return "You have achieved Grade A+ !!!"
        elif score >= 80 :
            return"You have achieved Grade A !!!"
        elif score >= 70 :
            return"You have achieved Grade B+ !!"
        elif score >= 60 :
            return"You have achieved Grade B !!"
        elif score >= 50 :
            return"You have achieved Grade C+ !"
        elif score < 50 :
            return"Try Again !!!"
        

    print("\nResults:")
    print("English:", marks_obtained(English))
    print("Maths:", marks_obtained(Mathematics))
    print("General Knowledge:", marks_obtained(GeneralKnowledge))
    print(f"Total Percentage : {percentage}")

main()