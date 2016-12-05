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
conda install /path/to/the/new/package
```

# Check user database
`http://localhost:8000/list`
