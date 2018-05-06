from peewee import Model,MySQLDatabase , PrimaryKeyField ,CharField ,IntegerField, Field, SQL, TextField

mysql_db = MySQLDatabase(database='qurandb' , user='root',host='127.0.0.1',port=3306)

class BaseMolel(Model):
    class Meta:
        database= mysql_db

class EnumField(Field):
    db_field = "enum"

    def pre_field_create(self, model):
        field = "e_%s" % self.name

        self.get_database().get_conn().cursor().execute(
            "DROP TYPE IF EXISTS %s;" % field
        )

        query = self.get_database().get_conn().cursor()

        tail = ', '.join(["'%s'"] * len(self.choices)) % tuple(self.choices)
        q = "CREATE TYPE %s AS ENUM (%s);" % (field, tail)
        query.execute(q)

    def post_field_create(self, model):
        self.db_field = "e_%s" % self.name

    def coerce(self, value):
        if value not in self.choices:
            raise Exception("Invalid Enum Value `%s`", value)
        return str(value)

    def get_column_type(self):
        return "enum"

    def __ddl_column__(self, ctype):
        return SQL("e_%s" % self.name)


class Curse (BaseMolel):
    id = PrimaryKeyField()
    list_prerequisite = CharField()
    name = CharField(30)
    price = IntegerField(30)
    presentation = EnumField(choices=['theoretic', 'practical'])
    status_prerequisite = EnumField(choices=['yes', 'no'])
    type = EnumField(choices=['basic', 'prime', 'professional', 'public'])
    unit_number= IntegerField(30)

    class Meta:
        db_table = "course"


class profssor (BaseMolel):
    id = PrimaryKeyField()
    firstname = CharField(45)
    lastname =  CharField(45)
    father =CharField(45)
    sex = EnumField(choices=['male', 'female'])
    national_code =CharField(45)
    birthday=CharField(45)
    location_brith=CharField(45)
    password=TextField()
    phone=CharField(45)
    mobile=CharField(45)
    address=TextField()
    img=CharField(45)

    class Meta:
        db_table = "professor"