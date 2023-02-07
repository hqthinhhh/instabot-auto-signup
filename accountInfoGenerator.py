import string
import random


# Generating name functions 
# You can create different surnames to increase the variety of usernames.
def generatingName():
    firstName = ["Anh", "An", "Ánh", "Ba", "Bá", "Bạ", "Béo", "Bình", "Bính", "Bưởi",
                 "Bọ", "Bê", "Bựa", "Huy Quang", "Abdalroof", "Abdihakim", "Abdirahman", "Abdisalam", "Abdul",
                 "Abdul-Aziz", "Abdulbasir", "Abdulkadir", "Abdulkarem", "Abdulkhader", "Abdullah", "Abdul-Majeed",
                 "Abdulmalik", "Abdul-Rehman", "Abdur", "Abdurraheem", "Abdur-Rahman", "Abdur-Rehmaan", "Abel",
                 "Abhinav", "Abhisumant", "Abid", "Abir", "Abraham", "Abu", "Abubakar", "Ace", "Adain", "Adam",
                 "Adam-James", "Addison", "Addisson", "Adegbola", "Adegbolahan", "Aden", "Adenn", "Adie", "Adil",
                 "Aditya", "Adnan", "Adrian", "Adrien", "Aedan", "Aedin", "Aedyn", "Aeron", "Afonso", "Ahmad", "Ahmed",
                 "Ahmed-Aziz", "Ahoua", "Ahtasham", "Aiadan", "Aidan", "Aiden", "Aiden-Jack", "Aiden-Vee", "Aidian",
                 "Aidy", "Ailin", "Aiman", "Ainsley", "Ainslie", "Airen", "Airidas", "Airlie", "AJ", "Ajay", "A-Jay",
                 "Ajayraj", "Akan", "Akram", "Al", "Ala", "Alan", "Alanas", "Alasdair", "Alastair", "Alber", "Albert",
                 "Albie", "Aldred", "Alec", "Aled", "Aleem", "Aleksandar", "Aleksander", "Aleksandr", "Aleksandrs",
                 "Alekzander", "Alessandro", "Alessio", "Alex", "Alexander", "Alexei", "Alexx", "Alexzander", "Alf",
                 "Alfee", "Alfie", "Alfred", "Alfy", "Alhaji", "Al-Hassan", "Ali", "Aliekber", "Alieu", "Alihaider",
                 "Alisdair", "Alishan", "Alistair", "Alistar", "Alister", "Aliyaan", "Allan", "Allan-Laiton", "Allen",
                 "Allesandro", "Allister", "Ally", "Alphonse", "jmknu", "Alum", "Alvern", "Alvin", "Alyas", "Amaan",
                 "Aman", "Amani", "Ambanimoh", "Ameer", "Amgad", "Ami", "Amin", "Amir", "Ammaar", "Ammar", "Ammer",
                 "Amolpreet", "Amos", "Amrinder", "Amrit", "Amro", "Anay", "Andrea", "Andreas", "Andrei", "Andrejs",
                 "Andrew", "Andy", "Anees", "Anesu", "Angel", "Angelo", "Angus", "Anir", "Anis", "Anish", "Anmolpreet",
                 "Annan", "Anndra", "Anselm", "Anthony", "Anthony-John", "Antoine", "Anton", "Antoni", "Antonio",
                 "Antony", "Antonyo", "Anubhav", "Aodhan", "Aon", "Aonghus", "Apisai", "Arafat", "Aran", "Arandeep",
                 "Arann", "Aray", "Arayan", "Archibald", "Archie", "Arda", "Ardal", "Ardeshir", "Areeb", "Areez",
                 "Aref", "Arfin", "Argyle", "Argyll", "Ari", "Aria", "Arian", "Arihant", "Aristomenis", "Aristotelis",
                 "Arjuna", "Arlo", "Armaan", "Arman", "Armen", "Arnab", "Arnav", "Arnold", "Aron", "Aronas", "Arran",
                 "Arrham", "Arron", "Arryn", "Arsalan", "Artem", "Arthur", "Artur", "Arturo", "Arun", "Arunas", "Arved",
                 "Arya", "Aryan", "Aryankhan", "Aryian", "Aryn", "Asa", "Asfhan", "Ash", "Ashlee-jay", "Ashley",
                 "Ashton", "Ashton-Lloyd", "Ashtyn", "Ashwin", "Asif", "Asim", "Aslam", "Asrar", "Ata", "Atal",
                 "Atapattu", "Ateeq", "Athol", "Athon", "Athos-Carlos", "Atli", "Atom", "Attila", "Aulay", "Aun",
                 "Austen", "Austin", "Avani", "Averon", "Avi", "Avinash", "Avraham", "Awais", "Awwal", "Axel", "Ayaan",
                 "Ayan", "Aydan", "Ayden", "Aydin", "Aydon", "Ayman", "Ayomide", "Ayren", "Ayrton", "Aytug", "Ayub",
                 "Ayyub", "Azaan", "Azedine", "Azeem", "Azim", "Aziz", "Azlan", "Azzam", "Azzedine", "Babatunmise",
                 "Babur", "Bader", "Badr", "Badsha", "Bailee", "Bailey", "Bailie", "Bailley", "Baillie", "Baley",
                 "Caedyn", "Cael", "Caelan", "Caelen", "Caethan", "Cahl", "Cahlum", "Cai", "Caidan", "Melim",'Băng', 'Bạch',
                 'Bảo', 'Bằng', 'Bội', 'Ca', 'Cam', 'Chi', 'Chinh', 'Chiêu', 'Chung', 'Châu', 'Cát', 'Cúc', 'Cương', 'Cầm', 'Cẩm',
                 'Dao', 'Di', 'Diên', 'Diễm', 'Diệp', 'Diệu', 'Du', 'Dung', 'Duy', 'Duyên', 'Dân', 'Dã', 'Dương', 'Dạ',
                 'Gia', 'Giang', 'Giao', 'Giáng', 'Hiếu', 'Hiền', 'Hiểu', 'Hiệp', 'Hoa', 'Hoan', 'Hoài', 'Hoàn', 'Hoàng',
                 'Hoạ', 'Huyền', 'Huệ', 'Huỳnh', 'Hà', 'Hàm', 'Hân', 'Hòa', 'Hương', 'Hướng', 'Hường', 'Hưởng', 'Hạ', 'Hạc',
                 'Hạnh', 'Hải', 'Hảo', 'Hậu', 'Hằng', 'Họa', 'Hồ', 'Hồng', 'Hợp', 'Khai', 'Khanh', 'Khiết', 'Khuyên', 'Khuê',
                 'Khánh', 'Khê', 'Khôi', 'Khúc', 'Khả', 'Khải', 'Kim', 'Kiết', 'Kiều', 'Kê', 'Kỳ', 'Lam', 'Lan', 'Linh', 'Liên',
                 'Liễu', 'Loan', 'Ly', 'Lâm', 'Lê', 'Lý', 'Lăng', 'Lưu', 'Lễ', 'Lệ', 'Lộc', 'Lợi', 'Lục', 'Mai', 'Mi', 'Minh', 'Miên',
                 'My', 'Mẫn', 'Mậu', 'Mộc', 'Mộng', 'Mỹ', 'Nga', 'Nghi', 'Nguyên', 'Nguyết', 'Nguyệt', 'Ngà', 'Ngân', 'Ngôn', 'Ngọc',
                 'Nhan','Nhi', 'Nhiên', 'Nhung', 'Nhàn', 'Nhân', 'Nhã', 'Nhơn', 'Như', 'Nhạn', 'Nhất', 'Nhật', 'Nương', 'Nữ', 'Oanh',
                 'Phi', 'Phong','Phúc','Phương', 'Phước', 'Phượng', 'Phụng', 'Quyên', 'Quân', 'Quế', 'Quỳnh', 'Sa', 'San', 'Sao', 'Sinh',
                 'Song', 'Sông', 'Sơn','Sương', 'Thanh','Thi', 'Thiên', 'Thiếu', 'Thiều', 'Thiện', 'Thoa', 'Thoại', 'Thu', 'Thuần',
                 'Thuận', 'Thy', 'Thái', 'Thêu', 'Thông','Thùy', 'Thúy', 'Thơ', 'Thư', 'Thương', 'Thường', 'Thạch', 'Thảo', 'Thắm',
                 'Thục', 'Thụy', 'Thủy', 'Tinh', 'Tiên','Tiểu', 'Trang', 'Tranh', 'Trinh', 'Triều', 'Triệu', 'Trung', 'Trà', 'Trâm',
                 'Trân', 'Trúc', 'Trầm', 'Tuyến', 'Tuyết', 'Tuyền', 'Tuệ', 'Ty', 'Tâm', 'Tùng', 'Tùy', 'Tú', 'Túy', 'Tường', 'Tịnh',
                 'Tố', 'Từ', 'Uyên', 'Uyển', 'Vi', 'Vinh', 'Việt', 'Vy', 'Vàng', 'Vành', 'Vân', 'Vũ', 'Vọng', 'Vỹ', 'Xuyến', 'Xuân',
                 'Yên', 'Yến', 'xanh', 'Ái', 'Ánh', 'Ân', 'Ðan', 'Ðinh', 'Ðiệp', 'Ðoan', 'Ðài', 'Ðàn', 'Ðào', 'Ðình', 'Ðông', 'Ðường',
                 'Ðồng', 'Ý', 'Đan', 'Đinh', 'Đoan', 'Đài', 'Đào', 'Đông', 'Đăng', 'Đơn', 'Đức', 'Ấu']

    surName = ["VA", "MA", "Bala", "yilmaz", "Ediz",
               "yasar", "Ozbal", "Aydin", "kara",
               "Bakar", "Zengin", "Bilgin", "Kilic",
               "Messi", "Abbas", "Hammoud", "Alan",
               "tilki", "Aslan", "Boz", "karaeski",
               "Hai", "Temiz", "Hoang", "Demirci",
               "Erol", "Guneri", "yasin", "yelken",
               "Elmas", "Altin", "guller", "Bagci",
               "yucel", "korkmaz", "cetin","Dari",
               "Albayrak", "Tekin", "Yurtkulu", "Metin",
               "Suvari", "Kizilay", "Inan", "tasi", "Akdeniz",
               "Albagu", "alk", "Acu", "Nam", "Karagul",
               "Avkar", "Hiep", "Alagan", "Akar"]
    return ''.join(random.choice(firstName) + ' ' + random.choice(surName))


