# TODO:
# APATHY
# MORE INFLUENCES ON VOTING
# COMMENTS
# USE AN API OR DATABASE SEARCH FOR NAMES INSTED OF LISTS

import random

candidates = []
voters = []
professions = []

male_first_names = ["Norman", "Kevin", "Hector", "Branden", "Quintin", "Dexter", "Elmo", "Freddie", "Arnoldo", "Cyril", "Marcus", "Emerson", "Art", "Dominic", "Nathaniel", "Jospeh", "Denny", "Julian", "Brady", "Geraldo", "Jeremiah", "Charley", "Theodore", "Caleb", "Justin", "Wilber", "Leonel", "Minh", "Reuben", "Avery", "Nestor", "Tod", "Dan", "Chas", "Buck", "Lloyd", "Isidro", "Carroll", "Damion", "Roman", "Vincenzo", "Gus", "Randolph", "Hassan", "Dominick", "Zachary", "Cortez", "Arden", "Issac", "Lou"]

female_first_names = ["Izetta", "Alissa", "See", "Bettye", "Maurine", "Denice", "Ruby", "Annett", "Nadene", "Hanna", "Alyssa", "Nicolasa", "Eve", "Asuncion", "Magen", "Gilda", "Dorotha", "Tiffanie", "Winnifred", "Felicita", "Rosamaria", "Caroline", "Jacelyn", "Carlene", "Adrianna", "Elia", "Azzie", "Kandis", "Loriann", "Merlyn", "Mercy", "Xochitl", "Tashia", "Nanci", "Conception", "Fay", "Tomasa", "Tona", "Maris", "Blanca", "Rochelle", "Tambra", "Cristine", "Tiara", "Danica", "Ola", "Cherrie", "Tynisha", "Lynna", "Celestina"]

last_names = ["Gurwitz", "Maguire", "Buttaro", "Namanny", "Brentz", "Gallaway", "Delph", "Ratledge", "Evans", "Stage", "Hilsinger", "Gitto", "Francescone", "Ulman", "Bulat", "Nylen", "Stickney", "Telles", "Bowen", "Montfort", "Neshem", "Brender", "Vastano", "Chaires", "Labreque", "Barroso", "Hattan", "Okerlund", "Lavander", "Greigo"]

class Candidate():
	def __init__(self, name, profession, gender, race, economic_ideology, age, advantaged_professions):
		self.name = name
		self.profession = profession # Used for establishment/anti - establishment stuff.
		self.gender = gender # Only two genders for now. Probably for ever.
		self.race = race # Not exactly race. White, black, French, etc.
		self.economic_ideology = economic_ideology # Socialism, Capitalism
		self.age = age # In years
		self.advantaged_professions = advantaged_professions # Professions that the candidate has been known to favor
		# Adds the candidate to the list of candidates.
		candidates.append(self)

class Voter():
	def __init__(self, name, profession, income, gender, race, age):
		self.name = name
		self.profession = profession # Used for advantaged professions from the candidate, and also to determine income.
		self.income = income # Mean annual wage
		self.gender = gender # Male of Female. Nothing else. Cause I'm lazy.
		self.race = race # Not exactly race. White, black, French, etc.
		self.age = age # In years.
		# Voting determination stuff.
		self.choice = []
		self.high_score = -1
		self.cand_score = [0, 0]
		# Adds the voter to the list of voter.
		voters.append(self)
	def vote(self, candidates):
		for i in range(len(candidates)):
			# Score bonus if the candidate favors/had enacted policies that favor the voter's profession
			if(self.profession in candidates[i].advantaged_professions):
				self.cand_score[i] = self.cand_score[i] + 100
			if(self.race == candidates[i].race):
				self.cand_score[i] = self.cand_score[i] + 30
			print(str(self.cand_score[i]) + candidates[i].name)
			if(self.cand_score[i] > self.high_score):
				self.choice = [i]
				self.high_score = self.cand_score[i]
			elif(self.cand_score[i] == self.high_score):
				self.choice.append(i)
				print("Tie")
		if(len(self.choice) == 1):
			return self.choice[0]
		else:
			return self.choice[random.randint(0, len(self.choice) - 1)]

professions_list_raw = open("wages.txt", "r")
professions_list = professions_list_raw.readlines()
for i in range(len(professions_list) - 1):
        professions_list[i] = professions_list[i].split("|")

def get_profession():
        weight = random.randint(0, 1000000)/1000
        additive = 0
        for i in range(len(professions_list) - 1):
                if(weight >= additive and weight < additive + float(professions_list[i][5])):
                        return professions_list[i]
                else:
                        additive = float(additive + float(professions_list[i][5]))

print(get_profession)

class Profession():
	def __init__(self, name, median_income, min_income, max_income):
		self.name = name
		self.median_income = median_income
		self.min_income = min_income
		self.max_income = max_income
		professions.append(self)

def generate_name(gender):
	if(gender == "Male"):
		return male_first_names[random.randint(0, len(male_first_names) - 1)] + " " + last_names[random.randint(0, len(last_names) - 1)]
	else:
		return female_first_names[random.randint(0, len(female_first_names) - 1)] + " " + last_names[random.randint(0, len(last_names) - 1)]

def gen_voter():
        gender = random.randint(0, 1)
        if(gender == 0):
                gender = "Male"
        else:
                gender = "Female"
        job = get_profession()
        return Voter(generate_name(gender), job, job[8], gender, "White", 0)

Hillary = Candidate(generate_name("Female"), "Congressperson", "Female", "White", "Capitalism", "70", [professions_list[1]])
John = Candidate(generate_name("Female"), "Congressperson", "Female", "Black", "Capitalism", "70", [professions_list[0]])

gen_voter()
Jess = gen_voter()

print("Candidates: \n")
for i in range(len(candidates)):
	print(candidates[i].name + "\n")

# Compulsory voting currently cause I don't have apathy yet
for i in range(len(voters)):
	voters[i].choice = voters[i].vote(candidates)
print(voters[0].name + " voted for " + candidates[voters[0].choice].name)
print(voters[0].profession)
print(Jess.cand_score)
print(voters[0].choice)
for i in candidates:
        print(i.name + " likes " + i.advantaged_professions[0][1])
