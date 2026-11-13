import asyncio
import time

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation
from pasco.pasco_ble_device import PASCOBLEDevice

# ==============================================================================
# CONFIGURATION : Ajoutez ou retirez les ID de vos chariots ici (Maximum 3)
# ==============================================================================
CARTS_CONFIG = {
    "Chariot_1": {"id": "955-689", "color": "tab:blue"},
    "Chariot_2": {"id": "654-321", "color": "tab:red"},
    "Chariot_3": {"id": "789-012", "color": "tab:green"},
}

# Structure pour stocker les objets de connexion et les listes de données
carts_data = {}
for name, cfg in CARTS_CONFIG.items():
    carts_data[name] = {
        "device": PASCOBLEDevice(),
        "id": cfg["id"],
        "color": cfg["color"],
        "time": [],
        "position": [],
        "velocity": [],
        "connected": False
    }

start_time = None
is_running = True

# ==============================================================================
# FONCTION ASYNCHRONE : Lecture des capteurs en arrière-plan
# ==============================================================================
async def read_carts_loop():
    global start_time, is_running
    print("\n--- ÉTAPE 1 : Connexion aux Smart Carts ---")
    
    # Tentative de connexion en parallèle pour chaque chariot configuré
    for name, data in carts_data.items():
        print(f"Tentative de connexion à {name} (ID: {data['id']})...")
        try:
            data["device"].connect_by_id(data["id"])
            if data["device"].is_connected():
                data["connected"] = True
                print(f"{name} connecté avec succès !")
            else:
                print(f"Impossible de connecter {name}.")
        except Exception as e:  # noqa: BLE001
            print(f"Erreur lors de la recherche de {name}: {e}")

    # Vérifier si au moins un chariot est connecté
    any_connected = any(d["connected"] for d in carts_data.values())
    if not any_connected:
        print("\nAucun chariot n'a pu être connecté. Fin du programme.")
        is_running = False
        return

    print("\nLancement de l'acquisition ! (Fermez la fenêtre graphique pour arrêter)")
    start_time = time.time()
    
    # Boucle d'acquisition en continu
    while is_running:
        current_time = time.time() - start_time
        
        for name, data in carts_data.items():
            if data["connected"]:
                try:
                    # Lecture simultanée de la position et de la vitesse
                    pos = data["device"].read_data('Position')
                    vel = data["device"].read_data('Velocity')
                    
                    data["time"].append(current_time)
                    data["position"].append(pos)
                    data["velocity"].append(vel)
                except Exception:  # noqa: BLE001, S110
                    # En cas de micro-coupure Bluetooth
                    pass
                    
        # Pause de 50ms pour échantillonner à environ 20 Hz
        await asyncio.sleep(0.05)

    # Déconnexion propre en fin de boucle
    print("\n--- ÉTAPE 3 : Déconnexion des appareils ---")
    for name, data in carts_data.items():
        if data["connected"]:
            data["device"].disconnect()
            print(f"Chariot {name} déconnecté.")

# ==============================================================================
# ANIMATION MATPLOTLIB : Rafraîchissement de la fenêtre en temps réel
# ==============================================================================
def update_plot(frame):
    global is_running
    
    # Si la fenêtre graphique est fermée, on arrête la boucle de lecture
    if not plt.fignum_exists(fig.number):
        is_running = False
        return list(lines_pos.values()) + list(lines_vel.values())

    # Mettre à jour les données de chaque courbe
    for name, data in carts_data.items():
        if data["connected"] and len(data["time"]) > 0:
            lines_pos[name].set_data(data["time"], data["position"])
            lines_vel[name].set_data(data["time"], data["velocity"])
    
    # Ajustement dynamique des limites des axes du graphique
    all_times = [t for d in carts_data.values() for t in d["time"]]
    all_pos = [p for d in carts_data.values() for p in d["position"]]
    all_vels = [v for d in carts_data.values() for v in d["velocity"]]
    
    if all_times:
        max_time = max(all_times)
        ax_pos.set_xlim(0, max_time + 1)
        
        # Ajustement de l'axe de la Position (Gauche)
        if all_pos:
            ax_pos.set_ylim(min(all_pos) - 0.1, max(all_pos) + 0.1)
            
        # Ajustement de l'axe de la Vitesse (Droite)
        if all_vels:
            ax_vel.set_ylim(min(all_vels) - 0.2, max(all_vels) + 0.2)
        
    return list(lines_pos.values()) + list(lines_vel.values())

# ==============================================================================
# PROGRAMME PRINCIPAL
# ==============================================================================
if __name__ == "__main__":
    # 1. Configuration de l'axe principal : POSITION (Axe Gauche)
    fig, ax_pos = plt.subplots(figsize=(11, 6))
    ax_pos.set_title("Position et Vitesse des Smart Carts en Temps Réel", fontsize=14, fontweight='bold')
    ax_pos.set_xlabel("Temps (s)")
    ax_pos.set_ylabel("Position (m) — [Ligne Continue]", fontweight='bold')
    ax_pos.grid(True, linestyle="--", alpha=0.5)

    # 2. Configuration du second axe : VITESSE (Axe Droite)
    ax_vel = ax_pos.twinx()
    ax_vel.set_ylabel("Vitesse (m/s) - - - [Ligne en Pointillés]", fontweight='bold')

    # Création des lignes de tracé vides pour chaque chariot connecté
    lines_pos = {}
    lines_vel = {}
    
    for name, data in carts_data.items():
        # Courbe de position : continue (lw=2)
        line_p, = ax_pos.plot([], [], label=f"{name} : Position", color=data["color"], lw=2)
        # Courbe de vitesse : pointillés (ls="--", lw=1.5)
        line_v, = ax_vel.plot([], [], label=f"{name} : Vitesse", color=data["color"], ls="--", lw=1.5)
        
        lines_pos[name] = line_p
        lines_vel[name] = line_v
    
    # Combiner les légendes des deux axes pour n'avoir qu'un seul bloc propre
    h1, l1 = ax_pos.get_legend_handles_labels()
    h2, l2 = ax_vel.get_legend_handles_labels()
    ax_pos.legend(h1 + h2, l1 + l2, loc="upper left", ncol=2)

    fig.tight_layout()

    # Lancement du thread asynchrone pour l'acquisition Bluetooth
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    acquire_task = loop.create_task(read_carts_loop())

    # Lancement de l'animation (rafraîchissement toutes les 50 ms)
    ani = FuncAnimation(fig, update_plot, interval=50, blit=True, cache_frame_data=False)
    
    # Affichage de la fenêtre graphique
    plt.show()

    # Une fois la fenêtre fermée, fermeture propre
    is_running = False
    loop.run_until_complete(acquire_task)
    
    # --- SAUVEGARDE AUTOMATIQUE DES DONNÉES EN CSV ---
    print("\n--- ÉTAPE 4 : Sauvegarde des fichiers ---")
    for name, data in carts_data.items():
        if data["connected"] and len(data["time"]) > 0:
            df = pd.DataFrame({
                'Temps (s)': data["time"],
                'Position (m)': data["position"],
                'Vitesse (m/s)': data["velocity"]
            })
            filename = f"donnees_{name}.csv"
            df.to_csv(filename, index=False)
            print(f"Fichier exporté : '{filename}' ({len(df)} points enregistrés)")
