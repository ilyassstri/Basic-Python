# Formated string 

first_name = "M. Ilyas"
last_name = "Tri Khaqiqi"
hobby = "Lintening Music rock"
kampus = "Universitas Logistik dan Bisnis Internasional"
cita_cita = "Dosen"

Message = first_name + " [" + last_name + "] "
print(Message)

Message = f"{first_name} [{last_name}]" 
print(Message)

Message = f"{hobby} every where "
print(Message)

age = 31

# Message = "Umur kamu " + str(age)
Message = f"Umur kamu {age}"
print(Message)

hasilnya = f"nama saya {first_name} {last_name} sama memiliki hobi {hobby}, dan saya baru saja lulus di kampus {kampus}. Kemudian cita-cita saya adalah menjadi {cita_cita}"
print(hasilnya)

