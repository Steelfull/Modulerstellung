from . import db

class Modul(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    module_name = db.Column(db.String(120), nullable=False)
    module_code = db.Column(db.String(20), nullable=True)  # Neues Feld für das Modulkürzel
    department = db.Column(db.String(120), nullable=False)
    module_type = db.Column(db.String(120), nullable=False)
    qualifications = db.Column(db.String(120), nullable=False)
    semesters = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    sws = db.Column(db.Integer, nullable=False)
    ects = db.Column(db.Integer, nullable=False)
    lecture_type = db.Column(db.String(120), nullable=True)
    cross_program = db.Column(db.Boolean, default=False)

    # Neue Felder für Arbeitsaufwand
    presence_time = db.Column(db.Integer, nullable=True)  # Präsenzzeit
    self_study_time = db.Column(db.Integer, nullable=True)  # Selbststudium
    total_hours = db.Column(db.Integer, nullable=True)  # Gesamtstunden
    prerequisites_formal = db.Column(db.Text, nullable=True)  # Formale Voraussetzungen
    prerequisites_content = db.Column(db.Text, nullable=True)  # Inhaltliche Voraussetzungen
    curriculum = db.Column(db.Text, nullable=True)  # Zuordnung zum Curriculum
    language_of_instruction = db.Column(db.String(120), nullable=True)  # Unterrichtssprache
    exam_type = db.Column(db.String(120), nullable=True)  # Prüfungsart
    exam_format_duration = db.Column(db.Text, nullable=True)  # Prüfungsform, -dauer, -umfang
    exam_language = db.Column(db.String(120), nullable=True)  # Prüfungssprache
    requirements_for_credits = db.Column(db.Text, nullable=True)  # Voraussetzungen für Leistungspunkte
    module_responsible = db.Column(db.String(120), nullable=True)  # Modulverantwortliche*r
    registration = db.Column(db.String(120), nullable=True)  # Anmeldung über
    knowledge = db.Column(db.Text, nullable=True)  # Kenntnisse
    skills = db.Column(db.Text, nullable=True)  # Fertigkeiten
    competences = db.Column(db.Text, nullable=True)  # Kompetenzen
    contents = db.Column(db.Text, nullable=True)  # Inhalte
    teaching_mode = db.Column(db.String(120), nullable=True)  # Lehrmodus
    learning_mode = db.Column(db.String(120), nullable=True)  # Lernmodus
    literature = db.Column(db.Text, nullable=True)  # Literatur
    equipment_costs = db.Column(db.Text, nullable=True)  # Ausrüstung und Kosten
    miscellaneous = db.Column(db.Text, nullable=True)  # Sonstiges
    last_update = db.Column(db.String(120), nullable=True)  # Letzte Aktualisierung

    def __repr__(self):
        return f'<Modul {self.module_name}>'
