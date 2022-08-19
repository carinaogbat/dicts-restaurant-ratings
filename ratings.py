"""Restaurant rating lister."""


# put your code here

#need a program that reads ratings and stores in dict



restaurant_ratings = {}

def create_rest_rating_dict(filename):
    file = open(filename)
    for line in file:
        restaurant, rating = line.rstrip().split(':')
        restaurant_ratings[restaurant] = rating
        restaurant_sorted = sorted(restaurant_ratings.keys())
        for restaurant in restaurant_sorted:
            print(f"{restaurant} rating is {restaurant_ratings[restaurant]}")
    return restaurant_sorted

print(create_rest_rating_dict('scores.txt'))

def ask_user_rest_and_rating(filename):
    new_user_rest = input("Please type the name of the restaurant you want to review ")
    new_user_rest_rating = input("Please rate the restaurant [1-5] ")
    restaurant_ratings[new_user_rest] = new_user_rest_rating
    sorted = create_rest_rating_dict(filename)
    print(sorted)

create_rest_rating_dict('scores.txt')
ask_user_rest_and_rating('scores.txt')



