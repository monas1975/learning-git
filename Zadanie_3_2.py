
#deklaracje
shopping_dict = {
    "warzywniak": ["buraki", "ziemniaki", "truskawki", "czereśnie"],
    "piekarnia": ["bułka", "chleb", "bagietka"]
}
towar=""
product_counter =0


for key, values in shopping_dict.items():
    for product in values:
        towar = towar + ", " + product.capitalize()
        product_counter +=1
    print("Idę do sklepu " + key.capitalize() + " po:" + towar)
    towar =""
    print("w sumie kupuję " + str(product_counter) + " produkty")
    
print("to jest 1 zmiana na poterzeby cwiczenia")