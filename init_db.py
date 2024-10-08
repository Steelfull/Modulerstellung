from app import create_app, db

app = create_app()

# Initialisiere den App-Kontext, um die Datenbank zu erstellen
with app.app_context():
    try:
        db.create_all()  # Erstellt die Tabellen in der Datenbank
        print("Datenbank und Tabellen erfolgreich erstellt.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
