class Band:
    def __init__(self, name, hometown):
        if not isinstance(name, str) or not name:
            raise ValueError("Band name must be a non-empty string")
        if not isinstance(hometown, str) or not hometown:
            raise ValueError("Hometown must be a non-empty string")

        self.name = name
        self._hometown = hometown
        self._concerts = []

    @property
    def hometown(self):
        return self._hometown
    
    def add_concert(self, concert):
        if concert not in self._concerts:
            self._concerts.append(concert)

    def concerts(self):
        return self._concerts

    def venues(self):
        return list({concert.venue for concert in self._concerts})

    def play_in_venue(self, venue, date):
        concert = Concert(date=date, band=self, venue=venue)
        self.add_concert(concert)
        return concert

    def all_introductions(self):
        return [concert.introduction() for concert in self._concerts]

    def __setattr__(self, key, value):
        if key == 'name' and (not isinstance(value, str) or not value):
            raise ValueError("Band name must be a non-empty string")
        if key == 'hometown':
            raise AttributeError("Hometown cannot be changed")
        super().__setattr__(key, value)


class Concert:
    all = []

    def __init__(self, date, band, venue):
        if not isinstance(date, str) or not date:
            raise ValueError("Date must be a non-empty string")
        if not isinstance(band, Band):
            raise ValueError("Band must be of type Band")
        if not isinstance(venue, Venue):
            raise ValueError("Venue must be of type Venue")

        self._date = date
        self.band = band
        self._venue = venue
        self.band.add_concert(self)
        self.venue.add_concert(self)
        Concert.all.append(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Date must be a non-empty string")
        self._date = value

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if not isinstance(value, Venue):
            raise ValueError("Venue must be of type Venue")
        self._venue = value

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

    def __setattr__(self, key, value):
        if key == 'band' and not isinstance(value, Band):
            raise ValueError("Band must be of type Band")
        if key == 'venue' and not isinstance(value, Venue):
            raise ValueError("Venue must be of type Venue")
        super().__setattr__(key, value)


class Venue:
    def __init__(self, name, city):
        if not isinstance(name, str) or not name:
            raise ValueError("Venue name must be a non-empty string")
        if not isinstance(city, str) or not city:
            raise ValueError("City must be a non-empty string")

        self.name = name
        self._city = city
        self._concerts = []

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("City must be a non-empty string")
        self._city = value

    def add_concert(self, concert):
        if concert not in self._concerts:
            self._concerts.append(concert)

    def concerts(self):
        return self._concerts

    def bands(self):
        return list({concert.band for concert in self._concerts})

    def __setattr__(self, key, value):
        if key == 'name' and (not isinstance(value, str) or not value):
            raise ValueError("Venue name must be a non-empty string")
        if key == 'city' and (not isinstance(value, str) or not value):
            raise ValueError("City must be a non-empty string")
        super().__setattr__(key, value)
