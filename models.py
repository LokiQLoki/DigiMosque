from app import db

class Mosque(db.Model):
    __tablename__ = 'mosques'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    lat = db.Column(db.String())
    lon = db.Column(db.String())
    FA = db.Column(db.String())
    ZU = db.Column(db.String())
    AS = db.Column(db.String())
    MA = db.Column(db.String())
    IS = db.Column(db.String())
    contact = db.Column(db.String())
    image_folder_name = db.Column(db.String())
    uploader_id = db.Column(db.String())

    def __init__(self, name, lat, lon, FA, ZU, AS, MA, IS, contact, image_folder_name,uploader_id):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.FA = FA
        self.ZU = ZU
        self.AS = AS
        self.MA = MA
        self.IS = IS
        self.contact = contact
        self.image_folder_name = image_folder_name
        self.uploader_id = uploader_id



    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'lat': self.lat,
            'lon': self.lon,
            'FA':self.FA,
            'ZU': self.ZU,
            'AS':self.AS,
            'MA': self.MA,
            'IS':self.IS,            
            'contact':self.contact,
            'image_folder_name':self.image_folder_name,
            'uploader_id':self.uploader_id

        }