

# Parent class plant
class plant:
    name = "Ricky"
    climate = "Humid"
    sun_exposure = "8 hours +"

    # input plant to track
    def inputPlant(self):
        entry_name = input("What is the name of the plant you'd like to track?\n>>>")
        entry_climate = input("What's your plant's climate?\n>>>")
        entry_sun_exposure = input("How much sun does your plant need?\n>>>")
        if (entry_name != "" and entry_climate != "" and entry_sun_exposure != ""):
            print(" {} needs {} enviornment and requires {} hours of sun per day".format(entry_name, entry_climate, entry_sun_exposure))



# Child class tree
class tree(plant):
    fruit = "Cherrys"
    season = "Summer"

    # same as plant entry but for trees

    def inputPlant(self):
        entry_fruit = input("What's your tree's fruit?\n>>>")
        entry_season = input("what season does your tree bloom in?\n>>>")
        if (entry_fruit != "" and entry_season != ""):
            print(" {} produces tasty {}'s and it blooms in {}".format(entry_fruit, entry_season))




# Child class schrub
class schrub(plant):
    flower = "Rose"
    color = "Red"

    # same as plant entry but for shrubs

    def inputPlant(self):
        entry_flower = input("What's your schrub's flower?\n>>>")
        entry_color = input("What color are your shrubs flowers?\n>>>")
        if (entry_flower != "" and entry_color != ""):
            print(" {} has {} that are {} and very beautiful".format(entry_flower, entry_color))


if __name__ == "__main__":
    myPlant = plant()
    myPlant.inputPlant()

    myTree = tree()
    myTree.inputPlant()

    mySchrub = schrub()
    mySchrub.inputPlant()

