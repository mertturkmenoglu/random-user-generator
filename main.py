import json
import random
import datetime

names_f = open('names.json')
surnames_f = open('surnames.json')
jobs_f = open('jobs.json')
locations_f = open('locations.json')
schools_f = open('schools.json')
languages_f = open('languages.json')
hobbies_f = open('hobbies.json')
users_f = open('users.json', 'w')

names = json.load(names_f)["names"]
surnames = json.load(surnames_f)["surnames"]
jobs = json.load(jobs_f)["jobs"]
locations = json.load(locations_f)["locations"]
schools = json.load(schools_f)["schools"]
languages = json.load(languages_f)["languages"]
hobbies = json.load(hobbies_f)["hobbies"]

data = {
	"users": []
}

proficiency = ['Elementary', 'Intermediate', 'Professional', 'Native']

for i in range(10000):
	name = random.choice(names)
	surname = random.choice(surnames)
	username = name.lower() + "_" + surname.lower() + "_" + str(random.randint(1000, 10000))
	gender = random.choice(["male", "female", "non-binary", ""])

	start_date = datetime.date(1970, 1, 1)
	end_date = datetime.date(2000, 12, 30)

	time_between_dates = end_date - start_date
	days_between_dates = time_between_dates.days

	rnd_number_of_days = random.randrange(days_between_dates)
	rnd_date = start_date + datetime.timedelta(days=rnd_number_of_days)

	feat_k = random.randint(1, 5)
	hobbies_k = random.randint(0, 8)

	feats = random.sample(hobbies, feat_k)
	hobbs = random.sample(hobbies, hobbies_k)

	langs_k = random.randint(1, 3)
	sample_langs = random.sample(languages, langs_k)
	lngs = []

	for l in sample_langs:
		lngs.append({
			"language": l,
			"proficiency": random.choice(proficiency)
		})

	idx = random.randint(0, len(lngs)-1)
	lngs[idx]["proficiency"] = "Native"

	langs_k = random.randint(1, 4)
	langs = []
	for l in languages:
		if not l in sample_langs:
			langs.append(l)

	sample_langs = random.sample(langs, langs_k)

	u = {
		"name": name + " " + surname,
		"job": random.choice(jobs),
		"location": random.choice(locations),
		"school": random.choice(schools),
		"username": username,
		"isAdmin": False,
		"email": username + "@example.com",
		"website": "",
		"twitter": "",
		"bio": "Hi, I'm " + name,
		"gender": gender,
		"bdate": str(rnd_date),
		"followers": [],
		"following": [],
		"features": feats,
		"hobbies": hobbs,
		"languages": lngs,
		"wish_to_speak": sample_langs
	}

	data["users"].append(u)

json.dump(data, users_f)

names_f.close()
surnames_f.close()
jobs_f.close()
locations_f.close()
schools_f.close()
languages_f.close()
hobbies_f.close()
users_f.close()