# **Word Counter** 📝📊  
A Django-based web application that calculates **TF-IDF** values for words in a text file.  


## **📦 Installation**  

### **1⃣ Clone the Repository**  
```bash
git clone https://github.com/yourusername/word-counter.git
cd word-counter
```

### **2⃣ Create a Virtual Environment**  
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### **3⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

---

## **⚙️ Configuration**  

### **4⃣ Setup Environment Variables**  
Create a `.env` file in the project root and add:  
```ini
# Security
SECRET_KEY=your-secret-key

# Debug Mode (Set to False in production)
DEBUG=True

# Allowed Hosts
ALLOWED_HOSTS=127.0.0.1,localhost

# Database Configuration
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
```

Ensure `.env` is **excluded from version control** by adding it to `.gitignore`:
```
.env
```

---

## **🛠 Database Setup**  
Run the following command to apply migrations:  
```bash
python manage.py migrate
```

---

## **🚀 Running the Project**  

### **5⃣ Start the Development Server**  
```bash
python manage.py runserver
```
The app will be available at:  
👉 **http://127.0.0.1:8000/**  

---

## **🛠 Running Tests**  
```bash
python manage.py test
```

---

## **🐂 Project Structure**  
```
word-counter/
│— word_counter/        
│   ├── templates/       
│   ├── views.py         
│   ├── urls.py          
│   ├── tests.py        
│— config/              
│— static/              
│— db.sqlite3           
│— manage.py           
│— .env                 
│— requirements.txt     
└─ README.md            
```



