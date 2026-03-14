import functions_framework

@functions_framework.cloud_event
def clean_data_trigger(cloud_event):
    # Récupère les infos du fichier déposé
    data = cloud_event.data
    print(f"Fichier reçu : {data['name']} dans le bucket {data['bucket']}")
    # Ta logique de Data Engineering ici