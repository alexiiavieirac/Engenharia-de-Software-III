sells = {"Tecnology": "iPhone", "Book": "Spider Man", "Computer": "Samsung Galaxy Book2"}
sells_tecnology = {"iPhone": 1500, "Samsung Galaxy Book2": 1000, "PS5": 500, "iPad": 580}

# Show by private words
book = sells["Book"]
cellphone = sells["Tecnology"]
computer = sells["Computer"]

# Show by sells 
samsumg_galaxy = sells_tecnology["Samsung Galaxy Book2"]
video_game = sells_tecnology["PS5"]
iphone = sells_tecnology["iPhone"]
ipad = sells_tecnology['iPad']

print("Product:")
print(f"Cellphone: {cellphone}")
print(f"Book: {book}")

print("Sells:")
print(f"Computer: {samsumg_galaxy}")
print(f"Video Game: {video_game}")