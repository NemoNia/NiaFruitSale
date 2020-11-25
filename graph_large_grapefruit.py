import matplotlib.pyplot as plt
from large_grapefruit import total_large_grapefruit2019, total_large_grapefruit2018, total_large_grapefruit2017



def large_grapefruit():
    #name = "Large Grapefruit Sales Over 3 Years"
    print(total_large_grapefruit2017)
    print(total_large_grapefruit2018)
    print(total_large_grapefruit2019)

    labels = '2019', '2018', '2017'
    sizes = [total_large_grapefruit2019,total_large_grapefruit2018,
             total_large_grapefruit2017 ]
    tot = sum(sizes)/100.0
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct=lambda x: "%d" % round(x*tot), shadow=True,
            startangle=90)
    ax1.axis('equal')
    plt.title("Total Large Grapefruit Sold Over 3 Years")


    plt.show()
