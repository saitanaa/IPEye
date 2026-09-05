import tkinter as tk
import requests

def is_local_ip(ip):
    # Liste des plages d'adresses IP réservées aux réseaux locaux
    local_networks = [
        '10.',     # 10.0.0.0 - 10.255.255.255
        '172.16.', # 172.16.0.0 - 172.31.255.255
        '192.168.' # 192.168.0.0 - 192.168.255.255
    ]
    for local_net in local_networks:
        if ip.startswith(local_net):
            return True
    return False

def get_ip_location(ip):
    if is_local_ip(ip):
        return "Error: You have entered a local IP address."
    else:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)
        data = response.json()
        if data['status'] == 'success':
            return f"IP: {data['query']}\nCountry: {data['country']}\nCity: {data['city']}\nISP: {data['isp']}"
        else:
            return "Failed to locate IP"

def locate_ip():
    ip = ip_entry.get()
    result_text.set(get_ip_location(ip))

def get_public_ip():
    response = requests.get('https://httpbin.org/ip')
    public_ip = response.json()['origin']
    result_text.set(f"Your Public IP Address: {public_ip}")
def get_ip_location(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()
    if data['status'] == 'success':
        return f"IP: {data['query']}\nCountry: {data['country']}\nCity: {data['city']}\nISP: {data['isp']}"
    else:
        return "Erreur lors de la localisation de l'IP :("

def locate_ip():
    ip = ip_entry.get()
    result_text.set(get_ip_location(ip))

def get_public_ip():
    response = requests.get('https://httpbin.org/ip')
    public_ip = response.json()['origin']
    result_text.set(f"Votre adresse IP Publique : {public_ip}")

# Créer la fenêtre principale
root = tk.Tk()
root.title("IPEye")
root.geometry("500x350")
root.configure(bg="black")  # Fond noir

# Texte "IPEye"
title_label = tk.Label(root, text="IPEye 0.1.2", font=('Helvetica', 16, 'bold'), bg="black", fg="purple")
title_label.pack(side=tk.TOP, pady=10)
title_label = tk.Label(root, text="Fonctionne uniquement avec les IP Publiques !", font=('Helvetica', 8, 'bold'), bg="black", fg="red")
title_label.pack(side=tk.TOP, pady=10)

# Cadre pour entrer l'adresse IP
frame = tk.Frame(root, bg="black")
frame.pack(pady=10)

# Champ de saisie pour l'adresse IP
ip_entry = tk.Entry(frame, font=('Helvetica', 12), width=20)
ip_entry.grid(row=0, column=0, padx=5)

# Bouton pour localiser l'adresse IP
locate_button = tk.Button(frame, text="Localiser l'IP", command=locate_ip, bg="#8A2BE2", fg="white")  # Violet
locate_button.grid(row=0, column=1, padx=5)

# Bouton pour obtenir l'adresse IP publique
public_ip_button = tk.Button(root, text="Obtenir son IP Publique", command=get_public_ip, bg="#FFA500", fg="white")  # Orange
public_ip_button.pack(side=tk.BOTTOM, pady=10)

# Texte pour afficher le résultat
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=('Helvetica', 12), justify=tk.LEFT, bg="black", fg="white")
result_label.pack(pady=10)



# Exécuter la boucle principale
root.mainloop()