# Generating a username
def username(size=8, chars=string.ascii_lowercase + random.choice(['.', '_'])):
    word_list = [
        "Nam", "AgnHes", "Huy", "Alice", "Amy", "Angela", "thenam", "Bridget", "Dit", 
        "Cordelia", "Dorothy", "Edith", "Faker", "Thien", "Emma", "Esther", "Florence", "Frances", 
        "coanacasn", "Helen", "Irene", "Tan", "Xiu", "Ngu", "Margaret", "Martha", 
        "Mary", "Da", "Naomi", "Phyllis", "Mong", "giakhanh", "Sabina", "Silvester", "Sophia", 
        "Winifred", "Abel", "Tai", "Ada", "Adam", "Adela", "Adelio", "Lien", "Adonis", "Khoi", 
        "Agatha", "Aggie", "Aida", "Ailish", "Aimee", "Alan", "Albert", "Albino", "Alex", 
        "Alexandra", "Alfred", "Ali", "Gia", "Alika", "bich", "Aloha", "Alvin", "Amanda", 
        "Ami", "Amos", "Amy", "Anais", "Andra", "Andrew", "Andy", "Angel", "Angelica", "Anika", 
        "Anna", "Beo", "Anthony", "Thieu", "Ozawa", "Ariel", "Arista", "Arnold", 
        "Arvid", "Asha", "Barcelona", "Astin", "PSg", "Ava", "Baba", "Bailey", "ngocbich", 
        "Bambi", "phuongnga", "Barbie", "Barley", "quocca", "Baron", "Basil", "Baxter", "Beau", 
        "Bebe", "Beck", "Becky", "Belita", "Bella", "Belle", "Ronglon", "Benny", "Berg", "Bessie", 
        "Biana", "Bianca", "Bibiane", "mom", "Bingo", "Bishop", "Bliss", "Blondie", "Bonita", "Bono", 
        "Boris", "Boss", "Bright", "Bruno", "Buck", "Buddy", "Bunny", "Caesar", "Caley", "Calix", 
        "Su", "Callia", "leesin", "Minh", "Cara", "Huong", "Carmen", "Casey", "Catherine", 
        "Cecil", "Hien", "Celina", "ChaCha", "Champ", "Kinh", "Charlie", "Chase", "Chavi", 
        "Chelsea", "Cherie", "Ania", "Chloe", "Chrissy", "Chubby", "renekton", "Clara", "PVA", 
        "Ronaldo", "Cleo", "Tung", "Cliff", "Coco", "Dao", "Phuong", "Connie", "coo", "Corby", 
        "Coy", "Hoang", "Crimson", "Chien", "Nguyen", "Cutie", "Cyclone", "Cyma", "Daisy", 
        "Dali", "Danika", "Darby", "Daria", "Dat", "Dario", "Darwin", "Dave", "David", "Dean", 
        "Della", "Delling", "Delphine", "Dennis", "Denver", "Derry", "Ngoc", "Dexter", "Diallo", 
        "Dick", "Dino", "Dixie", "Cam", "Doris", "Tao", "Douglas", "Duke", "Dustin", "Dyllis", 
        "Eavan", "Phong", "Echo", "Edan", "Truong", "Eden", "Dong", "Edwin", "Eilis", "Chung", 
        "Elf", "Phuonganh", "Elisha", "Elizabeth", "Elle", "Elroy", "Son", "Elvis", "Elysia", "Tien", 
        "Eric", "DucAnh", "Eros", "Cuong", "Thinh", "Eva", "Evan", "Trung", "Chu", "Rocha", 
        "Fedora", "Bac", "Gus", "Fella", "Phu", "Filia", "Fleta", "Florence", "Floria", 
        "Thanh", "Freeman", "Quan", "Gali", "Bai", "Trung", "Vinh", "Gilbert", "Gili", 
        "lccoasc", "Gloria", "Goofy", "Grace", "Grania", "Tay", "Haley", "Halona", "Happy", 
        "Harley", "Harmony", "Dang", "Harry", "Heba", "Mai", "Helia", "Hera", "Hero", "Hestia", 
        "Hollis", "Cun", "Hope", "Le", "Hue", "Huey", "Ian", "Iliana", "Ca", "Ingrid", 
        "Irina", "Quach", "Isaac", "Isabel", "Isadora", "Isis", "Jace", "Jack", "Jackson", "Jaclyn", 
        "Jade", "Jane", "Ricon", "anhthai", "Linh", "Jeffrey", "Jenifer", "Jennie", "Jeremy", 
        "Jericho", "Jerry", "Jess", "Buoi", "Jessie", "Jodie", "Johanna", "Jolly", "Jordan", "Joy", 
        "Jud", "Manh", "Pham", "Juliet", "Justin", "gtfolmj", "Kara", "Karena", "Karis", "Kassia", 
        "Kate", "sido", "Kelley", "Kerri", "Kevin", "Kitty", "Klaus", "Kori", "Kuper", "Kyra", 
        "Lakia", "Lala", "Lamis", "Lani", "Lappy", "Lara", "Lavina", "Lee", "Leena", "Lelia", "Leo", 'Love'
        "Hao", "Lev", "Cut", "Lily", "MoonFl", "Linda", "Lisa", "Lloyd", "Meo", "Lottie", "Louis", 
        "Lowell", "Lucia", "Lucifer", "Lucy", "hiephoang", "Luna", "Mabel", "Madonna", "Maggie", "Makaio", 
        "Malissa", "Malo", "Mana", "Mandelina", "Van", "Marcia", "Margaret", "Mary", "Mathilda", 
        "Nhat", "Melina", "Ruoc", "Mickey", "Duc", "Tuan", "Miranda", "Missy", "Misty", "Molly", 
        "Monet", "Bap", "Morris", "Muffin", "Mulan", "Murphy", "Nadia", "Nalo", "Nami", "Nana", 
        "Nani", "Naomi", "Nara", "Narcisse", "Navid", "Quoc", "Neema", "Nero", "Nia", "Nicholas", 
        "Nicky", "Nina", "Odelia", "Olga", "Olive", "Oliver", "Oscar", "Pablo", "Paloma", "Pamela", 
        "Patrick", "Pavel", "Peggy", "Pello", "Penda", "Peppi", "Petra", "Phila", "Phillip", "Pinky", 
        "Pluto", "Poco", "Polo", "Pooky", "Poppy", "Meo", "Cho", "Lon", "Puffy", "Rabia", 
        "Chau", "Ralph", "Rambo", "Rania", "Ravi", "Redford", "Reggie", "Rei", "Remy", "Rex", "Richard", 
        "Ricky", "Anh", "Rio", "Risa", "Robbie", "Robert", "Robin", "Rocky", "Chi", "Rollo", "Romeo", 
        "Vua", "Roxy", "Khanh", "Ruby", "Lan", "Duyen", "Ryan", "Sabrina", "Sally", "Salvatore", 
        "Sam", "Samson", "Thuy", "Sarah", "Sasha", "Xoai", "Scoop", "Sebastian", "Selina", "Selma", 
        "Serena", "Severino", "Shaina", "Shasa", "Sheri", "Nho", "Simba", "Simon", "Sniper", "Solomon", 
        "Sonia", "Ngoc Anh", "Sophie", "Viet", "Ruoi", "Spooky", "Bia", "Stella", "Steven", "Sting", 
        "Storm", "Sugar", "Duong", "Sweetie", "Sylvester", "Sylvia", "Talia", "Talli", "Tanesia", 
        "Tania", "Ted", "Kiet", "Terra", "Thai", "Thomas", "Tomo", "Binh", "Trudy", "Uba", 
        "Umberto", "Nga", "Vanessa", "Velika", "Vera", "Mai", "Veronica", "Victoria", 
        "Vincent", "Violet", "Vito", "Vivi", "Waldo", "Walter", "Weenie", "Wendy", "William", 
        "Wily", "Minh", "Woody", "Thao", "Yeti", "An", "Zaza", "Hung", "Zelia", "Zena", 
        "Zenia", "tranglinh", "halinh", "Zeus", "Han", "Zinna", "Zizi", "Zoe", "Trang", "Ha",
    ]
    word_list += chars

    result_username = 'x' * 100 # Init username as dummy words
    while len(result_username) < size or len(result_username) >= 30: ### Limit of instagram username length is 30
        ### Case 0: Combination of words
        n_word = random.randint(1,2)
        target_word_list = list(map(lambda x: x.lower(), random.choices(word_list , k=n_word)))

        ### Case 1: Flip each word (5%)
        for word_i, target_word in enumerate(target_word_list):
            if random.random() < 0.03:
                target_word = target_word[::-1] 
            target_word_list[word_i] = target_word

        ### Case 2: replace character to 'x' or 'y' or number (3%)
        for word_i, target_word in enumerate(target_word_list):
            for ch_i in range(len(target_word)):
                if random.random() < 0.03:
                    target_char = random.choice(['x', 'y']+list(map(str, range(10))))
                    target_word = target_word[:ch_i] + target_char + target_word[ch_i+1:] 
            target_word_list[word_i] = target_word

        ### Case 3: Repeat last character (7%, 1~4 times)
        for word_i, target_word in enumerate(target_word_list):
            # if random.random() < 0.07:
            #     target_word = (target_word[0]*random.randint(1,3)) + target_word 
            if random.random() < 0.07:
                target_word += (target_word[-1]*random.randint(1,4)) 
            target_word_list[word_i] = target_word

        ### Case 4: Join the words with '.' or '_'
        joining_char = random.choice(['.', '_'])
        result_username = joining_char.join(target_word_list)

        ### Case 5: Add some number to end (30%, 1~999999)
        if random.random() < 0.3:
            if random.random() < 0.6:
                result_username += joining_char
            additional_number_list = []
            number_list = list(map(str, range(10)))
            additional_number_list.append(random.choice(number_list))
            number_list += ['']*10
            additional_number_list += random.choices(number_list, k=5)
            result_username += ''.join(list(map(str, additional_number_list)))

    return result_username

# Generating a password
def generatePassword(passwd=None):
    if passwd is None:
        password_characters = string.ascii_letters + string.digits
        return ''.join(random.choice(password_characters) for i in range(12))
    else:
        return passwd

# Generating a Email
def generatingEmail():
    return ''.join(username() + '@mail.com')

if __name__=='__main__':
    print(username(size=12, chars=string.ascii_lowercase + random.choice(['.', '_'])))