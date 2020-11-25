import matplotlib.pyplot as plt
from large_basket import total_large_baskets2019, total_large_baskets2018, total_large_baskets2017



def large_baskets():
    #name = "Large Basket Sales Over 3 Years"
    print(total_large_baskets2017)
    print(total_large_baskets2018)
    print(total_large_baskets2019)

    labels = '2019', '2018', '2017'
    sizes = [total_large_baskets2019,total_large_baskets2018,
             total_large_baskets2017 ]
    tot = sum(sizes)/100.0
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct=lambda x: "%d" % round(x*tot), shadow=True,
            startangle=90)
    ax1.axis('equal')
    plt.title("Total Large Baskets Sold Over 3 Years")


    plt.show()
