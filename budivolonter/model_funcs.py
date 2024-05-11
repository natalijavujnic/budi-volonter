def getUsers():
    return (models.Korisnik.objects.all().values());
getUsers()
