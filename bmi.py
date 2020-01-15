
def get_bmi(h,w):
    return w / (h*h)
def get_cond(bmi):
    if bmi >= 18.5 and bmi < 25:
        return 'normal weight'
    elif bmi <18.5:
        return 'below normal weight'
    elif bmi >=25 and bmi < 30:
        return 'overweight'
    elif bmi >= 30 and bmi < 35:
        return 'class I obesity'
    elif bmi >= 35 and bmi < 40:
        return 'class II obesity'
    elif bmi>=40:
        return 'class III obesity'
    
weight = float(input('weight(kg): '))
height = float(input('height(m): '))

print('bmi: ' + str(get_bmi(height,weight)))
print('condition: ' + str(get_cond(get_bmi(height,weight))))