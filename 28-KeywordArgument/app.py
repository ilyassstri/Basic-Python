# Argumen adalah dimana akan tetap dijalankan sesuai dengan urutan fungsinya
# klo tidak memakai argument manaya positional argument jadi urutannya itu harus benar

"""
Jadi kegunaan dari argumen ini untuk memberikan parameter yng tepat walaupun tidak sesuai dengan urutannya
"""

def halo_user(name, level): # function dan nama function
    print(f"Halo {name} - {level}")
    print("Selamat belajar python") 

print("Start")
halo_user(level=10, name="ilyas") # argumen
print("Finish")

print("Start")
halo_user("ilyas", 10) # argumen
# calculate_total_cost(total_price = 100000, shipping_cost=50000, discount=5000)
print("Finish")

print("Latihan membuat argumen")

def hello_world(tingkat, kesulitan):
    print(f"untuk posisimu akan memiliki {tingkat} dan {kesulitan}")

hello_world(kesulitan="sangat sulit", tingkat="tinggi")