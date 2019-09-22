def weight_on_planets():
    earthweight = float(input("What do you weigh on earth? "))
    marsweight = earthweight * 0.38
    jupiterweight = earthweight * 2.34
    print("\nOn Mars you would weigh {0} pounds.\nOn Jupiter you would weigh {1} pounds.".format(marsweight, jupiterweight))


   
if __name__ == '__main__':
   weight_on_planets()