import matplotlib.pyplot as plt
from gold_apples import total_gold_apples2019, total_gold_apples2018, total_gold_apples2017



def gold_apples():
        #name = "Gold Apple Sales Over 3 Years"
        print(total_gold_apples2017)
        print(total_gold_apples2018)
        print(total_gold_apples2019)

        labels = '2019', '2018', '2017'
        sizes = [total_gold_apples2019,total_gold_apples2018, total_gold_apples2017 ]
        tot = sum(sizes)/100.0
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct=lambda x: "%d" % round(x*tot), shadow=True,
                startangle=90)
        ax1.axis('equal')
        plt.title("Total Gold Apples Sold Over 3 Years")


        plt.show()