from graph_red_apples import red_apples
from graph_gold_apples import gold_apples
from graph_gala_apples import gala_apples
from graph_small_oranges import small_oranges
from graph_santa_oranges import santa_oranges
from graph_large_oranges import large_oranges
from garph_clementines import clementines
from graph_large_grapefruit import large_grapefruit
from graph_small_grapefruit import small_grapefruit
from graph_money import money
from graph_small_baskets import small_baskets
from graph_large_baskets import large_baskets

print("Fruit codes: (Gold Apples = gold, Red Apples = red, Gala Apples = gala, Small Oranges = "
      "sml_o, Santa Oranges = santa, Large Oranges = lrg_o, \nClementines = clem, Large Grapefruit = lrg_gr, "
      "Small Grapefruit = sml_gr, Small Basket = sml_ba, Large Basket = lrg_ba, Total Money = money)\n"
      "Type q to QUIT")
while True:
    test = input("Type the code for the fruit sales you would like view: ")
    if test == 'q':
        break
    if test == 'gold':
        gold_apples()
    if test == 'gala':
        gala_apples()
    if test == 'red':
        red_apples()
    if test == 'sml_o':
        small_oranges()
    if test == 'santa':
        santa_oranges()
    if test == 'lrg_o':
        large_oranges()
    if test == 'clem':
        clementines()
    if test == 'lrg_gr':
        large_grapefruit()
    if test == 'sml_gr':
        small_grapefruit()
    if test == 'money':
        money()
    if test == 'sml_ba':
        small_baskets()
    if test == 'lrg_ba':
        large_baskets()
