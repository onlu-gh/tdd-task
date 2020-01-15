
def get_bmi(h,w):
    return w / (h*h)
def get_cond(bmi):
    if bmi >= 18.5 and bmi < 25:
        return 'normal weight'

weight = input('weight(kg): ')
height = input('height(m): ')

get_bmi(weight,height)