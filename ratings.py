"""Restaurant rating lister."""


# put your code here

#need a program that reads ratings and stores in dict





def create_rest_rating_dict(filename):
    file = open(filename)
    restaurant_ratings = {}
    for line in file:
        restaurant, rating = line.rstrip().split(':')
        restaurant_ratings[restaurant] = rating
        restaurant_sorted = sorted(restaurant_ratings.keys())
        for restaurant in restaurant_sorted:
            print(f"{restaurant} rating is {restaurant_ratings[restaurant]}")
    return ""


   
print(create_rest_rating_dict('scores.txt'))
