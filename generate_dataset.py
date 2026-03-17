import json
import random

usernames = [
    "health_guru","sports_fan","student_life","tech_world","fitness_daily",
    "travel_diaries","coding_student","mental_support","food_blog","career_path",
    "ai_learner","sports_zone","life_quotes","college_diaries","mind_care",
    "sports_daily","tech_updates","student_help","health_awareness","fitness_motivation",
    "movie_buff","crypto_trader","gamer_zone","politics_watch","finance_tips",
    "book_reader","startup_founder","science_today","nature_lover","daily_thoughts"
]

platforms = ["Twitter","Instagram","Reddit","LinkedIn","YouTube","Facebook"]

topics = {

"health":[
"Doctor recommended regular exercise for heart health",
"Cardiologist says daily walking improves heart condition",
"Eating healthy food helps prevent diseases",
"Regular health checkups are important",
"Yoga improves both mental and physical health"
],

"mental_health":[
"Feeling anxious and stressed lately",
"Meditation helps reduce anxiety and depression",
"Trying to stay positive during tough times",
"Talking to friends improves mental wellbeing",
"Mental health awareness is very important"
],

"sports":[
"The football match yesterday was incredible",
"Cricket world cup games are always exciting",
"Basketball finals were thrilling to watch",
"Morning running improves stamina",
"Gym workouts help maintain fitness"
],

"education":[
"Studying hard for upcoming exams",
"Assignments and deadlines are stressful",
"Learning new programming concepts today",
"Final year project development in progress",
"Time management is important for students"
],

"technology":[
"Artificial intelligence is changing the world",
"Learning machine learning and deep learning",
"Building web applications using Flask",
"Transformers are powerful NLP models",
"Cloud computing is the future of software"
],

"finance":[
"Investing in stocks requires patience",
"Cryptocurrency markets are very volatile",
"Saving money is important for financial stability",
"Learning about personal finance and budgeting",
"Stock market trends are unpredictable"
],

"movies":[
"The new sci-fi movie had amazing visuals",
"Watching classic films on the weekend",
"The storyline of that drama movie was powerful",
"Movie soundtracks can make scenes unforgettable",
"The latest superhero film broke box office records"
],

"gaming":[
"Played a new multiplayer game today",
"Gaming graphics are becoming very realistic",
"Competitive esports tournaments are exciting",
"Strategy games improve decision making",
"Streaming gameplay online is popular now"
],

"travel":[
"Traveling to the mountains this weekend",
"Exploring new cities and cultures",
"Beach vacations are relaxing",
"Solo travel can be life changing",
"Planning a road trip across the country"
],

"food":[
"Tried a new healthy salad recipe",
"Street food markets are always exciting",
"Cooking pasta at home today",
"Exploring different cuisines is fun",
"Healthy eating habits improve lifestyle"
],

"science":[
"Space exploration is advancing rapidly",
"Scientists discovered a new exoplanet",
"Climate change research is important",
"Physics explains many natural phenomena",
"Biotechnology is transforming medicine"
],

"environment":[
"Planting trees helps protect the environment",
"Climate change awareness is increasing",
"Recycling reduces environmental waste",
"Protecting wildlife is important",
"Nature conservation should be prioritized"
],

"politics":[
"The election debate was intense",
"Government policies affect the economy",
"Political discussions are trending online",
"Voting is important in a democracy",
"Public policies shape society"
],

"business":[
"Startups are disrupting traditional industries",
"Entrepreneurs need strong leadership skills",
"Business strategies evolve quickly",
"Marketing plays a huge role in success",
"Building a company requires persistence"
],

"books":[
"Reading books improves knowledge",
"Finished a great mystery novel",
"Literature opens new perspectives",
"Book recommendations are always welcome",
"Reading daily helps personal growth"
],

"lifestyle":[
"Morning routines boost productivity",
"Balancing work and life is important",
"Minimalist lifestyle reduces stress",
"Practicing gratitude improves happiness",
"Healthy habits build a better life"
]

}

posts = []

topic_list = list(topics.keys())

for i in range(1000):
    topic = random.choice(topic_list)
    text = random.choice(topics[topic])

    post = {
        "id": i + 1,
        "username": random.choice(usernames),
        "platform": random.choice(platforms),
        "text": text,
        "likes": random.randint(10, 2000)
    }

    posts.append(post)

with open("posts.json","w") as f:
    json.dump(posts,f,indent=2)

print("✅ Generated posts.json with 1000 diverse social media posts")