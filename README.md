# Require
```
conda install flask conda-build
```

# Create a server

```bash
cd server
python create_database.py # only do once
python app.py
```

# Try to build and to install a dummy package and to send user info to database.db

```bash
cd client
conda build recipe
conda install `conda build --output recipe`
```

# Check user database
`http://localhost:8000/list`
