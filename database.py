import mysql.connector
conn = mysql.connector.connect(
    user="root",
    host="localhost",
    passwd="engeslam@8505611.mysql",
    database="Ohmlatl"
)
mycursor = conn.cursor()


def insert_meal(meal_name, Meal_ingredient, meal_recipe):
    sql_statement = "INSERT INTO Recipe VALUES('%s','%s','%s')" % (
        meal_name, Meal_ingredient, meal_recipe)
    mycursor.execute(sql_statement)
    conn.commit()


name = "Seafood with White Sauce"
Meal_ingredient ="1 pound of seafood (shrimp, scallops, mussels, or a combination)\n1/4 cup of butter\n1/4 cup of all-purpose flour\n2 cups of milk\n2 cloves of garlic, minced\n1/4 teaspoon of paprika\nSalt and black pepper, to taste\n1/4 cup of grated Parmesan cheese\nFresh parsley, chopped (for garnish)"
meal_recipe = "Rinse and clean the seafood, then set aside.\nIn a large saucepan, melt the butter over medium heat.\nAdd the minced garlic to the melted butter and cook for 1-2 minutes, or until fragrant.\nGradually add the flour to the butter mixture, whisking constantly to form a smooth paste.\nSlowly pour the milk into the saucepan, whisking constantly to prevent lumps from forming.\nAdd the paprika, salt, and black pepper to the white sauce. Stir until well combined.\nIncrease the heat to medium-high and bring the white sauce to a simmer. Cook, stirring constantly, for 5-7 minutes or until the sauce has thickened.\nAdd the seafood to the white sauce and stir to combine.\nSimmer the seafood in the white sauce for 8-10 minutes, or until the seafood is fully cooked.\nRemove the saucepan from the heat and stir in the grated Parmesan cheese until it has melted and is well combined.\nServe the seafood with white sauce hot, garnished with chopped parsley.\nEnjoy your delicious seafood with white sauce!"
insert_meal(name, Meal_ingredient, meal_recipe)



