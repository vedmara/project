class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat_1 = Cat('Matiu', 4)
cat_2 = Cat('Bagel', 3)
cat_3 = Cat('Ashot', 8)

def get_cats_dict(cats_objs):
    cats = {}
    for cat in cats_objs:
        cats.update({cat.age: cat.name})
    return cats

def find_oldest_cat(age_list):
    return max(age_list)


cat_objects = [cat_1, cat_2, cat_3]
cats_dict = get_cats_dict(cat_objects)
oldest_cat = find_oldest_cat(cats_dict.keys())

print(f"The oldest cat is {oldest_cat} years old.\nThe cat name is {cats_dict.get(oldest_cat)}")



