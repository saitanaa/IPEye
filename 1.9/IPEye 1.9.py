import tkinter as tk
import requests
import socket
import webbrowser

def is_local_ip(ip):
    try:
        return ip.startswith("192.168.") or ip.startswith("10.") or ip.startswith("172.16.")
    except ValueError:
        return False

def get_ip_location(ip):
    if is_local_ip(ip):
        return "E2 : Vous venez d'entrer une IP Locale."
    else:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)
        data = response.json()
        if data['status'] == 'success':
            return f"| - IP : {data['query']}\n| - Pays : {data['country']}\n| - Ville : {data['city']}\n| - FAI : {data['isp']}\n| - Latitude: {data['lat']}\n| - Longitude: {data['lon']}\n| - OS : {data.get('os', 'Impossible de récupérer cette information')}\n| - Connecté : {'On' if is_device_on(ip) else 'Off'}"
        else:
            return "E1 : Impossible de localiser l'IP"

def is_device_on(ip):
    try:
        socket.create_connection((ip, 80), timeout=2)
        return True
    except OSError:
        return False

def locate_ip():
    ip = ip_entry.get()
    loading_label.config(text="Récupération des informations sur l'IP...")
    root.update()  # Forcer le rafraîchissement de l'interface graphique
    result_text.set(get_ip_location(ip))
    loading_label.config(text="")

def get_public_ip():
    response = requests.get('https://httpbin.org/ip')
    public_ip = response.json()['origin']
    result_text.set(f"Votre adresse IP Publique : {public_ip}")

# Créer la fenêtre principale
root = tk.Tk()
root.title("IPEye v1")
root.geometry("800x600")
root.configure(bg="black")  # Fond noir

# Définir la police d'écriture
font_style = "Doppio One"

# Fonction pour obtenir les coins arrondis
def round_corners(widget):
    widget.config(borderwidth=0, highlightthickness=0, relief="flat", background="#fff", font=(font_style, 12))  # Fond blanc, police Doppio One, taille 12

# Titre
title_label = tk.Label(root, text="--- IPEye ---", font=(font_style, 24, 'bold'), bg="black", fg="purple")  # Texte blanc
title_label.pack(side=tk.TOP, pady=10)

title_label = tk.Label(root, text=">_ Localiser toutes les IP Réseau du monde.", font=(font_style, 9, 'bold'), bg="black", fg="red")
title_label.pack(side=tk.TOP, pady=10)

title_label = tk.Label(root, text="> Saysaa - v1.9 <", font=(font_style, 9, 'bold'), bg="black", fg="orange")
title_label.pack(side=tk.TOP, pady=10)

# Cadre pour entrer l'adresse IP
frame = tk.Frame(root, bg="black")
frame.pack(pady=10)

# Champ de saisie pour l'adresse IP
ip_entry = tk.Entry(frame, font=('Helvetica', 15), width=15)
ip_entry.grid(row=0, column=0, padx=5)

# Bouton pour localiser l'adresse IP
locate_button = tk.Button(frame, text="Localiser l'IP", command=locate_ip, bg="#8A2BE2", fg="black")  # Violet
locate_button.grid(row=0, column=1, padx=5)

# Bouton pour obtenir l'adresse IP publique
public_ip_button = tk.Button(root, text="- - - Obtenir mon IP Publique - - -", command=get_public_ip, bg="#FFA500", fg="black")  # Orange
public_ip_button.pack(side=tk.BOTTOM, pady=10)

title_label = tk.Label(root, text="______________________________________________________________________________________", font=('Helvetica', 9, 'bold'), bg="black", fg="purple")
title_label.pack(side=tk.TOP, pady=10)


# Texte pour afficher le résultat
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=('Helvetica', 12), justify=tk.LEFT, bg="black", fg="white")
result_label.pack(pady=10)

def locate_ip():
    ip = ip_entry.get()
    result_text.set("")  # Effacer le texte précédent
    loading_label.config(text="Récupération des informations sur l'IP")
    loading_label.place(relx=0.8, rely=0.8, anchor=tk.CENTER)  # Centrer le label de chargement
    root.update()  # Forcer le rafraîchissement de l'interface graphique
    result = get_ip_location(ip)
    result_text.set(result)
    loading_label.config(text="")  # Effacer le texte de chargement après la récupération des informations

# Label de chargement
loading_label = tk.Label(root, font=('Helvetica', 12), bg="black", fg="white")
loading_label.pack(pady=10)


title_label = tk.Label(root, text="__________________________________________________________________________", font=('Helvetica', 9, 'bold'), bg="black", fg="purple")
title_label.pack(side=tk.TOP, pady=10)

title_label = tk.Label(root, text="Il se peut que certaines infos soit incorrectes.", font=(font_style, 7, 'bold'), bg="black", fg="red")
title_label.pack(side=tk.TOP, pady=1)

import webbrowser

def open_link(url):
    webbrowser.open(url)

# Créer le bouton pour le lien
download_button = tk.Button(root, text="- - - Rejoindre le Canal - - -", command=lambda: open_link("https://t.me/ipeyedownload"), bg="#FFA500", fg="black")  # Orange
download_button.pack(side=tk.BOTTOM, pady=10)

def animate_label(label, text, index=0):
    if index < len(text):
        label.config(text=label.cget("text") + text[index])
        label.after(50, animate_label, label, text, index+1)
    else:
        loading_label.config(text="")  # Masquer le label de chargement après l'animation

# Exécuter la boucle principale
root.mainloop()
