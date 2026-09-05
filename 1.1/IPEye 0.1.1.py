import tkinter as tk
import requests

def get_ip_location(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()
    if data['status'] == 'success':
        return f"IP: {data['query']}\nCountry: {data['country']}\nCity: {data['city']}\nISP: {data['isp']}"
    else:
        return "Erreur lors de la tentavive de localisation de l'IP :("

def locate_ip():
    ip = ip_entry.get()
    result_text.set(get_ip_location(ip))

# Créer la fenêtre principale
root = tk.Tk()
root.title("IPEye")
root.geometry("400x200")
root.configure(bg="black")  # Fond noir

# Texte "IPEye"
title_label = tk.Label(root, text="IPEye 0.1.1", font=('Helvetica', 16, 'bold'), bg="black", fg="white")
title_label.pack(side=tk.TOP, pady=10)

# Cadre pour entrer l'adresse IP
frame = tk.Frame(root, bg="black")
frame.pack(pady=20)

# Champ de saisie pour l'adresse IP
ip_entry = tk.Entry(frame, font=('Helvetica', 12), width=20)
ip_entry.grid(row=0, column=0, padx=10)

# Bouton pour localiser l'adresse IP
locate_button = tk.Button(frame, text="Locate IP", command=locate_ip, bg="#8A2BE2", fg="white")  # Violet
locate_button.grid(row=0, column=1, padx=10)

# Texte pour afficher le résultat
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=('Helvetica', 12), justify=tk.LEFT, bg="black", fg="white")
result_label.pack(pady=20)

# Exécuter la boucle principale
root.mainloop()
