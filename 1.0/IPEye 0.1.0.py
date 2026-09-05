import tkinter as tk
import requests

def get_ip_location(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()
    if data['status'] == 'success':
        return f"IP: {data['query']}\nCountry: {data['country']}\nCity: {data['city']}\nISP: {data['isp']}"
    else:
        return "Erreur lors de la tentative de localisation de l'IP"

def locate_ip():
    ip = ip_entry.get()
    result_text.set(get_ip_location(ip))

# Créer la fenêtre principale
root = tk.Tk()
root.title("IPEye")

# Cadre pour entrer l'adresse IP
frame = tk.Frame(root)
frame.pack(pady=20)

# Champ de saisie pour l'adresse IP
ip_entry = tk.Entry(frame, font=('Helvetica', 12))
ip_entry.pack(side=tk.LEFT, padx=10)

# Bouton pour localiser l'adresse IP
locate_button = tk.Button(frame, text="Localiser cette IP", command=locate_ip)
locate_button.pack(side=tk.LEFT)

# Texte pour afficher le résultat
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=('Helvetica', 12))
result_label.pack(pady=20)

# Exécuter la boucle principale
root.mainloop()
